import React, { useCallback, useEffect, useState } from "react";
import { Post } from "../../types/Post";
import { addPost, deletePost, getPost, getPosts, importPosts, updatePost } from "../../api/post";

const initialFormData: Omit<Post, "id"> = {
    title: "",
    body: "",
    tags: "",
    likes: 0,
    dislikes: 0,
    views: 0,
    user_id: null as any
};

export const usePosts = () => {
    const [loading, setLoading] = useState(false);
    const [posts, setPosts] = useState<Post[]>([]);
    const [sortBy, setSortBy] = useState<string | undefined>();
    const [sortOrder, setSortOrder] = useState<"asc" | "desc">("asc");

    const [page, setPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const pageSize = 12;

    const [isModal, setIsModal] = useState(false);
    const [editPost, setEditPost] = useState<Post | null>(null);
    const [formData, setFormData] = useState<Partial<Post>>(initialFormData);

    const load = useCallback(async () => {
        setLoading(true);
        try {
            const data = await getPosts(page, pageSize, sortBy, sortOrder);
            setPosts(data.items);
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

    const handleAddPost = () => {
        setEditPost(null);
        setFormData(initialFormData);
        setIsModal(true);
    };

    const handleEditPost = async (id: number) => {
        setLoading(true);
        try {
            const freshPostData = await getPost(id);
            setEditPost(freshPostData);
            setFormData(freshPostData);
            setIsModal(true);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    const handleDeletePost = async (id: number) => {
        if (window.confirm("Ви впевнені що хочете видалити цей пост?")) {
            await deletePost(id);
            await load();
        }
    };

    const closeModal = () => {
        setIsModal(false);
        setEditPost(null);
    };

    const handleImportPosts = async () => {
        setLoading(true);
        try {
            await importPosts();
            await load();
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = event.target;

        const numericFields = ["likes", "dislikes", "views"];

        if (name === "user_id") {
            const val = value === "" ? null : Number(value);
            setFormData(data => ({ ...data, [name]: val }));
            return;
        }

        setFormData(data => ({
            ...data,
            [name]: numericFields.includes(name) ? Number(value) : value
        }));
    };

    const handleSubmit = async (event: React.ChangeEvent) => {
        event.preventDefault();
        try {
            if (editPost) {
                await updatePost(editPost.id, formData);
            } else {
                await addPost(formData as Omit<Post, "id">);
            }
            closeModal();
            await load();
        } catch (error) {
            console.error(error);
            alert("Сталася помилка.");
        }
    };

    return {
        posts, loading, sortBy, page, totalPages, isModal, editPost, formData,
        setSortBy, setSortOrder, setPage,
        handleAddPost, handleEditPost, handleDeletePost, closeModal,
        handleImportPosts, handleChange, handleSubmit
    };
};