import React from "react";

interface SortOptions {
    value: string;
    label: string;
}

interface SortButtonsProps {
    sortBy: string | undefined;
    setSortBy: (value: string) => void;
    setSortOrder: React.Dispatch<React.SetStateAction<"asc" | "desc">>;
    options: SortOptions[];
}

export default function SortButtons({ sortBy, setSortBy, setSortOrder, options }: SortButtonsProps) {
    return (
        <div className="sort-controllers">
            <select
                value={sortBy || ""}
                onChange={(event) => setSortBy(event.target.value)}
            >
                <option value="">За замовчуванням</option>
                {options.map((option) => (
                    <option key={option.value} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>

            <button onClick={() => setSortOrder(value => value === "asc" ? "desc" : "asc")}
                    disabled={!sortBy}>
                Зміна напрямку сортування
            </button>
        </div>
    )
}