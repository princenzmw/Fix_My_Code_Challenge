Rails.application.routes.draw do
  devise_for :users
  devise_for :installs

  # Defining the root path
  root "posts#index"

  # Defining routes for posts and nested comments
  resources :posts do
    resources :comments
  end

  # Defining a route for the 'about' page
  get '/about', to: 'pages#about'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
