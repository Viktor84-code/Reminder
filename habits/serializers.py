from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user", "created_at")

    def validate(self, data):
        # 1. Нельзя выбрать связанную привычку и вознаграждение одновременно
        if data.get("related_habit") and data.get("reward"):
            raise serializers.ValidationError(
                "Нельзя одновременно указывать связанную привычку и вознаграждение"
            )

        # 2. Время выполнения не больше 120 секунд
        if data.get("duration", 0) > 120:
            raise serializers.ValidationError(
                "Время выполнения не должно превышать 120 секунд"
            )

        # 3. В связанные привычки могут попадать только приятные привычки
        if data.get("related_habit") and not data["related_habit"].is_pleasant:
            raise serializers.ValidationError("Связанная привычка должна быть приятной")

        # 4. У приятной привычки не может быть вознаграждения или связанной привычки
        if data.get("is_pleasant"):
            if data.get("reward") or data.get("related_habit"):
                raise serializers.ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )

        # 5. Периодичность от 1 до 7 дней
        if data.get("periodicity", 1) < 1 or data.get("periodicity", 1) > 7:
            raise serializers.ValidationError(
                "Периодичность должна быть от 1 до 7 дней"
            )

        return data
