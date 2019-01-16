Rails.application.routes.draw do
  root to: 'messages#home'
  resources :messages, only: [:index, :show, :create, :destroy]
end
