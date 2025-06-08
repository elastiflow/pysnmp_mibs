# SNMP MIB module (ATPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exalt_25651/ATPC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:22:49 2025
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

(almLocal,
 almRemote,
 perfLocal,
 perfRemote,
 performance,
 radioConfig) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "almLocal",
    "almRemote",
    "perfLocal",
    "perfRemote",
    "performance",
    "radioConfig")

(AlarmLevelT,
 EnableStatusT) = mibBuilder.importSymbols(
    "ExaltComm",
    "AlarmLevelT",
    "EnableStatusT")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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



# MIB Managed Objects in the order of their OIDs

_AdvSystemConfig_ObjectIdentity = ObjectIdentity
advSystemConfig = _AdvSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    advSystemConfig.setStatus("current")
_Atpc_ObjectIdentity = ObjectIdentity
atpc = _Atpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7)
)
if mibBuilder.loadTexts:
    atpc.setStatus("current")
_AtpcEnable_Type = EnableStatusT
_AtpcEnable_Object = MibScalar
atpcEnable = _AtpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 1),
    _AtpcEnable_Type()
)
atpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcEnable.setStatus("current")


class _AtpcRSLThreshold_Type(Integer32):
    """Custom type atpcRSLThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, -500),
    )


_AtpcRSLThreshold_Type.__name__ = "Integer32"
_AtpcRSLThreshold_Object = MibScalar
atpcRSLThreshold = _AtpcRSLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 2),
    _AtpcRSLThreshold_Type()
)
atpcRSLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcRSLThreshold.setStatus("current")
if mibBuilder.loadTexts:
    atpcRSLThreshold.setUnits("Tenths dBm")


class _AtpcMaxTxPower_Type(Integer32):
    """Custom type atpcMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_AtpcMaxTxPower_Type.__name__ = "Integer32"
_AtpcMaxTxPower_Object = MibScalar
atpcMaxTxPower = _AtpcMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 3),
    _AtpcMaxTxPower_Type()
)
atpcMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    atpcMaxTxPower.setUnits("Tenths dBm")
_AtpcTimerControl_Type = EnableStatusT
_AtpcTimerControl_Object = MibScalar
atpcTimerControl = _AtpcTimerControl_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 4),
    _AtpcTimerControl_Type()
)
atpcTimerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcTimerControl.setStatus("current")
_AtpcOverloadProtection_Type = EnableStatusT
_AtpcOverloadProtection_Object = MibScalar
atpcOverloadProtection = _AtpcOverloadProtection_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 5),
    _AtpcOverloadProtection_Type()
)
atpcOverloadProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcOverloadProtection.setStatus("current")


class _AtpcOverloadProtectionRslThreshold_Type(Integer32):
    """Custom type atpcOverloadProtectionRslThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, -200),
    )


_AtpcOverloadProtectionRslThreshold_Type.__name__ = "Integer32"
_AtpcOverloadProtectionRslThreshold_Object = MibScalar
atpcOverloadProtectionRslThreshold = _AtpcOverloadProtectionRslThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 6),
    _AtpcOverloadProtectionRslThreshold_Type()
)
atpcOverloadProtectionRslThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcOverloadProtectionRslThreshold.setStatus("current")
if mibBuilder.loadTexts:
    atpcOverloadProtectionRslThreshold.setUnits("Tenths dBm")


class _AtpcRslHighWmEventTrigger_Type(Integer32):
    """Custom type atpcRslHighWmEventTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, -200),
    )


_AtpcRslHighWmEventTrigger_Type.__name__ = "Integer32"
_AtpcRslHighWmEventTrigger_Object = MibScalar
atpcRslHighWmEventTrigger = _AtpcRslHighWmEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 7),
    _AtpcRslHighWmEventTrigger_Type()
)
atpcRslHighWmEventTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcRslHighWmEventTrigger.setStatus("current")
if mibBuilder.loadTexts:
    atpcRslHighWmEventTrigger.setUnits("Tenths dBm")
_CommitAtpcSettings_Type = DisplayString
_CommitAtpcSettings_Object = MibScalar
commitAtpcSettings = _CommitAtpcSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 7, 1000),
    _CommitAtpcSettings_Type()
)
commitAtpcSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitAtpcSettings.setStatus("current")
_LocAtpcAlarms_ObjectIdentity = ObjectIdentity
locAtpcAlarms = _LocAtpcAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 6)
)
_LocAtpcMaxPower_Type = AlarmLevelT
_LocAtpcMaxPower_Object = MibScalar
locAtpcMaxPower = _LocAtpcMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 6, 1),
    _LocAtpcMaxPower_Type()
)
locAtpcMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAtpcMaxPower.setStatus("current")
_RemAtpcAlarms_ObjectIdentity = ObjectIdentity
remAtpcAlarms = _RemAtpcAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 6)
)
_RemAtpcMaxPower_Type = AlarmLevelT
_RemAtpcMaxPower_Object = MibScalar
remAtpcMaxPower = _RemAtpcMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 6, 1),
    _RemAtpcMaxPower_Type()
)
remAtpcMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remAtpcMaxPower.setStatus("current")
_LocAtpcFarEndTxPwr_Type = Integer32
_LocAtpcFarEndTxPwr_Object = MibScalar
locAtpcFarEndTxPwr = _LocAtpcFarEndTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 31),
    _LocAtpcFarEndTxPwr_Type()
)
locAtpcFarEndTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAtpcFarEndTxPwr.setStatus("current")
_LocAtpcFarEndTxPwrStr_Type = DisplayString
_LocAtpcFarEndTxPwrStr_Object = MibScalar
locAtpcFarEndTxPwrStr = _LocAtpcFarEndTxPwrStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 32),
    _LocAtpcFarEndTxPwrStr_Type()
)
locAtpcFarEndTxPwrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAtpcFarEndTxPwrStr.setStatus("current")
_LocMaxAtpcFarEndTxTimestamp_Type = DisplayString
_LocMaxAtpcFarEndTxTimestamp_Object = MibScalar
locMaxAtpcFarEndTxTimestamp = _LocMaxAtpcFarEndTxTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 33),
    _LocMaxAtpcFarEndTxTimestamp_Type()
)
locMaxAtpcFarEndTxTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaxAtpcFarEndTxTimestamp.setStatus("current")
_RemAtpcFarEndTxPwr_Type = Integer32
_RemAtpcFarEndTxPwr_Object = MibScalar
remAtpcFarEndTxPwr = _RemAtpcFarEndTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 31),
    _RemAtpcFarEndTxPwr_Type()
)
remAtpcFarEndTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remAtpcFarEndTxPwr.setStatus("current")
_RemAtpcFarEndTxPwrStr_Type = DisplayString
_RemAtpcFarEndTxPwrStr_Object = MibScalar
remAtpcFarEndTxPwrStr = _RemAtpcFarEndTxPwrStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 32),
    _RemAtpcFarEndTxPwrStr_Type()
)
remAtpcFarEndTxPwrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remAtpcFarEndTxPwrStr.setStatus("current")
_RemMaxAtpcFarEndTxTimestamp_Type = DisplayString
_RemMaxAtpcFarEndTxTimestamp_Object = MibScalar
remMaxAtpcFarEndTxTimestamp = _RemMaxAtpcFarEndTxTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 33),
    _RemMaxAtpcFarEndTxTimestamp_Type()
)
remMaxAtpcFarEndTxTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMaxAtpcFarEndTxTimestamp.setStatus("current")
_PerfLocalAtpc_ObjectIdentity = ObjectIdentity
perfLocalAtpc = _PerfLocalAtpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 5)
)
_LocMaxPowerElapsedTime_Type = DisplayString
_LocMaxPowerElapsedTime_Object = MibScalar
locMaxPowerElapsedTime = _LocMaxPowerElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 5, 1),
    _LocMaxPowerElapsedTime_Type()
)
locMaxPowerElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaxPowerElapsedTime.setStatus("current")
_LocAtpcActiveElapsedTime_Type = DisplayString
_LocAtpcActiveElapsedTime_Object = MibScalar
locAtpcActiveElapsedTime = _LocAtpcActiveElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 5, 2),
    _LocAtpcActiveElapsedTime_Type()
)
locAtpcActiveElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAtpcActiveElapsedTime.setStatus("current")
_LocTimeSinceResetAtpc_Type = DisplayString
_LocTimeSinceResetAtpc_Object = MibScalar
locTimeSinceResetAtpc = _LocTimeSinceResetAtpc_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 5, 3),
    _LocTimeSinceResetAtpc_Type()
)
locTimeSinceResetAtpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locTimeSinceResetAtpc.setStatus("current")
_LocResetElapsedTime_Type = DisplayString
_LocResetElapsedTime_Object = MibScalar
locResetElapsedTime = _LocResetElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 5, 1000),
    _LocResetElapsedTime_Type()
)
locResetElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locResetElapsedTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATPC-MIB",
    **{"advSystemConfig": advSystemConfig,
       "atpc": atpc,
       "atpcEnable": atpcEnable,
       "atpcRSLThreshold": atpcRSLThreshold,
       "atpcMaxTxPower": atpcMaxTxPower,
       "atpcTimerControl": atpcTimerControl,
       "atpcOverloadProtection": atpcOverloadProtection,
       "atpcOverloadProtectionRslThreshold": atpcOverloadProtectionRslThreshold,
       "atpcRslHighWmEventTrigger": atpcRslHighWmEventTrigger,
       "commitAtpcSettings": commitAtpcSettings,
       "locAtpcAlarms": locAtpcAlarms,
       "locAtpcMaxPower": locAtpcMaxPower,
       "remAtpcAlarms": remAtpcAlarms,
       "remAtpcMaxPower": remAtpcMaxPower,
       "locAtpcFarEndTxPwr": locAtpcFarEndTxPwr,
       "locAtpcFarEndTxPwrStr": locAtpcFarEndTxPwrStr,
       "locMaxAtpcFarEndTxTimestamp": locMaxAtpcFarEndTxTimestamp,
       "remAtpcFarEndTxPwr": remAtpcFarEndTxPwr,
       "remAtpcFarEndTxPwrStr": remAtpcFarEndTxPwrStr,
       "remMaxAtpcFarEndTxTimestamp": remMaxAtpcFarEndTxTimestamp,
       "perfLocalAtpc": perfLocalAtpc,
       "locMaxPowerElapsedTime": locMaxPowerElapsedTime,
       "locAtpcActiveElapsedTime": locAtpcActiveElapsedTime,
       "locTimeSinceResetAtpc": locTimeSinceResetAtpc,
       "locResetElapsedTime": locResetElapsedTime}
)
