# SNMP MIB module (NMR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/opengate_29414/NMR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:53:41 2025
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

newmar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29414)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Spm_ObjectIdentity = ObjectIdentity
spm = _Spm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = DisplayString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = DisplayString
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 5),
    _ProductUrl_Type()
)
productUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productUrl.setStatus("current")


class _AlarmTripType_Type(Integer32):
    """Custom type alarmTripType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AlarmTripType_Type.__name__ = "Integer32"
_AlarmTripType_Object = MibScalar
alarmTripType = _AlarmTripType_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 6),
    _AlarmTripType_Type()
)
alarmTripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTripType.setStatus("current")
_ProductHardware_Type = DisplayString
_ProductHardware_Object = MibScalar
productHardware = _ProductHardware_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 7),
    _ProductHardware_Type()
)
productHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHardware.setStatus("current")
_SensorCountsBase_ObjectIdentity = ObjectIdentity
sensorCountsBase = _SensorCountsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8)
)
_SensorCounts_ObjectIdentity = ObjectIdentity
sensorCounts = _SensorCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1)
)


class _SpmCount_Type(Integer32):
    """Custom type spmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SpmCount_Type.__name__ = "Integer32"
_SpmCount_Object = MibScalar
spmCount = _SpmCount_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 2),
    _SpmCount_Type()
)
spmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmCount.setStatus("current")
_SpmTable_Object = MibTable
spmTable = _SpmTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2)
)
if mibBuilder.loadTexts:
    spmTable.setStatus("current")
_SpmEntry_Object = MibTableRow
spmEntry = _SpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1)
)
spmEntry.setIndexNames(
    (0, "NMR-MIB", "spmIndex"),
)
if mibBuilder.loadTexts:
    spmEntry.setStatus("current")


class _SpmIndex_Type(Integer32):
    """Custom type spmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SpmIndex_Type.__name__ = "Integer32"
_SpmIndex_Object = MibTableColumn
spmIndex = _SpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 1),
    _SpmIndex_Type()
)
spmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spmIndex.setStatus("current")
_SpmSerial_Type = DisplayString
_SpmSerial_Object = MibTableColumn
spmSerial = _SpmSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 2),
    _SpmSerial_Type()
)
spmSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmSerial.setStatus("current")
_SpmName_Type = DisplayString
_SpmName_Object = MibTableColumn
spmName = _SpmName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 3),
    _SpmName_Type()
)
spmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmName.setStatus("current")
_SpmAvail_Type = Unsigned32
_SpmAvail_Object = MibTableColumn
spmAvail = _SpmAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 4),
    _SpmAvail_Type()
)
spmAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmAvail.setStatus("current")


class _SpmTempC_Type(Integer32):
    """Custom type spmTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_SpmTempC_Type.__name__ = "Integer32"
_SpmTempC_Object = MibTableColumn
spmTempC = _SpmTempC_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 5),
    _SpmTempC_Type()
)
spmTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmTempC.setStatus("current")


class _SpmTempF_Type(Integer32):
    """Custom type spmTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_SpmTempF_Type.__name__ = "Integer32"
_SpmTempF_Object = MibTableColumn
spmTempF = _SpmTempF_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 6),
    _SpmTempF_Type()
)
spmTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmTempF.setStatus("current")
_SpmVoltsDcA_Type = Unsigned32
_SpmVoltsDcA_Object = MibTableColumn
spmVoltsDcA = _SpmVoltsDcA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 7),
    _SpmVoltsDcA_Type()
)
spmVoltsDcA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmVoltsDcA.setStatus("current")
_SpmVoltsDcB_Type = Unsigned32
_SpmVoltsDcB_Object = MibTableColumn
spmVoltsDcB = _SpmVoltsDcB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 8),
    _SpmVoltsDcB_Type()
)
spmVoltsDcB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmVoltsDcB.setStatus("current")


class _SpmVoltsDcC_Type(Integer32):
    """Custom type spmVoltsDcC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, 10),
    )


_SpmVoltsDcC_Type.__name__ = "Integer32"
_SpmVoltsDcC_Object = MibTableColumn
spmVoltsDcC = _SpmVoltsDcC_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 9),
    _SpmVoltsDcC_Type()
)
spmVoltsDcC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmVoltsDcC.setStatus("current")


class _SpmAmps_Type(Integer32):
    """Custom type spmAmps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 110),
    )


_SpmAmps_Type.__name__ = "Integer32"
_SpmAmps_Object = MibTableColumn
spmAmps = _SpmAmps_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 10),
    _SpmAmps_Type()
)
spmAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmAmps.setStatus("current")
_SpmVoltsAcA_Type = Unsigned32
_SpmVoltsAcA_Object = MibTableColumn
spmVoltsAcA = _SpmVoltsAcA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 11),
    _SpmVoltsAcA_Type()
)
spmVoltsAcA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmVoltsAcA.setStatus("current")
_SpmVoltsAcB_Type = Unsigned32
_SpmVoltsAcB_Object = MibTableColumn
spmVoltsAcB = _SpmVoltsAcB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 12),
    _SpmVoltsAcB_Type()
)
spmVoltsAcB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmVoltsAcB.setStatus("current")


class _SpmContactA_Type(Integer32):
    """Custom type spmContactA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpmContactA_Type.__name__ = "Integer32"
_SpmContactA_Object = MibTableColumn
spmContactA = _SpmContactA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 13),
    _SpmContactA_Type()
)
spmContactA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmContactA.setStatus("current")


class _SpmContactB_Type(Integer32):
    """Custom type spmContactB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpmContactB_Type.__name__ = "Integer32"
_SpmContactB_Object = MibTableColumn
spmContactB = _SpmContactB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 14),
    _SpmContactB_Type()
)
spmContactB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmContactB.setStatus("current")


class _SpmContactC_Type(Integer32):
    """Custom type spmContactC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpmContactC_Type.__name__ = "Integer32"
_SpmContactC_Object = MibTableColumn
spmContactC = _SpmContactC_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 15),
    _SpmContactC_Type()
)
spmContactC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmContactC.setStatus("current")


class _SpmAmpsX10_Type(Integer32):
    """Custom type spmAmpsX10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1100, 1100),
    )


_SpmAmpsX10_Type.__name__ = "Integer32"
_SpmAmpsX10_Object = MibTableColumn
spmAmpsX10 = _SpmAmpsX10_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 16),
    _SpmAmpsX10_Type()
)
spmAmpsX10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmAmpsX10.setStatus("current")
_SpmTrap_ObjectIdentity = ObjectIdentity
spmTrap = _SpmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767)
)
_SpmTrapPrefix_ObjectIdentity = ObjectIdentity
spmTrapPrefix = _SpmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0)
)

# Managed Objects groups


# Notification objects

spmTestNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10101)
)
if mibBuilder.loadTexts:
    spmTestNOTIFY.setStatus(
        "current"
    )

spmSpmTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10205)
)
spmSpmTempCNOTIFY.setObjects(
      *(("NMR-MIB", "spmTempC"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmTempCNOTIFY.setStatus(
        "current"
    )

spmSpmTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10206)
)
spmSpmTempFNOTIFY.setObjects(
      *(("NMR-MIB", "spmTempF"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmTempFNOTIFY.setStatus(
        "current"
    )

spmSpmVoltsDcANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10207)
)
spmSpmVoltsDcANOTIFY.setObjects(
      *(("NMR-MIB", "spmVoltsDcA"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsDcANOTIFY.setStatus(
        "current"
    )

spmSpmVoltsDcBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10208)
)
spmSpmVoltsDcBNOTIFY.setObjects(
      *(("NMR-MIB", "spmVoltsDcB"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsDcBNOTIFY.setStatus(
        "current"
    )

spmSpmVoltsDcCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10209)
)
spmSpmVoltsDcCNOTIFY.setObjects(
      *(("NMR-MIB", "spmVoltsDcC"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsDcCNOTIFY.setStatus(
        "current"
    )

spmSpmAmpsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10210)
)
spmSpmAmpsNOTIFY.setObjects(
      *(("NMR-MIB", "spmAmps"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmAmpsNOTIFY.setStatus(
        "current"
    )

spmSpmVoltsAcANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10211)
)
spmSpmVoltsAcANOTIFY.setObjects(
      *(("NMR-MIB", "spmVoltsAcA"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsAcANOTIFY.setStatus(
        "current"
    )

spmSpmVoltsAcBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10212)
)
spmSpmVoltsAcBNOTIFY.setObjects(
      *(("NMR-MIB", "spmVoltsAcB"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsAcBNOTIFY.setStatus(
        "current"
    )

spmSpmContactANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10213)
)
spmSpmContactANOTIFY.setObjects(
      *(("NMR-MIB", "spmContactA"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmContactANOTIFY.setStatus(
        "current"
    )

spmSpmContactBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10214)
)
spmSpmContactBNOTIFY.setObjects(
      *(("NMR-MIB", "spmContactB"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmContactBNOTIFY.setStatus(
        "current"
    )

spmSpmContactCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10215)
)
spmSpmContactCNOTIFY.setObjects(
      *(("NMR-MIB", "spmContactC"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmContactCNOTIFY.setStatus(
        "current"
    )

spmSpmAmpsX10NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10216)
)
spmSpmAmpsX10NOTIFY.setObjects(
      *(("NMR-MIB", "spmAmpsX10"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmAmpsX10NOTIFY.setStatus(
        "current"
    )

spmSpmTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20205)
)
spmSpmTempCCLEAR.setObjects(
      *(("NMR-MIB", "spmTempC"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmTempCCLEAR.setStatus(
        "current"
    )

spmSpmTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20206)
)
spmSpmTempFCLEAR.setObjects(
      *(("NMR-MIB", "spmTempF"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmTempFCLEAR.setStatus(
        "current"
    )

spmSpmVoltsDcACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20207)
)
spmSpmVoltsDcACLEAR.setObjects(
      *(("NMR-MIB", "spmVoltsDcA"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsDcACLEAR.setStatus(
        "current"
    )

spmSpmVoltsDcBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20208)
)
spmSpmVoltsDcBCLEAR.setObjects(
      *(("NMR-MIB", "spmVoltsDcB"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsDcBCLEAR.setStatus(
        "current"
    )

spmSpmVoltsDcCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20209)
)
spmSpmVoltsDcCCLEAR.setObjects(
      *(("NMR-MIB", "spmVoltsDcC"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsDcCCLEAR.setStatus(
        "current"
    )

spmSpmAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20210)
)
spmSpmAmpsCLEAR.setObjects(
      *(("NMR-MIB", "spmAmps"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmAmpsCLEAR.setStatus(
        "current"
    )

spmSpmVoltsAcACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20211)
)
spmSpmVoltsAcACLEAR.setObjects(
      *(("NMR-MIB", "spmVoltsAcA"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsAcACLEAR.setStatus(
        "current"
    )

spmSpmVoltsAcBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20212)
)
spmSpmVoltsAcBCLEAR.setObjects(
      *(("NMR-MIB", "spmVoltsAcB"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmVoltsAcBCLEAR.setStatus(
        "current"
    )

spmSpmContactACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20213)
)
spmSpmContactACLEAR.setObjects(
      *(("NMR-MIB", "spmContactA"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmContactACLEAR.setStatus(
        "current"
    )

spmSpmContactBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20214)
)
spmSpmContactBCLEAR.setObjects(
      *(("NMR-MIB", "spmContactB"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmContactBCLEAR.setStatus(
        "current"
    )

spmSpmContactCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20215)
)
spmSpmContactCCLEAR.setObjects(
      *(("NMR-MIB", "spmContactC"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmContactCCLEAR.setStatus(
        "current"
    )

spmSpmAmpsX10CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20216)
)
spmSpmAmpsX10CLEAR.setObjects(
      *(("NMR-MIB", "spmAmpsX10"),
        ("NMR-MIB", "spmName"),
        ("NMR-MIB", "productFriendlyName"),
        ("NMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    spmSpmAmpsX10CLEAR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMR-MIB",
    **{"newmar": newmar,
       "spm": spm,
       "deviceInfo": deviceInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productFriendlyName": productFriendlyName,
       "productMacAddress": productMacAddress,
       "productUrl": productUrl,
       "alarmTripType": alarmTripType,
       "productHardware": productHardware,
       "sensorCountsBase": sensorCountsBase,
       "sensorCounts": sensorCounts,
       "spmCount": spmCount,
       "spmTable": spmTable,
       "spmEntry": spmEntry,
       "spmIndex": spmIndex,
       "spmSerial": spmSerial,
       "spmName": spmName,
       "spmAvail": spmAvail,
       "spmTempC": spmTempC,
       "spmTempF": spmTempF,
       "spmVoltsDcA": spmVoltsDcA,
       "spmVoltsDcB": spmVoltsDcB,
       "spmVoltsDcC": spmVoltsDcC,
       "spmAmps": spmAmps,
       "spmVoltsAcA": spmVoltsAcA,
       "spmVoltsAcB": spmVoltsAcB,
       "spmContactA": spmContactA,
       "spmContactB": spmContactB,
       "spmContactC": spmContactC,
       "spmAmpsX10": spmAmpsX10,
       "spmTrap": spmTrap,
       "spmTrapPrefix": spmTrapPrefix,
       "spmTestNOTIFY": spmTestNOTIFY,
       "spmSpmTempCNOTIFY": spmSpmTempCNOTIFY,
       "spmSpmTempFNOTIFY": spmSpmTempFNOTIFY,
       "spmSpmVoltsDcANOTIFY": spmSpmVoltsDcANOTIFY,
       "spmSpmVoltsDcBNOTIFY": spmSpmVoltsDcBNOTIFY,
       "spmSpmVoltsDcCNOTIFY": spmSpmVoltsDcCNOTIFY,
       "spmSpmAmpsNOTIFY": spmSpmAmpsNOTIFY,
       "spmSpmVoltsAcANOTIFY": spmSpmVoltsAcANOTIFY,
       "spmSpmVoltsAcBNOTIFY": spmSpmVoltsAcBNOTIFY,
       "spmSpmContactANOTIFY": spmSpmContactANOTIFY,
       "spmSpmContactBNOTIFY": spmSpmContactBNOTIFY,
       "spmSpmContactCNOTIFY": spmSpmContactCNOTIFY,
       "spmSpmAmpsX10NOTIFY": spmSpmAmpsX10NOTIFY,
       "spmSpmTempCCLEAR": spmSpmTempCCLEAR,
       "spmSpmTempFCLEAR": spmSpmTempFCLEAR,
       "spmSpmVoltsDcACLEAR": spmSpmVoltsDcACLEAR,
       "spmSpmVoltsDcBCLEAR": spmSpmVoltsDcBCLEAR,
       "spmSpmVoltsDcCCLEAR": spmSpmVoltsDcCCLEAR,
       "spmSpmAmpsCLEAR": spmSpmAmpsCLEAR,
       "spmSpmVoltsAcACLEAR": spmSpmVoltsAcACLEAR,
       "spmSpmVoltsAcBCLEAR": spmSpmVoltsAcBCLEAR,
       "spmSpmContactACLEAR": spmSpmContactACLEAR,
       "spmSpmContactBCLEAR": spmSpmContactBCLEAR,
       "spmSpmContactCCLEAR": spmSpmContactCCLEAR,
       "spmSpmAmpsX10CLEAR": spmSpmAmpsX10CLEAR}
)
