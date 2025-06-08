# SNMP MIB module (BTRM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/twinfalls_34506/BTRM.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:23 2025
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

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

(KeyChange,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "KeyChange")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



class TFTUsmAuthPrivProtocol(TextualConvention, Integer32):
    status = "mandatory"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAuthProtocol", 1),
          ("hmacMD5Auth", 2),
          ("hmacSHAAuth", 3),
          ("noPrivProtocol", 4),
          ("desPrivProtocol", 5),
          ("aesPrivProtocol", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Btrm_ObjectIdentity = ObjectIdentity
btrm = _Btrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 34506, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 34506, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 34506, 1, 3),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("mandatory")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506, 2)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 34506, 2, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 34506, 2, 1, 1)
)
trapEntry.setIndexNames(
    (0, "BTRM", "trapReceiverNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")


class _TrapReceiverNumber_Type(Integer32):
    """Custom type trapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrapReceiverNumber_Type.__name__ = "Integer32"
_TrapReceiverNumber_Object = MibTableColumn
trapReceiverNumber = _TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 34506, 2, 1, 1, 1),
    _TrapReceiverNumber_Type()
)
trapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapReceiverNumber.setStatus("mandatory")


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibTableColumn
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34506, 2, 1, 1, 2),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("mandatory")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibTableColumn
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 34506, 2, 1, 1, 3),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("mandatory")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 34506, 2, 1, 1, 4),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506, 3)
)


class _LowBattCapacityalarm_Type(Integer32):
    """Custom type lowBattCapacityalarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LowBattCapacityalarm_Type.__name__ = "Integer32"
_LowBattCapacityalarm_Object = MibScalar
lowBattCapacityalarm = _LowBattCapacityalarm_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 1),
    _LowBattCapacityalarm_Type()
)
lowBattCapacityalarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowBattCapacityalarm.setStatus("mandatory")


class _LowBatteryVoltagealarm_Type(Integer32):
    """Custom type lowBatteryVoltagealarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LowBatteryVoltagealarm_Type.__name__ = "Integer32"
_LowBatteryVoltagealarm_Object = MibScalar
lowBatteryVoltagealarm = _LowBatteryVoltagealarm_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 2),
    _LowBatteryVoltagealarm_Type()
)
lowBatteryVoltagealarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowBatteryVoltagealarm.setStatus("mandatory")


class _IoChan1alarm_Type(Integer32):
    """Custom type ioChan1alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_IoChan1alarm_Type.__name__ = "Integer32"
_IoChan1alarm_Object = MibScalar
ioChan1alarm = _IoChan1alarm_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 3),
    _IoChan1alarm_Type()
)
ioChan1alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioChan1alarm.setStatus("mandatory")


class _IoChan2alarm_Type(Integer32):
    """Custom type ioChan2alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_IoChan2alarm_Type.__name__ = "Integer32"
_IoChan2alarm_Object = MibScalar
ioChan2alarm = _IoChan2alarm_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 4),
    _IoChan2alarm_Type()
)
ioChan2alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioChan2alarm.setStatus("mandatory")
_BatteryVoltage_Type = Integer32
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 20),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("mandatory")
_BatteryCurrentPositive_Type = Integer32
_BatteryCurrentPositive_Object = MibScalar
batteryCurrentPositive = _BatteryCurrentPositive_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 21),
    _BatteryCurrentPositive_Type()
)
batteryCurrentPositive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentPositive.setStatus("mandatory")
_BatteryCurrentNegative_Type = Integer32
_BatteryCurrentNegative_Object = MibScalar
batteryCurrentNegative = _BatteryCurrentNegative_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 22),
    _BatteryCurrentNegative_Type()
)
batteryCurrentNegative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentNegative.setStatus("mandatory")
_PowerSupply_Type = Integer32
_PowerSupply_Object = MibScalar
powerSupply = _PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 23),
    _PowerSupply_Type()
)
powerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply.setStatus("mandatory")
_ExpectedRunTime_Type = Integer32
_ExpectedRunTime_Object = MibScalar
expectedRunTime = _ExpectedRunTime_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 24),
    _ExpectedRunTime_Type()
)
expectedRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expectedRunTime.setStatus("mandatory")
_LastRunTime_Type = Integer32
_LastRunTime_Object = MibScalar
lastRunTime = _LastRunTime_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 25),
    _LastRunTime_Type()
)
lastRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastRunTime.setStatus("mandatory")
_IoChan1analog_Type = Integer32
_IoChan1analog_Object = MibScalar
ioChan1analog = _IoChan1analog_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 26),
    _IoChan1analog_Type()
)
ioChan1analog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioChan1analog.setStatus("mandatory")
_IoChan2analog_Type = Integer32
_IoChan2analog_Object = MibScalar
ioChan2analog = _IoChan2analog_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 27),
    _IoChan2analog_Type()
)
ioChan2analog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioChan2analog.setStatus("mandatory")
_Systemtemperature_Type = Integer32
_Systemtemperature_Object = MibScalar
systemtemperature = _Systemtemperature_Object(
    (1, 3, 6, 1, 4, 1, 34506, 3, 28),
    _Systemtemperature_Type()
)
systemtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemtemperature.setStatus("mandatory")
_SnmpUsm_ObjectIdentity = ObjectIdentity
snmpUsm = _SnmpUsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506, 4)
)
_MchpUsmUserTable_Object = MibTable
mchpUsmUserTable = _MchpUsmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1)
)
if mibBuilder.loadTexts:
    mchpUsmUserTable.setStatus("mandatory")
_MchpUsmUserEntry_Object = MibTableRow
mchpUsmUserEntry = _MchpUsmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1)
)
mchpUsmUserEntry.setIndexNames(
    (0, "BTRM", "usmIndex"),
)
if mibBuilder.loadTexts:
    mchpUsmUserEntry.setStatus("mandatory")


class _UsmIndex_Type(Integer32):
    """Custom type usmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UsmIndex_Type.__name__ = "Integer32"
_UsmIndex_Object = MibTableColumn
usmIndex = _UsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1, 1),
    _UsmIndex_Type()
)
usmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usmIndex.setStatus("mandatory")
_UsmSecurityName_Type = SnmpAdminString
_UsmSecurityName_Object = MibTableColumn
usmSecurityName = _UsmSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1, 2),
    _UsmSecurityName_Type()
)
usmSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmSecurityName.setStatus("mandatory")
_UsmAuthProtocol_Type = TFTUsmAuthPrivProtocol
_UsmAuthProtocol_Object = MibTableColumn
usmAuthProtocol = _UsmAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1, 3),
    _UsmAuthProtocol_Type()
)
usmAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmAuthProtocol.setStatus("mandatory")
_UsmAuthKey_Type = KeyChange
_UsmAuthKey_Object = MibTableColumn
usmAuthKey = _UsmAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1, 4),
    _UsmAuthKey_Type()
)
usmAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmAuthKey.setStatus("mandatory")
_UsmPrivProtocol_Type = TFTUsmAuthPrivProtocol
_UsmPrivProtocol_Object = MibTableColumn
usmPrivProtocol = _UsmPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1, 5),
    _UsmPrivProtocol_Type()
)
usmPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmPrivProtocol.setStatus("mandatory")
_UsmPrivKey_Type = KeyChange
_UsmPrivKey_Object = MibTableColumn
usmPrivKey = _UsmPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 34506, 4, 1, 1, 6),
    _UsmPrivKey_Type()
)
usmPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmPrivKey.setStatus("mandatory")
_SnmpTrap_ObjectIdentity = ObjectIdentity
snmpTrap = _SnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506, 5)
)
_MchpTargetTable_Object = MibTable
mchpTargetTable = _MchpTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1)
)
if mibBuilder.loadTexts:
    mchpTargetTable.setStatus("mandatory")
_MchpTargetEntry_Object = MibTableRow
mchpTargetEntry = _MchpTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1, 1)
)
mchpTargetEntry.setIndexNames(
    (0, "BTRM", "snmpTargetIndex"),
)
if mibBuilder.loadTexts:
    mchpTargetEntry.setStatus("mandatory")


class _SnmpTargetIndex_Type(Integer32):
    """Custom type snmpTargetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpTargetIndex_Type.__name__ = "Integer32"
_SnmpTargetIndex_Object = MibTableColumn
snmpTargetIndex = _SnmpTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1, 1, 1),
    _SnmpTargetIndex_Type()
)
snmpTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTargetIndex.setStatus("mandatory")
_SnmpTargetMPModel_Type = SnmpMessageProcessingModel
_SnmpTargetMPModel_Object = MibTableColumn
snmpTargetMPModel = _SnmpTargetMPModel_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1, 1, 2),
    _SnmpTargetMPModel_Type()
)
snmpTargetMPModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTargetMPModel.setStatus("mandatory")


class _SnmpTargetSecurityModel_Type(SnmpSecurityModel):
    """Custom type snmpTargetSecurityModel based on SnmpSecurityModel"""
    subtypeSpec = SnmpSecurityModel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpTargetSecurityModel_Type.__name__ = "SnmpSecurityModel"
_SnmpTargetSecurityModel_Object = MibTableColumn
snmpTargetSecurityModel = _SnmpTargetSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1, 1, 3),
    _SnmpTargetSecurityModel_Type()
)
snmpTargetSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTargetSecurityModel.setStatus("mandatory")
_SnmpTargetSecurityName_Type = SnmpAdminString
_SnmpTargetSecurityName_Object = MibTableColumn
snmpTargetSecurityName = _SnmpTargetSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1, 1, 4),
    _SnmpTargetSecurityName_Type()
)
snmpTargetSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTargetSecurityName.setStatus("mandatory")
_SnmpTargetSecurityLevel_Type = SnmpSecurityLevel
_SnmpTargetSecurityLevel_Object = MibTableColumn
snmpTargetSecurityLevel = _SnmpTargetSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 34506, 5, 1, 1, 5),
    _SnmpTargetSecurityLevel_Type()
)
snmpTargetSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTargetSecurityLevel.setStatus("mandatory")
_Snmpv3PvtObject_ObjectIdentity = ObjectIdentity
snmpv3PvtObject = _Snmpv3PvtObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34506, 6)
)
_Snmpv3PvtDemoObject_Type = Integer32
_Snmpv3PvtDemoObject_Object = MibScalar
snmpv3PvtDemoObject = _Snmpv3PvtDemoObject_Object(
    (1, 3, 6, 1, 4, 1, 34506, 6, 1),
    _Snmpv3PvtDemoObject_Type()
)
snmpv3PvtDemoObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3PvtDemoObject.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTRM",
    **{"TFTUsmAuthPrivProtocol": TFTUsmAuthPrivProtocol,
       "btrm": btrm,
       "product": product,
       "name": name,
       "version": version,
       "date": date,
       "setup": setup,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapReceiverNumber": trapReceiverNumber,
       "trapEnabled": trapEnabled,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapCommunity": trapCommunity,
       "control": control,
       "lowBattCapacityalarm": lowBattCapacityalarm,
       "lowBatteryVoltagealarm": lowBatteryVoltagealarm,
       "ioChan1alarm": ioChan1alarm,
       "ioChan2alarm": ioChan2alarm,
       "batteryVoltage": batteryVoltage,
       "batteryCurrentPositive": batteryCurrentPositive,
       "batteryCurrentNegative": batteryCurrentNegative,
       "powerSupply": powerSupply,
       "expectedRunTime": expectedRunTime,
       "lastRunTime": lastRunTime,
       "ioChan1analog": ioChan1analog,
       "ioChan2analog": ioChan2analog,
       "systemtemperature": systemtemperature,
       "snmpUsm": snmpUsm,
       "mchpUsmUserTable": mchpUsmUserTable,
       "mchpUsmUserEntry": mchpUsmUserEntry,
       "usmIndex": usmIndex,
       "usmSecurityName": usmSecurityName,
       "usmAuthProtocol": usmAuthProtocol,
       "usmAuthKey": usmAuthKey,
       "usmPrivProtocol": usmPrivProtocol,
       "usmPrivKey": usmPrivKey,
       "snmpTrap": snmpTrap,
       "mchpTargetTable": mchpTargetTable,
       "mchpTargetEntry": mchpTargetEntry,
       "snmpTargetIndex": snmpTargetIndex,
       "snmpTargetMPModel": snmpTargetMPModel,
       "snmpTargetSecurityModel": snmpTargetSecurityModel,
       "snmpTargetSecurityName": snmpTargetSecurityName,
       "snmpTargetSecurityLevel": snmpTargetSecurityLevel,
       "snmpv3PvtObject": snmpv3PvtObject,
       "snmpv3PvtDemoObject": snmpv3PvtDemoObject}
)
