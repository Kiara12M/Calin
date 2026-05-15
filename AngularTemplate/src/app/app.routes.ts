import { Routes } from '@angular/router';

export const routes: Routes = [

    {
        path: '',
        loadComponent: () => import("./layouts/main-layout/main-layout").then(c => c.MainLayout),
        children: [
            {
                path: '',
                loadComponent: () => import("./features/pagina-principal/pagina-principal").then(c => c.PaginaPrincipal),
            },
            {
              path: 'login',
              loadComponent:()=> import("./layouts/main-layout/components/login/login").then(c => c.Login),
            },
            {
                path: 'register',
                loadComponent:() => import("./layouts/main-layout/components/register/register").then(c => c.Register),
            },
            {
                path: 'cafes',
                loadComponent:() => import("./layouts/main-layout/components/cafes/cafes").then(c => c.Cafes),
            },
            {
                path: 'tes',
                loadComponent:() => import("./layouts/main-layout/components/tes/tes").then(c => c.Tes),
            },
            {
                path: 'accesorios',
                loadComponent:() => import("./layouts/main-layout/components/accesorios/accesorios").then(c => c.Accesorios),
            },
            {
                path: 'chocolates',
                loadComponent:() => import("./layouts/main-layout/components/chocolates/chocolates").then(c => c.Chocolates),
            },
            {
                path: 'checkout',
                loadComponent:() => import("./features/checkout/checkout.component").then(c => c.CheckoutComponent),
            },
            {
                path: 'mis-pedidos',
                loadComponent:() => import("./features/mis-pedidos/mis-pedidos.component").then(c => c.MisPedidosComponent),
            },
            {
                path: 'quienes-somos',
                loadComponent:() => import("./features/quienes-somos/quienes-somos").then(c => c.QuienesSomos),
            },
            {
                path: 'blog',
                loadComponent:() => import("./features/blog/blog").then(c => c.Blog),
            }

        ]
    },
];
