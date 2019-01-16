class MessagesController < ApplicationController
  skip_before_action :verify_authenticity_token, only: [:create, :destroy]

  def home; end

  def create
    Message.create(message_params)

    flash[:notice] = "Thanks! Your message should be printed shortly."
    redirect_to root_path
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

  private

  def message_params
    params.require(:message).permit(:text, :image)
  end
end
