import { serverInstance } from "./axios";
import { Post } from "../types/Post";
import { PaginatedResponse } from "../types/Pagination";

export const getPosts = async (page: number = 1, size: number = 12, sort_by?: string, sort_order?: string): Promise<PaginatedResponse<Post>> => {
    const response = await serverInstance.get("/post/get_all/", {
        params: { page, size, sort_by, sort_order }
    });
    return response.data;
}

export const getPost = async (id: number): Promise<Post> => {
    const response = await serverInstance.get(`/post/get/${id}/`);
    return response.data;
}

export const addPost = async (data: Omit<Post, "id">): Promise<Post> => {
    const response = await serverInstance.post("/post/add/", data);
    return response.data;
}

export const updatePost = async (id: number, data: Partial<Post>): Promise<Post> => {
    const response = await serverInstance.patch(`/post/update/${id}`, data);
    return response.data;
}

export const deletePost = async (id: number): Promise<number> => {
    const response = await serverInstance.delete(`/post/delete/${id}`);
    return response.data;
}

export const importPosts = async (): Promise<string> => {
    const response = await serverInstance.post("/post/import/");
    return response.data;
}

export const getPostsByUser = async (userId: number, page: number = 1, size: number = 12): Promise<PaginatedResponse<Post>> => {
    const response = await serverInstance.get(`/post/get_all_by_user/${userId}`, {
        params: { page, size }
    });
    return response.data;
}