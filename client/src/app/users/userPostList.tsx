import React, { useEffect, useState } from "react";
import { getPostsByUser } from "../../api/post";
import { Post } from "../../types/Post";

interface UserPostsListProps {
    userId: number;
}

export default function UserPostsList({ userId }: UserPostsListProps) {
    const [posts, setPosts] = useState<Post[]>([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const loadUserPosts = async () => {
            setLoading(true);
            try {
                const data = await getPostsByUser(userId);
                setPosts(data.items);
            } catch (error) {
                console.error(error);
            } finally {
                setLoading(false);
            }
        };

        if (userId) {
            loadUserPosts();
        }
    }, [userId]);

    if (loading)
        return <p>loading</p>;
    if (posts.length === 0)
        return <p>Цей користувач не має постів.</p>;

    return (
        <div>
            {posts.map(post => (
                <div key={post.id}>
                    <h4>{post.title}</h4>
                    <p>{post.body}</p>
                    <small>Лайки: {post.likes} | Перегляди: {post.views}</small>
                </div>
            ))}
        </div>
    );
}