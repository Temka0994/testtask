import { User } from "../../types/User";
import React, { useCallback, useEffect, useState } from "react";
import { addUser, deleteUser, getUser, getUsers, importUsers, updateUser } from "../../api/user";

const initialFormData: Omit<User, "id"> = {
    first_name: "",
    last_name: "",
    maiden_name: "",
    age: 0,
    gender: "",
    email: "",
    phone: "",
    country: ""
};

export const useUsers = () => {
    const [loading, setLoading] = useState(false);
    const [users, setUsers] = useState<User[]>([]);
    const [sortBy, setSortBy] = useState<string | undefined>();
    const [sortOrder, setSortOrder] = useState<"asc" | "desc">("asc");

    const [page, setPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const pageSize = 10;

    const [isModal, setIsModal] = useState(false);
    const [editUser, setEditUser] = useState<User | null>(null);
    const [formData, setFormData] = useState<Partial<User>>(initialFormData);

    const load = useCallback(async () => {
        setLoading(true);
        try {
            const data = await getUsers(page, pageSize, sortBy, sortOrder);
            setUsers(data.items)
            setLoading(false);
            if (data.pages) setTotalPages(data.pages);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    }, [sortBy, sortOrder, page]);

    useEffect(() => {
        void load();
    }, [load]);

    const handleAddUser = () => {
        setEditUser(null)
        setFormData(initialFormData)
        setIsModal(true);
    };

    const handleEditUser = async (id: number) => {
        setLoading(true);
        try {
            const freshUserData = await getUser(id)
            setEditUser(freshUserData)
            setFormData(freshUserData);
            setIsModal(true);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    const handleDeleteUser = async (id: number) => {
        if (window.confirm("Ви впевнені що хочете видалити цього користувача?")) {
            await deleteUser(id)
            await load();
        }
    };

    const closeModal = () => {
        setIsModal(false);
        setEditUser(null);
    };

    const handleImportUsers = async () => {
        setLoading(true);
        try {
            await importUsers();
            await load()
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = event.target;
        setFormData(data => ({
            ...data,
            [name]: name === "age" ? Number(value) : value
        }));
    };

    const handleSubmit = async (event: React.ChangeEvent) => {
        event.preventDefault();
        try {
            if (editUser) {
                await updateUser(editUser.id, formData);
            } else {
                await addUser(formData as Omit<User, "id">);
            }
            closeModal();
            await load()
        } catch (error) {
            console.error(error);
            alert("Сталася помилка.");
        }
    };

    return {
        users, loading, sortBy, page,
        totalPages, isModal, editUser, formData,
        setSortBy, setSortOrder, setPage,
        handleAddUser, handleEditUser, handleDeleteUser, closeModal,
        handleImportUsers, handleChange, handleSubmit
    }
}
