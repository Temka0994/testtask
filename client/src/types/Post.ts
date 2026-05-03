export interface Post {
    id: number;
    title: string;
    body: string;
    tags: string | null;
    likes: number;
    dislikes: number;
    views: number;
    user_id: number | null;
}