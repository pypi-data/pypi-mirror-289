<script lang="ts">
    import { onMount, onDestroy, createEventDispatcher } from "svelte";
    import { basicDark } from "cm6-theme-basic-dark";
    import { basicLight } from "cm6-theme-basic-light";
    import { EditorView, basicSetup } from "codemirror"
    import { keymap, placeholder as placeholderExt, ViewUpdate } from "@codemirror/view"
    import { StateEffect, EditorState, type Extension } from "@codemirror/state";
    import { unifiedMergeView } from "@codemirror/merge";
    import { getLanguageExtension } from "./language";
    import type { CodeData } from "./utils";
    import { indentWithTab } from "@codemirror/commands";

    export let class_names = "";
    export let value: CodeData;
    export let dark_mode: boolean;
    export let basic = true;
    export let language: string;
    export let lines = 5;
    export let extensions: Extension[] = [];
    export let use_tab = true;
    
    let lang_extension: Extension | undefined;
    let readonly = true;
    let element: HTMLDivElement;
    let view: EditorView;

    const dispatch = createEventDispatcher<{
        change: string;
        blur: undefined;
        focus: undefined;
    }>();

    $: if (view && (value || dark_mode || language)) {
        reconfigure();
    }
    $: get_lang(language);

    $: set_doc(value.diff);

    function set_doc(new_doc: string): void {
		if (view && new_doc !== view.state.doc.toString()) {
			view.dispatch({
				changes: {
					from: 0,
					to: view.state.doc.length,
					insert: new_doc
				}
			});
		}
	}

	async function get_lang(val: string): Promise<void> {
		const ext = await getLanguageExtension(val);
		lang_extension = ext;
	}

    function create_editor_view(): EditorView {
        const editorView = new EditorView({
            parent: element,
            state: create_editor_state(value.diff)
        });
        editorView.dom.addEventListener("focus", handle_focus, true);
        editorView.dom.addEventListener("blur", handle_blur, true);
        return editorView;
    }

    function handle_focus(): void {
        dispatch("focus");
    }

    function handle_blur(): void {
        dispatch("blur");
    }

    function handle_change(vu: ViewUpdate): void {
        if (vu.docChanged) {
            const doc = vu.state.doc;
            const text = doc.toString();
            value.diff = text;
            dispatch("change", text);
        }
        view.requestMeasure({ read: update_gutters });
    }

    function create_editor_state(_value: string): EditorState {
        return EditorState.create({
            doc: _value,
            extensions: get_extensions()
        });
    }

    function get_extensions(): Extension[] {
        const stateExtensions = [
            ...get_base_extensions(
                basic,
                use_tab,
                null,
                readonly,
                lang_extension
            ),
            FontTheme,
            ...get_theme(),
            ...extensions,
            unifiedMergeView({
                original: value.code,
                mergeControls: false,
                gutter: true,
            }),
            EditorView.updateListener.of(handle_change)
        ];
        return stateExtensions;
    }

    function reconfigure(): void {
        view?.dispatch({
            effects: StateEffect.reconfigure.of(get_extensions())
        });
    }

    onMount(() => {
        view = create_editor_view();
        return () => view?.destroy();
    });

    function getGutterLineHeight(_view: EditorView): string | null {
		let elements = _view.dom.querySelectorAll<HTMLElement>(".cm-gutterElement");
		if (elements.length === 0) {
			return null;
		}
		for (var i = 0; i < elements.length; i++) {
			let node = elements[i];
			let height = getComputedStyle(node)?.height ?? "0px";
			if (height != "0px") {
				return height;
			}
		}
		return null;
	}

	function update_gutters(_view: EditorView): any {
		let gutters = _view.dom.querySelectorAll<HTMLElement>(".cm-gutter");
		let _lines = lines + 1;
		let lineHeight = getGutterLineHeight(_view);
		if (!lineHeight) {
			return null;
		}
		for (var i = 0; i < gutters.length; i++) {
			let node = gutters[i];
			node.style.minHeight = `calc(${lineHeight} * ${_lines})`;
		}
		return null;
	}
    async function updateView(value: CodeData, language: string, dark_mode: boolean) {
        const langExtension = await getLanguageExtension(language);
        const theme = dark_mode ? basicDark : basicLight;

        if (view) {
            view.destroy();
        }

        view = new EditorView({
            state: EditorState.create({
                doc: value.diff,
                extensions: [
                    basicSetup,
                    EditorView.editable.of(!readonly),
                    EditorState.readOnly.of(readonly),
                    langExtension,
                    theme,
                    unifiedMergeView({
                        original: value.code,
                        mergeControls: false,
                        gutter: true,
                    })
                ],
            }),
            parent: element
        });
    }

    onDestroy(() => {
        if (view) {
            view.destroy();
        }
    });

	const FontTheme = EditorView.theme({
		"&": {
			fontSize: "var(--text-sm)",
			backgroundColor: "var(--border-color-secondary)"
		},
		".cm-content": {
			paddingTop: "5px",
			paddingBottom: "5px",
			color: "var(--body-text-color)",
			fontFamily: "var(--font-mono)",
			minHeight: "100%"
		},
		".cm-gutters": {
			marginRight: "1px",
			borderRight: "1px solid var(--border-color-primary)",
			backgroundColor: "var(--block-background-fill);",
			color: "var(--body-text-color-subdued)"
		},
		".cm-focused": {
			outline: "none"
		},
		".cm-scroller": {
			height: "auto"
		},
		".cm-cursor": {
			borderLeftColor: "var(--body-text-color)"
		}
	});

    function get_base_extensions(
        basic: boolean,
        use_tab: boolean,
        placeholder: string | HTMLElement | null | undefined,
        readonly: boolean,
        lang: Extension | null | undefined
    ): Extension[] {
        const extensions: Extension[] = [
            EditorView.editable.of(!readonly),
            EditorState.readOnly.of(readonly),
            // EditorView.contentAttributes.of({ "aria-label": "Code input container" })
        ];

        if (basic) {
            extensions.push(basicSetup);
        }
        if (use_tab) {
            extensions.push(keymap.of([indentWithTab]));
        }
        if (placeholder) {
            extensions.push(placeholderExt(placeholder));
        }
        if (lang) {
            extensions.push(lang);
        }
        return extensions;
    }

    function get_theme(): Extension[] {
        return dark_mode ? [basicDark] : [basicLight];
    }
</script>

<div class="wrap">
	<div class="codemirror-wrapper {class_names}" bind:this={element} />
</div>

<style>
	.wrap {
		display: flex;
		flex-direction: column;
		flex-flow: column;
		margin: 0;
		padding: 0;
		height: 100%;
	}
	.codemirror-wrapper {
		height: 100%;
		overflow: auto;
	}

	:global(.cm-editor) {
		height: 100%;
	}

	/* Dunno why this doesn't work through the theme API -- don't remove*/
	:global(.cm-selectionBackground) {
		background-color: #b9d2ff30 !important;
	}

	:global(.cm-focused) {
		outline: none !important;
	}
</style>
