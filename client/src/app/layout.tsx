import Header from "../components/header/header";
import Footer from "../components/footer/footer";
import "../styles/global.css"
import React from "react";

export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <Header/>
            <main className="main">{children}</main>
            <Footer/>
        </>
    );
}