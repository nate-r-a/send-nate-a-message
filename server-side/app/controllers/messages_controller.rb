class MessagesController < ApplicationController
  skip_before_action :verify_authenticity_token, only: :destroy

  def home
    @recent_messages = Message.not_private.last(5)
  end

  def create
    Message.create(message_params)

    flash[:notice] = "Thanks! Your message should be printed shortly. You may need to refresh to submit another picture."
    redirect_to root_path
  end

  def index
    render json: Message.unprinted
  end

  def show
    render json: Message.find(params[:id])
  end

  def update
    message = Message.find(params[:id])
    message.update(message_params)
  end

  def destroy
    message = Message.find(params[:id])
    message.destroy
  end

  private

  def message_params
    params.require(:message).permit(:text, :image, :printed, :private)
  end
end
