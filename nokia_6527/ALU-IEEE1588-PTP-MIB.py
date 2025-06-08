# SNMP MIB module (ALU-IEEE1588-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-IEEE1588-PTP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxPortAdminStatus,
 TmnxSETSRefSource,
 tmnxChassisIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxPortAdminStatus",
    "TmnxSETSRefSource",
    "tmnxChassisIndex")


# MODULE-IDENTITY

alu1588PtpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    alu1588PtpMIBModule.setRevisions(
        ("1910-07-01 00:00",
         "1909-01-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Alu1588PtpClockId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class Alu1588PtpClockIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class Alu1588PtpPortRecoveredClockState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("freeRun", 1),
          ("acquiring", 2),
          ("phase-tracking", 3),
          ("holdover", 4),
          ("locked", 5))
    )



class Alu1588PtpPortState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("pre-master", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )



# MIB Managed Objects in the order of their OIDs

_Alu1588PtpMIBConformance_ObjectIdentity = ObjectIdentity
alu1588PtpMIBConformance = _Alu1588PtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9)
)
_Alu1588PtpConformance_ObjectIdentity = ObjectIdentity
alu1588PtpConformance = _Alu1588PtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1)
)
_Alu1588PtpCompliances_ObjectIdentity = ObjectIdentity
alu1588PtpCompliances = _Alu1588PtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 1)
)
_Alu1588PtpComp7705_ObjectIdentity = ObjectIdentity
alu1588PtpComp7705 = _Alu1588PtpComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 1, 1)
)
_Alu1588PtpGroups_ObjectIdentity = ObjectIdentity
alu1588PtpGroups = _Alu1588PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2)
)
_Alu1588PtpObjs_ObjectIdentity = ObjectIdentity
alu1588PtpObjs = _Alu1588PtpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9)
)
_Alu1588PtpClock_ObjectIdentity = ObjectIdentity
alu1588PtpClock = _Alu1588PtpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1)
)
_Alu1588PtpClockConfigAdmTable_Object = MibTable
alu1588PtpClockConfigAdmTable = _Alu1588PtpClockConfigAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    alu1588PtpClockConfigAdmTable.setStatus("obsolete")
_Alu1588PtpClockConfigAdmEntry_Object = MibTableRow
alu1588PtpClockConfigAdmEntry = _Alu1588PtpClockConfigAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 1, 1)
)
alu1588PtpClockConfigAdmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpClockConfigAdmClockIndex"),
)
if mibBuilder.loadTexts:
    alu1588PtpClockConfigAdmEntry.setStatus("obsolete")
_Alu1588PtpClockConfigAdmClockIndex_Type = Alu1588PtpClockIndex
_Alu1588PtpClockConfigAdmClockIndex_Object = MibTableColumn
alu1588PtpClockConfigAdmClockIndex = _Alu1588PtpClockConfigAdmClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 1, 1, 1),
    _Alu1588PtpClockConfigAdmClockIndex_Type()
)
alu1588PtpClockConfigAdmClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alu1588PtpClockConfigAdmClockIndex.setStatus("obsolete")


class _Alu1588PtpClockConfigAdmDomain_Type(Unsigned32):
    """Custom type alu1588PtpClockConfigAdmDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Alu1588PtpClockConfigAdmDomain_Type.__name__ = "Unsigned32"
_Alu1588PtpClockConfigAdmDomain_Object = MibTableColumn
alu1588PtpClockConfigAdmDomain = _Alu1588PtpClockConfigAdmDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 1, 1, 2),
    _Alu1588PtpClockConfigAdmDomain_Type()
)
alu1588PtpClockConfigAdmDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpClockConfigAdmDomain.setStatus("obsolete")


class _Alu1588PtpClockConfigAdmSlaveOnly_Type(TruthValue):
    """Custom type alu1588PtpClockConfigAdmSlaveOnly based on TruthValue"""
    defaultValue = 1


_Alu1588PtpClockConfigAdmSlaveOnly_Type.__name__ = "TruthValue"
_Alu1588PtpClockConfigAdmSlaveOnly_Object = MibTableColumn
alu1588PtpClockConfigAdmSlaveOnly = _Alu1588PtpClockConfigAdmSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 1, 1, 3),
    _Alu1588PtpClockConfigAdmSlaveOnly_Type()
)
alu1588PtpClockConfigAdmSlaveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpClockConfigAdmSlaveOnly.setStatus("obsolete")
_Alu1588PtpClockDefaultDSTable_Object = MibTable
alu1588PtpClockDefaultDSTable = _Alu1588PtpClockDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSTable.setStatus("obsolete")
_Alu1588PtpClockDefaultDSEntry_Object = MibTableRow
alu1588PtpClockDefaultDSEntry = _Alu1588PtpClockDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1)
)
alu1588PtpClockDefaultDSEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpClockIndex"),
)
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSEntry.setStatus("obsolete")
_Alu1588PtpClockIndex_Type = Alu1588PtpClockIndex
_Alu1588PtpClockIndex_Object = MibTableColumn
alu1588PtpClockIndex = _Alu1588PtpClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 1),
    _Alu1588PtpClockIndex_Type()
)
alu1588PtpClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alu1588PtpClockIndex.setStatus("obsolete")
_Alu1588PtpClockDefaultDSIdentifier_Type = Alu1588PtpClockId
_Alu1588PtpClockDefaultDSIdentifier_Object = MibTableColumn
alu1588PtpClockDefaultDSIdentifier = _Alu1588PtpClockDefaultDSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 2),
    _Alu1588PtpClockDefaultDSIdentifier_Type()
)
alu1588PtpClockDefaultDSIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSIdentifier.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSDomain_Type(Unsigned32):
    """Custom type alu1588PtpClockDefaultDSDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Alu1588PtpClockDefaultDSDomain_Type.__name__ = "Unsigned32"
_Alu1588PtpClockDefaultDSDomain_Object = MibTableColumn
alu1588PtpClockDefaultDSDomain = _Alu1588PtpClockDefaultDSDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 3),
    _Alu1588PtpClockDefaultDSDomain_Type()
)
alu1588PtpClockDefaultDSDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSDomain.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSTwoStepFlag_Type(Integer32):
    """Custom type alu1588PtpClockDefaultDSTwoStepFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptpStepTypeUnknown", 0),
          ("ptpTwoStepType", 1),
          ("ptpOneStepType", 2))
    )


_Alu1588PtpClockDefaultDSTwoStepFlag_Type.__name__ = "Integer32"
_Alu1588PtpClockDefaultDSTwoStepFlag_Object = MibTableColumn
alu1588PtpClockDefaultDSTwoStepFlag = _Alu1588PtpClockDefaultDSTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 4),
    _Alu1588PtpClockDefaultDSTwoStepFlag_Type()
)
alu1588PtpClockDefaultDSTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSTwoStepFlag.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSType_Type(Integer32):
    """Custom type alu1588PtpClockDefaultDSType based on Integer32"""
    defaultValue = 2

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
        *(("ptpTypeUnknown", 0),
          ("ptpTypeBoundary", 1),
          ("ptpTypeOrdinary", 2),
          ("ptpTypeEndToEndTransparent", 3),
          ("ptpTypePeerToPeerTransparent", 4),
          ("ptpTypeManagementNode", 5))
    )


_Alu1588PtpClockDefaultDSType_Type.__name__ = "Integer32"
_Alu1588PtpClockDefaultDSType_Object = MibTableColumn
alu1588PtpClockDefaultDSType = _Alu1588PtpClockDefaultDSType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 5),
    _Alu1588PtpClockDefaultDSType_Type()
)
alu1588PtpClockDefaultDSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSType.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSNumberOfPorts_Type(Unsigned32):
    """Custom type alu1588PtpClockDefaultDSNumberOfPorts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Alu1588PtpClockDefaultDSNumberOfPorts_Type.__name__ = "Unsigned32"
_Alu1588PtpClockDefaultDSNumberOfPorts_Object = MibTableColumn
alu1588PtpClockDefaultDSNumberOfPorts = _Alu1588PtpClockDefaultDSNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 6),
    _Alu1588PtpClockDefaultDSNumberOfPorts_Type()
)
alu1588PtpClockDefaultDSNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSNumberOfPorts.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSClass_Type(Unsigned32):
    """Custom type alu1588PtpClockDefaultDSClass based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockDefaultDSClass_Type.__name__ = "Unsigned32"
_Alu1588PtpClockDefaultDSClass_Object = MibTableColumn
alu1588PtpClockDefaultDSClass = _Alu1588PtpClockDefaultDSClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 7),
    _Alu1588PtpClockDefaultDSClass_Type()
)
alu1588PtpClockDefaultDSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSClass.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSAccuracy_Type(Unsigned32):
    """Custom type alu1588PtpClockDefaultDSAccuracy based on Unsigned32"""
    defaultValue = 254

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockDefaultDSAccuracy_Type.__name__ = "Unsigned32"
_Alu1588PtpClockDefaultDSAccuracy_Object = MibTableColumn
alu1588PtpClockDefaultDSAccuracy = _Alu1588PtpClockDefaultDSAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 8),
    _Alu1588PtpClockDefaultDSAccuracy_Type()
)
alu1588PtpClockDefaultDSAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSAccuracy.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSOffsetScaledLogVariance_Type(Integer32):
    """Custom type alu1588PtpClockDefaultDSOffsetScaledLogVariance based on Integer32"""
    defaultValue = 65535


_Alu1588PtpClockDefaultDSOffsetScaledLogVariance_Type.__name__ = "Integer32"
_Alu1588PtpClockDefaultDSOffsetScaledLogVariance_Object = MibTableColumn
alu1588PtpClockDefaultDSOffsetScaledLogVariance = _Alu1588PtpClockDefaultDSOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 9),
    _Alu1588PtpClockDefaultDSOffsetScaledLogVariance_Type()
)
alu1588PtpClockDefaultDSOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSOffsetScaledLogVariance.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSPriority1_Type(Unsigned32):
    """Custom type alu1588PtpClockDefaultDSPriority1 based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockDefaultDSPriority1_Type.__name__ = "Unsigned32"
_Alu1588PtpClockDefaultDSPriority1_Object = MibTableColumn
alu1588PtpClockDefaultDSPriority1 = _Alu1588PtpClockDefaultDSPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 10),
    _Alu1588PtpClockDefaultDSPriority1_Type()
)
alu1588PtpClockDefaultDSPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSPriority1.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSPriority2_Type(Unsigned32):
    """Custom type alu1588PtpClockDefaultDSPriority2 based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockDefaultDSPriority2_Type.__name__ = "Unsigned32"
_Alu1588PtpClockDefaultDSPriority2_Object = MibTableColumn
alu1588PtpClockDefaultDSPriority2 = _Alu1588PtpClockDefaultDSPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 11),
    _Alu1588PtpClockDefaultDSPriority2_Type()
)
alu1588PtpClockDefaultDSPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSPriority2.setStatus("obsolete")


class _Alu1588PtpClockDefaultDSSlaveOnly_Type(TruthValue):
    """Custom type alu1588PtpClockDefaultDSSlaveOnly based on TruthValue"""
    defaultValue = 1


_Alu1588PtpClockDefaultDSSlaveOnly_Type.__name__ = "TruthValue"
_Alu1588PtpClockDefaultDSSlaveOnly_Object = MibTableColumn
alu1588PtpClockDefaultDSSlaveOnly = _Alu1588PtpClockDefaultDSSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 2, 1, 12),
    _Alu1588PtpClockDefaultDSSlaveOnly_Type()
)
alu1588PtpClockDefaultDSSlaveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockDefaultDSSlaveOnly.setStatus("obsolete")
_Alu1588PtpClockCurrentDSTable_Object = MibTable
alu1588PtpClockCurrentDSTable = _Alu1588PtpClockCurrentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    alu1588PtpClockCurrentDSTable.setStatus("obsolete")
_Alu1588PtpClockCurrentDSEntry_Object = MibTableRow
alu1588PtpClockCurrentDSEntry = _Alu1588PtpClockCurrentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 3, 1)
)
alu1588PtpClockCurrentDSEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpClockIndex"),
)
if mibBuilder.loadTexts:
    alu1588PtpClockCurrentDSEntry.setStatus("obsolete")


class _Alu1588PtpClockCurrentDSIdentifier_Type(OctetString):
    """Custom type alu1588PtpClockCurrentDSIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Alu1588PtpClockCurrentDSIdentifier_Type.__name__ = "OctetString"
_Alu1588PtpClockCurrentDSIdentifier_Object = MibTableColumn
alu1588PtpClockCurrentDSIdentifier = _Alu1588PtpClockCurrentDSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 3, 1, 1),
    _Alu1588PtpClockCurrentDSIdentifier_Type()
)
alu1588PtpClockCurrentDSIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockCurrentDSIdentifier.setStatus("obsolete")


class _Alu1588PtpClockCurrentDSStepsRemoved_Type(Unsigned32):
    """Custom type alu1588PtpClockCurrentDSStepsRemoved based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockCurrentDSStepsRemoved_Type.__name__ = "Unsigned32"
_Alu1588PtpClockCurrentDSStepsRemoved_Object = MibTableColumn
alu1588PtpClockCurrentDSStepsRemoved = _Alu1588PtpClockCurrentDSStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 3, 1, 2),
    _Alu1588PtpClockCurrentDSStepsRemoved_Type()
)
alu1588PtpClockCurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockCurrentDSStepsRemoved.setStatus("obsolete")
_Alu1588PtpClockParentDSTable_Object = MibTable
alu1588PtpClockParentDSTable = _Alu1588PtpClockParentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSTable.setStatus("obsolete")
_Alu1588PtpClockParentDSEntry_Object = MibTableRow
alu1588PtpClockParentDSEntry = _Alu1588PtpClockParentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1)
)
alu1588PtpClockParentDSEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpClockIndex"),
)
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSEntry.setStatus("obsolete")
_Alu1588PtpClockParentDSIdentifier_Type = Alu1588PtpClockId
_Alu1588PtpClockParentDSIdentifier_Object = MibTableColumn
alu1588PtpClockParentDSIdentifier = _Alu1588PtpClockParentDSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 1),
    _Alu1588PtpClockParentDSIdentifier_Type()
)
alu1588PtpClockParentDSIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSIdentifier.setStatus("obsolete")


class _Alu1588PtpClockParentDSPortNum_Type(Unsigned32):
    """Custom type alu1588PtpClockParentDSPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Alu1588PtpClockParentDSPortNum_Type.__name__ = "Unsigned32"
_Alu1588PtpClockParentDSPortNum_Object = MibTableColumn
alu1588PtpClockParentDSPortNum = _Alu1588PtpClockParentDSPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 2),
    _Alu1588PtpClockParentDSPortNum_Type()
)
alu1588PtpClockParentDSPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSPortNum.setStatus("obsolete")
_Alu1588PtpClockParentDSStats_Type = TruthValue
_Alu1588PtpClockParentDSStats_Object = MibTableColumn
alu1588PtpClockParentDSStats = _Alu1588PtpClockParentDSStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 3),
    _Alu1588PtpClockParentDSStats_Type()
)
alu1588PtpClockParentDSStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSStats.setStatus("obsolete")
_Alu1588PtpClockParentDSOffsetScaledLogVariance_Type = Integer32
_Alu1588PtpClockParentDSOffsetScaledLogVariance_Object = MibTableColumn
alu1588PtpClockParentDSOffsetScaledLogVariance = _Alu1588PtpClockParentDSOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 4),
    _Alu1588PtpClockParentDSOffsetScaledLogVariance_Type()
)
alu1588PtpClockParentDSOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSOffsetScaledLogVariance.setStatus("obsolete")
_Alu1588PtpClockParentDSGrandmasterClockId_Type = Alu1588PtpClockId
_Alu1588PtpClockParentDSGrandmasterClockId_Object = MibTableColumn
alu1588PtpClockParentDSGrandmasterClockId = _Alu1588PtpClockParentDSGrandmasterClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 6),
    _Alu1588PtpClockParentDSGrandmasterClockId_Type()
)
alu1588PtpClockParentDSGrandmasterClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSGrandmasterClockId.setStatus("obsolete")


class _Alu1588PtpClockParentDSGrandmasterClass_Type(Unsigned32):
    """Custom type alu1588PtpClockParentDSGrandmasterClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockParentDSGrandmasterClass_Type.__name__ = "Unsigned32"
_Alu1588PtpClockParentDSGrandmasterClass_Object = MibTableColumn
alu1588PtpClockParentDSGrandmasterClass = _Alu1588PtpClockParentDSGrandmasterClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 7),
    _Alu1588PtpClockParentDSGrandmasterClass_Type()
)
alu1588PtpClockParentDSGrandmasterClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSGrandmasterClass.setStatus("obsolete")


class _Alu1588PtpClockParentDSGrandmasterAccuracy_Type(Unsigned32):
    """Custom type alu1588PtpClockParentDSGrandmasterAccuracy based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockParentDSGrandmasterAccuracy_Type.__name__ = "Unsigned32"
_Alu1588PtpClockParentDSGrandmasterAccuracy_Object = MibTableColumn
alu1588PtpClockParentDSGrandmasterAccuracy = _Alu1588PtpClockParentDSGrandmasterAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 8),
    _Alu1588PtpClockParentDSGrandmasterAccuracy_Type()
)
alu1588PtpClockParentDSGrandmasterAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSGrandmasterAccuracy.setStatus("obsolete")
_Alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance_Type = Unsigned32
_Alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance_Object = MibTableColumn
alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance = _Alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 9),
    _Alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance_Type()
)
alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance.setStatus("obsolete")


class _Alu1588PtpClockParentDSGrandmasterPriority1_Type(Unsigned32):
    """Custom type alu1588PtpClockParentDSGrandmasterPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockParentDSGrandmasterPriority1_Type.__name__ = "Unsigned32"
_Alu1588PtpClockParentDSGrandmasterPriority1_Object = MibTableColumn
alu1588PtpClockParentDSGrandmasterPriority1 = _Alu1588PtpClockParentDSGrandmasterPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 10),
    _Alu1588PtpClockParentDSGrandmasterPriority1_Type()
)
alu1588PtpClockParentDSGrandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSGrandmasterPriority1.setStatus("obsolete")


class _Alu1588PtpClockParentDSGrandmasterPriority2_Type(Unsigned32):
    """Custom type alu1588PtpClockParentDSGrandmasterPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Alu1588PtpClockParentDSGrandmasterPriority2_Type.__name__ = "Unsigned32"
_Alu1588PtpClockParentDSGrandmasterPriority2_Object = MibTableColumn
alu1588PtpClockParentDSGrandmasterPriority2 = _Alu1588PtpClockParentDSGrandmasterPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 1, 4, 1, 11),
    _Alu1588PtpClockParentDSGrandmasterPriority2_Type()
)
alu1588PtpClockParentDSGrandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpClockParentDSGrandmasterPriority2.setStatus("obsolete")
_Alu1588PtpPort_ObjectIdentity = ObjectIdentity
alu1588PtpPort = _Alu1588PtpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2)
)
_Alu1588PtpPortConfigAdmTable_Object = MibTable
alu1588PtpPortConfigAdmTable = _Alu1588PtpPortConfigAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmTable.setStatus("obsolete")
_Alu1588PtpPortConfigAdmEntry_Object = MibTableRow
alu1588PtpPortConfigAdmEntry = _Alu1588PtpPortConfigAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1)
)
alu1588PtpPortConfigAdmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmReference"),
)
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmEntry.setStatus("obsolete")
_Alu1588PtpPortConfigAdmReference_Type = TmnxSETSRefSource
_Alu1588PtpPortConfigAdmReference_Object = MibTableColumn
alu1588PtpPortConfigAdmReference = _Alu1588PtpPortConfigAdmReference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 1),
    _Alu1588PtpPortConfigAdmReference_Type()
)
alu1588PtpPortConfigAdmReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmReference.setStatus("obsolete")
_Alu1588PtpPortConfigAdmClockIndex_Type = Alu1588PtpClockIndex
_Alu1588PtpPortConfigAdmClockIndex_Object = MibTableColumn
alu1588PtpPortConfigAdmClockIndex = _Alu1588PtpPortConfigAdmClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 2),
    _Alu1588PtpPortConfigAdmClockIndex_Type()
)
alu1588PtpPortConfigAdmClockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmClockIndex.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmMulticast_Type(TruthValue):
    """Custom type alu1588PtpPortConfigAdmMulticast based on TruthValue"""
    defaultValue = 2


_Alu1588PtpPortConfigAdmMulticast_Type.__name__ = "TruthValue"
_Alu1588PtpPortConfigAdmMulticast_Object = MibTableColumn
alu1588PtpPortConfigAdmMulticast = _Alu1588PtpPortConfigAdmMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 3),
    _Alu1588PtpPortConfigAdmMulticast_Type()
)
alu1588PtpPortConfigAdmMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmMulticast.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmMaster1IpAddrType_Type(InetAddressType):
    """Custom type alu1588PtpPortConfigAdmMaster1IpAddrType based on InetAddressType"""
    defaultValue = 0


_Alu1588PtpPortConfigAdmMaster1IpAddrType_Type.__name__ = "InetAddressType"
_Alu1588PtpPortConfigAdmMaster1IpAddrType_Object = MibTableColumn
alu1588PtpPortConfigAdmMaster1IpAddrType = _Alu1588PtpPortConfigAdmMaster1IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 4),
    _Alu1588PtpPortConfigAdmMaster1IpAddrType_Type()
)
alu1588PtpPortConfigAdmMaster1IpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmMaster1IpAddrType.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmMaster1IpAddr_Type(InetAddress):
    """Custom type alu1588PtpPortConfigAdmMaster1IpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Alu1588PtpPortConfigAdmMaster1IpAddr_Type.__name__ = "InetAddress"
_Alu1588PtpPortConfigAdmMaster1IpAddr_Object = MibTableColumn
alu1588PtpPortConfigAdmMaster1IpAddr = _Alu1588PtpPortConfigAdmMaster1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 5),
    _Alu1588PtpPortConfigAdmMaster1IpAddr_Type()
)
alu1588PtpPortConfigAdmMaster1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmMaster1IpAddr.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmMaster2IpAddrType_Type(InetAddressType):
    """Custom type alu1588PtpPortConfigAdmMaster2IpAddrType based on InetAddressType"""
    defaultValue = 0


_Alu1588PtpPortConfigAdmMaster2IpAddrType_Type.__name__ = "InetAddressType"
_Alu1588PtpPortConfigAdmMaster2IpAddrType_Object = MibTableColumn
alu1588PtpPortConfigAdmMaster2IpAddrType = _Alu1588PtpPortConfigAdmMaster2IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 6),
    _Alu1588PtpPortConfigAdmMaster2IpAddrType_Type()
)
alu1588PtpPortConfigAdmMaster2IpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmMaster2IpAddrType.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmMaster2IpAddr_Type(InetAddress):
    """Custom type alu1588PtpPortConfigAdmMaster2IpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Alu1588PtpPortConfigAdmMaster2IpAddr_Type.__name__ = "InetAddress"
_Alu1588PtpPortConfigAdmMaster2IpAddr_Object = MibTableColumn
alu1588PtpPortConfigAdmMaster2IpAddr = _Alu1588PtpPortConfigAdmMaster2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 7),
    _Alu1588PtpPortConfigAdmMaster2IpAddr_Type()
)
alu1588PtpPortConfigAdmMaster2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmMaster2IpAddr.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmAnnoRxTimeout_Type(Unsigned32):
    """Custom type alu1588PtpPortConfigAdmAnnoRxTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Alu1588PtpPortConfigAdmAnnoRxTimeout_Type.__name__ = "Unsigned32"
_Alu1588PtpPortConfigAdmAnnoRxTimeout_Object = MibTableColumn
alu1588PtpPortConfigAdmAnnoRxTimeout = _Alu1588PtpPortConfigAdmAnnoRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 8),
    _Alu1588PtpPortConfigAdmAnnoRxTimeout_Type()
)
alu1588PtpPortConfigAdmAnnoRxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmAnnoRxTimeout.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmLogAnnoInterval_Type(Integer32):
    """Custom type alu1588PtpPortConfigAdmLogAnnoInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Alu1588PtpPortConfigAdmLogAnnoInterval_Type.__name__ = "Integer32"
_Alu1588PtpPortConfigAdmLogAnnoInterval_Object = MibTableColumn
alu1588PtpPortConfigAdmLogAnnoInterval = _Alu1588PtpPortConfigAdmLogAnnoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 9),
    _Alu1588PtpPortConfigAdmLogAnnoInterval_Type()
)
alu1588PtpPortConfigAdmLogAnnoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmLogAnnoInterval.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmLogSyncInterval_Type(Integer32):
    """Custom type alu1588PtpPortConfigAdmLogSyncInterval based on Integer32"""
    defaultValue = -6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, -6),
    )


_Alu1588PtpPortConfigAdmLogSyncInterval_Type.__name__ = "Integer32"
_Alu1588PtpPortConfigAdmLogSyncInterval_Object = MibTableColumn
alu1588PtpPortConfigAdmLogSyncInterval = _Alu1588PtpPortConfigAdmLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 10),
    _Alu1588PtpPortConfigAdmLogSyncInterval_Type()
)
alu1588PtpPortConfigAdmLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmLogSyncInterval.setStatus("obsolete")
_Alu1588PtpPortConfigAdmAdminStatus_Type = TmnxPortAdminStatus
_Alu1588PtpPortConfigAdmAdminStatus_Object = MibTableColumn
alu1588PtpPortConfigAdmAdminStatus = _Alu1588PtpPortConfigAdmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 11),
    _Alu1588PtpPortConfigAdmAdminStatus_Type()
)
alu1588PtpPortConfigAdmAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmAdminStatus.setStatus("obsolete")
_Alu1588PtpPortConfigAdmVrtrIfIndex_Type = InterfaceIndex
_Alu1588PtpPortConfigAdmVrtrIfIndex_Object = MibTableColumn
alu1588PtpPortConfigAdmVrtrIfIndex = _Alu1588PtpPortConfigAdmVrtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 12),
    _Alu1588PtpPortConfigAdmVrtrIfIndex_Type()
)
alu1588PtpPortConfigAdmVrtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmVrtrIfIndex.setStatus("obsolete")


class _Alu1588PtpPortConfigAdmUnicastNegotiate_Type(TruthValue):
    """Custom type alu1588PtpPortConfigAdmUnicastNegotiate based on TruthValue"""
    defaultValue = 1


_Alu1588PtpPortConfigAdmUnicastNegotiate_Type.__name__ = "TruthValue"
_Alu1588PtpPortConfigAdmUnicastNegotiate_Object = MibTableColumn
alu1588PtpPortConfigAdmUnicastNegotiate = _Alu1588PtpPortConfigAdmUnicastNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 1, 1, 13),
    _Alu1588PtpPortConfigAdmUnicastNegotiate_Type()
)
alu1588PtpPortConfigAdmUnicastNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alu1588PtpPortConfigAdmUnicastNegotiate.setStatus("obsolete")
_Alu1588PtpPortDSTable_Object = MibTable
alu1588PtpPortDSTable = _Alu1588PtpPortDSTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    alu1588PtpPortDSTable.setStatus("obsolete")
_Alu1588PtpPortDSEntry_Object = MibTableRow
alu1588PtpPortDSEntry = _Alu1588PtpPortDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1)
)
alu1588PtpPortDSEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSReference"),
)
if mibBuilder.loadTexts:
    alu1588PtpPortDSEntry.setStatus("obsolete")
_Alu1588PtpPortDSReference_Type = TmnxSETSRefSource
_Alu1588PtpPortDSReference_Object = MibTableColumn
alu1588PtpPortDSReference = _Alu1588PtpPortDSReference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 1),
    _Alu1588PtpPortDSReference_Type()
)
alu1588PtpPortDSReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alu1588PtpPortDSReference.setStatus("obsolete")
_Alu1588PtpPortDSClockIndex_Type = Alu1588PtpClockIndex
_Alu1588PtpPortDSClockIndex_Object = MibTableColumn
alu1588PtpPortDSClockIndex = _Alu1588PtpPortDSClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 2),
    _Alu1588PtpPortDSClockIndex_Type()
)
alu1588PtpPortDSClockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSClockIndex.setStatus("obsolete")
_Alu1588PtpPortDSClockId_Type = Alu1588PtpClockId
_Alu1588PtpPortDSClockId_Object = MibTableColumn
alu1588PtpPortDSClockId = _Alu1588PtpPortDSClockId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 3),
    _Alu1588PtpPortDSClockId_Type()
)
alu1588PtpPortDSClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSClockId.setStatus("obsolete")


class _Alu1588PtpPortDSPortNum_Type(Unsigned32):
    """Custom type alu1588PtpPortDSPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Alu1588PtpPortDSPortNum_Type.__name__ = "Unsigned32"
_Alu1588PtpPortDSPortNum_Object = MibTableColumn
alu1588PtpPortDSPortNum = _Alu1588PtpPortDSPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 4),
    _Alu1588PtpPortDSPortNum_Type()
)
alu1588PtpPortDSPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSPortNum.setStatus("obsolete")


class _Alu1588PtpPortDSDomain_Type(Unsigned32):
    """Custom type alu1588PtpPortDSDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Alu1588PtpPortDSDomain_Type.__name__ = "Unsigned32"
_Alu1588PtpPortDSDomain_Object = MibTableColumn
alu1588PtpPortDSDomain = _Alu1588PtpPortDSDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 5),
    _Alu1588PtpPortDSDomain_Type()
)
alu1588PtpPortDSDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSDomain.setStatus("obsolete")


class _Alu1588PtpPortDSMulticast_Type(TruthValue):
    """Custom type alu1588PtpPortDSMulticast based on TruthValue"""
    defaultValue = 2


_Alu1588PtpPortDSMulticast_Type.__name__ = "TruthValue"
_Alu1588PtpPortDSMulticast_Object = MibTableColumn
alu1588PtpPortDSMulticast = _Alu1588PtpPortDSMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 6),
    _Alu1588PtpPortDSMulticast_Type()
)
alu1588PtpPortDSMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSMulticast.setStatus("obsolete")
_Alu1588PtpPortDSMaster1IpAddrType_Type = InetAddressType
_Alu1588PtpPortDSMaster1IpAddrType_Object = MibTableColumn
alu1588PtpPortDSMaster1IpAddrType = _Alu1588PtpPortDSMaster1IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 7),
    _Alu1588PtpPortDSMaster1IpAddrType_Type()
)
alu1588PtpPortDSMaster1IpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSMaster1IpAddrType.setStatus("obsolete")


class _Alu1588PtpPortDSMaster1IpAddr_Type(InetAddress):
    """Custom type alu1588PtpPortDSMaster1IpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Alu1588PtpPortDSMaster1IpAddr_Type.__name__ = "InetAddress"
_Alu1588PtpPortDSMaster1IpAddr_Object = MibTableColumn
alu1588PtpPortDSMaster1IpAddr = _Alu1588PtpPortDSMaster1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 8),
    _Alu1588PtpPortDSMaster1IpAddr_Type()
)
alu1588PtpPortDSMaster1IpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSMaster1IpAddr.setStatus("obsolete")
_Alu1588PtpPortDSMaster2IpAddrType_Type = InetAddressType
_Alu1588PtpPortDSMaster2IpAddrType_Object = MibTableColumn
alu1588PtpPortDSMaster2IpAddrType = _Alu1588PtpPortDSMaster2IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 9),
    _Alu1588PtpPortDSMaster2IpAddrType_Type()
)
alu1588PtpPortDSMaster2IpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSMaster2IpAddrType.setStatus("obsolete")


class _Alu1588PtpPortDSMaster2IpAddr_Type(InetAddress):
    """Custom type alu1588PtpPortDSMaster2IpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Alu1588PtpPortDSMaster2IpAddr_Type.__name__ = "InetAddress"
_Alu1588PtpPortDSMaster2IpAddr_Object = MibTableColumn
alu1588PtpPortDSMaster2IpAddr = _Alu1588PtpPortDSMaster2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 10),
    _Alu1588PtpPortDSMaster2IpAddr_Type()
)
alu1588PtpPortDSMaster2IpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSMaster2IpAddr.setStatus("obsolete")


class _Alu1588PtpPortDSAnnoRxTimeout_Type(Unsigned32):
    """Custom type alu1588PtpPortDSAnnoRxTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Alu1588PtpPortDSAnnoRxTimeout_Type.__name__ = "Unsigned32"
_Alu1588PtpPortDSAnnoRxTimeout_Object = MibTableColumn
alu1588PtpPortDSAnnoRxTimeout = _Alu1588PtpPortDSAnnoRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 11),
    _Alu1588PtpPortDSAnnoRxTimeout_Type()
)
alu1588PtpPortDSAnnoRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSAnnoRxTimeout.setStatus("obsolete")


class _Alu1588PtpPortDSLogAnnoInterval_Type(Integer32):
    """Custom type alu1588PtpPortDSLogAnnoInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Alu1588PtpPortDSLogAnnoInterval_Type.__name__ = "Integer32"
_Alu1588PtpPortDSLogAnnoInterval_Object = MibTableColumn
alu1588PtpPortDSLogAnnoInterval = _Alu1588PtpPortDSLogAnnoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 12),
    _Alu1588PtpPortDSLogAnnoInterval_Type()
)
alu1588PtpPortDSLogAnnoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSLogAnnoInterval.setStatus("obsolete")


class _Alu1588PtpPortDSLogSyncInterval_Type(Integer32):
    """Custom type alu1588PtpPortDSLogSyncInterval based on Integer32"""
    defaultValue = -6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, -6),
    )


_Alu1588PtpPortDSLogSyncInterval_Type.__name__ = "Integer32"
_Alu1588PtpPortDSLogSyncInterval_Object = MibTableColumn
alu1588PtpPortDSLogSyncInterval = _Alu1588PtpPortDSLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 13),
    _Alu1588PtpPortDSLogSyncInterval_Type()
)
alu1588PtpPortDSLogSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSLogSyncInterval.setStatus("obsolete")
_Alu1588PtpPortDSAdminStatus_Type = TmnxPortAdminStatus
_Alu1588PtpPortDSAdminStatus_Object = MibTableColumn
alu1588PtpPortDSAdminStatus = _Alu1588PtpPortDSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 14),
    _Alu1588PtpPortDSAdminStatus_Type()
)
alu1588PtpPortDSAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSAdminStatus.setStatus("obsolete")
_Alu1588PtpPortDSVrtrIfIndex_Type = InterfaceIndex
_Alu1588PtpPortDSVrtrIfIndex_Object = MibTableColumn
alu1588PtpPortDSVrtrIfIndex = _Alu1588PtpPortDSVrtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 15),
    _Alu1588PtpPortDSVrtrIfIndex_Type()
)
alu1588PtpPortDSVrtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSVrtrIfIndex.setStatus("obsolete")


class _Alu1588PtpPortDSPortState_Type(Alu1588PtpPortState):
    """Custom type alu1588PtpPortDSPortState based on Alu1588PtpPortState"""
    defaultValue = 1


_Alu1588PtpPortDSPortState_Type.__name__ = "Alu1588PtpPortState"
_Alu1588PtpPortDSPortState_Object = MibTableColumn
alu1588PtpPortDSPortState = _Alu1588PtpPortDSPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 16),
    _Alu1588PtpPortDSPortState_Type()
)
alu1588PtpPortDSPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSPortState.setStatus("obsolete")


class _Alu1588PtpPortDSDelayMechanism_Type(Integer32):
    """Custom type alu1588PtpPortDSDelayMechanism based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2),
          ("disabled", 254))
    )


_Alu1588PtpPortDSDelayMechanism_Type.__name__ = "Integer32"
_Alu1588PtpPortDSDelayMechanism_Object = MibTableColumn
alu1588PtpPortDSDelayMechanism = _Alu1588PtpPortDSDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 17),
    _Alu1588PtpPortDSDelayMechanism_Type()
)
alu1588PtpPortDSDelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSDelayMechanism.setStatus("obsolete")


class _Alu1588PtpPortDSVersionNumber_Type(Integer32):
    """Custom type alu1588PtpPortDSVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("v2", 2)
    )


_Alu1588PtpPortDSVersionNumber_Type.__name__ = "Integer32"
_Alu1588PtpPortDSVersionNumber_Object = MibTableColumn
alu1588PtpPortDSVersionNumber = _Alu1588PtpPortDSVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 18),
    _Alu1588PtpPortDSVersionNumber_Type()
)
alu1588PtpPortDSVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSVersionNumber.setStatus("obsolete")


class _Alu1588PtpPortDSUnicastNegotiate_Type(TruthValue):
    """Custom type alu1588PtpPortDSUnicastNegotiate based on TruthValue"""
    defaultValue = 1


_Alu1588PtpPortDSUnicastNegotiate_Type.__name__ = "TruthValue"
_Alu1588PtpPortDSUnicastNegotiate_Object = MibTableColumn
alu1588PtpPortDSUnicastNegotiate = _Alu1588PtpPortDSUnicastNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 19),
    _Alu1588PtpPortDSUnicastNegotiate_Type()
)
alu1588PtpPortDSUnicastNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSUnicastNegotiate.setStatus("obsolete")


class _Alu1588PtpPortDSRecoveredClockState_Type(Alu1588PtpPortRecoveredClockState):
    """Custom type alu1588PtpPortDSRecoveredClockState based on Alu1588PtpPortRecoveredClockState"""
    defaultValue = 1


_Alu1588PtpPortDSRecoveredClockState_Type.__name__ = "Alu1588PtpPortRecoveredClockState"
_Alu1588PtpPortDSRecoveredClockState_Object = MibTableColumn
alu1588PtpPortDSRecoveredClockState = _Alu1588PtpPortDSRecoveredClockState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 2, 1, 20),
    _Alu1588PtpPortDSRecoveredClockState_Type()
)
alu1588PtpPortDSRecoveredClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDSRecoveredClockState.setStatus("obsolete")
_Alu1588PtpPortPacketStatsTable_Object = MibTable
alu1588PtpPortPacketStatsTable = _Alu1588PtpPortPacketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3)
)
if mibBuilder.loadTexts:
    alu1588PtpPortPacketStatsTable.setStatus("obsolete")
_Alu1588PtpPortPacketStatsEntry_Object = MibTableRow
alu1588PtpPortPacketStatsEntry = _Alu1588PtpPortPacketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1)
)
alu1588PtpPortPacketStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSReference"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortMasterIndex"),
)
if mibBuilder.loadTexts:
    alu1588PtpPortPacketStatsEntry.setStatus("obsolete")
_Alu1588PtpPortMasterIndex_Type = Integer32
_Alu1588PtpPortMasterIndex_Object = MibTableColumn
alu1588PtpPortMasterIndex = _Alu1588PtpPortMasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 1),
    _Alu1588PtpPortMasterIndex_Type()
)
alu1588PtpPortMasterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alu1588PtpPortMasterIndex.setStatus("obsolete")
_Alu1588PtpPortBadVersionDisc_Type = Counter64
_Alu1588PtpPortBadVersionDisc_Object = MibTableColumn
alu1588PtpPortBadVersionDisc = _Alu1588PtpPortBadVersionDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 2),
    _Alu1588PtpPortBadVersionDisc_Type()
)
alu1588PtpPortBadVersionDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortBadVersionDisc.setStatus("obsolete")
_Alu1588PtpPortBadDomainDisc_Type = Counter64
_Alu1588PtpPortBadDomainDisc_Object = MibTableColumn
alu1588PtpPortBadDomainDisc = _Alu1588PtpPortBadDomainDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 3),
    _Alu1588PtpPortBadDomainDisc_Type()
)
alu1588PtpPortBadDomainDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortBadDomainDisc.setStatus("obsolete")
_Alu1588PtpPortAlternateMasterDisc_Type = Counter64
_Alu1588PtpPortAlternateMasterDisc_Object = MibTableColumn
alu1588PtpPortAlternateMasterDisc = _Alu1588PtpPortAlternateMasterDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 4),
    _Alu1588PtpPortAlternateMasterDisc_Type()
)
alu1588PtpPortAlternateMasterDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortAlternateMasterDisc.setStatus("obsolete")
_Alu1588PtpPortStepRemovedGreaterThan255Disc_Type = Counter64
_Alu1588PtpPortStepRemovedGreaterThan255Disc_Object = MibTableColumn
alu1588PtpPortStepRemovedGreaterThan255Disc = _Alu1588PtpPortStepRemovedGreaterThan255Disc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 5),
    _Alu1588PtpPortStepRemovedGreaterThan255Disc_Type()
)
alu1588PtpPortStepRemovedGreaterThan255Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortStepRemovedGreaterThan255Disc.setStatus("obsolete")
_Alu1588PtpPortAnnounceMsgTx_Type = Counter64
_Alu1588PtpPortAnnounceMsgTx_Object = MibTableColumn
alu1588PtpPortAnnounceMsgTx = _Alu1588PtpPortAnnounceMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 6),
    _Alu1588PtpPortAnnounceMsgTx_Type()
)
alu1588PtpPortAnnounceMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortAnnounceMsgTx.setStatus("obsolete")
_Alu1588PtpPortAnnounceMsgRx_Type = Counter64
_Alu1588PtpPortAnnounceMsgRx_Object = MibTableColumn
alu1588PtpPortAnnounceMsgRx = _Alu1588PtpPortAnnounceMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 7),
    _Alu1588PtpPortAnnounceMsgRx_Type()
)
alu1588PtpPortAnnounceMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortAnnounceMsgRx.setStatus("obsolete")
_Alu1588PtpPortSyncMsgTx_Type = Counter64
_Alu1588PtpPortSyncMsgTx_Object = MibTableColumn
alu1588PtpPortSyncMsgTx = _Alu1588PtpPortSyncMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 8),
    _Alu1588PtpPortSyncMsgTx_Type()
)
alu1588PtpPortSyncMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortSyncMsgTx.setStatus("obsolete")
_Alu1588PtpPortSyncMsgRx_Type = Counter64
_Alu1588PtpPortSyncMsgRx_Object = MibTableColumn
alu1588PtpPortSyncMsgRx = _Alu1588PtpPortSyncMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 9),
    _Alu1588PtpPortSyncMsgRx_Type()
)
alu1588PtpPortSyncMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortSyncMsgRx.setStatus("obsolete")
_Alu1588PtpPortSignalingMsgTx_Type = Counter64
_Alu1588PtpPortSignalingMsgTx_Object = MibTableColumn
alu1588PtpPortSignalingMsgTx = _Alu1588PtpPortSignalingMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 10),
    _Alu1588PtpPortSignalingMsgTx_Type()
)
alu1588PtpPortSignalingMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortSignalingMsgTx.setStatus("obsolete")
_Alu1588PtpPortSignalingMsgRx_Type = Counter64
_Alu1588PtpPortSignalingMsgRx_Object = MibTableColumn
alu1588PtpPortSignalingMsgRx = _Alu1588PtpPortSignalingMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 11),
    _Alu1588PtpPortSignalingMsgRx_Type()
)
alu1588PtpPortSignalingMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortSignalingMsgRx.setStatus("obsolete")
_Alu1588PtpPortTotalUdpGeneralMsgTx_Type = Counter64
_Alu1588PtpPortTotalUdpGeneralMsgTx_Object = MibTableColumn
alu1588PtpPortTotalUdpGeneralMsgTx = _Alu1588PtpPortTotalUdpGeneralMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 12),
    _Alu1588PtpPortTotalUdpGeneralMsgTx_Type()
)
alu1588PtpPortTotalUdpGeneralMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortTotalUdpGeneralMsgTx.setStatus("obsolete")
_Alu1588PtpPortTotalUdpGeneralMsgRx_Type = Counter64
_Alu1588PtpPortTotalUdpGeneralMsgRx_Object = MibTableColumn
alu1588PtpPortTotalUdpGeneralMsgRx = _Alu1588PtpPortTotalUdpGeneralMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 13),
    _Alu1588PtpPortTotalUdpGeneralMsgRx_Type()
)
alu1588PtpPortTotalUdpGeneralMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortTotalUdpGeneralMsgRx.setStatus("obsolete")
_Alu1588PtpPortTotalUdpEventMsgTx_Type = Counter64
_Alu1588PtpPortTotalUdpEventMsgTx_Object = MibTableColumn
alu1588PtpPortTotalUdpEventMsgTx = _Alu1588PtpPortTotalUdpEventMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 14),
    _Alu1588PtpPortTotalUdpEventMsgTx_Type()
)
alu1588PtpPortTotalUdpEventMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortTotalUdpEventMsgTx.setStatus("obsolete")
_Alu1588PtpPortTotalUdpEventMsgRx_Type = Counter64
_Alu1588PtpPortTotalUdpEventMsgRx_Object = MibTableColumn
alu1588PtpPortTotalUdpEventMsgRx = _Alu1588PtpPortTotalUdpEventMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 15),
    _Alu1588PtpPortTotalUdpEventMsgRx_Type()
)
alu1588PtpPortTotalUdpEventMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortTotalUdpEventMsgRx.setStatus("obsolete")
_Alu1588PtpPortUnicastReqAnnoTx_Type = Counter64
_Alu1588PtpPortUnicastReqAnnoTx_Object = MibTableColumn
alu1588PtpPortUnicastReqAnnoTx = _Alu1588PtpPortUnicastReqAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 16),
    _Alu1588PtpPortUnicastReqAnnoTx_Type()
)
alu1588PtpPortUnicastReqAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastReqAnnoTx.setStatus("obsolete")
_Alu1588PtpPortUnicastReqAnnoRx_Type = Counter64
_Alu1588PtpPortUnicastReqAnnoRx_Object = MibTableColumn
alu1588PtpPortUnicastReqAnnoRx = _Alu1588PtpPortUnicastReqAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 17),
    _Alu1588PtpPortUnicastReqAnnoRx_Type()
)
alu1588PtpPortUnicastReqAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastReqAnnoRx.setStatus("obsolete")
_Alu1588PtpPortUnicastGrantAnnoTx_Type = Counter64
_Alu1588PtpPortUnicastGrantAnnoTx_Object = MibTableColumn
alu1588PtpPortUnicastGrantAnnoTx = _Alu1588PtpPortUnicastGrantAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 18),
    _Alu1588PtpPortUnicastGrantAnnoTx_Type()
)
alu1588PtpPortUnicastGrantAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastGrantAnnoTx.setStatus("obsolete")
_Alu1588PtpPortUnicastGrantAnnoRx_Type = Counter64
_Alu1588PtpPortUnicastGrantAnnoRx_Object = MibTableColumn
alu1588PtpPortUnicastGrantAnnoRx = _Alu1588PtpPortUnicastGrantAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 19),
    _Alu1588PtpPortUnicastGrantAnnoRx_Type()
)
alu1588PtpPortUnicastGrantAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastGrantAnnoRx.setStatus("obsolete")
_Alu1588PtpPortUnicastReqSyncTx_Type = Counter64
_Alu1588PtpPortUnicastReqSyncTx_Object = MibTableColumn
alu1588PtpPortUnicastReqSyncTx = _Alu1588PtpPortUnicastReqSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 20),
    _Alu1588PtpPortUnicastReqSyncTx_Type()
)
alu1588PtpPortUnicastReqSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastReqSyncTx.setStatus("obsolete")
_Alu1588PtpPortUnicastReqSyncRx_Type = Counter64
_Alu1588PtpPortUnicastReqSyncRx_Object = MibTableColumn
alu1588PtpPortUnicastReqSyncRx = _Alu1588PtpPortUnicastReqSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 21),
    _Alu1588PtpPortUnicastReqSyncRx_Type()
)
alu1588PtpPortUnicastReqSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastReqSyncRx.setStatus("obsolete")
_Alu1588PtpPortUnicastGrantSyncTx_Type = Counter64
_Alu1588PtpPortUnicastGrantSyncTx_Object = MibTableColumn
alu1588PtpPortUnicastGrantSyncTx = _Alu1588PtpPortUnicastGrantSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 22),
    _Alu1588PtpPortUnicastGrantSyncTx_Type()
)
alu1588PtpPortUnicastGrantSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastGrantSyncTx.setStatus("obsolete")
_Alu1588PtpPortUnicastGrantSyncRx_Type = Counter64
_Alu1588PtpPortUnicastGrantSyncRx_Object = MibTableColumn
alu1588PtpPortUnicastGrantSyncRx = _Alu1588PtpPortUnicastGrantSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 23),
    _Alu1588PtpPortUnicastGrantSyncRx_Type()
)
alu1588PtpPortUnicastGrantSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastGrantSyncRx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelAnnoTx_Type = Counter64
_Alu1588PtpPortUnicastCancelAnnoTx_Object = MibTableColumn
alu1588PtpPortUnicastCancelAnnoTx = _Alu1588PtpPortUnicastCancelAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 24),
    _Alu1588PtpPortUnicastCancelAnnoTx_Type()
)
alu1588PtpPortUnicastCancelAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelAnnoTx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelAnnoRx_Type = Counter64
_Alu1588PtpPortUnicastCancelAnnoRx_Object = MibTableColumn
alu1588PtpPortUnicastCancelAnnoRx = _Alu1588PtpPortUnicastCancelAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 25),
    _Alu1588PtpPortUnicastCancelAnnoRx_Type()
)
alu1588PtpPortUnicastCancelAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelAnnoRx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelSyncTx_Type = Counter64
_Alu1588PtpPortUnicastCancelSyncTx_Object = MibTableColumn
alu1588PtpPortUnicastCancelSyncTx = _Alu1588PtpPortUnicastCancelSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 26),
    _Alu1588PtpPortUnicastCancelSyncTx_Type()
)
alu1588PtpPortUnicastCancelSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelSyncTx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelSyncRx_Type = Counter64
_Alu1588PtpPortUnicastCancelSyncRx_Object = MibTableColumn
alu1588PtpPortUnicastCancelSyncRx = _Alu1588PtpPortUnicastCancelSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 27),
    _Alu1588PtpPortUnicastCancelSyncRx_Type()
)
alu1588PtpPortUnicastCancelSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelSyncRx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelAckAnnoTx_Type = Counter64
_Alu1588PtpPortUnicastCancelAckAnnoTx_Object = MibTableColumn
alu1588PtpPortUnicastCancelAckAnnoTx = _Alu1588PtpPortUnicastCancelAckAnnoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 28),
    _Alu1588PtpPortUnicastCancelAckAnnoTx_Type()
)
alu1588PtpPortUnicastCancelAckAnnoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelAckAnnoTx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelAckAnnoRx_Type = Counter64
_Alu1588PtpPortUnicastCancelAckAnnoRx_Object = MibTableColumn
alu1588PtpPortUnicastCancelAckAnnoRx = _Alu1588PtpPortUnicastCancelAckAnnoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 29),
    _Alu1588PtpPortUnicastCancelAckAnnoRx_Type()
)
alu1588PtpPortUnicastCancelAckAnnoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelAckAnnoRx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelAckSyncTx_Type = Counter64
_Alu1588PtpPortUnicastCancelAckSyncTx_Object = MibTableColumn
alu1588PtpPortUnicastCancelAckSyncTx = _Alu1588PtpPortUnicastCancelAckSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 30),
    _Alu1588PtpPortUnicastCancelAckSyncTx_Type()
)
alu1588PtpPortUnicastCancelAckSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelAckSyncTx.setStatus("obsolete")
_Alu1588PtpPortUnicastCancelAckSyncRx_Type = Counter64
_Alu1588PtpPortUnicastCancelAckSyncRx_Object = MibTableColumn
alu1588PtpPortUnicastCancelAckSyncRx = _Alu1588PtpPortUnicastCancelAckSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 31),
    _Alu1588PtpPortUnicastCancelAckSyncRx_Type()
)
alu1588PtpPortUnicastCancelAckSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastCancelAckSyncRx.setStatus("obsolete")
_Alu1588PtpPortUnicastNegRejectsAnno_Type = Counter64
_Alu1588PtpPortUnicastNegRejectsAnno_Object = MibTableColumn
alu1588PtpPortUnicastNegRejectsAnno = _Alu1588PtpPortUnicastNegRejectsAnno_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 32),
    _Alu1588PtpPortUnicastNegRejectsAnno_Type()
)
alu1588PtpPortUnicastNegRejectsAnno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastNegRejectsAnno.setStatus("obsolete")
_Alu1588PtpPortUnicastNegRejectsSync_Type = Counter64
_Alu1588PtpPortUnicastNegRejectsSync_Object = MibTableColumn
alu1588PtpPortUnicastNegRejectsSync = _Alu1588PtpPortUnicastNegRejectsSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 33),
    _Alu1588PtpPortUnicastNegRejectsSync_Type()
)
alu1588PtpPortUnicastNegRejectsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastNegRejectsSync.setStatus("obsolete")
_Alu1588PtpPortOutOfOrderSyncPktRx_Type = Counter64
_Alu1588PtpPortOutOfOrderSyncPktRx_Object = MibTableColumn
alu1588PtpPortOutOfOrderSyncPktRx = _Alu1588PtpPortOutOfOrderSyncPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 34),
    _Alu1588PtpPortOutOfOrderSyncPktRx_Type()
)
alu1588PtpPortOutOfOrderSyncPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortOutOfOrderSyncPktRx.setStatus("obsolete")
_Alu1588PtpPortDuplicateMsgDisc_Type = Counter64
_Alu1588PtpPortDuplicateMsgDisc_Object = MibTableColumn
alu1588PtpPortDuplicateMsgDisc = _Alu1588PtpPortDuplicateMsgDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 35),
    _Alu1588PtpPortDuplicateMsgDisc_Type()
)
alu1588PtpPortDuplicateMsgDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortDuplicateMsgDisc.setStatus("obsolete")
_Alu1588PtpPortPacketStatsLastUpdateTime_Type = TimeStamp
_Alu1588PtpPortPacketStatsLastUpdateTime_Object = MibTableColumn
alu1588PtpPortPacketStatsLastUpdateTime = _Alu1588PtpPortPacketStatsLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 36),
    _Alu1588PtpPortPacketStatsLastUpdateTime_Type()
)
alu1588PtpPortPacketStatsLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortPacketStatsLastUpdateTime.setStatus("obsolete")
_Alu1588PtpPortUnicastReqAnnoTxTimeout_Type = Counter64
_Alu1588PtpPortUnicastReqAnnoTxTimeout_Object = MibTableColumn
alu1588PtpPortUnicastReqAnnoTxTimeout = _Alu1588PtpPortUnicastReqAnnoTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 37),
    _Alu1588PtpPortUnicastReqAnnoTxTimeout_Type()
)
alu1588PtpPortUnicastReqAnnoTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastReqAnnoTxTimeout.setStatus("obsolete")
_Alu1588PtpPortUnicastReqSyncTxTimeout_Type = Counter64
_Alu1588PtpPortUnicastReqSyncTxTimeout_Object = MibTableColumn
alu1588PtpPortUnicastReqSyncTxTimeout = _Alu1588PtpPortUnicastReqSyncTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 38),
    _Alu1588PtpPortUnicastReqSyncTxTimeout_Type()
)
alu1588PtpPortUnicastReqSyncTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastReqSyncTxTimeout.setStatus("obsolete")
_Alu1588PtpPortUnicastGrantAnnoRejected_Type = Counter64
_Alu1588PtpPortUnicastGrantAnnoRejected_Object = MibTableColumn
alu1588PtpPortUnicastGrantAnnoRejected = _Alu1588PtpPortUnicastGrantAnnoRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 39),
    _Alu1588PtpPortUnicastGrantAnnoRejected_Type()
)
alu1588PtpPortUnicastGrantAnnoRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastGrantAnnoRejected.setStatus("obsolete")
_Alu1588PtpPortUnicastGrantSyncRejected_Type = Counter64
_Alu1588PtpPortUnicastGrantSyncRejected_Object = MibTableColumn
alu1588PtpPortUnicastGrantSyncRejected = _Alu1588PtpPortUnicastGrantSyncRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 3, 1, 40),
    _Alu1588PtpPortUnicastGrantSyncRejected_Type()
)
alu1588PtpPortUnicastGrantSyncRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortUnicastGrantSyncRejected.setStatus("obsolete")
_Alu1588PtpPortRecClkStatsTable_Object = MibTable
alu1588PtpPortRecClkStatsTable = _Alu1588PtpPortRecClkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4)
)
if mibBuilder.loadTexts:
    alu1588PtpPortRecClkStatsTable.setStatus("obsolete")
_Alu1588PtpPortRecClkStatsEntry_Object = MibTableRow
alu1588PtpPortRecClkStatsEntry = _Alu1588PtpPortRecClkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1)
)
alu1588PtpPortRecClkStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSReference"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortMasterIndex"),
)
if mibBuilder.loadTexts:
    alu1588PtpPortRecClkStatsEntry.setStatus("obsolete")
_Alu1588PtpPortLastUpdateTime_Type = TimeStamp
_Alu1588PtpPortLastUpdateTime_Object = MibTableColumn
alu1588PtpPortLastUpdateTime = _Alu1588PtpPortLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 1),
    _Alu1588PtpPortLastUpdateTime_Type()
)
alu1588PtpPortLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortLastUpdateTime.setStatus("obsolete")
_Alu1588PtpPortTotalMinutesIn24Hour_Type = Unsigned32
_Alu1588PtpPortTotalMinutesIn24Hour_Object = MibTableColumn
alu1588PtpPortTotalMinutesIn24Hour = _Alu1588PtpPortTotalMinutesIn24Hour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 2),
    _Alu1588PtpPortTotalMinutesIn24Hour_Type()
)
alu1588PtpPortTotalMinutesIn24Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortTotalMinutesIn24Hour.setStatus("obsolete")
_Alu1588PtpPortCurrent24HourFreqOffsetMeanPpb_Type = Integer32
_Alu1588PtpPortCurrent24HourFreqOffsetMeanPpb_Object = MibTableColumn
alu1588PtpPortCurrent24HourFreqOffsetMeanPpb = _Alu1588PtpPortCurrent24HourFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 3),
    _Alu1588PtpPortCurrent24HourFreqOffsetMeanPpb_Type()
)
alu1588PtpPortCurrent24HourFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent24HourFreqOffsetMeanPpb.setStatus("obsolete")
_Alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb_Type = Unsigned32
_Alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb_Object = MibTableColumn
alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb = _Alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 4),
    _Alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb_Type()
)
alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb.setStatus("obsolete")
_Alu1588PtpPortMaxShortIntervalMinutes_Type = Unsigned32
_Alu1588PtpPortMaxShortIntervalMinutes_Object = MibTableColumn
alu1588PtpPortMaxShortIntervalMinutes = _Alu1588PtpPortMaxShortIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 5),
    _Alu1588PtpPortMaxShortIntervalMinutes_Type()
)
alu1588PtpPortMaxShortIntervalMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortMaxShortIntervalMinutes.setStatus("obsolete")
_Alu1588PtpPortTotalShortIntervalMinutes_Type = Unsigned32
_Alu1588PtpPortTotalShortIntervalMinutes_Object = MibTableColumn
alu1588PtpPortTotalShortIntervalMinutes = _Alu1588PtpPortTotalShortIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 6),
    _Alu1588PtpPortTotalShortIntervalMinutes_Type()
)
alu1588PtpPortTotalShortIntervalMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortTotalShortIntervalMinutes.setStatus("obsolete")
_Alu1588PtpPortCurrent1MinValidData_Type = TruthValue
_Alu1588PtpPortCurrent1MinValidData_Object = MibTableColumn
alu1588PtpPortCurrent1MinValidData = _Alu1588PtpPortCurrent1MinValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 7),
    _Alu1588PtpPortCurrent1MinValidData_Type()
)
alu1588PtpPortCurrent1MinValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent1MinValidData.setStatus("obsolete")
_Alu1588PtpPortCurrent1MinPhaseErrorMeanPpb_Type = Integer32
_Alu1588PtpPortCurrent1MinPhaseErrorMeanPpb_Object = MibTableColumn
alu1588PtpPortCurrent1MinPhaseErrorMeanPpb = _Alu1588PtpPortCurrent1MinPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 8),
    _Alu1588PtpPortCurrent1MinPhaseErrorMeanPpb_Type()
)
alu1588PtpPortCurrent1MinPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent1MinPhaseErrorMeanPpb.setStatus("obsolete")
_Alu1588PtpPortCurrent1MinPhaseErrorStdDevNs_Type = Unsigned32
_Alu1588PtpPortCurrent1MinPhaseErrorStdDevNs_Object = MibTableColumn
alu1588PtpPortCurrent1MinPhaseErrorStdDevNs = _Alu1588PtpPortCurrent1MinPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 9),
    _Alu1588PtpPortCurrent1MinPhaseErrorStdDevNs_Type()
)
alu1588PtpPortCurrent1MinPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent1MinPhaseErrorStdDevNs.setStatus("obsolete")
_Alu1588PtpPortCurrent1MinPhaseErrorMeanNs_Type = Integer32
_Alu1588PtpPortCurrent1MinPhaseErrorMeanNs_Object = MibTableColumn
alu1588PtpPortCurrent1MinPhaseErrorMeanNs = _Alu1588PtpPortCurrent1MinPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 10),
    _Alu1588PtpPortCurrent1MinPhaseErrorMeanNs_Type()
)
alu1588PtpPortCurrent1MinPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent1MinPhaseErrorMeanNs.setStatus("obsolete")
_Alu1588PtpPortCurrent1MinFreqOffsetMeanPpb_Type = Integer32
_Alu1588PtpPortCurrent1MinFreqOffsetMeanPpb_Object = MibTableColumn
alu1588PtpPortCurrent1MinFreqOffsetMeanPpb = _Alu1588PtpPortCurrent1MinFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 11),
    _Alu1588PtpPortCurrent1MinFreqOffsetMeanPpb_Type()
)
alu1588PtpPortCurrent1MinFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent1MinFreqOffsetMeanPpb.setStatus("obsolete")
_Alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb_Type = Unsigned32
_Alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb_Object = MibTableColumn
alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb = _Alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 4, 1, 12),
    _Alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb_Type()
)
alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb.setStatus("obsolete")
_Alu1588PtpPortRecClkStatsShortIntervalTable_Object = MibTable
alu1588PtpPortRecClkStatsShortIntervalTable = _Alu1588PtpPortRecClkStatsShortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5)
)
if mibBuilder.loadTexts:
    alu1588PtpPortRecClkStatsShortIntervalTable.setStatus("obsolete")
_Alu1588PtpPortRecClkStatsShortIntervalEntry_Object = MibTableRow
alu1588PtpPortRecClkStatsShortIntervalEntry = _Alu1588PtpPortRecClkStatsShortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1)
)
alu1588PtpPortRecClkStatsShortIntervalEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSReference"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortMasterIndex"),
    (0, "ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalNumber"),
)
if mibBuilder.loadTexts:
    alu1588PtpPortRecClkStatsShortIntervalEntry.setStatus("obsolete")


class _Alu1588PtpPortIntervalNumber_Type(Integer32):
    """Custom type alu1588PtpPortIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Alu1588PtpPortIntervalNumber_Type.__name__ = "Integer32"
_Alu1588PtpPortIntervalNumber_Object = MibTableColumn
alu1588PtpPortIntervalNumber = _Alu1588PtpPortIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 1),
    _Alu1588PtpPortIntervalNumber_Type()
)
alu1588PtpPortIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalNumber.setStatus("obsolete")
_Alu1588PtpPortIntervalValidData_Type = TruthValue
_Alu1588PtpPortIntervalValidData_Object = MibTableColumn
alu1588PtpPortIntervalValidData = _Alu1588PtpPortIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 2),
    _Alu1588PtpPortIntervalValidData_Type()
)
alu1588PtpPortIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalValidData.setStatus("obsolete")
_Alu1588PtpPortIntervalUpdateTime_Type = TimeStamp
_Alu1588PtpPortIntervalUpdateTime_Object = MibTableColumn
alu1588PtpPortIntervalUpdateTime = _Alu1588PtpPortIntervalUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 3),
    _Alu1588PtpPortIntervalUpdateTime_Type()
)
alu1588PtpPortIntervalUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalUpdateTime.setStatus("obsolete")
_Alu1588PtpPortIntervalPhaseErrorMeanPpb_Type = Integer32
_Alu1588PtpPortIntervalPhaseErrorMeanPpb_Object = MibTableColumn
alu1588PtpPortIntervalPhaseErrorMeanPpb = _Alu1588PtpPortIntervalPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 4),
    _Alu1588PtpPortIntervalPhaseErrorMeanPpb_Type()
)
alu1588PtpPortIntervalPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalPhaseErrorMeanPpb.setStatus("obsolete")
_Alu1588PtpPortIntervalPhaseErrorStdDevNs_Type = Unsigned32
_Alu1588PtpPortIntervalPhaseErrorStdDevNs_Object = MibTableColumn
alu1588PtpPortIntervalPhaseErrorStdDevNs = _Alu1588PtpPortIntervalPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 5),
    _Alu1588PtpPortIntervalPhaseErrorStdDevNs_Type()
)
alu1588PtpPortIntervalPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalPhaseErrorStdDevNs.setStatus("obsolete")
_Alu1588PtpPortIntervalPhaseErrorMeanNs_Type = Integer32
_Alu1588PtpPortIntervalPhaseErrorMeanNs_Object = MibTableColumn
alu1588PtpPortIntervalPhaseErrorMeanNs = _Alu1588PtpPortIntervalPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 6),
    _Alu1588PtpPortIntervalPhaseErrorMeanNs_Type()
)
alu1588PtpPortIntervalPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalPhaseErrorMeanNs.setStatus("obsolete")
_Alu1588PtpPortIntervalFreqOffsetMeanPpb_Type = Integer32
_Alu1588PtpPortIntervalFreqOffsetMeanPpb_Object = MibTableColumn
alu1588PtpPortIntervalFreqOffsetMeanPpb = _Alu1588PtpPortIntervalFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 7),
    _Alu1588PtpPortIntervalFreqOffsetMeanPpb_Type()
)
alu1588PtpPortIntervalFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalFreqOffsetMeanPpb.setStatus("obsolete")
_Alu1588PtpPortIntervalFreqOffsetStdDevPpb_Type = Unsigned32
_Alu1588PtpPortIntervalFreqOffsetStdDevPpb_Object = MibTableColumn
alu1588PtpPortIntervalFreqOffsetStdDevPpb = _Alu1588PtpPortIntervalFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 2, 5, 1, 8),
    _Alu1588PtpPortIntervalFreqOffsetStdDevPpb_Type()
)
alu1588PtpPortIntervalFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alu1588PtpPortIntervalFreqOffsetStdDevPpb.setStatus("obsolete")
_Alu1588PtpNotificationObjects_ObjectIdentity = ObjectIdentity
alu1588PtpNotificationObjects = _Alu1588PtpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 9, 3)
)
_Alu1588PtpNotifyPrefix_ObjectIdentity = ObjectIdentity
alu1588PtpNotifyPrefix = _Alu1588PtpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 5)
)
_Alu1588PtpNotification_ObjectIdentity = ObjectIdentity
alu1588PtpNotification = _Alu1588PtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 5, 0)
)

# Managed Objects groups

alu1588PtpClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 1)
)
alu1588PtpClockGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockConfigAdmDomain"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockConfigAdmSlaveOnly"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSDomain"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSTwoStepFlag"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSNumberOfPorts"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSClass"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSAccuracy"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSOffsetScaledLogVariance"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSPriority1"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSPriority2"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSSlaveOnly"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockCurrentDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockCurrentDSStepsRemoved"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSPortNum"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSStats"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSOffsetScaledLogVariance"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterClockId"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterClass"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterAccuracy"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterPriority1"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterPriority2"))
)
if mibBuilder.loadTexts:
    alu1588PtpClockGroup.setStatus("obsolete")

alu1588PtpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 2)
)
alu1588PtpPortGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmClockIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMulticast"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster1IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster1IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster2IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster2IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmAnnoRxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmLogAnnoInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmLogSyncInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmAdminStatus"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmVrtrIfIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmUnicastNegotiate"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSClockIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSClockId"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortNum"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSDomain"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMulticast"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster1IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster1IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster2IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster2IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSAnnoRxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSLogAnnoInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSLogSyncInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSAdminStatus"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSVrtrIfIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortState"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSDelayMechanism"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSVersionNumber"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSUnicastNegotiate"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSRecoveredClockState"))
)
if mibBuilder.loadTexts:
    alu1588PtpPortGroup.setStatus("obsolete")

alu1588PtpPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 3)
)
alu1588PtpPortStatsGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortBadVersionDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortBadDomainDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortAlternateMasterDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDuplicateMsgDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortStepRemovedGreaterThan255Disc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortAnnounceMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortAnnounceMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSyncMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSyncMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSignalingMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSignalingMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpGeneralMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpGeneralMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpEventMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpEventMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastNegRejectsAnno"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastNegRejectsSync"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortOutOfOrderSyncPktRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortPacketStatsLastUpdateTime"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortLastUpdateTime"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalMinutesIn24Hour"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent24HourFreqOffsetMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortMaxShortIntervalMinutes"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalShortIntervalMinutes"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinValidData"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinPhaseErrorMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinPhaseErrorStdDevNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinPhaseErrorMeanNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinFreqOffsetMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalNumber"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalValidData"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalUpdateTime"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalPhaseErrorMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalPhaseErrorStdDevNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalPhaseErrorMeanNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalFreqOffsetMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalFreqOffsetStdDevPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqAnnoTxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqSyncTxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantAnnoRejected"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantSyncRejected"))
)
if mibBuilder.loadTexts:
    alu1588PtpPortStatsGroup.setStatus("obsolete")

alu1588PtpClockObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 5)
)
alu1588PtpClockObsoleteGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockConfigAdmDomain"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockConfigAdmSlaveOnly"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSDomain"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSTwoStepFlag"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSNumberOfPorts"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSClass"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSAccuracy"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSOffsetScaledLogVariance"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSPriority1"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSPriority2"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDefaultDSSlaveOnly"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockCurrentDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockCurrentDSStepsRemoved"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSPortNum"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSStats"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSOffsetScaledLogVariance"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterClockId"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterClass"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterAccuracy"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterPriority1"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSGrandmasterPriority2"))
)
if mibBuilder.loadTexts:
    alu1588PtpClockObsoleteGroup.setStatus("current")

alu1588PtpPortObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 6)
)
alu1588PtpPortObsoleteGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmClockIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMulticast"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster1IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster1IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster2IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmMaster2IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmAnnoRxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmLogAnnoInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmLogSyncInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmAdminStatus"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmVrtrIfIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortConfigAdmUnicastNegotiate"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSClockIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSClockId"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortNum"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSDomain"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMulticast"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster1IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster1IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster2IpAddrType"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSMaster2IpAddr"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSAnnoRxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSLogAnnoInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSLogSyncInterval"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSAdminStatus"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSVrtrIfIndex"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortState"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSDelayMechanism"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSVersionNumber"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSUnicastNegotiate"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSRecoveredClockState"))
)
if mibBuilder.loadTexts:
    alu1588PtpPortObsoleteGroup.setStatus("current")

alu1588PtpPortStatsObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 7)
)
alu1588PtpPortStatsObsoleteGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortBadVersionDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortBadDomainDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortAlternateMasterDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDuplicateMsgDisc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortStepRemovedGreaterThan255Disc"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortAnnounceMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortAnnounceMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSyncMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSyncMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSignalingMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortSignalingMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpGeneralMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpGeneralMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpEventMsgTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalUdpEventMsgRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckAnnoTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckAnnoRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckSyncTx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastCancelAckSyncRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastNegRejectsAnno"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastNegRejectsSync"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortOutOfOrderSyncPktRx"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortPacketStatsLastUpdateTime"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortLastUpdateTime"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalMinutesIn24Hour"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent24HourFreqOffsetMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortMaxShortIntervalMinutes"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortTotalShortIntervalMinutes"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinValidData"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinPhaseErrorMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinPhaseErrorStdDevNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinPhaseErrorMeanNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinFreqOffsetMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalNumber"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalValidData"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalUpdateTime"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalPhaseErrorMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalPhaseErrorStdDevNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalPhaseErrorMeanNs"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalFreqOffsetMeanPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortIntervalFreqOffsetStdDevPpb"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqAnnoTxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastReqSyncTxTimeout"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantAnnoRejected"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortUnicastGrantSyncRejected"))
)
if mibBuilder.loadTexts:
    alu1588PtpPortStatsObsoleteGroup.setStatus("current")


# Notification objects

alu1588PtpPortDSStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 5, 0, 1)
)
alu1588PtpPortDSStateChange.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortState"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSClockId"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortNum"))
)
if mibBuilder.loadTexts:
    alu1588PtpPortDSStateChange.setStatus(
        "obsolete"
    )

alu1588PtpPortDSRecovClkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 5, 0, 2)
)
alu1588PtpPortDSRecovClkChange.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSRecoveredClockState"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSClockId"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSPortNum"))
)
if mibBuilder.loadTexts:
    alu1588PtpPortDSRecovClkChange.setStatus(
        "obsolete"
    )

alu1588PtpClockDSChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 5, 0, 3)
)
alu1588PtpClockDSChange.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSIdentifier"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockParentDSPortNum"))
)
if mibBuilder.loadTexts:
    alu1588PtpClockDSChange.setStatus(
        "obsolete"
    )


# Notifications groups

alu1588PtpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 4)
)
alu1588PtpNotificationGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSStateChange"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSRecovClkChange"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDSChange"))
)
if mibBuilder.loadTexts:
    alu1588PtpNotificationGroup.setStatus(
        "obsolete"
    )

alu1588PtpNotifObsoleteGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 2, 8)
)
alu1588PtpNotifObsoleteGroup.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSStateChange"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortDSRecovClkChange"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockDSChange"))
)
if mibBuilder.loadTexts:
    alu1588PtpNotifObsoleteGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alu1588PtpComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 9, 1, 1, 1, 1)
)
alu1588PtpComp7705V1v0.setObjects(
      *(("ALU-IEEE1588-PTP-MIB", "alu1588PtpClockGroup"),
        ("ALU-IEEE1588-PTP-MIB", "alu1588PtpPortGroup"))
)
if mibBuilder.loadTexts:
    alu1588PtpComp7705V1v0.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-IEEE1588-PTP-MIB",
    **{"Alu1588PtpClockId": Alu1588PtpClockId,
       "Alu1588PtpClockIndex": Alu1588PtpClockIndex,
       "Alu1588PtpPortRecoveredClockState": Alu1588PtpPortRecoveredClockState,
       "Alu1588PtpPortState": Alu1588PtpPortState,
       "alu1588PtpMIBModule": alu1588PtpMIBModule,
       "alu1588PtpMIBConformance": alu1588PtpMIBConformance,
       "alu1588PtpConformance": alu1588PtpConformance,
       "alu1588PtpCompliances": alu1588PtpCompliances,
       "alu1588PtpComp7705": alu1588PtpComp7705,
       "alu1588PtpComp7705V1v0": alu1588PtpComp7705V1v0,
       "alu1588PtpGroups": alu1588PtpGroups,
       "alu1588PtpClockGroup": alu1588PtpClockGroup,
       "alu1588PtpPortGroup": alu1588PtpPortGroup,
       "alu1588PtpPortStatsGroup": alu1588PtpPortStatsGroup,
       "alu1588PtpNotificationGroup": alu1588PtpNotificationGroup,
       "alu1588PtpClockObsoleteGroup": alu1588PtpClockObsoleteGroup,
       "alu1588PtpPortObsoleteGroup": alu1588PtpPortObsoleteGroup,
       "alu1588PtpPortStatsObsoleteGroup": alu1588PtpPortStatsObsoleteGroup,
       "alu1588PtpNotifObsoleteGroup": alu1588PtpNotifObsoleteGroup,
       "alu1588PtpObjs": alu1588PtpObjs,
       "alu1588PtpClock": alu1588PtpClock,
       "alu1588PtpClockConfigAdmTable": alu1588PtpClockConfigAdmTable,
       "alu1588PtpClockConfigAdmEntry": alu1588PtpClockConfigAdmEntry,
       "alu1588PtpClockConfigAdmClockIndex": alu1588PtpClockConfigAdmClockIndex,
       "alu1588PtpClockConfigAdmDomain": alu1588PtpClockConfigAdmDomain,
       "alu1588PtpClockConfigAdmSlaveOnly": alu1588PtpClockConfigAdmSlaveOnly,
       "alu1588PtpClockDefaultDSTable": alu1588PtpClockDefaultDSTable,
       "alu1588PtpClockDefaultDSEntry": alu1588PtpClockDefaultDSEntry,
       "alu1588PtpClockIndex": alu1588PtpClockIndex,
       "alu1588PtpClockDefaultDSIdentifier": alu1588PtpClockDefaultDSIdentifier,
       "alu1588PtpClockDefaultDSDomain": alu1588PtpClockDefaultDSDomain,
       "alu1588PtpClockDefaultDSTwoStepFlag": alu1588PtpClockDefaultDSTwoStepFlag,
       "alu1588PtpClockDefaultDSType": alu1588PtpClockDefaultDSType,
       "alu1588PtpClockDefaultDSNumberOfPorts": alu1588PtpClockDefaultDSNumberOfPorts,
       "alu1588PtpClockDefaultDSClass": alu1588PtpClockDefaultDSClass,
       "alu1588PtpClockDefaultDSAccuracy": alu1588PtpClockDefaultDSAccuracy,
       "alu1588PtpClockDefaultDSOffsetScaledLogVariance": alu1588PtpClockDefaultDSOffsetScaledLogVariance,
       "alu1588PtpClockDefaultDSPriority1": alu1588PtpClockDefaultDSPriority1,
       "alu1588PtpClockDefaultDSPriority2": alu1588PtpClockDefaultDSPriority2,
       "alu1588PtpClockDefaultDSSlaveOnly": alu1588PtpClockDefaultDSSlaveOnly,
       "alu1588PtpClockCurrentDSTable": alu1588PtpClockCurrentDSTable,
       "alu1588PtpClockCurrentDSEntry": alu1588PtpClockCurrentDSEntry,
       "alu1588PtpClockCurrentDSIdentifier": alu1588PtpClockCurrentDSIdentifier,
       "alu1588PtpClockCurrentDSStepsRemoved": alu1588PtpClockCurrentDSStepsRemoved,
       "alu1588PtpClockParentDSTable": alu1588PtpClockParentDSTable,
       "alu1588PtpClockParentDSEntry": alu1588PtpClockParentDSEntry,
       "alu1588PtpClockParentDSIdentifier": alu1588PtpClockParentDSIdentifier,
       "alu1588PtpClockParentDSPortNum": alu1588PtpClockParentDSPortNum,
       "alu1588PtpClockParentDSStats": alu1588PtpClockParentDSStats,
       "alu1588PtpClockParentDSOffsetScaledLogVariance": alu1588PtpClockParentDSOffsetScaledLogVariance,
       "alu1588PtpClockParentDSGrandmasterClockId": alu1588PtpClockParentDSGrandmasterClockId,
       "alu1588PtpClockParentDSGrandmasterClass": alu1588PtpClockParentDSGrandmasterClass,
       "alu1588PtpClockParentDSGrandmasterAccuracy": alu1588PtpClockParentDSGrandmasterAccuracy,
       "alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance": alu1588PtpClockParentDSGrandmasterOffsetScaledLogVariance,
       "alu1588PtpClockParentDSGrandmasterPriority1": alu1588PtpClockParentDSGrandmasterPriority1,
       "alu1588PtpClockParentDSGrandmasterPriority2": alu1588PtpClockParentDSGrandmasterPriority2,
       "alu1588PtpPort": alu1588PtpPort,
       "alu1588PtpPortConfigAdmTable": alu1588PtpPortConfigAdmTable,
       "alu1588PtpPortConfigAdmEntry": alu1588PtpPortConfigAdmEntry,
       "alu1588PtpPortConfigAdmReference": alu1588PtpPortConfigAdmReference,
       "alu1588PtpPortConfigAdmClockIndex": alu1588PtpPortConfigAdmClockIndex,
       "alu1588PtpPortConfigAdmMulticast": alu1588PtpPortConfigAdmMulticast,
       "alu1588PtpPortConfigAdmMaster1IpAddrType": alu1588PtpPortConfigAdmMaster1IpAddrType,
       "alu1588PtpPortConfigAdmMaster1IpAddr": alu1588PtpPortConfigAdmMaster1IpAddr,
       "alu1588PtpPortConfigAdmMaster2IpAddrType": alu1588PtpPortConfigAdmMaster2IpAddrType,
       "alu1588PtpPortConfigAdmMaster2IpAddr": alu1588PtpPortConfigAdmMaster2IpAddr,
       "alu1588PtpPortConfigAdmAnnoRxTimeout": alu1588PtpPortConfigAdmAnnoRxTimeout,
       "alu1588PtpPortConfigAdmLogAnnoInterval": alu1588PtpPortConfigAdmLogAnnoInterval,
       "alu1588PtpPortConfigAdmLogSyncInterval": alu1588PtpPortConfigAdmLogSyncInterval,
       "alu1588PtpPortConfigAdmAdminStatus": alu1588PtpPortConfigAdmAdminStatus,
       "alu1588PtpPortConfigAdmVrtrIfIndex": alu1588PtpPortConfigAdmVrtrIfIndex,
       "alu1588PtpPortConfigAdmUnicastNegotiate": alu1588PtpPortConfigAdmUnicastNegotiate,
       "alu1588PtpPortDSTable": alu1588PtpPortDSTable,
       "alu1588PtpPortDSEntry": alu1588PtpPortDSEntry,
       "alu1588PtpPortDSReference": alu1588PtpPortDSReference,
       "alu1588PtpPortDSClockIndex": alu1588PtpPortDSClockIndex,
       "alu1588PtpPortDSClockId": alu1588PtpPortDSClockId,
       "alu1588PtpPortDSPortNum": alu1588PtpPortDSPortNum,
       "alu1588PtpPortDSDomain": alu1588PtpPortDSDomain,
       "alu1588PtpPortDSMulticast": alu1588PtpPortDSMulticast,
       "alu1588PtpPortDSMaster1IpAddrType": alu1588PtpPortDSMaster1IpAddrType,
       "alu1588PtpPortDSMaster1IpAddr": alu1588PtpPortDSMaster1IpAddr,
       "alu1588PtpPortDSMaster2IpAddrType": alu1588PtpPortDSMaster2IpAddrType,
       "alu1588PtpPortDSMaster2IpAddr": alu1588PtpPortDSMaster2IpAddr,
       "alu1588PtpPortDSAnnoRxTimeout": alu1588PtpPortDSAnnoRxTimeout,
       "alu1588PtpPortDSLogAnnoInterval": alu1588PtpPortDSLogAnnoInterval,
       "alu1588PtpPortDSLogSyncInterval": alu1588PtpPortDSLogSyncInterval,
       "alu1588PtpPortDSAdminStatus": alu1588PtpPortDSAdminStatus,
       "alu1588PtpPortDSVrtrIfIndex": alu1588PtpPortDSVrtrIfIndex,
       "alu1588PtpPortDSPortState": alu1588PtpPortDSPortState,
       "alu1588PtpPortDSDelayMechanism": alu1588PtpPortDSDelayMechanism,
       "alu1588PtpPortDSVersionNumber": alu1588PtpPortDSVersionNumber,
       "alu1588PtpPortDSUnicastNegotiate": alu1588PtpPortDSUnicastNegotiate,
       "alu1588PtpPortDSRecoveredClockState": alu1588PtpPortDSRecoveredClockState,
       "alu1588PtpPortPacketStatsTable": alu1588PtpPortPacketStatsTable,
       "alu1588PtpPortPacketStatsEntry": alu1588PtpPortPacketStatsEntry,
       "alu1588PtpPortMasterIndex": alu1588PtpPortMasterIndex,
       "alu1588PtpPortBadVersionDisc": alu1588PtpPortBadVersionDisc,
       "alu1588PtpPortBadDomainDisc": alu1588PtpPortBadDomainDisc,
       "alu1588PtpPortAlternateMasterDisc": alu1588PtpPortAlternateMasterDisc,
       "alu1588PtpPortStepRemovedGreaterThan255Disc": alu1588PtpPortStepRemovedGreaterThan255Disc,
       "alu1588PtpPortAnnounceMsgTx": alu1588PtpPortAnnounceMsgTx,
       "alu1588PtpPortAnnounceMsgRx": alu1588PtpPortAnnounceMsgRx,
       "alu1588PtpPortSyncMsgTx": alu1588PtpPortSyncMsgTx,
       "alu1588PtpPortSyncMsgRx": alu1588PtpPortSyncMsgRx,
       "alu1588PtpPortSignalingMsgTx": alu1588PtpPortSignalingMsgTx,
       "alu1588PtpPortSignalingMsgRx": alu1588PtpPortSignalingMsgRx,
       "alu1588PtpPortTotalUdpGeneralMsgTx": alu1588PtpPortTotalUdpGeneralMsgTx,
       "alu1588PtpPortTotalUdpGeneralMsgRx": alu1588PtpPortTotalUdpGeneralMsgRx,
       "alu1588PtpPortTotalUdpEventMsgTx": alu1588PtpPortTotalUdpEventMsgTx,
       "alu1588PtpPortTotalUdpEventMsgRx": alu1588PtpPortTotalUdpEventMsgRx,
       "alu1588PtpPortUnicastReqAnnoTx": alu1588PtpPortUnicastReqAnnoTx,
       "alu1588PtpPortUnicastReqAnnoRx": alu1588PtpPortUnicastReqAnnoRx,
       "alu1588PtpPortUnicastGrantAnnoTx": alu1588PtpPortUnicastGrantAnnoTx,
       "alu1588PtpPortUnicastGrantAnnoRx": alu1588PtpPortUnicastGrantAnnoRx,
       "alu1588PtpPortUnicastReqSyncTx": alu1588PtpPortUnicastReqSyncTx,
       "alu1588PtpPortUnicastReqSyncRx": alu1588PtpPortUnicastReqSyncRx,
       "alu1588PtpPortUnicastGrantSyncTx": alu1588PtpPortUnicastGrantSyncTx,
       "alu1588PtpPortUnicastGrantSyncRx": alu1588PtpPortUnicastGrantSyncRx,
       "alu1588PtpPortUnicastCancelAnnoTx": alu1588PtpPortUnicastCancelAnnoTx,
       "alu1588PtpPortUnicastCancelAnnoRx": alu1588PtpPortUnicastCancelAnnoRx,
       "alu1588PtpPortUnicastCancelSyncTx": alu1588PtpPortUnicastCancelSyncTx,
       "alu1588PtpPortUnicastCancelSyncRx": alu1588PtpPortUnicastCancelSyncRx,
       "alu1588PtpPortUnicastCancelAckAnnoTx": alu1588PtpPortUnicastCancelAckAnnoTx,
       "alu1588PtpPortUnicastCancelAckAnnoRx": alu1588PtpPortUnicastCancelAckAnnoRx,
       "alu1588PtpPortUnicastCancelAckSyncTx": alu1588PtpPortUnicastCancelAckSyncTx,
       "alu1588PtpPortUnicastCancelAckSyncRx": alu1588PtpPortUnicastCancelAckSyncRx,
       "alu1588PtpPortUnicastNegRejectsAnno": alu1588PtpPortUnicastNegRejectsAnno,
       "alu1588PtpPortUnicastNegRejectsSync": alu1588PtpPortUnicastNegRejectsSync,
       "alu1588PtpPortOutOfOrderSyncPktRx": alu1588PtpPortOutOfOrderSyncPktRx,
       "alu1588PtpPortDuplicateMsgDisc": alu1588PtpPortDuplicateMsgDisc,
       "alu1588PtpPortPacketStatsLastUpdateTime": alu1588PtpPortPacketStatsLastUpdateTime,
       "alu1588PtpPortUnicastReqAnnoTxTimeout": alu1588PtpPortUnicastReqAnnoTxTimeout,
       "alu1588PtpPortUnicastReqSyncTxTimeout": alu1588PtpPortUnicastReqSyncTxTimeout,
       "alu1588PtpPortUnicastGrantAnnoRejected": alu1588PtpPortUnicastGrantAnnoRejected,
       "alu1588PtpPortUnicastGrantSyncRejected": alu1588PtpPortUnicastGrantSyncRejected,
       "alu1588PtpPortRecClkStatsTable": alu1588PtpPortRecClkStatsTable,
       "alu1588PtpPortRecClkStatsEntry": alu1588PtpPortRecClkStatsEntry,
       "alu1588PtpPortLastUpdateTime": alu1588PtpPortLastUpdateTime,
       "alu1588PtpPortTotalMinutesIn24Hour": alu1588PtpPortTotalMinutesIn24Hour,
       "alu1588PtpPortCurrent24HourFreqOffsetMeanPpb": alu1588PtpPortCurrent24HourFreqOffsetMeanPpb,
       "alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb": alu1588PtpPortCurrent24HourFreqOffsetStdDevPpb,
       "alu1588PtpPortMaxShortIntervalMinutes": alu1588PtpPortMaxShortIntervalMinutes,
       "alu1588PtpPortTotalShortIntervalMinutes": alu1588PtpPortTotalShortIntervalMinutes,
       "alu1588PtpPortCurrent1MinValidData": alu1588PtpPortCurrent1MinValidData,
       "alu1588PtpPortCurrent1MinPhaseErrorMeanPpb": alu1588PtpPortCurrent1MinPhaseErrorMeanPpb,
       "alu1588PtpPortCurrent1MinPhaseErrorStdDevNs": alu1588PtpPortCurrent1MinPhaseErrorStdDevNs,
       "alu1588PtpPortCurrent1MinPhaseErrorMeanNs": alu1588PtpPortCurrent1MinPhaseErrorMeanNs,
       "alu1588PtpPortCurrent1MinFreqOffsetMeanPpb": alu1588PtpPortCurrent1MinFreqOffsetMeanPpb,
       "alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb": alu1588PtpPortCurrent1MinFreqOffsetStdDevPpb,
       "alu1588PtpPortRecClkStatsShortIntervalTable": alu1588PtpPortRecClkStatsShortIntervalTable,
       "alu1588PtpPortRecClkStatsShortIntervalEntry": alu1588PtpPortRecClkStatsShortIntervalEntry,
       "alu1588PtpPortIntervalNumber": alu1588PtpPortIntervalNumber,
       "alu1588PtpPortIntervalValidData": alu1588PtpPortIntervalValidData,
       "alu1588PtpPortIntervalUpdateTime": alu1588PtpPortIntervalUpdateTime,
       "alu1588PtpPortIntervalPhaseErrorMeanPpb": alu1588PtpPortIntervalPhaseErrorMeanPpb,
       "alu1588PtpPortIntervalPhaseErrorStdDevNs": alu1588PtpPortIntervalPhaseErrorStdDevNs,
       "alu1588PtpPortIntervalPhaseErrorMeanNs": alu1588PtpPortIntervalPhaseErrorMeanNs,
       "alu1588PtpPortIntervalFreqOffsetMeanPpb": alu1588PtpPortIntervalFreqOffsetMeanPpb,
       "alu1588PtpPortIntervalFreqOffsetStdDevPpb": alu1588PtpPortIntervalFreqOffsetStdDevPpb,
       "alu1588PtpNotificationObjects": alu1588PtpNotificationObjects,
       "alu1588PtpNotifyPrefix": alu1588PtpNotifyPrefix,
       "alu1588PtpNotification": alu1588PtpNotification,
       "alu1588PtpPortDSStateChange": alu1588PtpPortDSStateChange,
       "alu1588PtpPortDSRecovClkChange": alu1588PtpPortDSRecovClkChange,
       "alu1588PtpClockDSChange": alu1588PtpClockDSChange}
)
