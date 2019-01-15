class MessagesController < ApplicationController
  skip_before_action :verify_authenticity_token, only: :destroy

  def create
    Message.create(params[:message])
  end

  def index
    render json: Message.all
  end

  def show
    render json: Message.find(params[:id])
  end

  def destroy
    message = Message.find(params[:id])
    message.destroy
  end
end
