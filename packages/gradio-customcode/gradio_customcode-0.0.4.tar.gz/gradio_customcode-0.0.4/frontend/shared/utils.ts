export type SelectedCode = {
    start: number;
    end: number;
    text: string;
}

export type CodeData = {
    code: string;
    selected_code: SelectedCode;
    diff: string;
}
