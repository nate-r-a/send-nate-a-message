Rails.application.routes.draw do
  root to: 'messages#home'
  resources :messages, only: [:index, :create, :destroy] #, :show
end
