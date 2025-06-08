# SNMP MIB module (CP9K-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/harmonic_france_38142/CP9K-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:31:58 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vibeCP9k = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7)
)
if mibBuilder.loadTexts:
    vibeCP9k.setRevisions(
        ("1919-09-24 15:55",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Boolean(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )



class RowStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )



class OBJECTID(TextualConvention, ObjectIdentifier):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HarmonicFrance_ObjectIdentity = ObjectIdentity
harmonicFrance = _HarmonicFrance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1)
)
_GenManagerTable_Object = MibTable
genManagerTable = _GenManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1)
)
if mibBuilder.loadTexts:
    genManagerTable.setStatus("current")
_GenManagerEntry_Object = MibTableRow
genManagerEntry = _GenManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1)
)
genManagerEntry.setIndexNames(
    (0, "CP9K-MIB", "genManagerIndex"),
)
if mibBuilder.loadTexts:
    genManagerEntry.setStatus("current")


class _GenManagerIndex_Type(Integer32):
    """Custom type genManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GenManagerIndex_Type.__name__ = "Integer32"
_GenManagerIndex_Object = MibTableColumn
genManagerIndex = _GenManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 1),
    _GenManagerIndex_Type()
)
genManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genManagerIndex.setStatus("current")
_GenManagerIpAddress_Type = IpAddress
_GenManagerIpAddress_Object = MibTableColumn
genManagerIpAddress = _GenManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 2),
    _GenManagerIpAddress_Type()
)
genManagerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerIpAddress.setStatus("current")
_GenManagerTrapEnable_Type = Boolean
_GenManagerTrapEnable_Object = MibTableColumn
genManagerTrapEnable = _GenManagerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 3),
    _GenManagerTrapEnable_Type()
)
genManagerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerTrapEnable.setStatus("current")
_GenManagerTrapTypeSelection_Type = Unsigned32
_GenManagerTrapTypeSelection_Object = MibTableColumn
genManagerTrapTypeSelection = _GenManagerTrapTypeSelection_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 4),
    _GenManagerTrapTypeSelection_Type()
)
genManagerTrapTypeSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerTrapTypeSelection.setStatus("current")


class _GenManagerEventTrapSeverityFilter_Type(Integer32):
    """Custom type genManagerEventTrapSeverityFilter based on Integer32"""
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
        *(("allSeverity", 1),
          ("severityWarning", 2),
          ("severityMinor", 3),
          ("severityMajor", 4),
          ("severityCritical", 5))
    )


_GenManagerEventTrapSeverityFilter_Type.__name__ = "Integer32"
_GenManagerEventTrapSeverityFilter_Object = MibTableColumn
genManagerEventTrapSeverityFilter = _GenManagerEventTrapSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 5),
    _GenManagerEventTrapSeverityFilter_Type()
)
genManagerEventTrapSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerEventTrapSeverityFilter.setStatus("current")


class _GenManagerTrapGenericFilter_Type(DisplayString):
    """Custom type genManagerTrapGenericFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GenManagerTrapGenericFilter_Type.__name__ = "DisplayString"
_GenManagerTrapGenericFilter_Object = MibTableColumn
genManagerTrapGenericFilter = _GenManagerTrapGenericFilter_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 6),
    _GenManagerTrapGenericFilter_Type()
)
genManagerTrapGenericFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerTrapGenericFilter.setStatus("current")
_GenManagerPersistent_Type = Boolean
_GenManagerPersistent_Object = MibTableColumn
genManagerPersistent = _GenManagerPersistent_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 7),
    _GenManagerPersistent_Type()
)
genManagerPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerPersistent.setStatus("current")
_GenManagerConfigLock_Type = Integer32
_GenManagerConfigLock_Object = MibTableColumn
genManagerConfigLock = _GenManagerConfigLock_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 1, 1, 8),
    _GenManagerConfigLock_Type()
)
genManagerConfigLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genManagerConfigLock.setStatus("current")
_GenSystemInfo_ObjectIdentity = ObjectIdentity
genSystemInfo = _GenSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2)
)


class _GenSysTypeName_Type(DisplayString):
    """Custom type genSysTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenSysTypeName_Type.__name__ = "DisplayString"
_GenSysTypeName_Object = MibScalar
genSysTypeName = _GenSysTypeName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 1),
    _GenSysTypeName_Type()
)
genSysTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysTypeName.setStatus("current")


class _GenSysTypeDescr_Type(DisplayString):
    """Custom type genSysTypeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GenSysTypeDescr_Type.__name__ = "DisplayString"
_GenSysTypeDescr_Object = MibScalar
genSysTypeDescr = _GenSysTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 2),
    _GenSysTypeDescr_Type()
)
genSysTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysTypeDescr.setStatus("current")


class _GenMibVersion_Type(DisplayString):
    """Custom type genMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenMibVersion_Type.__name__ = "DisplayString"
_GenMibVersion_Object = MibScalar
genMibVersion = _GenMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 3),
    _GenMibVersion_Type()
)
genMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMibVersion.setStatus("current")
_GenDeviceId_Type = Unsigned32
_GenDeviceId_Object = MibScalar
genDeviceId = _GenDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 4),
    _GenDeviceId_Type()
)
genDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDeviceId.setStatus("current")


class _GenDeviceName_Type(DisplayString):
    """Custom type genDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenDeviceName_Type.__name__ = "DisplayString"
_GenDeviceName_Object = MibScalar
genDeviceName = _GenDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 5),
    _GenDeviceName_Type()
)
genDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDeviceName.setStatus("current")


class _GenProductSerialNumber_Type(DisplayString):
    """Custom type genProductSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenProductSerialNumber_Type.__name__ = "DisplayString"
_GenProductSerialNumber_Object = MibScalar
genProductSerialNumber = _GenProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 6),
    _GenProductSerialNumber_Type()
)
genProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProductSerialNumber.setStatus("current")


class _GenProductSoftVersion_Type(DisplayString):
    """Custom type genProductSoftVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenProductSoftVersion_Type.__name__ = "DisplayString"
_GenProductSoftVersion_Object = MibScalar
genProductSoftVersion = _GenProductSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 7),
    _GenProductSoftVersion_Type()
)
genProductSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProductSoftVersion.setStatus("current")


class _GenSysAlarmOutput1_Type(Integer32):
    """Custom type genSysAlarmOutput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("fault", 1))
    )


_GenSysAlarmOutput1_Type.__name__ = "Integer32"
_GenSysAlarmOutput1_Object = MibScalar
genSysAlarmOutput1 = _GenSysAlarmOutput1_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 8),
    _GenSysAlarmOutput1_Type()
)
genSysAlarmOutput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysAlarmOutput1.setStatus("current")


class _GenSysAlarmOutput2_Type(Integer32):
    """Custom type genSysAlarmOutput2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("fault", 1))
    )


_GenSysAlarmOutput2_Type.__name__ = "Integer32"
_GenSysAlarmOutput2_Object = MibScalar
genSysAlarmOutput2 = _GenSysAlarmOutput2_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 9),
    _GenSysAlarmOutput2_Type()
)
genSysAlarmOutput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysAlarmOutput2.setStatus("current")


class _GenSysAlarmStatus_Type(Integer32):
    """Custom type genSysAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("severityCleared", 0),
          ("severityWarning", 2),
          ("severityMinor", 3),
          ("severityMajor", 4),
          ("severityCritical", 5))
    )


_GenSysAlarmStatus_Type.__name__ = "Integer32"
_GenSysAlarmStatus_Object = MibScalar
genSysAlarmStatus = _GenSysAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 10),
    _GenSysAlarmStatus_Type()
)
genSysAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysAlarmStatus.setStatus("current")
_GenSysAlarmUpdate_Type = DateAndTime
_GenSysAlarmUpdate_Object = MibScalar
genSysAlarmUpdate = _GenSysAlarmUpdate_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 11),
    _GenSysAlarmUpdate_Type()
)
genSysAlarmUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysAlarmUpdate.setStatus("current")


class _GenSysRedundStatus_Type(Integer32):
    """Custom type genSysRedundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("onAir", 1),
          ("offAir", 2))
    )


_GenSysRedundStatus_Type.__name__ = "Integer32"
_GenSysRedundStatus_Object = MibScalar
genSysRedundStatus = _GenSysRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 12),
    _GenSysRedundStatus_Type()
)
genSysRedundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysRedundStatus.setStatus("current")


class _GenOptionEqpCode_Type(DisplayString):
    """Custom type genOptionEqpCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GenOptionEqpCode_Type.__name__ = "DisplayString"
_GenOptionEqpCode_Object = MibScalar
genOptionEqpCode = _GenOptionEqpCode_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 13),
    _GenOptionEqpCode_Type()
)
genOptionEqpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionEqpCode.setStatus("current")
_GenBoardInfoTable_Object = MibTable
genBoardInfoTable = _GenBoardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50)
)
if mibBuilder.loadTexts:
    genBoardInfoTable.setStatus("current")
_GenBoardInfoEntry_Object = MibTableRow
genBoardInfoEntry = _GenBoardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1)
)
genBoardInfoEntry.setIndexNames(
    (0, "CP9K-MIB", "genBoardSlotNb"),
)
if mibBuilder.loadTexts:
    genBoardInfoEntry.setStatus("current")


class _GenBoardSlotNb_Type(Integer32):
    """Custom type genBoardSlotNb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GenBoardSlotNb_Type.__name__ = "Integer32"
_GenBoardSlotNb_Object = MibTableColumn
genBoardSlotNb = _GenBoardSlotNb_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 1),
    _GenBoardSlotNb_Type()
)
genBoardSlotNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardSlotNb.setStatus("current")


class _GenBoardTypeDetected_Type(DisplayString):
    """Custom type genBoardTypeDetected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenBoardTypeDetected_Type.__name__ = "DisplayString"
_GenBoardTypeDetected_Object = MibTableColumn
genBoardTypeDetected = _GenBoardTypeDetected_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 2),
    _GenBoardTypeDetected_Type()
)
genBoardTypeDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardTypeDetected.setStatus("current")


class _GenBoardSerialNumber_Type(DisplayString):
    """Custom type genBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenBoardSerialNumber_Type.__name__ = "DisplayString"
_GenBoardSerialNumber_Object = MibTableColumn
genBoardSerialNumber = _GenBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 3),
    _GenBoardSerialNumber_Type()
)
genBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardSerialNumber.setStatus("current")


class _GenBoardTypeDeclared_Type(DisplayString):
    """Custom type genBoardTypeDeclared based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenBoardTypeDeclared_Type.__name__ = "DisplayString"
_GenBoardTypeDeclared_Object = MibTableColumn
genBoardTypeDeclared = _GenBoardTypeDeclared_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 4),
    _GenBoardTypeDeclared_Type()
)
genBoardTypeDeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardTypeDeclared.setStatus("current")
_GenBoardSubSystemId_Type = Unsigned32
_GenBoardSubSystemId_Object = MibTableColumn
genBoardSubSystemId = _GenBoardSubSystemId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 5),
    _GenBoardSubSystemId_Type()
)
genBoardSubSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardSubSystemId.setStatus("current")


class _GenBoardAlarmStatus_Type(Integer32):
    """Custom type genBoardAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("severityCleared", 0),
          ("severityWarning", 2),
          ("severityMinor", 3),
          ("severityMajor", 4),
          ("severityCritical", 5))
    )


_GenBoardAlarmStatus_Type.__name__ = "Integer32"
_GenBoardAlarmStatus_Object = MibTableColumn
genBoardAlarmStatus = _GenBoardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 6),
    _GenBoardAlarmStatus_Type()
)
genBoardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardAlarmStatus.setStatus("current")


class _GenBoardRedundStatus_Type(Integer32):
    """Custom type genBoardRedundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("onAir", 1),
          ("offAir", 2))
    )


_GenBoardRedundStatus_Type.__name__ = "Integer32"
_GenBoardRedundStatus_Object = MibTableColumn
genBoardRedundStatus = _GenBoardRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 50, 1, 7),
    _GenBoardRedundStatus_Type()
)
genBoardRedundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genBoardRedundStatus.setStatus("current")
_GenRidInfoTable_Object = MibTable
genRidInfoTable = _GenRidInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 51)
)
if mibBuilder.loadTexts:
    genRidInfoTable.setStatus("current")
_GenRidInfoEntry_Object = MibTableRow
genRidInfoEntry = _GenRidInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 51, 1)
)
genRidInfoEntry.setIndexNames(
    (0, "CP9K-MIB", "genRidSlotNb"),
    (0, "CP9K-MIB", "genRidAttributeName"),
)
if mibBuilder.loadTexts:
    genRidInfoEntry.setStatus("current")


class _GenRidSlotNb_Type(Integer32):
    """Custom type genRidSlotNb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GenRidSlotNb_Type.__name__ = "Integer32"
_GenRidSlotNb_Object = MibTableColumn
genRidSlotNb = _GenRidSlotNb_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 51, 1, 1),
    _GenRidSlotNb_Type()
)
genRidSlotNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genRidSlotNb.setStatus("current")


class _GenRidAttributeName_Type(DisplayString):
    """Custom type genRidAttributeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenRidAttributeName_Type.__name__ = "DisplayString"
_GenRidAttributeName_Object = MibTableColumn
genRidAttributeName = _GenRidAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 51, 1, 2),
    _GenRidAttributeName_Type()
)
genRidAttributeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genRidAttributeName.setStatus("current")


class _GenRidAttributeValue_Type(DisplayString):
    """Custom type genRidAttributeValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenRidAttributeValue_Type.__name__ = "DisplayString"
_GenRidAttributeValue_Object = MibTableColumn
genRidAttributeValue = _GenRidAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 51, 1, 3),
    _GenRidAttributeValue_Type()
)
genRidAttributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genRidAttributeValue.setStatus("current")
_GenSubSystemInfoTable_Object = MibTable
genSubSystemInfoTable = _GenSubSystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52)
)
if mibBuilder.loadTexts:
    genSubSystemInfoTable.setStatus("current")
_GenSubSystemInfoEntry_Object = MibTableRow
genSubSystemInfoEntry = _GenSubSystemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1)
)
genSubSystemInfoEntry.setIndexNames(
    (0, "CP9K-MIB", "genSubSystemId"),
)
if mibBuilder.loadTexts:
    genSubSystemInfoEntry.setStatus("current")
_GenSubSystemId_Type = Unsigned32
_GenSubSystemId_Object = MibTableColumn
genSubSystemId = _GenSubSystemId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1, 1),
    _GenSubSystemId_Type()
)
genSubSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSubSystemId.setStatus("current")
_GenSubSystemType_Type = Integer32
_GenSubSystemType_Object = MibTableColumn
genSubSystemType = _GenSubSystemType_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1, 2),
    _GenSubSystemType_Type()
)
genSubSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSubSystemType.setStatus("current")


class _GenSubSystemTypeName_Type(DisplayString):
    """Custom type genSubSystemTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenSubSystemTypeName_Type.__name__ = "DisplayString"
_GenSubSystemTypeName_Object = MibTableColumn
genSubSystemTypeName = _GenSubSystemTypeName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1, 3),
    _GenSubSystemTypeName_Type()
)
genSubSystemTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSubSystemTypeName.setStatus("current")


class _GenSubSystemName_Type(DisplayString):
    """Custom type genSubSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenSubSystemName_Type.__name__ = "DisplayString"
_GenSubSystemName_Object = MibTableColumn
genSubSystemName = _GenSubSystemName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1, 4),
    _GenSubSystemName_Type()
)
genSubSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSubSystemName.setStatus("current")


class _GenSubSystemAlarmStatus_Type(Integer32):
    """Custom type genSubSystemAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("severityCleared", 0),
          ("severityWarning", 2),
          ("severityMinor", 3),
          ("severityMajor", 4),
          ("severityCritical", 5))
    )


_GenSubSystemAlarmStatus_Type.__name__ = "Integer32"
_GenSubSystemAlarmStatus_Object = MibTableColumn
genSubSystemAlarmStatus = _GenSubSystemAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1, 5),
    _GenSubSystemAlarmStatus_Type()
)
genSubSystemAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSubSystemAlarmStatus.setStatus("current")


class _GenSubSystemRedundStatus_Type(Integer32):
    """Custom type genSubSystemRedundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("onAir", 1),
          ("offAir", 2))
    )


_GenSubSystemRedundStatus_Type.__name__ = "Integer32"
_GenSubSystemRedundStatus_Object = MibTableColumn
genSubSystemRedundStatus = _GenSubSystemRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 52, 1, 6),
    _GenSubSystemRedundStatus_Type()
)
genSubSystemRedundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSubSystemRedundStatus.setStatus("current")
_GenSoftwareInfoTable_Object = MibTable
genSoftwareInfoTable = _GenSoftwareInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 53)
)
if mibBuilder.loadTexts:
    genSoftwareInfoTable.setStatus("current")
_GenSoftwareInfoEntry_Object = MibTableRow
genSoftwareInfoEntry = _GenSoftwareInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 53, 1)
)
genSoftwareInfoEntry.setIndexNames(
    (0, "CP9K-MIB", "genSoftSlotNb"),
    (0, "CP9K-MIB", "genSoftTypeName"),
    (0, "CP9K-MIB", "genSoftStatus"),
)
if mibBuilder.loadTexts:
    genSoftwareInfoEntry.setStatus("current")


class _GenSoftSlotNb_Type(Integer32):
    """Custom type genSoftSlotNb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GenSoftSlotNb_Type.__name__ = "Integer32"
_GenSoftSlotNb_Object = MibTableColumn
genSoftSlotNb = _GenSoftSlotNb_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 53, 1, 1),
    _GenSoftSlotNb_Type()
)
genSoftSlotNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftSlotNb.setStatus("current")


class _GenSoftTypeName_Type(DisplayString):
    """Custom type genSoftTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenSoftTypeName_Type.__name__ = "DisplayString"
_GenSoftTypeName_Object = MibTableColumn
genSoftTypeName = _GenSoftTypeName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 53, 1, 2),
    _GenSoftTypeName_Type()
)
genSoftTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftTypeName.setStatus("current")


class _GenSoftStatus_Type(Integer32):
    """Custom type genSoftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1))
    )


_GenSoftStatus_Type.__name__ = "Integer32"
_GenSoftStatus_Object = MibTableColumn
genSoftStatus = _GenSoftStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 53, 1, 3),
    _GenSoftStatus_Type()
)
genSoftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftStatus.setStatus("current")


class _GenSoftVersion_Type(DisplayString):
    """Custom type genSoftVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenSoftVersion_Type.__name__ = "DisplayString"
_GenSoftVersion_Object = MibTableColumn
genSoftVersion = _GenSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 53, 1, 4),
    _GenSoftVersion_Type()
)
genSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftVersion.setStatus("current")
_GenOptionInfoTable_Object = MibTable
genOptionInfoTable = _GenOptionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54)
)
if mibBuilder.loadTexts:
    genOptionInfoTable.setStatus("current")
_GenOptionInfoEntry_Object = MibTableRow
genOptionInfoEntry = _GenOptionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1)
)
genOptionInfoEntry.setIndexNames(
    (0, "CP9K-MIB", "genOptionSubSystemId"),
    (0, "CP9K-MIB", "genOptionId"),
)
if mibBuilder.loadTexts:
    genOptionInfoEntry.setStatus("current")
_GenOptionSubSystemId_Type = Unsigned32
_GenOptionSubSystemId_Object = MibTableColumn
genOptionSubSystemId = _GenOptionSubSystemId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1, 1),
    _GenOptionSubSystemId_Type()
)
genOptionSubSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionSubSystemId.setStatus("current")
_GenOptionId_Type = Integer32
_GenOptionId_Object = MibTableColumn
genOptionId = _GenOptionId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1, 2),
    _GenOptionId_Type()
)
genOptionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionId.setStatus("current")


class _GenOptionTypeName_Type(DisplayString):
    """Custom type genOptionTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenOptionTypeName_Type.__name__ = "DisplayString"
_GenOptionTypeName_Object = MibTableColumn
genOptionTypeName = _GenOptionTypeName_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1, 3),
    _GenOptionTypeName_Type()
)
genOptionTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionTypeName.setStatus("current")
_GenOptionInstalled_Type = Boolean
_GenOptionInstalled_Object = MibTableColumn
genOptionInstalled = _GenOptionInstalled_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1, 4),
    _GenOptionInstalled_Type()
)
genOptionInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionInstalled.setStatus("current")
_GenOptionExpiryDate_Type = DateAndTime
_GenOptionExpiryDate_Object = MibTableColumn
genOptionExpiryDate = _GenOptionExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1, 5),
    _GenOptionExpiryDate_Type()
)
genOptionExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionExpiryDate.setStatus("current")
_GenOptionAmount_Type = Integer32
_GenOptionAmount_Object = MibTableColumn
genOptionAmount = _GenOptionAmount_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 54, 1, 6),
    _GenOptionAmount_Type()
)
genOptionAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOptionAmount.setStatus("current")
_GenIpInterfaceTable_Object = MibTable
genIpInterfaceTable = _GenIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55)
)
if mibBuilder.loadTexts:
    genIpInterfaceTable.setStatus("current")
_GenIpInterfaceEntry_Object = MibTableRow
genIpInterfaceEntry = _GenIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1)
)
genIpInterfaceEntry.setIndexNames(
    (0, "CP9K-MIB", "genIpIfSlotNb"),
    (0, "CP9K-MIB", "genIpIfId"),
)
if mibBuilder.loadTexts:
    genIpInterfaceEntry.setStatus("current")


class _GenIpIfSlotNb_Type(Integer32):
    """Custom type genIpIfSlotNb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GenIpIfSlotNb_Type.__name__ = "Integer32"
_GenIpIfSlotNb_Object = MibTableColumn
genIpIfSlotNb = _GenIpIfSlotNb_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1, 1),
    _GenIpIfSlotNb_Type()
)
genIpIfSlotNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIpIfSlotNb.setStatus("current")
_GenIpIfId_Type = Integer32
_GenIpIfId_Object = MibTableColumn
genIpIfId = _GenIpIfId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1, 2),
    _GenIpIfId_Type()
)
genIpIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIpIfId.setStatus("current")
_GenIpIfAddress_Type = IpAddress
_GenIpIfAddress_Object = MibTableColumn
genIpIfAddress = _GenIpIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1, 3),
    _GenIpIfAddress_Type()
)
genIpIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIpIfAddress.setStatus("current")
_GenIpIfNetmask_Type = IpAddress
_GenIpIfNetmask_Object = MibTableColumn
genIpIfNetmask = _GenIpIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1, 4),
    _GenIpIfNetmask_Type()
)
genIpIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIpIfNetmask.setStatus("current")
_GenIpIfGateway_Type = IpAddress
_GenIpIfGateway_Object = MibTableColumn
genIpIfGateway = _GenIpIfGateway_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1, 5),
    _GenIpIfGateway_Type()
)
genIpIfGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIpIfGateway.setStatus("current")


class _GenIpIfMacAddress_Type(OctetString):
    """Custom type genIpIfMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_GenIpIfMacAddress_Type.__name__ = "OctetString"
_GenIpIfMacAddress_Object = MibTableColumn
genIpIfMacAddress = _GenIpIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 2, 55, 1, 6),
    _GenIpIfMacAddress_Type()
)
genIpIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIpIfMacAddress.setStatus("current")
_GenAlarmTable_Object = MibTable
genAlarmTable = _GenAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3)
)
if mibBuilder.loadTexts:
    genAlarmTable.setStatus("current")
_GenAlarmEntry_Object = MibTableRow
genAlarmEntry = _GenAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1)
)
genAlarmEntry.setIndexNames(
    (0, "CP9K-MIB", "genAlarmSubsystemId"),
    (0, "CP9K-MIB", "genAlarmObjectReference"),
    (0, "CP9K-MIB", "genAlarmProbableCause"),
    (0, "CP9K-MIB", "genAlarmSpecificProblem"),
)
if mibBuilder.loadTexts:
    genAlarmEntry.setStatus("current")
_GenAlarmSubsystemId_Type = Unsigned32
_GenAlarmSubsystemId_Object = MibTableColumn
genAlarmSubsystemId = _GenAlarmSubsystemId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 1),
    _GenAlarmSubsystemId_Type()
)
genAlarmSubsystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmSubsystemId.setStatus("current")
_GenAlarmObjectReference_Type = Unsigned32
_GenAlarmObjectReference_Object = MibTableColumn
genAlarmObjectReference = _GenAlarmObjectReference_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 2),
    _GenAlarmObjectReference_Type()
)
genAlarmObjectReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmObjectReference.setStatus("current")
_GenAlarmProbableCause_Type = Unsigned32
_GenAlarmProbableCause_Object = MibTableColumn
genAlarmProbableCause = _GenAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 3),
    _GenAlarmProbableCause_Type()
)
genAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmProbableCause.setStatus("current")
_GenAlarmSpecificProblem_Type = Unsigned32
_GenAlarmSpecificProblem_Object = MibTableColumn
genAlarmSpecificProblem = _GenAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 4),
    _GenAlarmSpecificProblem_Type()
)
genAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmSpecificProblem.setStatus("current")
_GenAlarmTime_Type = DateAndTime
_GenAlarmTime_Object = MibTableColumn
genAlarmTime = _GenAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 5),
    _GenAlarmTime_Type()
)
genAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmTime.setStatus("current")


class _GenAlarmSeverity_Type(Integer32):
    """Custom type genAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("severityWarning", 2),
          ("severityMinor", 3),
          ("severityMajor", 4),
          ("severityCritical", 5))
    )


_GenAlarmSeverity_Type.__name__ = "Integer32"
_GenAlarmSeverity_Object = MibTableColumn
genAlarmSeverity = _GenAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 6),
    _GenAlarmSeverity_Type()
)
genAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmSeverity.setStatus("current")


class _GenAlarmCategory_Type(Integer32):
    """Custom type genAlarmCategory based on Integer32"""
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
        *(("communication", 1),
          ("qualityOfService", 2),
          ("processing", 3),
          ("equipment", 4),
          ("environment", 5),
          ("other", 6))
    )


_GenAlarmCategory_Type.__name__ = "Integer32"
_GenAlarmCategory_Object = MibTableColumn
genAlarmCategory = _GenAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 7),
    _GenAlarmCategory_Type()
)
genAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmCategory.setStatus("current")
_GenAlarmSubsystemType_Type = Integer32
_GenAlarmSubsystemType_Object = MibTableColumn
genAlarmSubsystemType = _GenAlarmSubsystemType_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 8),
    _GenAlarmSubsystemType_Type()
)
genAlarmSubsystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmSubsystemType.setStatus("current")


class _GenAlarmLabel_Type(DisplayString):
    """Custom type genAlarmLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GenAlarmLabel_Type.__name__ = "DisplayString"
_GenAlarmLabel_Object = MibTableColumn
genAlarmLabel = _GenAlarmLabel_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 9),
    _GenAlarmLabel_Type()
)
genAlarmLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmLabel.setStatus("current")
_GenAlarmOptAlarmId_Type = Unsigned32
_GenAlarmOptAlarmId_Object = MibTableColumn
genAlarmOptAlarmId = _GenAlarmOptAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 10),
    _GenAlarmOptAlarmId_Type()
)
genAlarmOptAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmOptAlarmId.setStatus("current")
_GenAlarmOptAlarmIdExt_Type = Unsigned32
_GenAlarmOptAlarmIdExt_Object = MibTableColumn
genAlarmOptAlarmIdExt = _GenAlarmOptAlarmIdExt_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 3, 1, 11),
    _GenAlarmOptAlarmIdExt_Type()
)
genAlarmOptAlarmIdExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAlarmOptAlarmIdExt.setStatus("current")
_GenEventTable_Object = MibTable
genEventTable = _GenEventTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4)
)
if mibBuilder.loadTexts:
    genEventTable.setStatus("current")
_GenEventEntry_Object = MibTableRow
genEventEntry = _GenEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1)
)
genEventEntry.setIndexNames(
    (0, "CP9K-MIB", "genEventRecordId"),
)
if mibBuilder.loadTexts:
    genEventEntry.setStatus("current")
_GenEventRecordId_Type = Unsigned32
_GenEventRecordId_Object = MibTableColumn
genEventRecordId = _GenEventRecordId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 1),
    _GenEventRecordId_Type()
)
genEventRecordId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventRecordId.setStatus("current")
_GenEventTime_Type = DateAndTime
_GenEventTime_Object = MibTableColumn
genEventTime = _GenEventTime_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 2),
    _GenEventTime_Type()
)
genEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventTime.setStatus("current")
_GenEventDeviceId_Type = Unsigned32
_GenEventDeviceId_Object = MibTableColumn
genEventDeviceId = _GenEventDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 3),
    _GenEventDeviceId_Type()
)
genEventDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventDeviceId.setStatus("current")
_GenEventSubsystemId_Type = Unsigned32
_GenEventSubsystemId_Object = MibTableColumn
genEventSubsystemId = _GenEventSubsystemId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 4),
    _GenEventSubsystemId_Type()
)
genEventSubsystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventSubsystemId.setStatus("current")
_GenEventObjectReference_Type = Unsigned32
_GenEventObjectReference_Object = MibTableColumn
genEventObjectReference = _GenEventObjectReference_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 5),
    _GenEventObjectReference_Type()
)
genEventObjectReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventObjectReference.setStatus("current")


class _GenEventType_Type(Integer32):
    """Custom type genEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("typeAttributeValueChange", 1),
          ("typeObjectCreation", 2),
          ("typeObjectDeletion", 3),
          ("typeAlarm", 4))
    )


_GenEventType_Type.__name__ = "Integer32"
_GenEventType_Object = MibTableColumn
genEventType = _GenEventType_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 6),
    _GenEventType_Type()
)
genEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventType.setStatus("current")
_GenEventProbableCause_Type = Unsigned32
_GenEventProbableCause_Object = MibTableColumn
genEventProbableCause = _GenEventProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 7),
    _GenEventProbableCause_Type()
)
genEventProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventProbableCause.setStatus("current")
_GenEventSpecificProblem_Type = Unsigned32
_GenEventSpecificProblem_Object = MibTableColumn
genEventSpecificProblem = _GenEventSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 8),
    _GenEventSpecificProblem_Type()
)
genEventSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventSpecificProblem.setStatus("current")


class _GenEventSeverity_Type(Integer32):
    """Custom type genEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("severityCleared", 0),
          ("severityNone", 1),
          ("severityWarning", 2),
          ("severityMinor", 3),
          ("severityMajor", 4),
          ("severityCritical", 5))
    )


_GenEventSeverity_Type.__name__ = "Integer32"
_GenEventSeverity_Object = MibTableColumn
genEventSeverity = _GenEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 9),
    _GenEventSeverity_Type()
)
genEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventSeverity.setStatus("current")


class _GenEventCategory_Type(Integer32):
    """Custom type genEventCategory based on Integer32"""
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
        *(("communication", 1),
          ("qualityOfService", 2),
          ("processing", 3),
          ("equipment", 4),
          ("environment", 5),
          ("other", 6))
    )


_GenEventCategory_Type.__name__ = "Integer32"
_GenEventCategory_Object = MibTableColumn
genEventCategory = _GenEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 10),
    _GenEventCategory_Type()
)
genEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventCategory.setStatus("current")
_GenEventSubsystemType_Type = Integer32
_GenEventSubsystemType_Object = MibTableColumn
genEventSubsystemType = _GenEventSubsystemType_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 11),
    _GenEventSubsystemType_Type()
)
genEventSubsystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventSubsystemType.setStatus("current")


class _GenEventLabel_Type(DisplayString):
    """Custom type genEventLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GenEventLabel_Type.__name__ = "DisplayString"
_GenEventLabel_Object = MibTableColumn
genEventLabel = _GenEventLabel_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 12),
    _GenEventLabel_Type()
)
genEventLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventLabel.setStatus("current")
_GenEventExtraInfo_Type = Unsigned32
_GenEventExtraInfo_Object = MibTableColumn
genEventExtraInfo = _GenEventExtraInfo_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 13),
    _GenEventExtraInfo_Type()
)
genEventExtraInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventExtraInfo.setStatus("current")
_GenEventOldValue_Type = Integer32
_GenEventOldValue_Object = MibTableColumn
genEventOldValue = _GenEventOldValue_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 14),
    _GenEventOldValue_Type()
)
genEventOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventOldValue.setStatus("current")
_GenEventNewValue_Type = Integer32
_GenEventNewValue_Object = MibTableColumn
genEventNewValue = _GenEventNewValue_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 15),
    _GenEventNewValue_Type()
)
genEventNewValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventNewValue.setStatus("current")
_GenEventOptEventId_Type = Unsigned32
_GenEventOptEventId_Object = MibTableColumn
genEventOptEventId = _GenEventOptEventId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 16),
    _GenEventOptEventId_Type()
)
genEventOptEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventOptEventId.setStatus("current")
_GenEventOptEventIdExt_Type = Unsigned32
_GenEventOptEventIdExt_Object = MibTableColumn
genEventOptEventIdExt = _GenEventOptEventIdExt_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 4, 1, 17),
    _GenEventOptEventIdExt_Type()
)
genEventOptEventIdExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEventOptEventIdExt.setStatus("current")
_GenCommands_ObjectIdentity = ObjectIdentity
genCommands = _GenCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5)
)
_GenCmdReboot_Type = Integer32
_GenCmdReboot_Object = MibScalar
genCmdReboot = _GenCmdReboot_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 1),
    _GenCmdReboot_Type()
)
genCmdReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCmdReboot.setStatus("current")
_GenCmdRecallConfig_ObjectIdentity = ObjectIdentity
genCmdRecallConfig = _GenCmdRecallConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 2)
)
_GenRecallConfigId_Type = Integer32
_GenRecallConfigId_Object = MibScalar
genRecallConfigId = _GenRecallConfigId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 2, 1),
    _GenRecallConfigId_Type()
)
genRecallConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRecallConfigId.setStatus("current")
_GenRecallSubsystemId_Type = Unsigned32
_GenRecallSubsystemId_Object = MibScalar
genRecallSubsystemId = _GenRecallSubsystemId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 2, 2),
    _GenRecallSubsystemId_Type()
)
genRecallSubsystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRecallSubsystemId.setStatus("current")
_GenRecallApply_Type = Integer32
_GenRecallApply_Object = MibScalar
genRecallApply = _GenRecallApply_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 2, 3),
    _GenRecallApply_Type()
)
genRecallApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRecallApply.setStatus("current")
_GenCmdShutdown_Type = Integer32
_GenCmdShutdown_Object = MibScalar
genCmdShutdown = _GenCmdShutdown_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 5),
    _GenCmdShutdown_Type()
)
genCmdShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCmdShutdown.setStatus("current")
_GenCmdBroadcast_ObjectIdentity = ObjectIdentity
genCmdBroadcast = _GenCmdBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 6)
)


class _GenCmdBcastStatus_Type(Integer32):
    """Custom type genCmdBcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onAir", 1),
          ("offAir", 2))
    )


_GenCmdBcastStatus_Type.__name__ = "Integer32"
_GenCmdBcastStatus_Object = MibScalar
genCmdBcastStatus = _GenCmdBcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 6, 1),
    _GenCmdBcastStatus_Type()
)
genCmdBcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCmdBcastStatus.setStatus("current")
_GenCmdConfigTransfer_ObjectIdentity = ObjectIdentity
genCmdConfigTransfer = _GenCmdConfigTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 7)
)


class _GenConfigTransferBufferMaxSize_Type(Integer32):
    """Custom type genConfigTransferBufferMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("bufferMaxSize1024", 1024),
          ("bufferMaxSize2048", 2048),
          ("bufferMaxSize4096", 4096))
    )


_GenConfigTransferBufferMaxSize_Type.__name__ = "Integer32"
_GenConfigTransferBufferMaxSize_Object = MibScalar
genConfigTransferBufferMaxSize = _GenConfigTransferBufferMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 7, 1),
    _GenConfigTransferBufferMaxSize_Type()
)
genConfigTransferBufferMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genConfigTransferBufferMaxSize.setStatus("current")


class _GenConfigTransferCommand_Type(Integer32):
    """Custom type genConfigTransferCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmdConfigDownload", 1),
          ("cmdConfigUpload", 2))
    )


_GenConfigTransferCommand_Type.__name__ = "Integer32"
_GenConfigTransferCommand_Object = MibScalar
genConfigTransferCommand = _GenConfigTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 7, 2),
    _GenConfigTransferCommand_Type()
)
genConfigTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genConfigTransferCommand.setStatus("current")
_GenCmdExecutionInfo_ObjectIdentity = ObjectIdentity
genCmdExecutionInfo = _GenCmdExecutionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 100)
)


class _GenCmdStatus_Type(Integer32):
    """Custom type genCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cmdInProgress", 1),
          ("cmdDone", 2),
          ("cmdDoneWithWarning", 3),
          ("cmdFailed", 4))
    )


_GenCmdStatus_Type.__name__ = "Integer32"
_GenCmdStatus_Object = MibScalar
genCmdStatus = _GenCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 100, 1),
    _GenCmdStatus_Type()
)
genCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCmdStatus.setStatus("current")


class _GenCmdReport_Type(DisplayString):
    """Custom type genCmdReport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GenCmdReport_Type.__name__ = "DisplayString"
_GenCmdReport_Object = MibScalar
genCmdReport = _GenCmdReport_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 100, 2),
    _GenCmdReport_Type()
)
genCmdReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCmdReport.setStatus("current")


class _GenCmdId_Type(Integer32):
    """Custom type genCmdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cmdIDRecallConfig", 2),
          ("cmdIDReboot", 3),
          ("cmdIDShutDown", 5),
          ("cmdIDBroadcast", 6),
          ("cmdIDConfigDownload", 7),
          ("cmdIDConfigUpload", 8))
    )


_GenCmdId_Type.__name__ = "Integer32"
_GenCmdId_Object = MibScalar
genCmdId = _GenCmdId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 100, 3),
    _GenCmdId_Type()
)
genCmdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCmdId.setStatus("current")
_GenCmdOid_Type = OBJECTID
_GenCmdOid_Object = MibScalar
genCmdOid = _GenCmdOid_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 100, 4),
    _GenCmdOid_Type()
)
genCmdOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCmdOid.setStatus("current")
_GenCmdExecutionDate_Type = DateAndTime
_GenCmdExecutionDate_Object = MibScalar
genCmdExecutionDate = _GenCmdExecutionDate_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 100, 5),
    _GenCmdExecutionDate_Type()
)
genCmdExecutionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCmdExecutionDate.setStatus("current")
_GenTransferFileContent_ObjectIdentity = ObjectIdentity
genTransferFileContent = _GenTransferFileContent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200)
)
_GenTransferFileSize_Type = Integer32
_GenTransferFileSize_Object = MibScalar
genTransferFileSize = _GenTransferFileSize_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200, 1),
    _GenTransferFileSize_Type()
)
genTransferFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genTransferFileSize.setStatus("current")
_GenTransferBufferTable_Object = MibTable
genTransferBufferTable = _GenTransferBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200, 2)
)
if mibBuilder.loadTexts:
    genTransferBufferTable.setStatus("current")
_GenTransferBufferEntry_Object = MibTableRow
genTransferBufferEntry = _GenTransferBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200, 2, 1)
)
genTransferBufferEntry.setIndexNames(
    (0, "CP9K-MIB", "genTransferBufferId"),
)
if mibBuilder.loadTexts:
    genTransferBufferEntry.setStatus("current")
_GenTransferBufferId_Type = Unsigned32
_GenTransferBufferId_Object = MibTableColumn
genTransferBufferId = _GenTransferBufferId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200, 2, 1, 1),
    _GenTransferBufferId_Type()
)
genTransferBufferId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genTransferBufferId.setStatus("current")


class _GenTransferBufferValue_Type(OctetString):
    """Custom type genTransferBufferValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_GenTransferBufferValue_Type.__name__ = "OctetString"
_GenTransferBufferValue_Object = MibTableColumn
genTransferBufferValue = _GenTransferBufferValue_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200, 2, 1, 2),
    _GenTransferBufferValue_Type()
)
genTransferBufferValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genTransferBufferValue.setStatus("current")
_GenTransferBufferRowStatus_Type = RowStatus
_GenTransferBufferRowStatus_Object = MibTableColumn
genTransferBufferRowStatus = _GenTransferBufferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 5, 200, 2, 1, 3),
    _GenTransferBufferRowStatus_Type()
)
genTransferBufferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genTransferBufferRowStatus.setStatus("current")
_GenTraps_ObjectIdentity = ObjectIdentity
genTraps = _GenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6)
)
_GenTrapSpecificVariables_ObjectIdentity = ObjectIdentity
genTrapSpecificVariables = _GenTrapSpecificVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 1)
)
_GenTrapNumber_Type = Integer32
_GenTrapNumber_Object = MibScalar
genTrapNumber = _GenTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 1, 1),
    _GenTrapNumber_Type()
)
genTrapNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    genTrapNumber.setStatus("current")
_GenTrapPreviousNumber_Type = Integer32
_GenTrapPreviousNumber_Object = MibScalar
genTrapPreviousNumber = _GenTrapPreviousNumber_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 1, 2),
    _GenTrapPreviousNumber_Type()
)
genTrapPreviousNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    genTrapPreviousNumber.setStatus("current")
_GenTrapStatusOid_Type = OBJECTID
_GenTrapStatusOid_Object = MibScalar
genTrapStatusOid = _GenTrapStatusOid_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 1, 3),
    _GenTrapStatusOid_Type()
)
genTrapStatusOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    genTrapStatusOid.setStatus("current")


class _GenTrapGenericSrvMessage_Type(DisplayString):
    """Custom type genTrapGenericSrvMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GenTrapGenericSrvMessage_Type.__name__ = "DisplayString"
_GenTrapGenericSrvMessage_Object = MibScalar
genTrapGenericSrvMessage = _GenTrapGenericSrvMessage_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 1, 4),
    _GenTrapGenericSrvMessage_Type()
)
genTrapGenericSrvMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    genTrapGenericSrvMessage.setStatus("current")
_GenTrapVibeIpAddress_Type = IpAddress
_GenTrapVibeIpAddress_Object = MibScalar
genTrapVibeIpAddress = _GenTrapVibeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 1, 5),
    _GenTrapVibeIpAddress_Type()
)
genTrapVibeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genTrapVibeIpAddress.setStatus("current")
_GenPredefinedConfigTable_Object = MibTable
genPredefinedConfigTable = _GenPredefinedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7)
)
if mibBuilder.loadTexts:
    genPredefinedConfigTable.setStatus("current")
_GenPredefinedConfigEntry_Object = MibTableRow
genPredefinedConfigEntry = _GenPredefinedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1)
)
genPredefinedConfigEntry.setIndexNames(
    (0, "CP9K-MIB", "genPreConfigId"),
)
if mibBuilder.loadTexts:
    genPredefinedConfigEntry.setStatus("current")
_GenPreConfigId_Type = Integer32
_GenPreConfigId_Object = MibTableColumn
genPreConfigId = _GenPreConfigId_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1, 1),
    _GenPreConfigId_Type()
)
genPreConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPreConfigId.setStatus("current")


class _GenPreConfigType_Type(DisplayString):
    """Custom type genPreConfigType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenPreConfigType_Type.__name__ = "DisplayString"
_GenPreConfigType_Object = MibTableColumn
genPreConfigType = _GenPreConfigType_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1, 2),
    _GenPreConfigType_Type()
)
genPreConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPreConfigType.setStatus("current")


class _GenPreConfigDescription_Type(DisplayString):
    """Custom type genPreConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GenPreConfigDescription_Type.__name__ = "DisplayString"
_GenPreConfigDescription_Object = MibTableColumn
genPreConfigDescription = _GenPreConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1, 3),
    _GenPreConfigDescription_Type()
)
genPreConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPreConfigDescription.setStatus("current")
_GenPreConfigSaveDate_Type = DateAndTime
_GenPreConfigSaveDate_Object = MibTableColumn
genPreConfigSaveDate = _GenPreConfigSaveDate_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1, 4),
    _GenPreConfigSaveDate_Type()
)
genPreConfigSaveDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPreConfigSaveDate.setStatus("current")


class _GenPreConfigOrigin_Type(DisplayString):
    """Custom type genPreConfigOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenPreConfigOrigin_Type.__name__ = "DisplayString"
_GenPreConfigOrigin_Object = MibTableColumn
genPreConfigOrigin = _GenPreConfigOrigin_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1, 5),
    _GenPreConfigOrigin_Type()
)
genPreConfigOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPreConfigOrigin.setStatus("current")


class _GenPreConfigAuthor_Type(DisplayString):
    """Custom type genPreConfigAuthor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenPreConfigAuthor_Type.__name__ = "DisplayString"
_GenPreConfigAuthor_Object = MibTableColumn
genPreConfigAuthor = _GenPreConfigAuthor_Object(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 7, 1, 6),
    _GenPreConfigAuthor_Type()
)
genPreConfigAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPreConfigAuthor.setStatus("current")

# Managed Objects groups


# Notification objects

genTrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 2)
)
genTrapAlarm.setObjects(
      *(("CP9K-MIB", "genTrapNumber"),
        ("CP9K-MIB", "genTrapPreviousNumber"),
        ("CP9K-MIB", "genEventRecordId"),
        ("CP9K-MIB", "genEventTime"),
        ("CP9K-MIB", "genEventDeviceId"),
        ("CP9K-MIB", "genEventSubsystemId"),
        ("CP9K-MIB", "genEventObjectReference"),
        ("CP9K-MIB", "genEventType"),
        ("CP9K-MIB", "genEventProbableCause"),
        ("CP9K-MIB", "genEventSpecificProblem"),
        ("CP9K-MIB", "genEventSeverity"),
        ("CP9K-MIB", "genEventCategory"),
        ("CP9K-MIB", "genEventSubsystemType"),
        ("CP9K-MIB", "genEventLabel"),
        ("CP9K-MIB", "genTrapVibeIpAddress"))
)
if mibBuilder.loadTexts:
    genTrapAlarm.setStatus(
        "current"
    )

genTrapOtherEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 3)
)
genTrapOtherEvent.setObjects(
      *(("CP9K-MIB", "genTrapNumber"),
        ("CP9K-MIB", "genTrapPreviousNumber"),
        ("CP9K-MIB", "genEventRecordId"),
        ("CP9K-MIB", "genEventTime"),
        ("CP9K-MIB", "genEventDeviceId"),
        ("CP9K-MIB", "genEventSubsystemId"),
        ("CP9K-MIB", "genEventObjectReference"),
        ("CP9K-MIB", "genEventType"),
        ("CP9K-MIB", "genEventCategory"),
        ("CP9K-MIB", "genEventSubsystemType"),
        ("CP9K-MIB", "genEventLabel"),
        ("CP9K-MIB", "genEventExtraInfo"),
        ("CP9K-MIB", "genEventOldValue"),
        ("CP9K-MIB", "genEventNewValue"),
        ("CP9K-MIB", "genTrapVibeIpAddress"))
)
if mibBuilder.loadTexts:
    genTrapOtherEvent.setStatus(
        "current"
    )

genTrapStatusVarChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 4)
)
genTrapStatusVarChange.setObjects(
      *(("CP9K-MIB", "genTrapNumber"),
        ("CP9K-MIB", "genTrapPreviousNumber"),
        ("CP9K-MIB", "genTrapStatusOid"),
        ("CP9K-MIB", "genTrapVibeIpAddress"))
)
if mibBuilder.loadTexts:
    genTrapStatusVarChange.setStatus(
        "current"
    )

genTrapGenericService = NotificationType(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 20)
)
genTrapGenericService.setObjects(
      *(("CP9K-MIB", "genTrapNumber"),
        ("CP9K-MIB", "genTrapPreviousNumber"),
        ("CP9K-MIB", "genTrapGenericSrvMessage"),
        ("CP9K-MIB", "genTrapVibeIpAddress"))
)
if mibBuilder.loadTexts:
    genTrapGenericService.setStatus(
        "current"
    )

genTrapConfigurationApply = NotificationType(
    (1, 3, 6, 1, 4, 1, 38124, 7, 1, 6, 30)
)
genTrapConfigurationApply.setObjects(
      *(("CP9K-MIB", "genTrapNumber"),
        ("CP9K-MIB", "genTrapPreviousNumber"),
        ("CP9K-MIB", "genTrapVibeIpAddress"))
)
if mibBuilder.loadTexts:
    genTrapConfigurationApply.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CP9K-MIB",
    **{"Boolean": Boolean,
       "RowStatus": RowStatus,
       "OBJECTID": OBJECTID,
       "harmonicFrance": harmonicFrance,
       "vibeCP9k": vibeCP9k,
       "general": general,
       "genManagerTable": genManagerTable,
       "genManagerEntry": genManagerEntry,
       "genManagerIndex": genManagerIndex,
       "genManagerIpAddress": genManagerIpAddress,
       "genManagerTrapEnable": genManagerTrapEnable,
       "genManagerTrapTypeSelection": genManagerTrapTypeSelection,
       "genManagerEventTrapSeverityFilter": genManagerEventTrapSeverityFilter,
       "genManagerTrapGenericFilter": genManagerTrapGenericFilter,
       "genManagerPersistent": genManagerPersistent,
       "genManagerConfigLock": genManagerConfigLock,
       "genSystemInfo": genSystemInfo,
       "genSysTypeName": genSysTypeName,
       "genSysTypeDescr": genSysTypeDescr,
       "genMibVersion": genMibVersion,
       "genDeviceId": genDeviceId,
       "genDeviceName": genDeviceName,
       "genProductSerialNumber": genProductSerialNumber,
       "genProductSoftVersion": genProductSoftVersion,
       "genSysAlarmOutput1": genSysAlarmOutput1,
       "genSysAlarmOutput2": genSysAlarmOutput2,
       "genSysAlarmStatus": genSysAlarmStatus,
       "genSysAlarmUpdate": genSysAlarmUpdate,
       "genSysRedundStatus": genSysRedundStatus,
       "genOptionEqpCode": genOptionEqpCode,
       "genBoardInfoTable": genBoardInfoTable,
       "genBoardInfoEntry": genBoardInfoEntry,
       "genBoardSlotNb": genBoardSlotNb,
       "genBoardTypeDetected": genBoardTypeDetected,
       "genBoardSerialNumber": genBoardSerialNumber,
       "genBoardTypeDeclared": genBoardTypeDeclared,
       "genBoardSubSystemId": genBoardSubSystemId,
       "genBoardAlarmStatus": genBoardAlarmStatus,
       "genBoardRedundStatus": genBoardRedundStatus,
       "genRidInfoTable": genRidInfoTable,
       "genRidInfoEntry": genRidInfoEntry,
       "genRidSlotNb": genRidSlotNb,
       "genRidAttributeName": genRidAttributeName,
       "genRidAttributeValue": genRidAttributeValue,
       "genSubSystemInfoTable": genSubSystemInfoTable,
       "genSubSystemInfoEntry": genSubSystemInfoEntry,
       "genSubSystemId": genSubSystemId,
       "genSubSystemType": genSubSystemType,
       "genSubSystemTypeName": genSubSystemTypeName,
       "genSubSystemName": genSubSystemName,
       "genSubSystemAlarmStatus": genSubSystemAlarmStatus,
       "genSubSystemRedundStatus": genSubSystemRedundStatus,
       "genSoftwareInfoTable": genSoftwareInfoTable,
       "genSoftwareInfoEntry": genSoftwareInfoEntry,
       "genSoftSlotNb": genSoftSlotNb,
       "genSoftTypeName": genSoftTypeName,
       "genSoftStatus": genSoftStatus,
       "genSoftVersion": genSoftVersion,
       "genOptionInfoTable": genOptionInfoTable,
       "genOptionInfoEntry": genOptionInfoEntry,
       "genOptionSubSystemId": genOptionSubSystemId,
       "genOptionId": genOptionId,
       "genOptionTypeName": genOptionTypeName,
       "genOptionInstalled": genOptionInstalled,
       "genOptionExpiryDate": genOptionExpiryDate,
       "genOptionAmount": genOptionAmount,
       "genIpInterfaceTable": genIpInterfaceTable,
       "genIpInterfaceEntry": genIpInterfaceEntry,
       "genIpIfSlotNb": genIpIfSlotNb,
       "genIpIfId": genIpIfId,
       "genIpIfAddress": genIpIfAddress,
       "genIpIfNetmask": genIpIfNetmask,
       "genIpIfGateway": genIpIfGateway,
       "genIpIfMacAddress": genIpIfMacAddress,
       "genAlarmTable": genAlarmTable,
       "genAlarmEntry": genAlarmEntry,
       "genAlarmSubsystemId": genAlarmSubsystemId,
       "genAlarmObjectReference": genAlarmObjectReference,
       "genAlarmProbableCause": genAlarmProbableCause,
       "genAlarmSpecificProblem": genAlarmSpecificProblem,
       "genAlarmTime": genAlarmTime,
       "genAlarmSeverity": genAlarmSeverity,
       "genAlarmCategory": genAlarmCategory,
       "genAlarmSubsystemType": genAlarmSubsystemType,
       "genAlarmLabel": genAlarmLabel,
       "genAlarmOptAlarmId": genAlarmOptAlarmId,
       "genAlarmOptAlarmIdExt": genAlarmOptAlarmIdExt,
       "genEventTable": genEventTable,
       "genEventEntry": genEventEntry,
       "genEventRecordId": genEventRecordId,
       "genEventTime": genEventTime,
       "genEventDeviceId": genEventDeviceId,
       "genEventSubsystemId": genEventSubsystemId,
       "genEventObjectReference": genEventObjectReference,
       "genEventType": genEventType,
       "genEventProbableCause": genEventProbableCause,
       "genEventSpecificProblem": genEventSpecificProblem,
       "genEventSeverity": genEventSeverity,
       "genEventCategory": genEventCategory,
       "genEventSubsystemType": genEventSubsystemType,
       "genEventLabel": genEventLabel,
       "genEventExtraInfo": genEventExtraInfo,
       "genEventOldValue": genEventOldValue,
       "genEventNewValue": genEventNewValue,
       "genEventOptEventId": genEventOptEventId,
       "genEventOptEventIdExt": genEventOptEventIdExt,
       "genCommands": genCommands,
       "genCmdReboot": genCmdReboot,
       "genCmdRecallConfig": genCmdRecallConfig,
       "genRecallConfigId": genRecallConfigId,
       "genRecallSubsystemId": genRecallSubsystemId,
       "genRecallApply": genRecallApply,
       "genCmdShutdown": genCmdShutdown,
       "genCmdBroadcast": genCmdBroadcast,
       "genCmdBcastStatus": genCmdBcastStatus,
       "genCmdConfigTransfer": genCmdConfigTransfer,
       "genConfigTransferBufferMaxSize": genConfigTransferBufferMaxSize,
       "genConfigTransferCommand": genConfigTransferCommand,
       "genCmdExecutionInfo": genCmdExecutionInfo,
       "genCmdStatus": genCmdStatus,
       "genCmdReport": genCmdReport,
       "genCmdId": genCmdId,
       "genCmdOid": genCmdOid,
       "genCmdExecutionDate": genCmdExecutionDate,
       "genTransferFileContent": genTransferFileContent,
       "genTransferFileSize": genTransferFileSize,
       "genTransferBufferTable": genTransferBufferTable,
       "genTransferBufferEntry": genTransferBufferEntry,
       "genTransferBufferId": genTransferBufferId,
       "genTransferBufferValue": genTransferBufferValue,
       "genTransferBufferRowStatus": genTransferBufferRowStatus,
       "genTraps": genTraps,
       "genTrapSpecificVariables": genTrapSpecificVariables,
       "genTrapNumber": genTrapNumber,
       "genTrapPreviousNumber": genTrapPreviousNumber,
       "genTrapStatusOid": genTrapStatusOid,
       "genTrapGenericSrvMessage": genTrapGenericSrvMessage,
       "genTrapVibeIpAddress": genTrapVibeIpAddress,
       "genTrapAlarm": genTrapAlarm,
       "genTrapOtherEvent": genTrapOtherEvent,
       "genTrapStatusVarChange": genTrapStatusVarChange,
       "genTrapGenericService": genTrapGenericService,
       "genTrapConfigurationApply": genTrapConfigurationApply,
       "genPredefinedConfigTable": genPredefinedConfigTable,
       "genPredefinedConfigEntry": genPredefinedConfigEntry,
       "genPreConfigId": genPreConfigId,
       "genPreConfigType": genPreConfigType,
       "genPreConfigDescription": genPreConfigDescription,
       "genPreConfigSaveDate": genPreConfigSaveDate,
       "genPreConfigOrigin": genPreConfigOrigin,
       "genPreConfigAuthor": genPreConfigAuthor}
)
