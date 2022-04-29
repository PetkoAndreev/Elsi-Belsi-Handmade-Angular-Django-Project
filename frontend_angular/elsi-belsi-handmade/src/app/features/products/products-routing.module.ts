import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from 'src/app/core/guards/auth.guard';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { ProductNewComponent } from './product-new/product-new.component';
import { ProductsPageComponent } from './products-page/products-page.component';



// Added login, register and profile navigation paths
const routes: Routes = [
    {
        path: '',
        pathMatch: 'full',
        component: ProductsPageComponent,
    },
    {
        // Place this first to not override the logic to search for product id
        path: 'new',
        canActivate: [AuthGuard],
        component: ProductNewComponent,
    },
    {
        path: ':productId',
        component: ProductDetailsComponent,
    }
];

export const ProductsRoutingModule = RouterModule.forChild(routes);