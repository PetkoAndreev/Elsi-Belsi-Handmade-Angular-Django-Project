import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './features/pages/home-page/home-page.component';

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
  //   path: 'themes',
  //   loadChildren: () => import('./features/themes/themes.module').then(m => m.ThemesModule)
  // },
  // {
  //   path: '**',
  //   component: PageNotFoundComponent,
  // },
];

export const AppRoutingModule = RouterModule.forRoot(routes);