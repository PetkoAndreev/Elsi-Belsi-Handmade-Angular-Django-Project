import { RouterModule, Routes } from '@angular/router';
import { ProductItemComponent } from './product-item/product-item.component';
import { ProductsPageComponent } from './products-page/products-page.component';



// Added login, register and profile navigation paths
const routes: Routes = [
    {
        path: 'products',
        component: ProductsPageComponent,
    },
    {
        path: 'products/:id',
        component: ProductItemComponent,
    }
];

export const ProductsRoutingModule = RouterModule.forChild(routes);