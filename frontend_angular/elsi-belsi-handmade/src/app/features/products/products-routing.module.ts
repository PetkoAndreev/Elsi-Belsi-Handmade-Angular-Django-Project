import { RouterModule, Routes } from '@angular/router';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { ProductsPageComponent } from './products-page/products-page.component';



// Added login, register and profile navigation paths
const routes: Routes = [
    {
        path: 'products',
        // pathMatch: 'full',
        component: ProductsPageComponent,
    },
    {
        // Place this first to not override the logic to search for product id
        path: 'products/new',
        // pathMatch: 'full',
        component: ProductsPageComponent,
    },
    {
        path: 'products/:productId',
        component: ProductDetailsComponent,
    }
];

export const ProductsRoutingModule = RouterModule.forChild(routes);