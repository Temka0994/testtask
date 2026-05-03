export interface User {
    id: number;
    first_name: string;
    last_name: string;
    maiden_name: string | null;
    age: number;
    gender: string;
    email: string;
    phone: string;
    country: string;
}