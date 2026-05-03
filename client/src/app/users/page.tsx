import React from "react";
import Pagination from "../../components/Pagination";
import SortButtons from "../../components/SortButtons";
import Modal from "../../components/Modal";
import { useUsers } from "./useUsers";
import UserPostsList from "./userPostList";

const userSortOptions = [
    { value: "id", label: "За ідентифікатором" },
    { value: "first_name", label: "За іменем" },
    { value: "last_name", label: "За прізвищем" },
    { value: "age", label: "За віком" }
];

export default function UsersPage() {
    const [viewPostsUserId, setViewPostsUserId] = React.useState<number | null>(null);

    const {
        users, loading, sortBy, page, totalPages, isModal, editUser, formData,
        setSortBy, setSortOrder, setPage,
        handleAddUser, handleEditUser, handleDeleteUser, closeModal,
        handleImportUsers, handleChange, handleSubmit
    } = useUsers();

    return (
        <div className="page-container">
            <div className="page-header">
                <h1>Users</h1>
                <div className="page-actions">
                    <button onClick={handleImportUsers}>Імпорт користувачів</button>
                    <button onClick={handleAddUser}>Додати користувача</button>
                </div>
            </div>

            <SortButtons
                sortBy={sortBy}
                setSortBy={setSortBy}
                setSortOrder={setSortOrder}
                options={userSortOptions}
            />

            <Modal
                isOpen={isModal}
                onClose={closeModal}
                title={editUser ? "Редагувати користувача" : "Додати користувача"}
            >
                <form onSubmit={handleSubmit}>
                    <label>
                        Ім'я
                        <input required type="text" name="first_name" value={formData.first_name || ""}
                               onChange={handleChange}/>
                    </label>
                    <label>
                        Прізвище
                        <input required type="text" name="last_name" value={formData.last_name || ""}
                               onChange={handleChange}/>
                    </label>
                    <label>
                        Дівоче прізвище
                        <input type="text" name="maiden_name" value={formData.maiden_name || ""}
                               onChange={handleChange}/>
                    </label>
                    <label>
                        Вік
                        <input required type="number" name="age" value={formData.age || ""}
                               onChange={handleChange}/>
                    </label>
                    <label>
                        Стать
                        <select
                            required
                            name="gender"
                            value={formData.gender || ""}
                            onChange={handleChange}
                        >
                            <option value="" disabled>Оберіть стать</option>
                            <option value="male">Чоловіча</option>
                            <option value="female">Жіноча</option>
                        </select>
                    </label>
                    <label>
                        Електронна пошта
                        <input required type="email" name="email" value={formData.email || ""}
                               onChange={handleChange}/>
                    </label>
                    <label>
                        Номер телефону
                        <input required type="text" name="phone" value={formData.phone || ""}
                               onChange={handleChange}/>
                    </label>
                    <label>
                        Країна
                        <input required type="text" name="country" value={formData.country || ""}
                               onChange={handleChange}/>
                    </label>

                    <div className="modal-buttons">
                        <button type="button" onClick={closeModal}>Скасувати</button>
                        <button type="submit">Зберегти</button>
                    </div>
                </form>
            </Modal>

            <Modal
                isOpen={viewPostsUserId !== null}
                onClose={() => setViewPostsUserId(null)}
                title="Публікації користувача"
            >
                {viewPostsUserId && <UserPostsList userId={viewPostsUserId} />}
            </Modal>

            {loading ? (
                <p>loading</p>
            ) : (
                <div className="users-list">
                    <div className="user-container">
                        {users.map((user) => (
                            <div key={user.id}>
                                <div><strong>Ім'я:</strong> {user.first_name}</div>
                                <div><strong>Прізвище:</strong> {user.last_name}</div>
                                {user.maiden_name && <div><strong>Дівоче прізвище:</strong> {user.maiden_name}</div>}
                                <div><strong>Вік:</strong> {user.age}</div>
                                <div><strong>Стать:</strong> {user.gender}</div>
                                <div><strong>Електронна пошта:</strong> {user.email}</div>
                                <div><strong>Номер телефону:</strong> {user.phone}</div>
                                <div><strong>Країна:</strong> {user.country}</div>

                                <div className="user-container-buttons">
                                    <button onClick={() => setViewPostsUserId(user.id)}>
                                        Пости
                                    </button>
                                    <button onClick={() => handleEditUser(user.id)}>Редагувати</button>
                                    <button onClick={() => handleDeleteUser(user.id)}>Видалити</button>
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
    )
}