import React from "react";
import { PageRoutes } from "../../constants/routes";
import { Link } from "react-router-dom";
import "./header.css"

const pages = [
    { label: "Users", href: PageRoutes.Users },
    { label: "Posts", href: PageRoutes.Posts },

]

export default function Header() {
    return (
        <header className="header">
            <div className="logo">
                <Link key={PageRoutes.Users} to={PageRoutes.Users}>TestTask</Link>
            </div>
            <nav>
                {pages.map((page) => (
                    <Link key={page.href} to={page.href}> {page.label} </Link>
                ))}
            </nav>
        </header>
)
}