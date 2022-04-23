import { IProduct } from "./product"

export interface IUser {
    user_id: number;
    first_name: string;
    last_name: string;
    age: number;
    profile_image: string;
    facebook_url: string;
    linked_in_url: string;
    github_url: string;
    products: IProduct[];
    favorites: IProduct[];
}
