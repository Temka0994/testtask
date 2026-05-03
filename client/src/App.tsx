import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./styles/global.css"
import Layout from "./app/layout";
import { PageRoutes } from "./constants/routes";
import UsersPage from "./app/users/page";
import PostsPage from "./app/posts/page";

export default function App() {
    return (
        <BrowserRouter>
            <Layout>
                <Routes>
                    <Route path={PageRoutes.Users} element={<UsersPage/>}></Route>
                    <Route path={PageRoutes.Posts} element={<PostsPage/>}></Route>
                </Routes>
            </Layout>
        </BrowserRouter>
    );
}