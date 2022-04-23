export interface IProduct {
    id: number;
    product_name: string;
    prd_category: string;
    prd_description: string;
    prd_image: string;
    prd_date_added: string;
    prd_date_updated: string;
    prd_price: string;
    prd_user: number;
    likes: number[],
    favorites: number[]
}

        
