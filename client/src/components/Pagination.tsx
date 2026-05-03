interface PaginationProps {
    page: number;
    totalPages: number;
    setPage: (page: number) => void;
}

export default function Pagination({ page, totalPages, setPage }: PaginationProps) {
    return (
        <div className="pagination">
            <button
                className="pagination-button"
                disabled={page === 1}
                onClick={() => setPage(1)}
            >
                На початок
            </button>
            <button
                className="pagination-button"
                disabled={page === 1}
                onClick={() => setPage(page - 1)}
            >
                Попередня
            </button>
            <span>Сторінка {page} з {totalPages}</span>
            <button
                className="pagination-button"
                disabled={page >= totalPages}
                onClick={() => setPage(page + 1)}
            >
                Наступна
            </button>
            <button
                className="pagination-button"
                disabled={page === totalPages}
                onClick={() => setPage(totalPages)}
            >
                В кінець
            </button>
        </div>
    )
}