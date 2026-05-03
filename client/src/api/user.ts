import { serverInstance } from "./axios";
import { User } from "../types/User";
import { PaginatedResponse } from "../types/Pagination";

export const getUsers = async (page: number = 1, size: number = 10, sort_by?: string, sort_order?: string): Promise<PaginatedResponse<User>> => {
    const response = await serverInstance.get("/user/get_all/", {
        params: { page, size, sort_by, sort_order }
    });
    return response.data;
}

export const getUser = async (id: number): Promise<User> => {
    const response = await serverInstance.get(`/user/get/${id}/`);
    return response.data;
}

export const addUser = async (data: Omit<User, "id">): Promise<User> => {
    const response = await serverInstance.post("/user/add/", data);
    return response.data;
}

export const updateUser = async (id: number, data: Partial<User>): Promise<User> => {
    const response = await serverInstance.patch(`/user/update/${id}`, data);
    return response.data;
}

export const deleteUser = async (id: number): Promise<number> => {
    const response = await serverInstance.delete(`/user/delete/${id}`);
    return response.data;
}

export const importUsers = async (): Promise<string> => {
    const response = await serverInstance.post("/user/import/");
    return response.data;
}