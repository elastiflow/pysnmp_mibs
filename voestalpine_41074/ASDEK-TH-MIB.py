# SNMP MIB module (ASDEK-TH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/voestalpine_41074/ASDEK-TH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:07:16 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

voestalpine = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41074)
)

tens = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41074, 2524)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asdek_ObjectIdentity = ObjectIdentity
asdek = _Asdek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2)
)
_Tis_ObjectIdentity = ObjectIdentity
tis = _Tis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1)
)
_TisTable_Object = MibTable
tisTable = _TisTable_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tisTable.setStatus("current")
_TisEntry_Object = MibTableRow
tisEntry = _TisEntry_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1)
)
tisEntry.setIndexNames(
    (0, "ASDEK-TH-MIB", "tisIndex"),
)
if mibBuilder.loadTexts:
    tisEntry.setStatus("current")


class _TisIndex_Type(Integer32):
    """Custom type tisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TisIndex_Type.__name__ = "Integer32"
_TisIndex_Object = MibTableColumn
tisIndex = _TisIndex_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 1),
    _TisIndex_Type()
)
tisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tisIndex.setStatus("current")


class _SelfTestResult_Type(Integer32):
    """Custom type selfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_SelfTestResult_Type.__name__ = "Integer32"
_SelfTestResult_Object = MibTableColumn
selfTestResult = _SelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 2),
    _SelfTestResult_Type()
)
selfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfTestResult.setStatus("current")
_SelfTestTime_Type = DisplayString
_SelfTestTime_Object = MibTableColumn
selfTestTime = _SelfTestTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 3),
    _SelfTestTime_Type()
)
selfTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfTestTime.setStatus("current")
_SelfTestInfo_Type = DisplayString
_SelfTestInfo_Object = MibTableColumn
selfTestInfo = _SelfTestInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 4),
    _SelfTestInfo_Type()
)
selfTestInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfTestInfo.setStatus("current")


class _StandByResult_Type(Integer32):
    """Custom type standByResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_StandByResult_Type.__name__ = "Integer32"
_StandByResult_Object = MibTableColumn
standByResult = _StandByResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 5),
    _StandByResult_Type()
)
standByResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standByResult.setStatus("current")
_StandByChangeTime_Type = DisplayString
_StandByChangeTime_Object = MibTableColumn
standByChangeTime = _StandByChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 6),
    _StandByChangeTime_Type()
)
standByChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standByChangeTime.setStatus("current")
_StandByInfo_Type = DisplayString
_StandByInfo_Object = MibTableColumn
standByInfo = _StandByInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 7),
    _StandByInfo_Type()
)
standByInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standByInfo.setStatus("current")


class _TrainDetectionResult_Type(Integer32):
    """Custom type trainDetectionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_TrainDetectionResult_Type.__name__ = "Integer32"
_TrainDetectionResult_Object = MibTableColumn
trainDetectionResult = _TrainDetectionResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 8),
    _TrainDetectionResult_Type()
)
trainDetectionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trainDetectionResult.setStatus("current")
_TrainDetectionTime_Type = DisplayString
_TrainDetectionTime_Object = MibTableColumn
trainDetectionTime = _TrainDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 9),
    _TrainDetectionTime_Type()
)
trainDetectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trainDetectionTime.setStatus("current")
_TrainNumber_Type = DisplayString
_TrainNumber_Object = MibTableColumn
trainNumber = _TrainNumber_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 10),
    _TrainNumber_Type()
)
trainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trainNumber.setStatus("current")
_TrainDetectionInfo_Type = DisplayString
_TrainDetectionInfo_Object = MibTableColumn
trainDetectionInfo = _TrainDetectionInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 11),
    _TrainDetectionInfo_Type()
)
trainDetectionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trainDetectionInfo.setStatus("current")


class _PowerStatusResult_Type(Integer32):
    """Custom type powerStatusResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_PowerStatusResult_Type.__name__ = "Integer32"
_PowerStatusResult_Object = MibTableColumn
powerStatusResult = _PowerStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 12),
    _PowerStatusResult_Type()
)
powerStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusResult.setStatus("current")
_PowerStatusChangeTime_Type = DisplayString
_PowerStatusChangeTime_Object = MibTableColumn
powerStatusChangeTime = _PowerStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 13),
    _PowerStatusChangeTime_Type()
)
powerStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusChangeTime.setStatus("current")
_PowerStatusInfo_Type = DisplayString
_PowerStatusInfo_Object = MibTableColumn
powerStatusInfo = _PowerStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 14),
    _PowerStatusInfo_Type()
)
powerStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusInfo.setStatus("current")


class _LinkStatusResult_Type(Integer32):
    """Custom type linkStatusResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_LinkStatusResult_Type.__name__ = "Integer32"
_LinkStatusResult_Object = MibTableColumn
linkStatusResult = _LinkStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 15),
    _LinkStatusResult_Type()
)
linkStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusResult.setStatus("current")
_LinkStatusChangeTime_Type = DisplayString
_LinkStatusChangeTime_Object = MibTableColumn
linkStatusChangeTime = _LinkStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 16),
    _LinkStatusChangeTime_Type()
)
linkStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusChangeTime.setStatus("current")
_LinkStatusInfo_Type = DisplayString
_LinkStatusInfo_Object = MibTableColumn
linkStatusInfo = _LinkStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 17),
    _LinkStatusInfo_Type()
)
linkStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusInfo.setStatus("current")


class _InnerTemperatureResult_Type(Integer32):
    """Custom type innerTemperatureResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_InnerTemperatureResult_Type.__name__ = "Integer32"
_InnerTemperatureResult_Object = MibTableColumn
innerTemperatureResult = _InnerTemperatureResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 18),
    _InnerTemperatureResult_Type()
)
innerTemperatureResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innerTemperatureResult.setStatus("current")
_InnerTemperatureChangeTime_Type = DisplayString
_InnerTemperatureChangeTime_Object = MibTableColumn
innerTemperatureChangeTime = _InnerTemperatureChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 19),
    _InnerTemperatureChangeTime_Type()
)
innerTemperatureChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innerTemperatureChangeTime.setStatus("current")
_InnerTemperatureValue_Type = Integer32
_InnerTemperatureValue_Object = MibTableColumn
innerTemperatureValue = _InnerTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 20),
    _InnerTemperatureValue_Type()
)
innerTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innerTemperatureValue.setStatus("current")
_InnerTemperatureInfo_Type = DisplayString
_InnerTemperatureInfo_Object = MibTableColumn
innerTemperatureInfo = _InnerTemperatureInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 21),
    _InnerTemperatureInfo_Type()
)
innerTemperatureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innerTemperatureInfo.setStatus("current")


class _FireAlarmResult_Type(Integer32):
    """Custom type fireAlarmResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_FireAlarmResult_Type.__name__ = "Integer32"
_FireAlarmResult_Object = MibTableColumn
fireAlarmResult = _FireAlarmResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 22),
    _FireAlarmResult_Type()
)
fireAlarmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireAlarmResult.setStatus("current")
_FireAlarmChangeTime_Type = DisplayString
_FireAlarmChangeTime_Object = MibTableColumn
fireAlarmChangeTime = _FireAlarmChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 23),
    _FireAlarmChangeTime_Type()
)
fireAlarmChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireAlarmChangeTime.setStatus("current")
_FireAlarmInfo_Type = DisplayString
_FireAlarmInfo_Object = MibTableColumn
fireAlarmInfo = _FireAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 24),
    _FireAlarmInfo_Type()
)
fireAlarmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireAlarmInfo.setStatus("current")


class _BurglarAlarmResult_Type(Integer32):
    """Custom type burglarAlarmResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warn", 2),
          ("ok", 3))
    )


_BurglarAlarmResult_Type.__name__ = "Integer32"
_BurglarAlarmResult_Object = MibTableColumn
burglarAlarmResult = _BurglarAlarmResult_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 25),
    _BurglarAlarmResult_Type()
)
burglarAlarmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    burglarAlarmResult.setStatus("current")
_BurglarAlarmChangeTime_Type = DisplayString
_BurglarAlarmChangeTime_Object = MibTableColumn
burglarAlarmChangeTime = _BurglarAlarmChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 26),
    _BurglarAlarmChangeTime_Type()
)
burglarAlarmChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    burglarAlarmChangeTime.setStatus("current")
_BurglarAlarmInfo_Type = DisplayString
_BurglarAlarmInfo_Object = MibTableColumn
burglarAlarmInfo = _BurglarAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 27),
    _BurglarAlarmInfo_Type()
)
burglarAlarmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    burglarAlarmInfo.setStatus("current")
_TisName_Type = DisplayString
_TisName_Object = MibTableColumn
tisName = _TisName_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 28),
    _TisName_Type()
)
tisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tisName.setStatus("current")
_TisId_Type = DisplayString
_TisId_Object = MibTableColumn
tisId = _TisId_Object(
    (1, 3, 6, 1, 4, 1, 41074, 2524, 2, 1, 1, 1, 29),
    _TisId_Type()
)
tisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tisId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASDEK-TH-MIB",
    **{"voestalpine": voestalpine,
       "tens": tens,
       "asdek": asdek,
       "tis": tis,
       "tisTable": tisTable,
       "tisEntry": tisEntry,
       "tisIndex": tisIndex,
       "selfTestResult": selfTestResult,
       "selfTestTime": selfTestTime,
       "selfTestInfo": selfTestInfo,
       "standByResult": standByResult,
       "standByChangeTime": standByChangeTime,
       "standByInfo": standByInfo,
       "trainDetectionResult": trainDetectionResult,
       "trainDetectionTime": trainDetectionTime,
       "trainNumber": trainNumber,
       "trainDetectionInfo": trainDetectionInfo,
       "powerStatusResult": powerStatusResult,
       "powerStatusChangeTime": powerStatusChangeTime,
       "powerStatusInfo": powerStatusInfo,
       "linkStatusResult": linkStatusResult,
       "linkStatusChangeTime": linkStatusChangeTime,
       "linkStatusInfo": linkStatusInfo,
       "innerTemperatureResult": innerTemperatureResult,
       "innerTemperatureChangeTime": innerTemperatureChangeTime,
       "innerTemperatureValue": innerTemperatureValue,
       "innerTemperatureInfo": innerTemperatureInfo,
       "fireAlarmResult": fireAlarmResult,
       "fireAlarmChangeTime": fireAlarmChangeTime,
       "fireAlarmInfo": fireAlarmInfo,
       "burglarAlarmResult": burglarAlarmResult,
       "burglarAlarmChangeTime": burglarAlarmChangeTime,
       "burglarAlarmInfo": burglarAlarmInfo,
       "tisName": tisName,
       "tisId": tisId}
)
