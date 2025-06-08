# SNMP MIB module (CIENA-CES-PORT-XCVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-PORT-XCVR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:47 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

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

cienaCesPortXcvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9)
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrMIB.setRevisions(
        ("2017-06-07 00:00",
         "2016-10-07 00:00",
         "2011-08-23 00:00",
         "2011-07-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesPortXcvrMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrMIBObjects = _CienaCesPortXcvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1)
)
_CienaCesPortXcvr_ObjectIdentity = ObjectIdentity
cienaCesPortXcvr = _CienaCesPortXcvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1)
)
_CienaCesPortXcvrTable_Object = MibTable
cienaCesPortXcvrTable = _CienaCesPortXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTable.setStatus("current")
_CienaCesPortXcvrEntry_Object = MibTableRow
cienaCesPortXcvrEntry = _CienaCesPortXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1)
)
cienaCesPortXcvrEntry.setIndexNames(
    (0, "CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrId"),
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrEntry.setStatus("current")


class _CienaCesPortXcvrId_Type(Integer32):
    """Custom type cienaCesPortXcvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrId_Type.__name__ = "Integer32"
_CienaCesPortXcvrId_Object = MibTableColumn
cienaCesPortXcvrId = _CienaCesPortXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 1),
    _CienaCesPortXcvrId_Type()
)
cienaCesPortXcvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPortXcvrId.setStatus("current")


class _CienaCesPortXcvrOperState_Type(Integer32):
    """Custom type cienaCesPortXcvrOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("loopback", 3),
          ("notPresent", 4),
          ("faulted", 5))
    )


_CienaCesPortXcvrOperState_Type.__name__ = "Integer32"
_CienaCesPortXcvrOperState_Object = MibTableColumn
cienaCesPortXcvrOperState = _CienaCesPortXcvrOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 2),
    _CienaCesPortXcvrOperState_Type()
)
cienaCesPortXcvrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrOperState.setStatus("current")


class _CienaCesPortXcvrTemperature_Type(Integer32):
    """Custom type cienaCesPortXcvrTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrTemperature_Type.__name__ = "Integer32"
_CienaCesPortXcvrTemperature_Object = MibTableColumn
cienaCesPortXcvrTemperature = _CienaCesPortXcvrTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 3),
    _CienaCesPortXcvrTemperature_Type()
)
cienaCesPortXcvrTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTemperature.setStatus("current")


class _CienaCesPortXcvrVcc_Type(Integer32):
    """Custom type cienaCesPortXcvrVcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrVcc_Type.__name__ = "Integer32"
_CienaCesPortXcvrVcc_Object = MibTableColumn
cienaCesPortXcvrVcc = _CienaCesPortXcvrVcc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 4),
    _CienaCesPortXcvrVcc_Type()
)
cienaCesPortXcvrVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrVcc.setStatus("current")


class _CienaCesPortXcvrBias_Type(Integer32):
    """Custom type cienaCesPortXcvrBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrBias_Type.__name__ = "Integer32"
_CienaCesPortXcvrBias_Object = MibTableColumn
cienaCesPortXcvrBias = _CienaCesPortXcvrBias_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 5),
    _CienaCesPortXcvrBias_Type()
)
cienaCesPortXcvrBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrBias.setStatus("current")


class _CienaCesPortXcvrRxPower_Type(Integer32):
    """Custom type cienaCesPortXcvrRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrRxPower_Type.__name__ = "Integer32"
_CienaCesPortXcvrRxPower_Object = MibTableColumn
cienaCesPortXcvrRxPower = _CienaCesPortXcvrRxPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 6),
    _CienaCesPortXcvrRxPower_Type()
)
cienaCesPortXcvrRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortXcvrRxPower.setUnits("uW")
_CienaCesPortXcvrHighTempAlarmThreshold_Type = Integer32
_CienaCesPortXcvrHighTempAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrHighTempAlarmThreshold = _CienaCesPortXcvrHighTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 7),
    _CienaCesPortXcvrHighTempAlarmThreshold_Type()
)
cienaCesPortXcvrHighTempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighTempAlarmThreshold.setStatus("current")
_CienaCesPortXcvrLowTempAlarmThreshold_Type = Integer32
_CienaCesPortXcvrLowTempAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrLowTempAlarmThreshold = _CienaCesPortXcvrLowTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 8),
    _CienaCesPortXcvrLowTempAlarmThreshold_Type()
)
cienaCesPortXcvrLowTempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowTempAlarmThreshold.setStatus("current")
_CienaCesPortXcvrHighVccAlarmThreshold_Type = Integer32
_CienaCesPortXcvrHighVccAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrHighVccAlarmThreshold = _CienaCesPortXcvrHighVccAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 9),
    _CienaCesPortXcvrHighVccAlarmThreshold_Type()
)
cienaCesPortXcvrHighVccAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighVccAlarmThreshold.setStatus("current")
_CienaCesPortXcvrLowVccAlarmThreshold_Type = Integer32
_CienaCesPortXcvrLowVccAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrLowVccAlarmThreshold = _CienaCesPortXcvrLowVccAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 10),
    _CienaCesPortXcvrLowVccAlarmThreshold_Type()
)
cienaCesPortXcvrLowVccAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowVccAlarmThreshold.setStatus("current")
_CienaCesPortXcvrHighBiasAlarmThreshold_Type = Integer32
_CienaCesPortXcvrHighBiasAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrHighBiasAlarmThreshold = _CienaCesPortXcvrHighBiasAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 11),
    _CienaCesPortXcvrHighBiasAlarmThreshold_Type()
)
cienaCesPortXcvrHighBiasAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighBiasAlarmThreshold.setStatus("current")
_CienaCesPortXcvrLowBiasAlarmThreshold_Type = Integer32
_CienaCesPortXcvrLowBiasAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrLowBiasAlarmThreshold = _CienaCesPortXcvrLowBiasAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 12),
    _CienaCesPortXcvrLowBiasAlarmThreshold_Type()
)
cienaCesPortXcvrLowBiasAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowBiasAlarmThreshold.setStatus("current")
_CienaCesPortXcvrHighTxPwAlarmThreshold_Type = Integer32
_CienaCesPortXcvrHighTxPwAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrHighTxPwAlarmThreshold = _CienaCesPortXcvrHighTxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 13),
    _CienaCesPortXcvrHighTxPwAlarmThreshold_Type()
)
cienaCesPortXcvrHighTxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighTxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighTxPwAlarmThreshold.setUnits("uW")
_CienaCesPortXcvrLowTxPwAlarmThreshold_Type = Integer32
_CienaCesPortXcvrLowTxPwAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrLowTxPwAlarmThreshold = _CienaCesPortXcvrLowTxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 14),
    _CienaCesPortXcvrLowTxPwAlarmThreshold_Type()
)
cienaCesPortXcvrLowTxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowTxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowTxPwAlarmThreshold.setUnits("uW")
_CienaCesPortXcvrHighRxPwAlarmThreshold_Type = Integer32
_CienaCesPortXcvrHighRxPwAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrHighRxPwAlarmThreshold = _CienaCesPortXcvrHighRxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 15),
    _CienaCesPortXcvrHighRxPwAlarmThreshold_Type()
)
cienaCesPortXcvrHighRxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighRxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortXcvrHighRxPwAlarmThreshold.setUnits("uW")
_CienaCesPortXcvrLowRxPwAlarmThreshold_Type = Integer32
_CienaCesPortXcvrLowRxPwAlarmThreshold_Object = MibTableColumn
cienaCesPortXcvrLowRxPwAlarmThreshold = _CienaCesPortXcvrLowRxPwAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 16),
    _CienaCesPortXcvrLowRxPwAlarmThreshold_Type()
)
cienaCesPortXcvrLowRxPwAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowRxPwAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortXcvrLowRxPwAlarmThreshold.setUnits("uW")


class _CienaCesPortXcvrNotifChassisIndex_Type(Unsigned32):
    """Custom type cienaCesPortXcvrNotifChassisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesPortXcvrNotifChassisIndex_Type.__name__ = "Unsigned32"
_CienaCesPortXcvrNotifChassisIndex_Object = MibTableColumn
cienaCesPortXcvrNotifChassisIndex = _CienaCesPortXcvrNotifChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 17),
    _CienaCesPortXcvrNotifChassisIndex_Type()
)
cienaCesPortXcvrNotifChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortXcvrNotifChassisIndex.setStatus("current")


class _CienaCesPortXcvrNotifShelfIndex_Type(Unsigned32):
    """Custom type cienaCesPortXcvrNotifShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesPortXcvrNotifShelfIndex_Type.__name__ = "Unsigned32"
_CienaCesPortXcvrNotifShelfIndex_Object = MibTableColumn
cienaCesPortXcvrNotifShelfIndex = _CienaCesPortXcvrNotifShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 18),
    _CienaCesPortXcvrNotifShelfIndex_Type()
)
cienaCesPortXcvrNotifShelfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortXcvrNotifShelfIndex.setStatus("current")


class _CienaCesPortXcvrNotifSlotIndex_Type(Unsigned32):
    """Custom type cienaCesPortXcvrNotifSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CienaCesPortXcvrNotifSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesPortXcvrNotifSlotIndex_Object = MibTableColumn
cienaCesPortXcvrNotifSlotIndex = _CienaCesPortXcvrNotifSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 19),
    _CienaCesPortXcvrNotifSlotIndex_Type()
)
cienaCesPortXcvrNotifSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortXcvrNotifSlotIndex.setStatus("current")


class _CienaCesPortXcvrNotifPortNumber_Type(Unsigned32):
    """Custom type cienaCesPortXcvrNotifPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrNotifPortNumber_Type.__name__ = "Unsigned32"
_CienaCesPortXcvrNotifPortNumber_Object = MibTableColumn
cienaCesPortXcvrNotifPortNumber = _CienaCesPortXcvrNotifPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 20),
    _CienaCesPortXcvrNotifPortNumber_Type()
)
cienaCesPortXcvrNotifPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortXcvrNotifPortNumber.setStatus("current")


class _CienaCesPortXcvrIdentiferType_Type(Integer32):
    """Custom type cienaCesPortXcvrIdentiferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("gbic", 2),
          ("solderedType", 3),
          ("sfp", 4),
          ("xbi", 5),
          ("xenpak", 6),
          ("xfp", 7),
          ("xff", 8),
          ("xfpe", 9),
          ("xpak", 10),
          ("x2", 11),
          ("reserved", 12),
          ("vendorSpecific", 13))
    )


_CienaCesPortXcvrIdentiferType_Type.__name__ = "Integer32"
_CienaCesPortXcvrIdentiferType_Object = MibTableColumn
cienaCesPortXcvrIdentiferType = _CienaCesPortXcvrIdentiferType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 21),
    _CienaCesPortXcvrIdentiferType_Type()
)
cienaCesPortXcvrIdentiferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrIdentiferType.setStatus("current")
_CienaCesPortXcvrExtIdentiferType_Type = Integer32
_CienaCesPortXcvrExtIdentiferType_Object = MibTableColumn
cienaCesPortXcvrExtIdentiferType = _CienaCesPortXcvrExtIdentiferType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 22),
    _CienaCesPortXcvrExtIdentiferType_Type()
)
cienaCesPortXcvrExtIdentiferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrExtIdentiferType.setStatus("current")


class _CienaCesPortXcvrConnectorType_Type(Integer32):
    """Custom type cienaCesPortXcvrConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrConnectorType_Type.__name__ = "Integer32"
_CienaCesPortXcvrConnectorType_Object = MibTableColumn
cienaCesPortXcvrConnectorType = _CienaCesPortXcvrConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 23),
    _CienaCesPortXcvrConnectorType_Type()
)
cienaCesPortXcvrConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrConnectorType.setStatus("current")


class _CienaCesPortXcvrType_Type(Integer32):
    """Custom type cienaCesPortXcvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrType_Type.__name__ = "Integer32"
_CienaCesPortXcvrType_Object = MibTableColumn
cienaCesPortXcvrType = _CienaCesPortXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 24),
    _CienaCesPortXcvrType_Type()
)
cienaCesPortXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrType.setStatus("current")
_CienaCesPortXcvrVendorName_Type = DisplayString
_CienaCesPortXcvrVendorName_Object = MibTableColumn
cienaCesPortXcvrVendorName = _CienaCesPortXcvrVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 25),
    _CienaCesPortXcvrVendorName_Type()
)
cienaCesPortXcvrVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrVendorName.setStatus("current")


class _CienaCesPortXcvrVendorOUI_Type(OctetString):
    """Custom type cienaCesPortXcvrVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesPortXcvrVendorOUI_Type.__name__ = "OctetString"
_CienaCesPortXcvrVendorOUI_Object = MibTableColumn
cienaCesPortXcvrVendorOUI = _CienaCesPortXcvrVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 26),
    _CienaCesPortXcvrVendorOUI_Type()
)
cienaCesPortXcvrVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrVendorOUI.setStatus("current")
_CienaCesPortXcvrVendorPartNum_Type = DisplayString
_CienaCesPortXcvrVendorPartNum_Object = MibTableColumn
cienaCesPortXcvrVendorPartNum = _CienaCesPortXcvrVendorPartNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 27),
    _CienaCesPortXcvrVendorPartNum_Type()
)
cienaCesPortXcvrVendorPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrVendorPartNum.setStatus("current")
_CienaCesPortXcvrRevNum_Type = DisplayString
_CienaCesPortXcvrRevNum_Object = MibTableColumn
cienaCesPortXcvrRevNum = _CienaCesPortXcvrRevNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 28),
    _CienaCesPortXcvrRevNum_Type()
)
cienaCesPortXcvrRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrRevNum.setStatus("current")
_CienaCesPortXcvrSerialNum_Type = DisplayString
_CienaCesPortXcvrSerialNum_Object = MibTableColumn
cienaCesPortXcvrSerialNum = _CienaCesPortXcvrSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 29),
    _CienaCesPortXcvrSerialNum_Type()
)
cienaCesPortXcvrSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrSerialNum.setStatus("current")
_CienaCesPortXcvrMfgDate_Type = DisplayString
_CienaCesPortXcvrMfgDate_Object = MibTableColumn
cienaCesPortXcvrMfgDate = _CienaCesPortXcvrMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 30),
    _CienaCesPortXcvrMfgDate_Type()
)
cienaCesPortXcvrMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrMfgDate.setStatus("current")


class _CienaCesPortXcvrWaveLength_Type(Integer32):
    """Custom type cienaCesPortXcvrWaveLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrWaveLength_Type.__name__ = "Integer32"
_CienaCesPortXcvrWaveLength_Object = MibTableColumn
cienaCesPortXcvrWaveLength = _CienaCesPortXcvrWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 31),
    _CienaCesPortXcvrWaveLength_Type()
)
cienaCesPortXcvrWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrWaveLength.setStatus("current")


class _CienaCesPortXcvrTxState_Type(Integer32):
    """Custom type cienaCesPortXcvrTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesPortXcvrTxState_Type.__name__ = "Integer32"
_CienaCesPortXcvrTxState_Object = MibTableColumn
cienaCesPortXcvrTxState = _CienaCesPortXcvrTxState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 32),
    _CienaCesPortXcvrTxState_Type()
)
cienaCesPortXcvrTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxState.setStatus("current")


class _CienaCesPortXcvrTxFaultStatus_Type(Integer32):
    """Custom type cienaCesPortXcvrTxFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("noFault", 2))
    )


_CienaCesPortXcvrTxFaultStatus_Type.__name__ = "Integer32"
_CienaCesPortXcvrTxFaultStatus_Object = MibTableColumn
cienaCesPortXcvrTxFaultStatus = _CienaCesPortXcvrTxFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 33),
    _CienaCesPortXcvrTxFaultStatus_Type()
)
cienaCesPortXcvrTxFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxFaultStatus.setStatus("current")


class _CienaCesPortXcvrAdminState_Type(Integer32):
    """Custom type cienaCesPortXcvrAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("loopback", 3))
    )


_CienaCesPortXcvrAdminState_Type.__name__ = "Integer32"
_CienaCesPortXcvrAdminState_Object = MibTableColumn
cienaCesPortXcvrAdminState = _CienaCesPortXcvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 34),
    _CienaCesPortXcvrAdminState_Type()
)
cienaCesPortXcvrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrAdminState.setStatus("current")


class _CienaCesPortXcvrTxOutputPower_Type(Integer32):
    """Custom type cienaCesPortXcvrTxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortXcvrTxOutputPower_Type.__name__ = "Integer32"
_CienaCesPortXcvrTxOutputPower_Object = MibTableColumn
cienaCesPortXcvrTxOutputPower = _CienaCesPortXcvrTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 1, 1, 1, 35),
    _CienaCesPortXcvrTxOutputPower_Type()
)
cienaCesPortXcvrTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxOutputPower.setUnits("uW")
_CienaCesPortXcvrNotif_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrNotif = _CienaCesPortXcvrNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 2)
)


class _CienaCesPortXcvrEventType_Type(Integer32):
    """Custom type cienaCesPortXcvrEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("removed", 2))
    )


_CienaCesPortXcvrEventType_Type.__name__ = "Integer32"
_CienaCesPortXcvrEventType_Object = MibScalar
cienaCesPortXcvrEventType = _CienaCesPortXcvrEventType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 2, 1),
    _CienaCesPortXcvrEventType_Type()
)
cienaCesPortXcvrEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortXcvrEventType.setStatus("current")


class _CienaCesPortXcvrErrorType_Type(Integer32):
    """Custom type cienaCesPortXcvrErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("chksumFailed", 1),
          ("opticalFault", 2))
    )


_CienaCesPortXcvrErrorType_Type.__name__ = "Integer32"
_CienaCesPortXcvrErrorType_Object = MibScalar
cienaCesPortXcvrErrorType = _CienaCesPortXcvrErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 1, 2, 2),
    _CienaCesPortXcvrErrorType_Type()
)
cienaCesPortXcvrErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortXcvrErrorType.setStatus("current")
_CienaCesPortXcvrMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrMIBConformance = _CienaCesPortXcvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 3)
)
_CienaCesPortXcvrMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrMIBCompliances = _CienaCesPortXcvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 3, 1)
)
_CienaCesPortXcvrMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrMIBGroups = _CienaCesPortXcvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 9, 3, 2)
)
_CienaCesPortXcvrMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrMIBNotificationPrefix = _CienaCesPortXcvrMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9)
)
_CienaCesPortXcvrMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesPortXcvrMIBNotifications = _CienaCesPortXcvrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0)
)

# Managed Objects groups


# Notification objects

cienaCesPortXcvrRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 1)
)
cienaCesPortXcvrRemovedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrRemovedNotification.setStatus(
        "current"
    )

cienaCesPortXcvrInsertedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 2)
)
cienaCesPortXcvrInsertedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrInsertedNotification.setStatus(
        "current"
    )

cienaCesPortXcvrErrorTypeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 5)
)
cienaCesPortXcvrErrorTypeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrErrorType"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrErrorTypeNotification.setStatus(
        "current"
    )

cienaCesPortXcvrTempHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 6)
)
cienaCesPortXcvrTempHighNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTempHighNotification.setStatus(
        "current"
    )

cienaCesPortXcvrTempLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 7)
)
cienaCesPortXcvrTempLowNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTempLowNotification.setStatus(
        "current"
    )

cienaCesPortXcvrTempNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 8)
)
cienaCesPortXcvrTempNormalNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTempNormalNotification.setStatus(
        "current"
    )

cienaCesPortXcvrVoltageHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 9)
)
cienaCesPortXcvrVoltageHighNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrVoltageHighNotification.setStatus(
        "current"
    )

cienaCesPortXcvrVoltageLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 10)
)
cienaCesPortXcvrVoltageLowNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrVoltageLowNotification.setStatus(
        "current"
    )

cienaCesPortXcvrVoltageNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 11)
)
cienaCesPortXcvrVoltageNormalNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrVoltageNormalNotification.setStatus(
        "current"
    )

cienaCesPortXcvrBiasHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 12)
)
cienaCesPortXcvrBiasHighNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrBiasHighNotification.setStatus(
        "current"
    )

cienaCesPortXcvrBiasLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 13)
)
cienaCesPortXcvrBiasLowNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrBiasLowNotification.setStatus(
        "current"
    )

cienaCesPortXcvrBiasNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 14)
)
cienaCesPortXcvrBiasNormalNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrBiasNormalNotification.setStatus(
        "current"
    )

cienaCesPortXcvrTxPowerHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 15)
)
cienaCesPortXcvrTxPowerHighNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxPowerHighNotification.setStatus(
        "current"
    )

cienaCesPortXcvrTxPowerLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 16)
)
cienaCesPortXcvrTxPowerLowNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxPowerLowNotification.setStatus(
        "current"
    )

cienaCesPortXcvrTxPowerNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 17)
)
cienaCesPortXcvrTxPowerNormalNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrTxPowerNormalNotification.setStatus(
        "current"
    )

cienaCesPortXcvrRxPowerHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 18)
)
cienaCesPortXcvrRxPowerHighNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrRxPowerHighNotification.setStatus(
        "current"
    )

cienaCesPortXcvrRxPowerLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 19)
)
cienaCesPortXcvrRxPowerLowNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrRxPowerLowNotification.setStatus(
        "current"
    )

cienaCesPortXcvrRxPowerNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 20)
)
cienaCesPortXcvrRxPowerNormalNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrRxPowerNormalNotification.setStatus(
        "current"
    )

cienaCesPortXcvrSpeedInfoMissingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 21)
)
cienaCesPortXcvrSpeedInfoMissingNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrSpeedInfoMissingNotification.setStatus(
        "current"
    )

cienaCesPortXcvrUncertifiedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 9, 0, 22)
)
cienaCesPortXcvrUncertifiedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifChassisIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifShelfIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifSlotIndex"),
        ("CIENA-CES-PORT-XCVR-MIB", "cienaCesPortXcvrNotifPortNumber"))
)
if mibBuilder.loadTexts:
    cienaCesPortXcvrUncertifiedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-PORT-XCVR-MIB",
    **{"cienaCesPortXcvrMIB": cienaCesPortXcvrMIB,
       "cienaCesPortXcvrMIBObjects": cienaCesPortXcvrMIBObjects,
       "cienaCesPortXcvr": cienaCesPortXcvr,
       "cienaCesPortXcvrTable": cienaCesPortXcvrTable,
       "cienaCesPortXcvrEntry": cienaCesPortXcvrEntry,
       "cienaCesPortXcvrId": cienaCesPortXcvrId,
       "cienaCesPortXcvrOperState": cienaCesPortXcvrOperState,
       "cienaCesPortXcvrTemperature": cienaCesPortXcvrTemperature,
       "cienaCesPortXcvrVcc": cienaCesPortXcvrVcc,
       "cienaCesPortXcvrBias": cienaCesPortXcvrBias,
       "cienaCesPortXcvrRxPower": cienaCesPortXcvrRxPower,
       "cienaCesPortXcvrHighTempAlarmThreshold": cienaCesPortXcvrHighTempAlarmThreshold,
       "cienaCesPortXcvrLowTempAlarmThreshold": cienaCesPortXcvrLowTempAlarmThreshold,
       "cienaCesPortXcvrHighVccAlarmThreshold": cienaCesPortXcvrHighVccAlarmThreshold,
       "cienaCesPortXcvrLowVccAlarmThreshold": cienaCesPortXcvrLowVccAlarmThreshold,
       "cienaCesPortXcvrHighBiasAlarmThreshold": cienaCesPortXcvrHighBiasAlarmThreshold,
       "cienaCesPortXcvrLowBiasAlarmThreshold": cienaCesPortXcvrLowBiasAlarmThreshold,
       "cienaCesPortXcvrHighTxPwAlarmThreshold": cienaCesPortXcvrHighTxPwAlarmThreshold,
       "cienaCesPortXcvrLowTxPwAlarmThreshold": cienaCesPortXcvrLowTxPwAlarmThreshold,
       "cienaCesPortXcvrHighRxPwAlarmThreshold": cienaCesPortXcvrHighRxPwAlarmThreshold,
       "cienaCesPortXcvrLowRxPwAlarmThreshold": cienaCesPortXcvrLowRxPwAlarmThreshold,
       "cienaCesPortXcvrNotifChassisIndex": cienaCesPortXcvrNotifChassisIndex,
       "cienaCesPortXcvrNotifShelfIndex": cienaCesPortXcvrNotifShelfIndex,
       "cienaCesPortXcvrNotifSlotIndex": cienaCesPortXcvrNotifSlotIndex,
       "cienaCesPortXcvrNotifPortNumber": cienaCesPortXcvrNotifPortNumber,
       "cienaCesPortXcvrIdentiferType": cienaCesPortXcvrIdentiferType,
       "cienaCesPortXcvrExtIdentiferType": cienaCesPortXcvrExtIdentiferType,
       "cienaCesPortXcvrConnectorType": cienaCesPortXcvrConnectorType,
       "cienaCesPortXcvrType": cienaCesPortXcvrType,
       "cienaCesPortXcvrVendorName": cienaCesPortXcvrVendorName,
       "cienaCesPortXcvrVendorOUI": cienaCesPortXcvrVendorOUI,
       "cienaCesPortXcvrVendorPartNum": cienaCesPortXcvrVendorPartNum,
       "cienaCesPortXcvrRevNum": cienaCesPortXcvrRevNum,
       "cienaCesPortXcvrSerialNum": cienaCesPortXcvrSerialNum,
       "cienaCesPortXcvrMfgDate": cienaCesPortXcvrMfgDate,
       "cienaCesPortXcvrWaveLength": cienaCesPortXcvrWaveLength,
       "cienaCesPortXcvrTxState": cienaCesPortXcvrTxState,
       "cienaCesPortXcvrTxFaultStatus": cienaCesPortXcvrTxFaultStatus,
       "cienaCesPortXcvrAdminState": cienaCesPortXcvrAdminState,
       "cienaCesPortXcvrTxOutputPower": cienaCesPortXcvrTxOutputPower,
       "cienaCesPortXcvrNotif": cienaCesPortXcvrNotif,
       "cienaCesPortXcvrEventType": cienaCesPortXcvrEventType,
       "cienaCesPortXcvrErrorType": cienaCesPortXcvrErrorType,
       "cienaCesPortXcvrMIBConformance": cienaCesPortXcvrMIBConformance,
       "cienaCesPortXcvrMIBCompliances": cienaCesPortXcvrMIBCompliances,
       "cienaCesPortXcvrMIBGroups": cienaCesPortXcvrMIBGroups,
       "cienaCesPortXcvrMIBNotificationPrefix": cienaCesPortXcvrMIBNotificationPrefix,
       "cienaCesPortXcvrMIBNotifications": cienaCesPortXcvrMIBNotifications,
       "cienaCesPortXcvrRemovedNotification": cienaCesPortXcvrRemovedNotification,
       "cienaCesPortXcvrInsertedNotification": cienaCesPortXcvrInsertedNotification,
       "cienaCesPortXcvrErrorTypeNotification": cienaCesPortXcvrErrorTypeNotification,
       "cienaCesPortXcvrTempHighNotification": cienaCesPortXcvrTempHighNotification,
       "cienaCesPortXcvrTempLowNotification": cienaCesPortXcvrTempLowNotification,
       "cienaCesPortXcvrTempNormalNotification": cienaCesPortXcvrTempNormalNotification,
       "cienaCesPortXcvrVoltageHighNotification": cienaCesPortXcvrVoltageHighNotification,
       "cienaCesPortXcvrVoltageLowNotification": cienaCesPortXcvrVoltageLowNotification,
       "cienaCesPortXcvrVoltageNormalNotification": cienaCesPortXcvrVoltageNormalNotification,
       "cienaCesPortXcvrBiasHighNotification": cienaCesPortXcvrBiasHighNotification,
       "cienaCesPortXcvrBiasLowNotification": cienaCesPortXcvrBiasLowNotification,
       "cienaCesPortXcvrBiasNormalNotification": cienaCesPortXcvrBiasNormalNotification,
       "cienaCesPortXcvrTxPowerHighNotification": cienaCesPortXcvrTxPowerHighNotification,
       "cienaCesPortXcvrTxPowerLowNotification": cienaCesPortXcvrTxPowerLowNotification,
       "cienaCesPortXcvrTxPowerNormalNotification": cienaCesPortXcvrTxPowerNormalNotification,
       "cienaCesPortXcvrRxPowerHighNotification": cienaCesPortXcvrRxPowerHighNotification,
       "cienaCesPortXcvrRxPowerLowNotification": cienaCesPortXcvrRxPowerLowNotification,
       "cienaCesPortXcvrRxPowerNormalNotification": cienaCesPortXcvrRxPowerNormalNotification,
       "cienaCesPortXcvrSpeedInfoMissingNotification": cienaCesPortXcvrSpeedInfoMissingNotification,
       "cienaCesPortXcvrUncertifiedNotification": cienaCesPortXcvrUncertifiedNotification}
)
