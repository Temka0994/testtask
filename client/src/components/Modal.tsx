import React from "react";

interface ModalProps {
    isOpen: boolean;
    onClose: () => void;
    title: string;
    children: React.ReactNode;
}

export default function Modal({ isOpen, title, children }: ModalProps) {
    if (!isOpen) return null;

    return (
        <div className="modal-window">
            <div className="modal-content">
                <h2>{title}</h2>
                {children}
            </div>
        </div>
    );
}