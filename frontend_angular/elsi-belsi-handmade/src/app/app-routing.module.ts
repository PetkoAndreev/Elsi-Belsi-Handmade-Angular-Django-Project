import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './features/pages/home-page/home-page.component';
import { PageNotFoundComponent } from './features/pages/page-not-found/page-not-found.component';

const routes: Routes = [
  // 13.04 - added home page navigation - path '' and 'home'
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'home',
  },
  {
    path: 'home',
    component: HomePageComponent,
  },
  // {
  //   path: 'user',
  //   loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule)
  // },
  // {
  //   path: 'products',
  //   loadChildren: () => import('./features/products/products.module').then(p => p.ProductsModule)
  // },
  // 14.04 - added page-not-found navigation

  {
    path: 'not-found',
    component: PageNotFoundComponent,
  },
  {
    path: '**',
    redirectTo: 'not-found',
  }
];

export const AppRoutingModule = RouterModule.forRoot(routes)
