import React from "react";
import Pagination from "../../components/Pagination";
import SortButtons from "../../components/SortButtons";
import Modal from "../../components/Modal";
import { usePosts } from "./usePosts";

const postSortOptions = [
    { value: "id", label: "За ідентифікатором" },
    { value: "title", label: "За заголовком" },
    { value: "likes", label: "За лайками" },
    { value: "views", label: "За переглядами" }
];

export default function PostPage() {
    const {
        posts, loading, sortBy, page, totalPages, isModal, editPost, formData,
        setSortBy, setSortOrder, setPage,
        handleAddPost, handleEditPost, handleDeletePost, closeModal,
        handleImportPosts, handleChange, handleSubmit
    } = usePosts();

    return (
        <div className="page-container">
            <div className="page-header">
                <h1>Posts</h1>
                <div className="page-actions">
                    <button onClick={handleImportPosts}>Імпорт постів</button>
                    <button onClick={handleAddPost}>Додати пост</button>
                </div>
            </div>

            <SortButtons
                sortBy={sortBy}
                setSortBy={setSortBy}
                setSortOrder={setSortOrder}
                options={postSortOptions}
            />

            <Modal
                isOpen={isModal}
                onClose={closeModal}
                title={editPost ? "Редагувати пост" : "Додати пост"}
            >
                <form onSubmit={handleSubmit}>
                    <label>
                        Заголовок
                        <input required type="text" name="title" value={formData.title || ""} onChange={handleChange}/>
                    </label>
                    <label>
                        Вміст
                        <input required type="text" name="body" value={formData.body || ""} onChange={handleChange}/>
                    </label>
                    <label>
                        Теги
                        <input type="text" name="tags" value={formData.tags || ""} onChange={handleChange}/>
                    </label>
                    <label>
                        ID Користувача
                        <input type="number" name="user_id" value={formData.user_id || ""} onChange={handleChange}/>
                    </label>

                    <div className="modal-buttons">
                        <button type="button" onClick={closeModal}>Скасувати</button>
                        <button type="submit">Зберегти</button>
                    </div>
                </form>
            </Modal>

            {loading ? (
                <p>loading...</p>
            ) : (
                <div className="posts-list">
                    <div className="post-container">
                        {posts.map((post) => (
                            <div key={post.id}>
                                <div><strong>Заголовок:</strong> {post.title}</div>
                                <div><strong>Вміст:</strong> {post.body}</div>
                                {post.tags && <div><strong>Теги:</strong> {post.tags}</div>}
                                <div>
                                    Лайки: {post.likes} | Дизлайки: {post.dislikes} | Перегляди: {post.views}
                                </div>
                                {}
                                {post.user_id && <div><strong>ID Автора:</strong> {post.user_id}</div>}

                                <div className="post-container-buttons">
                                    <button onClick={() => handleEditPost(post.id)}>Редагувати</button>
                                    <button onClick={() => handleDeletePost(post.id)}>Видалити</button>
                                </div>
                            </div>
                        ))}
                    </div>

                    <Pagination
                        page={page}
                        totalPages={totalPages}
                        setPage={setPage}
                    />
                </div>
            )}
        </div>
    );
}