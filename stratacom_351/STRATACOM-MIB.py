# SNMP MIB module (STRATACOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/STRATACOM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_SnmpAgents_ObjectIdentity = ObjectIdentity
snmpAgents = _SnmpAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100)
)
_StrmSwitchMIB_ObjectIdentity = ObjectIdentity
strmSwitchMIB = _StrmSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4)
)
_SwitchInterfaces_ObjectIdentity = ObjectIdentity
switchInterfaces = _SwitchInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1)
)
_SwitchIfTable_Object = MibTable
switchIfTable = _SwitchIfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1)
)
if mibBuilder.loadTexts:
    switchIfTable.setStatus("mandatory")
_SwitchIfEntry_Object = MibTableRow
switchIfEntry = _SwitchIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1)
)
switchIfEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    switchIfEntry.setStatus("mandatory")
_SwitchIfIndex_Type = Integer32
_SwitchIfIndex_Object = MibTableColumn
switchIfIndex = _SwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 1),
    _SwitchIfIndex_Type()
)
switchIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfIndex.setStatus("mandatory")


class _SwitchIfSlot_Type(Integer32):
    """Custom type switchIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwitchIfSlot_Type.__name__ = "Integer32"
_SwitchIfSlot_Object = MibTableColumn
switchIfSlot = _SwitchIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 2),
    _SwitchIfSlot_Type()
)
switchIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfSlot.setStatus("mandatory")


class _SwitchIfPort_Type(Integer32):
    """Custom type switchIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwitchIfPort_Type.__name__ = "Integer32"
_SwitchIfPort_Object = MibTableColumn
switchIfPort = _SwitchIfPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 3),
    _SwitchIfPort_Type()
)
switchIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfPort.setStatus("mandatory")


class _SwitchIfSubPort_Type(Integer32):
    """Custom type switchIfSubPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SwitchIfSubPort_Type.__name__ = "Integer32"
_SwitchIfSubPort_Object = MibTableColumn
switchIfSubPort = _SwitchIfSubPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 4),
    _SwitchIfSubPort_Type()
)
switchIfSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfSubPort.setStatus("mandatory")


class _SwitchIfMediaType_Type(Integer32):
    """Custom type switchIfMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              18,
              22,
              30,
              39)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ds1", 18),
          ("serialPort", 22),
          ("ds3", 30),
          ("sonet", 39))
    )


_SwitchIfMediaType_Type.__name__ = "Integer32"
_SwitchIfMediaType_Object = MibTableColumn
switchIfMediaType = _SwitchIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 5),
    _SwitchIfMediaType_Type()
)
switchIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfMediaType.setStatus("mandatory")


class _SwitchIfService_Type(Integer32):
    """Custom type switchIfService based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("frameRelay", 2),
          ("atmAccessPort", 3),
          ("voiceData", 4),
          ("fpRoutingTrk", 5),
          ("atmRoutingTrk", 6),
          ("atmAxisIntfTrk", 7),
          ("atmIPXAFIntfTrk", 8),
          ("atmFdrIntfTrk", 9),
          ("atmAPSIntfTrk", 10),
          ("imaRoutingTrunk", 11),
          ("physicalMedia", 12),
          ("atmVsiIntfTrk", 13),
          ("atmParIntfTrk", 14))
    )


_SwitchIfService_Type.__name__ = "Integer32"
_SwitchIfService_Object = MibTableColumn
switchIfService = _SwitchIfService_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 6),
    _SwitchIfService_Type()
)
switchIfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfService.setStatus("mandatory")


class _SwitchIfAdmStatus_Type(Integer32):
    """Custom type switchIfAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("added", 6),
          ("deleted", 7))
    )


_SwitchIfAdmStatus_Type.__name__ = "Integer32"
_SwitchIfAdmStatus_Object = MibTableColumn
switchIfAdmStatus = _SwitchIfAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 7),
    _SwitchIfAdmStatus_Type()
)
switchIfAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfAdmStatus.setStatus("mandatory")


class _SwitchIfOperStatus_Type(Integer32):
    """Custom type switchIfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("added", 6))
    )


_SwitchIfOperStatus_Type.__name__ = "Integer32"
_SwitchIfOperStatus_Object = MibTableColumn
switchIfOperStatus = _SwitchIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 8),
    _SwitchIfOperStatus_Type()
)
switchIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOperStatus.setStatus("mandatory")
_SwitchIfPhysPort_Type = Integer32
_SwitchIfPhysPort_Object = MibTableColumn
switchIfPhysPort = _SwitchIfPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 9),
    _SwitchIfPhysPort_Type()
)
switchIfPhysPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfPhysPort.setStatus("mandatory")


class _SwitchIfPartiId_Type(Integer32):
    """Custom type switchIfPartiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SwitchIfPartiId_Type.__name__ = "Integer32"
_SwitchIfPartiId_Object = MibTableColumn
switchIfPartiId = _SwitchIfPartiId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 10),
    _SwitchIfPartiId_Type()
)
switchIfPartiId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfPartiId.setStatus("mandatory")


class _SwitchIfCtrlerId_Type(Integer32):
    """Custom type switchIfCtrlerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )


_SwitchIfCtrlerId_Type.__name__ = "Integer32"
_SwitchIfCtrlerId_Object = MibTableColumn
switchIfCtrlerId = _SwitchIfCtrlerId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 11),
    _SwitchIfCtrlerId_Type()
)
switchIfCtrlerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfCtrlerId.setStatus("mandatory")
_SwitchServiceObjects_ObjectIdentity = ObjectIdentity
switchServiceObjects = _SwitchServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2)
)
_FrServiceObjects_ObjectIdentity = ObjectIdentity
frServiceObjects = _FrServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1)
)
_FrLportCnfTable_Object = MibTable
frLportCnfTable = _FrLportCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    frLportCnfTable.setStatus("mandatory")
_FrLportCnfEntry_Object = MibTableRow
frLportCnfEntry = _FrLportCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1)
)
frLportCnfEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frLportSlotIndex"),
    (0, "STRATACOM-MIB", "frLportPortIndex"),
)
if mibBuilder.loadTexts:
    frLportCnfEntry.setStatus("mandatory")


class _FrLportSlotIndex_Type(Integer32):
    """Custom type frLportSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrLportSlotIndex_Type.__name__ = "Integer32"
_FrLportSlotIndex_Object = MibTableColumn
frLportSlotIndex = _FrLportSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 1),
    _FrLportSlotIndex_Type()
)
frLportSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSlotIndex.setStatus("mandatory")


class _FrLportPortIndex_Type(Integer32):
    """Custom type frLportPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrLportPortIndex_Type.__name__ = "Integer32"
_FrLportPortIndex_Object = MibTableColumn
frLportPortIndex = _FrLportPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 2),
    _FrLportPortIndex_Type()
)
frLportPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportPortIndex.setStatus("mandatory")
_FrLportPortDLCI_Type = Integer32
_FrLportPortDLCI_Object = MibTableColumn
frLportPortDLCI = _FrLportPortDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 3),
    _FrLportPortDLCI_Type()
)
frLportPortDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportPortDLCI.setStatus("mandatory")


class _FrLportAdminStatus_Type(Integer32):
    """Custom type frLportAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("modify", 3),
          ("writeOnly", 4),
          ("add", 5),
          ("delete", 6))
    )


_FrLportAdminStatus_Type.__name__ = "Integer32"
_FrLportAdminStatus_Object = MibTableColumn
frLportAdminStatus = _FrLportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 4),
    _FrLportAdminStatus_Type()
)
frLportAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportAdminStatus.setStatus("mandatory")


class _FrLportOperStatus_Type(Integer32):
    """Custom type frLportOperStatus based on Integer32"""
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
        *(("inActive", 1),
          ("active", 2),
          ("looped", 3),
          ("failed", 4),
          ("unknown", 5))
    )


_FrLportOperStatus_Type.__name__ = "Integer32"
_FrLportOperStatus_Object = MibTableColumn
frLportOperStatus = _FrLportOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 5),
    _FrLportOperStatus_Type()
)
frLportOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportOperStatus.setStatus("mandatory")
_FrLportPortSpeed_Type = Integer32
_FrLportPortSpeed_Object = MibTableColumn
frLportPortSpeed = _FrLportPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 6),
    _FrLportPortSpeed_Type()
)
frLportPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportPortSpeed.setStatus("mandatory")


class _FrLportClockType_Type(Integer32):
    """Custom type frLportClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("looped", 2),
          ("none", 3))
    )


_FrLportClockType_Type.__name__ = "Integer32"
_FrLportClockType_Object = MibTableColumn
frLportClockType = _FrLportClockType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 7),
    _FrLportClockType_Type()
)
frLportClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportClockType.setStatus("mandatory")


class _FrLportPortType_Type(Integer32):
    """Custom type frLportPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fr", 1),
          ("atm", 2))
    )


_FrLportPortType_Type.__name__ = "Integer32"
_FrLportPortType_Object = MibTableColumn
frLportPortType = _FrLportPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 8),
    _FrLportPortType_Type()
)
frLportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportPortType.setStatus("mandatory")


class _FrLportVcCount_Type(Integer32):
    """Custom type frLportVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
    )


_FrLportVcCount_Type.__name__ = "Integer32"
_FrLportVcCount_Object = MibTableColumn
frLportVcCount = _FrLportVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 9),
    _FrLportVcCount_Type()
)
frLportVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportVcCount.setStatus("mandatory")
_FrLportFirstVcPtr_Type = ObjectIdentifier
_FrLportFirstVcPtr_Object = MibTableColumn
frLportFirstVcPtr = _FrLportFirstVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 10),
    _FrLportFirstVcPtr_Type()
)
frLportFirstVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportFirstVcPtr.setStatus("mandatory")
_FrLportAggrChCnt_Type = Integer32
_FrLportAggrChCnt_Object = MibTableColumn
frLportAggrChCnt = _FrLportAggrChCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 11),
    _FrLportAggrChCnt_Type()
)
frLportAggrChCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportAggrChCnt.setStatus("mandatory")


class _FrLportChSpeed_Type(Integer32):
    """Custom type frLportChSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s56k", 1),
          ("s64k", 2),
          ("na", 3))
    )


_FrLportChSpeed_Type.__name__ = "Integer32"
_FrLportChSpeed_Object = MibTableColumn
frLportChSpeed = _FrLportChSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 12),
    _FrLportChSpeed_Type()
)
frLportChSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportChSpeed.setStatus("mandatory")


class _FrLportMaxTxQDepth_Type(Integer32):
    """Custom type frLportMaxTxQDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrLportMaxTxQDepth_Type.__name__ = "Integer32"
_FrLportMaxTxQDepth_Object = MibTableColumn
frLportMaxTxQDepth = _FrLportMaxTxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 13),
    _FrLportMaxTxQDepth_Type()
)
frLportMaxTxQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportMaxTxQDepth.setStatus("mandatory")


class _FrLportECNQThresh_Type(Integer32):
    """Custom type frLportECNQThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrLportECNQThresh_Type.__name__ = "Integer32"
_FrLportECNQThresh_Object = MibTableColumn
frLportECNQThresh = _FrLportECNQThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 14),
    _FrLportECNQThresh_Type()
)
frLportECNQThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportECNQThresh.setStatus("mandatory")


class _FrLportDEThresh_Type(Integer32):
    """Custom type frLportDEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrLportDEThresh_Type.__name__ = "Integer32"
_FrLportDEThresh_Object = MibTableColumn
frLportDEThresh = _FrLportDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 15),
    _FrLportDEThresh_Type()
)
frLportDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportDEThresh.setStatus("mandatory")


class _FrLportIDEMap_Type(Integer32):
    """Custom type frLportIDEMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportIDEMap_Type.__name__ = "Integer32"
_FrLportIDEMap_Object = MibTableColumn
frLportIDEMap = _FrLportIDEMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 16),
    _FrLportIDEMap_Type()
)
frLportIDEMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportIDEMap.setStatus("mandatory")


class _FrLportSigProt_Type(Integer32):
    """Custom type frLportSigProt based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("xdisabled", 1),
          ("lmi-asyn", 2),
          ("disabled", 3),
          ("lmi-noasyn", 4),
          ("uni-annexA", 5),
          ("uni-annexD", 6),
          ("nni-annexA", 7),
          ("nni-annexD", 8),
          ("auto-det", 9))
    )


_FrLportSigProt_Type.__name__ = "Integer32"
_FrLportSigProt_Object = MibTableColumn
frLportSigProt = _FrLportSigProt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 17),
    _FrLportSigProt_Type()
)
frLportSigProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportSigProt.setStatus("mandatory")


class _FrLportNNIStatus_Type(Integer32):
    """Custom type frLportNNIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportNNIStatus_Type.__name__ = "Integer32"
_FrLportNNIStatus_Object = MibTableColumn
frLportNNIStatus = _FrLportNNIStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 18),
    _FrLportNNIStatus_Type()
)
frLportNNIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportNNIStatus.setStatus("mandatory")


class _FrLportAsynStatus_Type(Integer32):
    """Custom type frLportAsynStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportAsynStatus_Type.__name__ = "Integer32"
_FrLportAsynStatus_Object = MibTableColumn
frLportAsynStatus = _FrLportAsynStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 19),
    _FrLportAsynStatus_Type()
)
frLportAsynStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportAsynStatus.setStatus("mandatory")


class _FrLportPolVerTmr_Type(Integer32):
    """Custom type frLportPolVerTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrLportPolVerTmr_Type.__name__ = "Integer32"
_FrLportPolVerTmr_Object = MibTableColumn
frLportPolVerTmr = _FrLportPolVerTmr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 20),
    _FrLportPolVerTmr_Type()
)
frLportPolVerTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportPolVerTmr.setStatus("mandatory")


class _FrLportErrThresh_Type(Integer32):
    """Custom type frLportErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLportErrThresh_Type.__name__ = "Integer32"
_FrLportErrThresh_Object = MibTableColumn
frLportErrThresh = _FrLportErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 21),
    _FrLportErrThresh_Type()
)
frLportErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportErrThresh.setStatus("mandatory")


class _FrLportMonEveCnt_Type(Integer32):
    """Custom type frLportMonEveCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLportMonEveCnt_Type.__name__ = "Integer32"
_FrLportMonEveCnt_Object = MibTableColumn
frLportMonEveCnt = _FrLportMonEveCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 22),
    _FrLportMonEveCnt_Type()
)
frLportMonEveCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportMonEveCnt.setStatus("mandatory")


class _FrLportCommPri_Type(Integer32):
    """Custom type frLportCommPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportCommPri_Type.__name__ = "Integer32"
_FrLportCommPri_Object = MibTableColumn
frLportCommPri = _FrLportCommPri_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 23),
    _FrLportCommPri_Type()
)
frLportCommPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportCommPri.setStatus("mandatory")


class _FrLportUpRNR_Type(Integer32):
    """Custom type frLportUpRNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrLportUpRNR_Type.__name__ = "Integer32"
_FrLportUpRNR_Object = MibTableColumn
frLportUpRNR = _FrLportUpRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 24),
    _FrLportUpRNR_Type()
)
frLportUpRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportUpRNR.setStatus("mandatory")


class _FrLportLowRNR_Type(Integer32):
    """Custom type frLportLowRNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrLportLowRNR_Type.__name__ = "Integer32"
_FrLportLowRNR_Object = MibTableColumn
frLportLowRNR = _FrLportLowRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 25),
    _FrLportLowRNR_Type()
)
frLportLowRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportLowRNR.setStatus("mandatory")


class _FrLportMinFrmFlgs_Type(Integer32):
    """Custom type frLportMinFrmFlgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrLportMinFrmFlgs_Type.__name__ = "Integer32"
_FrLportMinFrmFlgs_Object = MibTableColumn
frLportMinFrmFlgs = _FrLportMinFrmFlgs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 26),
    _FrLportMinFrmFlgs_Type()
)
frLportMinFrmFlgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportMinFrmFlgs.setStatus("mandatory")


class _FrLportOamThresh_Type(Integer32):
    """Custom type frLportOamThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrLportOamThresh_Type.__name__ = "Integer32"
_FrLportOamThresh_Object = MibTableColumn
frLportOamThresh = _FrLportOamThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 27),
    _FrLportOamThresh_Type()
)
frLportOamThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportOamThresh.setStatus("mandatory")


class _FrLportLinkTimer_Type(Integer32):
    """Custom type frLportLinkTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrLportLinkTimer_Type.__name__ = "Integer32"
_FrLportLinkTimer_Object = MibTableColumn
frLportLinkTimer = _FrLportLinkTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 28),
    _FrLportLinkTimer_Type()
)
frLportLinkTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportLinkTimer.setStatus("mandatory")


class _FrLportPollCycle_Type(Integer32):
    """Custom type frLportPollCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrLportPollCycle_Type.__name__ = "Integer32"
_FrLportPollCycle_Object = MibTableColumn
frLportPollCycle = _FrLportPollCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 29),
    _FrLportPollCycle_Type()
)
frLportPollCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportPollCycle.setStatus("mandatory")
_FrLportCLLMTimer_Type = Integer32
_FrLportCLLMTimer_Object = MibTableColumn
frLportCLLMTimer = _FrLportCLLMTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 30),
    _FrLportCLLMTimer_Type()
)
frLportCLLMTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportCLLMTimer.setStatus("mandatory")


class _FrLportEFCItoBECN_Type(Integer32):
    """Custom type frLportEFCItoBECN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2),
          ("na", 3))
    )


_FrLportEFCItoBECN_Type.__name__ = "Integer32"
_FrLportEFCItoBECN_Object = MibTableColumn
frLportEFCItoBECN = _FrLportEFCItoBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 31),
    _FrLportEFCItoBECN_Type()
)
frLportEFCItoBECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportEFCItoBECN.setStatus("mandatory")


class _FrLportSrRTS_Type(Integer32):
    """Custom type frLportSrRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("na", 3))
    )


_FrLportSrRTS_Type.__name__ = "Integer32"
_FrLportSrRTS_Object = MibTableColumn
frLportSrRTS = _FrLportSrRTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 32),
    _FrLportSrRTS_Type()
)
frLportSrRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrRTS.setStatus("mandatory")


class _FrLportSrDTR_Type(Integer32):
    """Custom type frLportSrDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("na", 3))
    )


_FrLportSrDTR_Type.__name__ = "Integer32"
_FrLportSrDTR_Object = MibTableColumn
frLportSrDTR = _FrLportSrDTR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 33),
    _FrLportSrDTR_Type()
)
frLportSrDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrDTR.setStatus("mandatory")


class _FrLportSrDCD_Type(Integer32):
    """Custom type frLportSrDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("na", 3))
    )


_FrLportSrDCD_Type.__name__ = "Integer32"
_FrLportSrDCD_Object = MibTableColumn
frLportSrDCD = _FrLportSrDCD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 34),
    _FrLportSrDCD_Type()
)
frLportSrDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrDCD.setStatus("mandatory")


class _FrLportSrCTS_Type(Integer32):
    """Custom type frLportSrCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("na", 3))
    )


_FrLportSrCTS_Type.__name__ = "Integer32"
_FrLportSrCTS_Object = MibTableColumn
frLportSrCTS = _FrLportSrCTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 35),
    _FrLportSrCTS_Type()
)
frLportSrCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrCTS.setStatus("mandatory")


class _FrLportSrDSR_Type(Integer32):
    """Custom type frLportSrDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("na", 3))
    )


_FrLportSrDSR_Type.__name__ = "Integer32"
_FrLportSrDSR_Object = MibTableColumn
frLportSrDSR = _FrLportSrDSR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 36),
    _FrLportSrDSR_Type()
)
frLportSrDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrDSR.setStatus("mandatory")


class _FrLportLoopBack_Type(Integer32):
    """Custom type frLportLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("local", 2))
    )


_FrLportLoopBack_Type.__name__ = "Integer32"
_FrLportLoopBack_Object = MibTableColumn
frLportLoopBack = _FrLportLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 37),
    _FrLportLoopBack_Type()
)
frLportLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLoopBack.setStatus("mandatory")


class _FrLportExtConFail_Type(Integer32):
    """Custom type frLportExtConFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrLportExtConFail_Type.__name__ = "Integer32"
_FrLportExtConFail_Object = MibTableColumn
frLportExtConFail = _FrLportExtConFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 38),
    _FrLportExtConFail_Type()
)
frLportExtConFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportExtConFail.setStatus("mandatory")
_FrLportLine_Type = Integer32
_FrLportLine_Object = MibTableColumn
frLportLine = _FrLportLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 39),
    _FrLportLine_Type()
)
frLportLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportLine.setStatus("mandatory")
_FrLportStartCh_Type = Integer32
_FrLportStartCh_Object = MibTableColumn
frLportStartCh = _FrLportStartCh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 40),
    _FrLportStartCh_Type()
)
frLportStartCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportStartCh.setStatus("mandatory")


class _FrLportExtProt_Type(Integer32):
    """Custom type frLportExtProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrLportExtProt_Type.__name__ = "Integer32"
_FrLportExtProt_Object = MibTableColumn
frLportExtProt = _FrLportExtProt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 41),
    _FrLportExtProt_Type()
)
frLportExtProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportExtProt.setStatus("mandatory")


class _FrLportDte_Type(Integer32):
    """Custom type frLportDte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2),
          ("na", 3))
    )


_FrLportDte_Type.__name__ = "Integer32"
_FrLportDte_Object = MibTableColumn
frLportDte = _FrLportDte_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 42),
    _FrLportDte_Type()
)
frLportDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportDte.setStatus("mandatory")
_FrLportStatTable_Object = MibTable
frLportStatTable = _FrLportStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    frLportStatTable.setStatus("mandatory")
_FrLportStatEntry_Object = MibTableRow
frLportStatEntry = _FrLportStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1)
)
frLportStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frLportSlotIndex"),
    (0, "STRATACOM-MIB", "frLportPortIndex"),
)
if mibBuilder.loadTexts:
    frLportStatEntry.setStatus("mandatory")
_FrLportRxBytes_Type = Counter32
_FrLportRxBytes_Object = MibTableColumn
frLportRxBytes = _FrLportRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 1),
    _FrLportRxBytes_Type()
)
frLportRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportRxBytes.setStatus("mandatory")
_FrLportRxFrms_Type = Counter32
_FrLportRxFrms_Object = MibTableColumn
frLportRxFrms = _FrLportRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 2),
    _FrLportRxFrms_Type()
)
frLportRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportRxFrms.setStatus("mandatory")
_FrLportTxBytes_Type = Counter32
_FrLportTxBytes_Object = MibTableColumn
frLportTxBytes = _FrLportTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 3),
    _FrLportTxBytes_Type()
)
frLportTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxBytes.setStatus("mandatory")
_FrLportTxFrms_Type = Counter32
_FrLportTxFrms_Object = MibTableColumn
frLportTxFrms = _FrLportTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 4),
    _FrLportTxFrms_Type()
)
frLportTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxFrms.setStatus("mandatory")
_FrLportTxFrmsFecns_Type = Counter32
_FrLportTxFrmsFecns_Object = MibTableColumn
frLportTxFrmsFecns = _FrLportTxFrmsFecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 5),
    _FrLportTxFrmsFecns_Type()
)
frLportTxFrmsFecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxFrmsFecns.setStatus("mandatory")
_FrLportTxFrmsBecns_Type = Counter32
_FrLportTxFrmsBecns_Object = MibTableColumn
frLportTxFrmsBecns = _FrLportTxFrmsBecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 6),
    _FrLportTxFrmsBecns_Type()
)
frLportTxFrmsBecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxFrmsBecns.setStatus("mandatory")
_FrLportCrcErrors_Type = Counter32
_FrLportCrcErrors_Object = MibTableColumn
frLportCrcErrors = _FrLportCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 7),
    _FrLportCrcErrors_Type()
)
frLportCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCrcErrors.setStatus("mandatory")
_FrLportBadFmts_Type = Counter32
_FrLportBadFmts_Object = MibTableColumn
frLportBadFmts = _FrLportBadFmts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 8),
    _FrLportBadFmts_Type()
)
frLportBadFmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportBadFmts.setStatus("mandatory")
_FrLportAlgnErrors_Type = Counter32
_FrLportAlgnErrors_Object = MibTableColumn
frLportAlgnErrors = _FrLportAlgnErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 9),
    _FrLportAlgnErrors_Type()
)
frLportAlgnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportAlgnErrors.setStatus("mandatory")
_FrLportIllegLengths_Type = Counter32
_FrLportIllegLengths_Object = MibTableColumn
frLportIllegLengths = _FrLportIllegLengths_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 10),
    _FrLportIllegLengths_Type()
)
frLportIllegLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportIllegLengths.setStatus("mandatory")
_FrLportDmaOvruns_Type = Counter32
_FrLportDmaOvruns_Object = MibTableColumn
frLportDmaOvruns = _FrLportDmaOvruns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 11),
    _FrLportDmaOvruns_Type()
)
frLportDmaOvruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDmaOvruns.setStatus("mandatory")
_FrLportStatEnqUnis_Type = Counter32
_FrLportStatEnqUnis_Object = MibTableColumn
frLportStatEnqUnis = _FrLportStatEnqUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 12),
    _FrLportStatEnqUnis_Type()
)
frLportStatEnqUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatEnqUnis.setStatus("mandatory")
_FrLportStatTxUnis_Type = Counter32
_FrLportStatTxUnis_Object = MibTableColumn
frLportStatTxUnis = _FrLportStatTxUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 13),
    _FrLportStatTxUnis_Type()
)
frLportStatTxUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatTxUnis.setStatus("mandatory")
_FrLportUpdtTxUnis_Type = Counter32
_FrLportUpdtTxUnis_Object = MibTableColumn
frLportUpdtTxUnis = _FrLportUpdtTxUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 14),
    _FrLportUpdtTxUnis_Type()
)
frLportUpdtTxUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportUpdtTxUnis.setStatus("mandatory")
_FrLportInvldReqCnts_Type = Counter32
_FrLportInvldReqCnts_Object = MibTableColumn
frLportInvldReqCnts = _FrLportInvldReqCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 15),
    _FrLportInvldReqCnts_Type()
)
frLportInvldReqCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportInvldReqCnts.setStatus("mandatory")
_FrLportToutCntUnis_Type = Counter32
_FrLportToutCntUnis_Object = MibTableColumn
frLportToutCntUnis = _FrLportToutCntUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 16),
    _FrLportToutCntUnis_Type()
)
frLportToutCntUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportToutCntUnis.setStatus("mandatory")
_FrLportSeqnmErrUnis_Type = Counter32
_FrLportSeqnmErrUnis_Object = MibTableColumn
frLportSeqnmErrUnis = _FrLportSeqnmErrUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 17),
    _FrLportSeqnmErrUnis_Type()
)
frLportSeqnmErrUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSeqnmErrUnis.setStatus("mandatory")
_FrLportUnknDlcis_Type = Counter32
_FrLportUnknDlcis_Object = MibTableColumn
frLportUnknDlcis = _FrLportUnknDlcis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 18),
    _FrLportUnknDlcis_Type()
)
frLportUnknDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportUnknDlcis.setStatus("mandatory")
_FrLportDeFrmsDrops_Type = Counter32
_FrLportDeFrmsDrops_Object = MibTableColumn
frLportDeFrmsDrops = _FrLportDeFrmsDrops_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 19),
    _FrLportDeFrmsDrops_Type()
)
frLportDeFrmsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDeFrmsDrops.setStatus("mandatory")
_FrLportStatEnqNnis_Type = Counter32
_FrLportStatEnqNnis_Object = MibTableColumn
frLportStatEnqNnis = _FrLportStatEnqNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 20),
    _FrLportStatEnqNnis_Type()
)
frLportStatEnqNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatEnqNnis.setStatus("mandatory")
_FrLportStatRxNnis_Type = Counter32
_FrLportStatRxNnis_Object = MibTableColumn
frLportStatRxNnis = _FrLportStatRxNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 21),
    _FrLportStatRxNnis_Type()
)
frLportStatRxNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatRxNnis.setStatus("mandatory")
_FrLportUpdtRxNnis_Type = Counter32
_FrLportUpdtRxNnis_Object = MibTableColumn
frLportUpdtRxNnis = _FrLportUpdtRxNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 22),
    _FrLportUpdtRxNnis_Type()
)
frLportUpdtRxNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportUpdtRxNnis.setStatus("mandatory")
_FrLportToutCntNnis_Type = Counter32
_FrLportToutCntNnis_Object = MibTableColumn
frLportToutCntNnis = _FrLportToutCntNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 23),
    _FrLportToutCntNnis_Type()
)
frLportToutCntNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportToutCntNnis.setStatus("mandatory")
_FrLportSeqnmErrNnis_Type = Counter32
_FrLportSeqnmErrNnis_Object = MibTableColumn
frLportSeqnmErrNnis = _FrLportSeqnmErrNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 24),
    _FrLportSeqnmErrNnis_Type()
)
frLportSeqnmErrNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSeqnmErrNnis.setStatus("mandatory")
_FrLportCllmTxFrms_Type = Counter32
_FrLportCllmTxFrms_Object = MibTableColumn
frLportCllmTxFrms = _FrLportCllmTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 25),
    _FrLportCllmTxFrms_Type()
)
frLportCllmTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmTxFrms.setStatus("mandatory")
_FrLportCllmTxBytes_Type = Counter32
_FrLportCllmTxBytes_Object = MibTableColumn
frLportCllmTxBytes = _FrLportCllmTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 26),
    _FrLportCllmTxBytes_Type()
)
frLportCllmTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmTxBytes.setStatus("mandatory")
_FrLportCllmRxFrms_Type = Counter32
_FrLportCllmRxFrms_Object = MibTableColumn
frLportCllmRxFrms = _FrLportCllmRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 27),
    _FrLportCllmRxFrms_Type()
)
frLportCllmRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmRxFrms.setStatus("mandatory")
_FrLportCllmRxBytes_Type = Counter32
_FrLportCllmRxBytes_Object = MibTableColumn
frLportCllmRxBytes = _FrLportCllmRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 28),
    _FrLportCllmRxBytes_Type()
)
frLportCllmRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmRxBytes.setStatus("mandatory")
_FrLportCllmFailures_Type = Counter32
_FrLportCllmFailures_Object = MibTableColumn
frLportCllmFailures = _FrLportCllmFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 29),
    _FrLportCllmFailures_Type()
)
frLportCllmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmFailures.setStatus("mandatory")
_FrLportDscdQTxFrms_Type = Counter32
_FrLportDscdQTxFrms_Object = MibTableColumn
frLportDscdQTxFrms = _FrLportDscdQTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 30),
    _FrLportDscdQTxFrms_Type()
)
frLportDscdQTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDscdQTxFrms.setStatus("mandatory")
_FrLportDscdQTxBytes_Type = Counter32
_FrLportDscdQTxBytes_Object = MibTableColumn
frLportDscdQTxBytes = _FrLportDscdQTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 31),
    _FrLportDscdQTxBytes_Type()
)
frLportDscdQTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDscdQTxBytes.setStatus("mandatory")
_FrLportLmiFailFrms_Type = Counter32
_FrLportLmiFailFrms_Object = MibTableColumn
frLportLmiFailFrms = _FrLportLmiFailFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 32),
    _FrLportLmiFailFrms_Type()
)
frLportLmiFailFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLmiFailFrms.setStatus("mandatory")
_FrLportLmiFailBytes_Type = Counter32
_FrLportLmiFailBytes_Object = MibTableColumn
frLportLmiFailBytes = _FrLportLmiFailBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 33),
    _FrLportLmiFailBytes_Type()
)
frLportLmiFailBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLmiFailBytes.setStatus("mandatory")
_AtmServiceObjects_ObjectIdentity = ObjectIdentity
atmServiceObjects = _AtmServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2)
)
_AtmPortTable_Object = MibTable
atmPortTable = _AtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmPortTable.setStatus("mandatory")
_AtmPortEntry_Object = MibTableRow
atmPortEntry = _AtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1)
)
atmPortEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmPortSlot"),
    (0, "STRATACOM-MIB", "atmPortPort"),
)
if mibBuilder.loadTexts:
    atmPortEntry.setStatus("mandatory")


class _AtmPortSlot_Type(Integer32):
    """Custom type atmPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmPortSlot_Type.__name__ = "Integer32"
_AtmPortSlot_Object = MibTableColumn
atmPortSlot = _AtmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 1),
    _AtmPortSlot_Type()
)
atmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSlot.setStatus("mandatory")
_AtmPortPort_Type = Integer32
_AtmPortPort_Object = MibTableColumn
atmPortPort = _AtmPortPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 2),
    _AtmPortPort_Type()
)
atmPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortPort.setStatus("mandatory")


class _AtmPortAdminStatus_Type(Integer32):
    """Custom type atmPortAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("modify", 3),
          ("writeOnly", 4))
    )


_AtmPortAdminStatus_Type.__name__ = "Integer32"
_AtmPortAdminStatus_Object = MibTableColumn
atmPortAdminStatus = _AtmPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 3),
    _AtmPortAdminStatus_Type()
)
atmPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAdminStatus.setStatus("mandatory")


class _AtmPortOperStatus_Type(Integer32):
    """Custom type atmPortOperStatus based on Integer32"""
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
        *(("inactive", 1),
          ("active", 2),
          ("looped", 3),
          ("failed", 4),
          ("unknown", 5))
    )


_AtmPortOperStatus_Type.__name__ = "Integer32"
_AtmPortOperStatus_Object = MibTableColumn
atmPortOperStatus = _AtmPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 4),
    _AtmPortOperStatus_Type()
)
atmPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortOperStatus.setStatus("mandatory")


class _AtmPortType_Type(Integer32):
    """Custom type atmPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uni", 1),
          ("nni", 2))
    )


_AtmPortType_Type.__name__ = "Integer32"
_AtmPortType_Object = MibTableColumn
atmPortType = _AtmPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 5),
    _AtmPortType_Type()
)
atmPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortType.setStatus("mandatory")


class _AtmPortIfType_Type(Integer32):
    """Custom type atmPortIfType based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t3", 2),
          ("e3", 3),
          ("oc3-smf", 4),
          ("oc3-mmf", 5),
          ("oc3-stm1", 6),
          ("oc3-utp", 7),
          ("oc3-stp", 8),
          ("oc3-smflr", 9),
          ("oc12-smf", 10),
          ("oc12-mmf", 11),
          ("oc12-smflr", 12),
          ("t1", 13),
          ("e1", 14),
          ("oc3-xlr", 15),
          ("oc12-xlr", 16))
    )


_AtmPortIfType_Type.__name__ = "Integer32"
_AtmPortIfType_Object = MibTableColumn
atmPortIfType = _AtmPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 6),
    _AtmPortIfType_Type()
)
atmPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortIfType.setStatus("mandatory")
_AtmPortSpeed_Type = Integer32
_AtmPortSpeed_Object = MibTableColumn
atmPortSpeed = _AtmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 7),
    _AtmPortSpeed_Type()
)
atmPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSpeed.setStatus("mandatory")


class _AtmPortAxis_Type(Integer32):
    """Custom type atmPortAxis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("t1", 2),
          ("e1", 3))
    )


_AtmPortAxis_Type.__name__ = "Integer32"
_AtmPortAxis_Object = MibTableColumn
atmPortAxis = _AtmPortAxis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 8),
    _AtmPortAxis_Type()
)
atmPortAxis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAxis.setStatus("mandatory")
_AtmPortVcCount_Type = Integer32
_AtmPortVcCount_Object = MibTableColumn
atmPortVcCount = _AtmPortVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 9),
    _AtmPortVcCount_Type()
)
atmPortVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortVcCount.setStatus("mandatory")
_AtmPortFirstVcPtr_Type = ObjectIdentifier
_AtmPortFirstVcPtr_Object = MibTableColumn
atmPortFirstVcPtr = _AtmPortFirstVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 10),
    _AtmPortFirstVcPtr_Type()
)
atmPortFirstVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortFirstVcPtr.setStatus("mandatory")


class _AtmPortMetro_Type(Integer32):
    """Custom type atmPortMetro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmPortMetro_Type.__name__ = "Integer32"
_AtmPortMetro_Object = MibTableColumn
atmPortMetro = _AtmPortMetro_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 11),
    _AtmPortMetro_Type()
)
atmPortMetro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortMetro.setStatus("mandatory")


class _AtmPortMgmtProto_Type(Integer32):
    """Custom type atmPortMgmtProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lmi", 2),
          ("ilmi", 3))
    )


_AtmPortMgmtProto_Type.__name__ = "Integer32"
_AtmPortMgmtProto_Object = MibTableColumn
atmPortMgmtProto = _AtmPortMgmtProto_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 12),
    _AtmPortMgmtProto_Type()
)
atmPortMgmtProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortMgmtProto.setStatus("mandatory")


class _AtmPortIlmiVpi_Type(Integer32):
    """Custom type atmPortIlmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmPortIlmiVpi_Type.__name__ = "Integer32"
_AtmPortIlmiVpi_Object = MibTableColumn
atmPortIlmiVpi = _AtmPortIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 13),
    _AtmPortIlmiVpi_Type()
)
atmPortIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiVpi.setStatus("mandatory")


class _AtmPortIlmiVci_Type(Integer32):
    """Custom type atmPortIlmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmPortIlmiVci_Type.__name__ = "Integer32"
_AtmPortIlmiVci_Object = MibTableColumn
atmPortIlmiVci = _AtmPortIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 14),
    _AtmPortIlmiVci_Type()
)
atmPortIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiVci.setStatus("mandatory")


class _AtmPortIlmiPollEnable_Type(Integer32):
    """Custom type atmPortIlmiPollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmPortIlmiPollEnable_Type.__name__ = "Integer32"
_AtmPortIlmiPollEnable_Object = MibTableColumn
atmPortIlmiPollEnable = _AtmPortIlmiPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 15),
    _AtmPortIlmiPollEnable_Type()
)
atmPortIlmiPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiPollEnable.setStatus("mandatory")


class _AtmPortIlmiTrapEnable_Type(Integer32):
    """Custom type atmPortIlmiTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmPortIlmiTrapEnable_Type.__name__ = "Integer32"
_AtmPortIlmiTrapEnable_Object = MibTableColumn
atmPortIlmiTrapEnable = _AtmPortIlmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 16),
    _AtmPortIlmiTrapEnable_Type()
)
atmPortIlmiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiTrapEnable.setStatus("mandatory")


class _AtmPortIlmiPollIntrvl_Type(Integer32):
    """Custom type atmPortIlmiPollIntrvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_AtmPortIlmiPollIntrvl_Type.__name__ = "Integer32"
_AtmPortIlmiPollIntrvl_Object = MibTableColumn
atmPortIlmiPollIntrvl = _AtmPortIlmiPollIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 17),
    _AtmPortIlmiPollIntrvl_Type()
)
atmPortIlmiPollIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiPollIntrvl.setStatus("mandatory")


class _AtmPortIlmiErrorThresh_Type(Integer32):
    """Custom type atmPortIlmiErrorThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortIlmiErrorThresh_Type.__name__ = "Integer32"
_AtmPortIlmiErrorThresh_Object = MibTableColumn
atmPortIlmiErrorThresh = _AtmPortIlmiErrorThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 18),
    _AtmPortIlmiErrorThresh_Type()
)
atmPortIlmiErrorThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiErrorThresh.setStatus("mandatory")


class _AtmPortIlmiEventThresh_Type(Integer32):
    """Custom type atmPortIlmiEventThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortIlmiEventThresh_Type.__name__ = "Integer32"
_AtmPortIlmiEventThresh_Object = MibTableColumn
atmPortIlmiEventThresh = _AtmPortIlmiEventThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 19),
    _AtmPortIlmiEventThresh_Type()
)
atmPortIlmiEventThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiEventThresh.setStatus("mandatory")


class _AtmPortLmiVpi_Type(Integer32):
    """Custom type atmPortLmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmPortLmiVpi_Type.__name__ = "Integer32"
_AtmPortLmiVpi_Object = MibTableColumn
atmPortLmiVpi = _AtmPortLmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 20),
    _AtmPortLmiVpi_Type()
)
atmPortLmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiVpi.setStatus("mandatory")


class _AtmPortLmiVci_Type(Integer32):
    """Custom type atmPortLmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmPortLmiVci_Type.__name__ = "Integer32"
_AtmPortLmiVci_Object = MibTableColumn
atmPortLmiVci = _AtmPortLmiVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 21),
    _AtmPortLmiVci_Type()
)
atmPortLmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiVci.setStatus("mandatory")


class _AtmPortLmiPollEnable_Type(Integer32):
    """Custom type atmPortLmiPollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmPortLmiPollEnable_Type.__name__ = "Integer32"
_AtmPortLmiPollEnable_Object = MibTableColumn
atmPortLmiPollEnable = _AtmPortLmiPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 22),
    _AtmPortLmiPollEnable_Type()
)
atmPortLmiPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiPollEnable.setStatus("mandatory")


class _AtmPortLmiStatEnqTimer_Type(Integer32):
    """Custom type atmPortLmiStatEnqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AtmPortLmiStatEnqTimer_Type.__name__ = "Integer32"
_AtmPortLmiStatEnqTimer_Object = MibTableColumn
atmPortLmiStatEnqTimer = _AtmPortLmiStatEnqTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 23),
    _AtmPortLmiStatEnqTimer_Type()
)
atmPortLmiStatEnqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiStatEnqTimer.setStatus("mandatory")


class _AtmPortLmiUpdStatTimer_Type(Integer32):
    """Custom type atmPortLmiUpdStatTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AtmPortLmiUpdStatTimer_Type.__name__ = "Integer32"
_AtmPortLmiUpdStatTimer_Object = MibTableColumn
atmPortLmiUpdStatTimer = _AtmPortLmiUpdStatTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 24),
    _AtmPortLmiUpdStatTimer_Type()
)
atmPortLmiUpdStatTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiUpdStatTimer.setStatus("mandatory")


class _AtmPortLmiStatEnqRetry_Type(Integer32):
    """Custom type atmPortLmiStatEnqRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortLmiStatEnqRetry_Type.__name__ = "Integer32"
_AtmPortLmiStatEnqRetry_Object = MibTableColumn
atmPortLmiStatEnqRetry = _AtmPortLmiStatEnqRetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 25),
    _AtmPortLmiStatEnqRetry_Type()
)
atmPortLmiStatEnqRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiStatEnqRetry.setStatus("mandatory")


class _AtmPortLmiUpdStatRetry_Type(Integer32):
    """Custom type atmPortLmiUpdStatRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortLmiUpdStatRetry_Type.__name__ = "Integer32"
_AtmPortLmiUpdStatRetry_Object = MibTableColumn
atmPortLmiUpdStatRetry = _AtmPortLmiUpdStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 26),
    _AtmPortLmiUpdStatRetry_Type()
)
atmPortLmiUpdStatRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiUpdStatRetry.setStatus("mandatory")


class _AtmPortLmiPollTimer_Type(Integer32):
    """Custom type atmPortLmiPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AtmPortLmiPollTimer_Type.__name__ = "Integer32"
_AtmPortLmiPollTimer_Object = MibTableColumn
atmPortLmiPollTimer = _AtmPortLmiPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 27),
    _AtmPortLmiPollTimer_Type()
)
atmPortLmiPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiPollTimer.setStatus("mandatory")


class _AtmPortPercUtil_Type(Integer32):
    """Custom type atmPortPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmPortPercUtil_Type.__name__ = "Integer32"
_AtmPortPercUtil_Object = MibTableColumn
atmPortPercUtil = _AtmPortPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 28),
    _AtmPortPercUtil_Type()
)
atmPortPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortPercUtil.setStatus("mandatory")
_AtmPortSvcChannels_Type = Integer32
_AtmPortSvcChannels_Object = MibTableColumn
atmPortSvcChannels = _AtmPortSvcChannels_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 29),
    _AtmPortSvcChannels_Type()
)
atmPortSvcChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcChannels.setStatus("mandatory")


class _AtmPortShareLcn_Type(Integer32):
    """Custom type atmPortShareLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("cardBased", 2))
    )


_AtmPortShareLcn_Type.__name__ = "Integer32"
_AtmPortShareLcn_Object = MibTableColumn
atmPortShareLcn = _AtmPortShareLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 30),
    _AtmPortShareLcn_Type()
)
atmPortShareLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortShareLcn.setStatus("mandatory")
_AtmPortSvcLcnLow_Type = Integer32
_AtmPortSvcLcnLow_Object = MibTableColumn
atmPortSvcLcnLow = _AtmPortSvcLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 31),
    _AtmPortSvcLcnLow_Type()
)
atmPortSvcLcnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcLcnLow.setStatus("mandatory")
_AtmPortSvcLcnHigh_Type = Integer32
_AtmPortSvcLcnHigh_Object = MibTableColumn
atmPortSvcLcnHigh = _AtmPortSvcLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 32),
    _AtmPortSvcLcnHigh_Type()
)
atmPortSvcLcnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcLcnHigh.setStatus("mandatory")
_AtmPortSvcVpiLow_Type = Integer32
_AtmPortSvcVpiLow_Object = MibTableColumn
atmPortSvcVpiLow = _AtmPortSvcVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 33),
    _AtmPortSvcVpiLow_Type()
)
atmPortSvcVpiLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcVpiLow.setStatus("mandatory")
_AtmPortSvcVpiHigh_Type = Integer32
_AtmPortSvcVpiHigh_Object = MibTableColumn
atmPortSvcVpiHigh = _AtmPortSvcVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 34),
    _AtmPortSvcVpiHigh_Type()
)
atmPortSvcVpiHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcVpiHigh.setStatus("mandatory")
_AtmPortSvcVciLow_Type = Integer32
_AtmPortSvcVciLow_Object = MibTableColumn
atmPortSvcVciLow = _AtmPortSvcVciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 35),
    _AtmPortSvcVciLow_Type()
)
atmPortSvcVciLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmPortSvcVciLow.setStatus("deprecated")
_AtmPortSvcVciHigh_Type = Integer32
_AtmPortSvcVciHigh_Object = MibTableColumn
atmPortSvcVciHigh = _AtmPortSvcVciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 36),
    _AtmPortSvcVciHigh_Type()
)
atmPortSvcVciHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmPortSvcVciHigh.setStatus("deprecated")
_AtmPortSvcQbinBitMap_Type = OctetString
_AtmPortSvcQbinBitMap_Object = MibTableColumn
atmPortSvcQbinBitMap = _AtmPortSvcQbinBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 37),
    _AtmPortSvcQbinBitMap_Type()
)
atmPortSvcQbinBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcQbinBitMap.setStatus("mandatory")
_AtmPortSvcQbinSz_Type = Integer32
_AtmPortSvcQbinSz_Object = MibTableColumn
atmPortSvcQbinSz = _AtmPortSvcQbinSz_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 38),
    _AtmPortSvcQbinSz_Type()
)
atmPortSvcQbinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcQbinSz.setStatus("mandatory")
_AtmPortSvcBw_Type = Integer32
_AtmPortSvcBw_Object = MibTableColumn
atmPortSvcBw = _AtmPortSvcBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 39),
    _AtmPortSvcBw_Type()
)
atmPortSvcBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSvcBw.setStatus("mandatory")


class _AtmPortSvcInUse_Type(Integer32):
    """Custom type atmPortSvcInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_AtmPortSvcInUse_Type.__name__ = "Integer32"
_AtmPortSvcInUse_Object = MibTableColumn
atmPortSvcInUse = _AtmPortSvcInUse_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 40),
    _AtmPortSvcInUse_Type()
)
atmPortSvcInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortSvcInUse.setStatus("mandatory")


class _AtmPortPvcInUse_Type(Integer32):
    """Custom type atmPortPvcInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_AtmPortPvcInUse_Type.__name__ = "Integer32"
_AtmPortPvcInUse_Object = MibTableColumn
atmPortPvcInUse = _AtmPortPvcInUse_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 41),
    _AtmPortPvcInUse_Type()
)
atmPortPvcInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortPvcInUse.setStatus("mandatory")


class _AtmPortIlmiAddrReg_Type(Integer32):
    """Custom type atmPortIlmiAddrReg based on Integer32"""
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


_AtmPortIlmiAddrReg_Type.__name__ = "Integer32"
_AtmPortIlmiAddrReg_Object = MibTableColumn
atmPortIlmiAddrReg = _AtmPortIlmiAddrReg_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 42),
    _AtmPortIlmiAddrReg_Type()
)
atmPortIlmiAddrReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiAddrReg.setStatus("mandatory")


class _AtmPortCACOverride_Type(Integer32):
    """Custom type atmPortCACOverride based on Integer32"""
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


_AtmPortCACOverride_Type.__name__ = "Integer32"
_AtmPortCACOverride_Object = MibTableColumn
atmPortCACOverride = _AtmPortCACOverride_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 43),
    _AtmPortCACOverride_Type()
)
atmPortCACOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortCACOverride.setStatus("mandatory")
_AtmPortLoad_Type = Integer32
_AtmPortLoad_Object = MibTableColumn
atmPortLoad = _AtmPortLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 44),
    _AtmPortLoad_Type()
)
atmPortLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortLoad.setStatus("mandatory")
_AtmPortQueueTable_Object = MibTable
atmPortQueueTable = _AtmPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    atmPortQueueTable.setStatus("mandatory")
_AtmPortQueueEntry_Object = MibTableRow
atmPortQueueEntry = _AtmPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1)
)
atmPortQueueEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmPortSlot"),
    (0, "STRATACOM-MIB", "atmPortPort"),
    (0, "STRATACOM-MIB", "atmPortQueueIndex"),
)
if mibBuilder.loadTexts:
    atmPortQueueEntry.setStatus("mandatory")


class _AtmPortQueueIndex_Type(Integer32):
    """Custom type atmPortQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmPortQueueIndex_Type.__name__ = "Integer32"
_AtmPortQueueIndex_Object = MibTableColumn
atmPortQueueIndex = _AtmPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 1),
    _AtmPortQueueIndex_Type()
)
atmPortQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortQueueIndex.setStatus("mandatory")


class _AtmPortQueueAdminStatus_Type(Integer32):
    """Custom type atmPortQueueAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modify", 1),
          ("writeOnly", 2))
    )


_AtmPortQueueAdminStatus_Type.__name__ = "Integer32"
_AtmPortQueueAdminStatus_Object = MibTableColumn
atmPortQueueAdminStatus = _AtmPortQueueAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 2),
    _AtmPortQueueAdminStatus_Type()
)
atmPortQueueAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueAdminStatus.setStatus("mandatory")


class _AtmPortQueueType_Type(Integer32):
    """Custom type atmPortQueueType based on Integer32"""
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
        *(("unknown", 1),
          ("unused", 2),
          ("cbr", 3),
          ("abr", 4),
          ("vbr", 5),
          ("axis", 6))
    )


_AtmPortQueueType_Type.__name__ = "Integer32"
_AtmPortQueueType_Object = MibTableColumn
atmPortQueueType = _AtmPortQueueType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 3),
    _AtmPortQueueType_Type()
)
atmPortQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortQueueType.setStatus("mandatory")


class _AtmPortQueueDepth_Type(Integer32):
    """Custom type atmPortQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11000),
    )


_AtmPortQueueDepth_Type.__name__ = "Integer32"
_AtmPortQueueDepth_Object = MibTableColumn
atmPortQueueDepth = _AtmPortQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 4),
    _AtmPortQueueDepth_Type()
)
atmPortQueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueDepth.setStatus("mandatory")


class _AtmPortQueueClpHi_Type(Integer32):
    """Custom type atmPortQueueClpHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmPortQueueClpHi_Type.__name__ = "Integer32"
_AtmPortQueueClpHi_Object = MibTableColumn
atmPortQueueClpHi = _AtmPortQueueClpHi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 5),
    _AtmPortQueueClpHi_Type()
)
atmPortQueueClpHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueClpHi.setStatus("mandatory")


class _AtmPortQueueClpLo_Type(Integer32):
    """Custom type atmPortQueueClpLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmPortQueueClpLo_Type.__name__ = "Integer32"
_AtmPortQueueClpLo_Object = MibTableColumn
atmPortQueueClpLo = _AtmPortQueueClpLo_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 6),
    _AtmPortQueueClpLo_Type()
)
atmPortQueueClpLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueClpLo.setStatus("mandatory")


class _AtmPortQueueEfciTh_Type(Integer32):
    """Custom type atmPortQueueEfciTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmPortQueueEfciTh_Type.__name__ = "Integer32"
_AtmPortQueueEfciTh_Object = MibTableColumn
atmPortQueueEfciTh = _AtmPortQueueEfciTh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 7),
    _AtmPortQueueEfciTh_Type()
)
atmPortQueueEfciTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueEfciTh.setStatus("mandatory")


class _AtmPortQueueAlgorithm_Type(Integer32):
    """Custom type atmPortQueueAlgorithm based on Integer32"""
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
        *(("off", 1),
          ("always", 2),
          ("ok", 3),
          ("minGuar", 4),
          ("minSmooth", 5),
          ("minDelay", 6))
    )


_AtmPortQueueAlgorithm_Type.__name__ = "Integer32"
_AtmPortQueueAlgorithm_Object = MibTableColumn
atmPortQueueAlgorithm = _AtmPortQueueAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 8),
    _AtmPortQueueAlgorithm_Type()
)
atmPortQueueAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortQueueAlgorithm.setStatus("mandatory")
_AtmPortStatTable_Object = MibTable
atmPortStatTable = _AtmPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    atmPortStatTable.setStatus("mandatory")
_AtmPortStatEntry_Object = MibTableRow
atmPortStatEntry = _AtmPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1)
)
atmPortStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmPortSlot"),
    (0, "STRATACOM-MIB", "atmPortPort"),
)
if mibBuilder.loadTexts:
    atmPortStatEntry.setStatus("mandatory")
_AtmPortStatUnknVpiVcis_Type = Counter32
_AtmPortStatUnknVpiVcis_Object = MibTableColumn
atmPortStatUnknVpiVcis = _AtmPortStatUnknVpiVcis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 1),
    _AtmPortStatUnknVpiVcis_Type()
)
atmPortStatUnknVpiVcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatUnknVpiVcis.setStatus("mandatory")
_AtmPortStatBufferOvfls_Type = Counter32
_AtmPortStatBufferOvfls_Object = MibTableColumn
atmPortStatBufferOvfls = _AtmPortStatBufferOvfls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 2),
    _AtmPortStatBufferOvfls_Type()
)
atmPortStatBufferOvfls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatBufferOvfls.setStatus("mandatory")
_AtmPortStatNonZeroGfcs_Type = Counter32
_AtmPortStatNonZeroGfcs_Object = MibTableColumn
atmPortStatNonZeroGfcs = _AtmPortStatNonZeroGfcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 3),
    _AtmPortStatNonZeroGfcs_Type()
)
atmPortStatNonZeroGfcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatNonZeroGfcs.setStatus("mandatory")
_AtmPortStatIsuDiscards_Type = Counter32
_AtmPortStatIsuDiscards_Object = MibTableColumn
atmPortStatIsuDiscards = _AtmPortStatIsuDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 4),
    _AtmPortStatIsuDiscards_Type()
)
atmPortStatIsuDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIsuDiscards.setStatus("mandatory")
_AtmPortStatIsuEmptys_Type = Counter32
_AtmPortStatIsuEmptys_Object = MibTableColumn
atmPortStatIsuEmptys = _AtmPortStatIsuEmptys_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 5),
    _AtmPortStatIsuEmptys_Type()
)
atmPortStatIsuEmptys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIsuEmptys.setStatus("mandatory")
_AtmPortStatAisRxs_Type = Counter32
_AtmPortStatAisRxs_Object = MibTableColumn
atmPortStatAisRxs = _AtmPortStatAisRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 6),
    _AtmPortStatAisRxs_Type()
)
atmPortStatAisRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatAisRxs.setStatus("mandatory")
_AtmPortStatFerfRxs_Type = Counter32
_AtmPortStatFerfRxs_Object = MibTableColumn
atmPortStatFerfRxs = _AtmPortStatFerfRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 7),
    _AtmPortStatFerfRxs_Type()
)
atmPortStatFerfRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatFerfRxs.setStatus("mandatory")
_AtmPortStatCellsRxs_Type = Counter32
_AtmPortStatCellsRxs_Object = MibTableColumn
atmPortStatCellsRxs = _AtmPortStatCellsRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 8),
    _AtmPortStatCellsRxs_Type()
)
atmPortStatCellsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatCellsRxs.setStatus("mandatory")
_AtmPortStatClpRxs_Type = Counter32
_AtmPortStatClpRxs_Object = MibTableColumn
atmPortStatClpRxs = _AtmPortStatClpRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 9),
    _AtmPortStatClpRxs_Type()
)
atmPortStatClpRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatClpRxs.setStatus("mandatory")
_AtmPortStatEfciRxs_Type = Counter32
_AtmPortStatEfciRxs_Object = MibTableColumn
atmPortStatEfciRxs = _AtmPortStatEfciRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 10),
    _AtmPortStatEfciRxs_Type()
)
atmPortStatEfciRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatEfciRxs.setStatus("mandatory")
_AtmPortStatBcmRxs_Type = Counter32
_AtmPortStatBcmRxs_Object = MibTableColumn
atmPortStatBcmRxs = _AtmPortStatBcmRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 11),
    _AtmPortStatBcmRxs_Type()
)
atmPortStatBcmRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatBcmRxs.setStatus("mandatory")
_AtmPortStatCellsTxs_Type = Counter32
_AtmPortStatCellsTxs_Object = MibTableColumn
atmPortStatCellsTxs = _AtmPortStatCellsTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 12),
    _AtmPortStatCellsTxs_Type()
)
atmPortStatCellsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatCellsTxs.setStatus("mandatory")
_AtmPortStatOamRxs_Type = Counter32
_AtmPortStatOamRxs_Object = MibTableColumn
atmPortStatOamRxs = _AtmPortStatOamRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 13),
    _AtmPortStatOamRxs_Type()
)
atmPortStatOamRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatOamRxs.setStatus("mandatory")
_AtmPortStatPayldErrs_Type = Counter32
_AtmPortStatPayldErrs_Object = MibTableColumn
atmPortStatPayldErrs = _AtmPortStatPayldErrs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 14),
    _AtmPortStatPayldErrs_Type()
)
atmPortStatPayldErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatPayldErrs.setStatus("mandatory")
_AtmPortStatClpTxs_Type = Counter32
_AtmPortStatClpTxs_Object = MibTableColumn
atmPortStatClpTxs = _AtmPortStatClpTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 15),
    _AtmPortStatClpTxs_Type()
)
atmPortStatClpTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatClpTxs.setStatus("mandatory")
_AtmPortStatEfciTxs_Type = Counter32
_AtmPortStatEfciTxs_Object = MibTableColumn
atmPortStatEfciTxs = _AtmPortStatEfciTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 16),
    _AtmPortStatEfciTxs_Type()
)
atmPortStatEfciTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatEfciTxs.setStatus("mandatory")
_AtmPortStatHdrDiscards_Type = Counter32
_AtmPortStatHdrDiscards_Object = MibTableColumn
atmPortStatHdrDiscards = _AtmPortStatHdrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 17),
    _AtmPortStatHdrDiscards_Type()
)
atmPortStatHdrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatHdrDiscards.setStatus("mandatory")
_AtmPortStatIlmiGetRxs_Type = Counter32
_AtmPortStatIlmiGetRxs_Object = MibTableColumn
atmPortStatIlmiGetRxs = _AtmPortStatIlmiGetRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 18),
    _AtmPortStatIlmiGetRxs_Type()
)
atmPortStatIlmiGetRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetRxs.setStatus("mandatory")
_AtmPortStatIlmiGetNextRxs_Type = Counter32
_AtmPortStatIlmiGetNextRxs_Object = MibTableColumn
atmPortStatIlmiGetNextRxs = _AtmPortStatIlmiGetNextRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 19),
    _AtmPortStatIlmiGetNextRxs_Type()
)
atmPortStatIlmiGetNextRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetNextRxs.setStatus("mandatory")
_AtmPortStatIlmiGetNextTxs_Type = Counter32
_AtmPortStatIlmiGetNextTxs_Object = MibTableColumn
atmPortStatIlmiGetNextTxs = _AtmPortStatIlmiGetNextTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 20),
    _AtmPortStatIlmiGetNextTxs_Type()
)
atmPortStatIlmiGetNextTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetNextTxs.setStatus("mandatory")
_AtmPortStatIlmiSetRxs_Type = Counter32
_AtmPortStatIlmiSetRxs_Object = MibTableColumn
atmPortStatIlmiSetRxs = _AtmPortStatIlmiSetRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 21),
    _AtmPortStatIlmiSetRxs_Type()
)
atmPortStatIlmiSetRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiSetRxs.setStatus("mandatory")
_AtmPortStatIlmiTrapRxs_Type = Counter32
_AtmPortStatIlmiTrapRxs_Object = MibTableColumn
atmPortStatIlmiTrapRxs = _AtmPortStatIlmiTrapRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 22),
    _AtmPortStatIlmiTrapRxs_Type()
)
atmPortStatIlmiTrapRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiTrapRxs.setStatus("mandatory")
_AtmPortStatIlmiGetRspRxs_Type = Counter32
_AtmPortStatIlmiGetRspRxs_Object = MibTableColumn
atmPortStatIlmiGetRspRxs = _AtmPortStatIlmiGetRspRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 23),
    _AtmPortStatIlmiGetRspRxs_Type()
)
atmPortStatIlmiGetRspRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetRspRxs.setStatus("mandatory")
_AtmPortStatIlmiGetTxs_Type = Counter32
_AtmPortStatIlmiGetTxs_Object = MibTableColumn
atmPortStatIlmiGetTxs = _AtmPortStatIlmiGetTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 24),
    _AtmPortStatIlmiGetTxs_Type()
)
atmPortStatIlmiGetTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetTxs.setStatus("mandatory")
_AtmPortStatIlmiGetRspTxs_Type = Counter32
_AtmPortStatIlmiGetRspTxs_Object = MibTableColumn
atmPortStatIlmiGetRspTxs = _AtmPortStatIlmiGetRspTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 25),
    _AtmPortStatIlmiGetRspTxs_Type()
)
atmPortStatIlmiGetRspTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetRspTxs.setStatus("mandatory")
_AtmPortStatIlmiTrapTxs_Type = Counter32
_AtmPortStatIlmiTrapTxs_Object = MibTableColumn
atmPortStatIlmiTrapTxs = _AtmPortStatIlmiTrapTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 26),
    _AtmPortStatIlmiTrapTxs_Type()
)
atmPortStatIlmiTrapTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiTrapTxs.setStatus("mandatory")
_AtmPortStatIlmiUnkRxs_Type = Counter32
_AtmPortStatIlmiUnkRxs_Object = MibTableColumn
atmPortStatIlmiUnkRxs = _AtmPortStatIlmiUnkRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 27),
    _AtmPortStatIlmiUnkRxs_Type()
)
atmPortStatIlmiUnkRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiUnkRxs.setStatus("mandatory")
_AtmPortStatLmiStatTxs_Type = Counter32
_AtmPortStatLmiStatTxs_Object = MibTableColumn
atmPortStatLmiStatTxs = _AtmPortStatLmiStatTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 28),
    _AtmPortStatLmiStatTxs_Type()
)
atmPortStatLmiStatTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatTxs.setStatus("mandatory")
_AtmPortStatLmiUpdtStatTxs_Type = Counter32
_AtmPortStatLmiUpdtStatTxs_Object = MibTableColumn
atmPortStatLmiUpdtStatTxs = _AtmPortStatLmiUpdtStatTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 29),
    _AtmPortStatLmiUpdtStatTxs_Type()
)
atmPortStatLmiUpdtStatTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiUpdtStatTxs.setStatus("mandatory")
_AtmPortStatLmiStatAckTxs_Type = Counter32
_AtmPortStatLmiStatAckTxs_Object = MibTableColumn
atmPortStatLmiStatAckTxs = _AtmPortStatLmiStatAckTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 30),
    _AtmPortStatLmiStatAckTxs_Type()
)
atmPortStatLmiStatAckTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatAckTxs.setStatus("mandatory")
_AtmPortStatLmiStatEnqTxs_Type = Counter32
_AtmPortStatLmiStatEnqTxs_Object = MibTableColumn
atmPortStatLmiStatEnqTxs = _AtmPortStatLmiStatEnqTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 31),
    _AtmPortStatLmiStatEnqTxs_Type()
)
atmPortStatLmiStatEnqTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatEnqTxs.setStatus("mandatory")
_AtmPortStatLmiStatEnqRxs_Type = Counter32
_AtmPortStatLmiStatEnqRxs_Object = MibTableColumn
atmPortStatLmiStatEnqRxs = _AtmPortStatLmiStatEnqRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 32),
    _AtmPortStatLmiStatEnqRxs_Type()
)
atmPortStatLmiStatEnqRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatEnqRxs.setStatus("mandatory")
_AtmPortStatLmiStatRxs_Type = Counter32
_AtmPortStatLmiStatRxs_Object = MibTableColumn
atmPortStatLmiStatRxs = _AtmPortStatLmiStatRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 33),
    _AtmPortStatLmiStatRxs_Type()
)
atmPortStatLmiStatRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatRxs.setStatus("mandatory")
_AtmPortStatLmiUpdStatRxs_Type = Counter32
_AtmPortStatLmiUpdStatRxs_Object = MibTableColumn
atmPortStatLmiUpdStatRxs = _AtmPortStatLmiUpdStatRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 34),
    _AtmPortStatLmiUpdStatRxs_Type()
)
atmPortStatLmiUpdStatRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiUpdStatRxs.setStatus("mandatory")
_AtmPortStatLmiStatAckRxs_Type = Counter32
_AtmPortStatLmiStatAckRxs_Object = MibTableColumn
atmPortStatLmiStatAckRxs = _AtmPortStatLmiStatAckRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 35),
    _AtmPortStatLmiStatAckRxs_Type()
)
atmPortStatLmiStatAckRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatAckRxs.setStatus("mandatory")
_VoiceServiceObjects_ObjectIdentity = ObjectIdentity
voiceServiceObjects = _VoiceServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3)
)
_TrunkServiceObjects_ObjectIdentity = ObjectIdentity
trunkServiceObjects = _TrunkServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4)
)
_FpRoutingTrunks_Object = MibTable
fpRoutingTrunks = _FpRoutingTrunks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fpRoutingTrunks.setStatus("mandatory")
_FpRteTrkEntry_Object = MibTableRow
fpRteTrkEntry = _FpRteTrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1)
)
fpRteTrkEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    fpRteTrkEntry.setStatus("mandatory")


class _FpRteTrkStatus_Type(Integer32):
    """Custom type fpRteTrkStatus based on Integer32"""
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
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("down", 4),
          ("deact", 5))
    )


_FpRteTrkStatus_Type.__name__ = "Integer32"
_FpRteTrkStatus_Object = MibTableColumn
fpRteTrkStatus = _FpRteTrkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 1),
    _FpRteTrkStatus_Type()
)
fpRteTrkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkStatus.setStatus("mandatory")


class _FpRteTrkAlmEnable_Type(Integer32):
    """Custom type fpRteTrkAlmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FpRteTrkAlmEnable_Type.__name__ = "Integer32"
_FpRteTrkAlmEnable_Object = MibTableColumn
fpRteTrkAlmEnable = _FpRteTrkAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 2),
    _FpRteTrkAlmEnable_Type()
)
fpRteTrkAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkAlmEnable.setStatus("mandatory")


class _FpRteTrkComStatus_Type(Integer32):
    """Custom type fpRteTrkComStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commOK", 1),
          ("commFAIL", 2))
    )


_FpRteTrkComStatus_Type.__name__ = "Integer32"
_FpRteTrkComStatus_Object = MibTableColumn
fpRteTrkComStatus = _FpRteTrkComStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 3),
    _FpRteTrkComStatus_Type()
)
fpRteTrkComStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkComStatus.setStatus("mandatory")
_FpRteTrkTrnsCap_Type = Integer32
_FpRteTrkTrnsCap_Object = MibTableColumn
fpRteTrkTrnsCap = _FpRteTrkTrnsCap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 4),
    _FpRteTrkTrnsCap_Type()
)
fpRteTrkTrnsCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkTrnsCap.setStatus("mandatory")
_FpRteTrkTrnsLoad_Type = Integer32
_FpRteTrkTrnsLoad_Object = MibTableColumn
fpRteTrkTrnsLoad = _FpRteTrkTrnsLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 5),
    _FpRteTrkTrnsLoad_Type()
)
fpRteTrkTrnsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkTrnsLoad.setStatus("mandatory")
_FpRteTrkRcvCap_Type = Integer32
_FpRteTrkRcvCap_Object = MibTableColumn
fpRteTrkRcvCap = _FpRteTrkRcvCap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 6),
    _FpRteTrkRcvCap_Type()
)
fpRteTrkRcvCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkRcvCap.setStatus("mandatory")
_FpRteTrkRcvLoad_Type = Integer32
_FpRteTrkRcvLoad_Object = MibTableColumn
fpRteTrkRcvLoad = _FpRteTrkRcvLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 7),
    _FpRteTrkRcvLoad_Type()
)
fpRteTrkRcvLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkRcvLoad.setStatus("mandatory")


class _FpRteTrkOeNdType_Type(Integer32):
    """Custom type fpRteTrkOeNdType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("ndTypeOther", 1),
          ("ndTypeIPX", 2),
          ("ndTypeBPX", 3),
          ("ndTypeIPXAF", 4),
          ("ndTypeAXIS", 5),
          ("ndTypeIGX", 6),
          ("ndTypeIGXAF", 7),
          ("ndType8450", 16))
    )


_FpRteTrkOeNdType_Type.__name__ = "Integer32"
_FpRteTrkOeNdType_Object = MibTableColumn
fpRteTrkOeNdType = _FpRteTrkOeNdType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 8),
    _FpRteTrkOeNdType_Type()
)
fpRteTrkOeNdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkOeNdType.setStatus("mandatory")
_FpRteTrkOeName_Type = DisplayString
_FpRteTrkOeName_Object = MibTableColumn
fpRteTrkOeName = _FpRteTrkOeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 9),
    _FpRteTrkOeName_Type()
)
fpRteTrkOeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkOeName.setStatus("mandatory")
_FpRteTrkOeIpAddr_Type = IpAddress
_FpRteTrkOeIpAddr_Object = MibTableColumn
fpRteTrkOeIpAddr = _FpRteTrkOeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 10),
    _FpRteTrkOeIpAddr_Type()
)
fpRteTrkOeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkOeIpAddr.setStatus("mandatory")
_FpRteTrkOeIfIndex_Type = Integer32
_FpRteTrkOeIfIndex_Object = MibTableColumn
fpRteTrkOeIfIndex = _FpRteTrkOeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 11),
    _FpRteTrkOeIfIndex_Type()
)
fpRteTrkOeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkOeIfIndex.setStatus("mandatory")
_FpRteTrkOeDomain_Type = Integer32
_FpRteTrkOeDomain_Object = MibTableColumn
fpRteTrkOeDomain = _FpRteTrkOeDomain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 12),
    _FpRteTrkOeDomain_Type()
)
fpRteTrkOeDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkOeDomain.setStatus("mandatory")
_FpRteTrkXmitRate_Type = Integer32
_FpRteTrkXmitRate_Object = MibTableColumn
fpRteTrkXmitRate = _FpRteTrkXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 13),
    _FpRteTrkXmitRate_Type()
)
fpRteTrkXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpRteTrkXmitRate.setStatus("mandatory")


class _FpRteTrkPassSync_Type(Integer32):
    """Custom type fpRteTrkPassSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FpRteTrkPassSync_Type.__name__ = "Integer32"
_FpRteTrkPassSync_Object = MibTableColumn
fpRteTrkPassSync = _FpRteTrkPassSync_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 14),
    _FpRteTrkPassSync_Type()
)
fpRteTrkPassSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkPassSync.setStatus("mandatory")


class _FpRteTrkStatRes_Type(Integer32):
    """Custom type fpRteTrkStatRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10666),
    )


_FpRteTrkStatRes_Type.__name__ = "Integer32"
_FpRteTrkStatRes_Object = MibTableColumn
fpRteTrkStatRes = _FpRteTrkStatRes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 15),
    _FpRteTrkStatRes_Type()
)
fpRteTrkStatRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkStatRes.setStatus("mandatory")


class _FpRteTrkLoopClock_Type(Integer32):
    """Custom type fpRteTrkLoopClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FpRteTrkLoopClock_Type.__name__ = "Integer32"
_FpRteTrkLoopClock_Object = MibTableColumn
fpRteTrkLoopClock = _FpRteTrkLoopClock_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 16),
    _FpRteTrkLoopClock_Type()
)
fpRteTrkLoopClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkLoopClock.setStatus("mandatory")


class _FpRteTrkBdataBTxQlen_Type(Integer32):
    """Custom type fpRteTrkBdataBTxQlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_FpRteTrkBdataBTxQlen_Type.__name__ = "Integer32"
_FpRteTrkBdataBTxQlen_Object = MibTableColumn
fpRteTrkBdataBTxQlen = _FpRteTrkBdataBTxQlen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 17),
    _FpRteTrkBdataBTxQlen_Type()
)
fpRteTrkBdataBTxQlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkBdataBTxQlen.setStatus("mandatory")


class _FpRteTrkBdataBTxEfcn_Type(Integer32):
    """Custom type fpRteTrkBdataBTxEfcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_FpRteTrkBdataBTxEfcn_Type.__name__ = "Integer32"
_FpRteTrkBdataBTxEfcn_Object = MibTableColumn
fpRteTrkBdataBTxEfcn = _FpRteTrkBdataBTxEfcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 18),
    _FpRteTrkBdataBTxEfcn_Type()
)
fpRteTrkBdataBTxEfcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkBdataBTxEfcn.setStatus("mandatory")


class _FpRteTrkBdataBTxHiClp_Type(Integer32):
    """Custom type fpRteTrkBdataBTxHiClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FpRteTrkBdataBTxHiClp_Type.__name__ = "Integer32"
_FpRteTrkBdataBTxHiClp_Object = MibTableColumn
fpRteTrkBdataBTxHiClp = _FpRteTrkBdataBTxHiClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 19),
    _FpRteTrkBdataBTxHiClp_Type()
)
fpRteTrkBdataBTxHiClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkBdataBTxHiClp.setStatus("mandatory")


class _FpRteTrkBdataBTxLoClp_Type(Integer32):
    """Custom type fpRteTrkBdataBTxLoClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FpRteTrkBdataBTxLoClp_Type.__name__ = "Integer32"
_FpRteTrkBdataBTxLoClp_Object = MibTableColumn
fpRteTrkBdataBTxLoClp = _FpRteTrkBdataBTxLoClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 20),
    _FpRteTrkBdataBTxLoClp_Type()
)
fpRteTrkBdataBTxLoClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkBdataBTxLoClp.setStatus("mandatory")


class _FpRteTrkLinkType_Type(Integer32):
    """Custom type fpRteTrkLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("terrestrial", 1),
          ("satellite", 2))
    )


_FpRteTrkLinkType_Type.__name__ = "Integer32"
_FpRteTrkLinkType_Object = MibTableColumn
fpRteTrkLinkType = _FpRteTrkLinkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 1, 1, 21),
    _FpRteTrkLinkType_Type()
)
fpRteTrkLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpRteTrkLinkType.setStatus("mandatory")
_AtmTrunks_Object = MibTable
atmTrunks = _AtmTrunks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    atmTrunks.setStatus("mandatory")
_AtmTrkEntry_Object = MibTableRow
atmTrkEntry = _AtmTrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1)
)
atmTrkEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    atmTrkEntry.setStatus("mandatory")


class _AtmTrkStatus_Type(Integer32):
    """Custom type atmTrkStatus based on Integer32"""
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
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("down", 4),
          ("deact", 5))
    )


_AtmTrkStatus_Type.__name__ = "Integer32"
_AtmTrkStatus_Object = MibTableColumn
atmTrkStatus = _AtmTrkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 1),
    _AtmTrkStatus_Type()
)
atmTrkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatus.setStatus("mandatory")


class _AtmTrkAlmEnable_Type(Integer32):
    """Custom type atmTrkAlmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmTrkAlmEnable_Type.__name__ = "Integer32"
_AtmTrkAlmEnable_Object = MibTableColumn
atmTrkAlmEnable = _AtmTrkAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 2),
    _AtmTrkAlmEnable_Type()
)
atmTrkAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkAlmEnable.setStatus("mandatory")


class _AtmTrkComStatus_Type(Integer32):
    """Custom type atmTrkComStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commOK", 1),
          ("commFAIL", 2))
    )


_AtmTrkComStatus_Type.__name__ = "Integer32"
_AtmTrkComStatus_Object = MibTableColumn
atmTrkComStatus = _AtmTrkComStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 3),
    _AtmTrkComStatus_Type()
)
atmTrkComStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkComStatus.setStatus("mandatory")
_AtmTrkRcvRate_Type = Integer32
_AtmTrkRcvRate_Object = MibTableColumn
atmTrkRcvRate = _AtmTrkRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 4),
    _AtmTrkRcvRate_Type()
)
atmTrkRcvRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkRcvRate.setStatus("mandatory")
_AtmTrkTrnsCap_Type = Integer32
_AtmTrkTrnsCap_Object = MibTableColumn
atmTrkTrnsCap = _AtmTrkTrnsCap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 5),
    _AtmTrkTrnsCap_Type()
)
atmTrkTrnsCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkTrnsCap.setStatus("mandatory")
_AtmTrkTrnsLoad_Type = Integer32
_AtmTrkTrnsLoad_Object = MibTableColumn
atmTrkTrnsLoad = _AtmTrkTrnsLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 6),
    _AtmTrkTrnsLoad_Type()
)
atmTrkTrnsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkTrnsLoad.setStatus("mandatory")
_AtmTrkRcvCap_Type = Integer32
_AtmTrkRcvCap_Object = MibTableColumn
atmTrkRcvCap = _AtmTrkRcvCap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 7),
    _AtmTrkRcvCap_Type()
)
atmTrkRcvCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkRcvCap.setStatus("mandatory")
_AtmTrkRcvLoad_Type = Integer32
_AtmTrkRcvLoad_Object = MibTableColumn
atmTrkRcvLoad = _AtmTrkRcvLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 8),
    _AtmTrkRcvLoad_Type()
)
atmTrkRcvLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkRcvLoad.setStatus("mandatory")


class _AtmTrkType_Type(Integer32):
    """Custom type atmTrkType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("trkTypePHY", 1),
          ("trkTypeCBR", 2),
          ("trkTypeVBR", 3),
          ("trkTypeABR", 4),
          ("trkTypeIPXAF", 5),
          ("trkTypeAXISAF", 6),
          ("trkTypeESPAF", 7),
          ("trkTypeIGXAF", 8),
          ("trkTypeVSIAF", 9),
          ("trkTypePARAF", 10))
    )


_AtmTrkType_Type.__name__ = "Integer32"
_AtmTrkType_Object = MibTableColumn
atmTrkType = _AtmTrkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 9),
    _AtmTrkType_Type()
)
atmTrkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkType.setStatus("mandatory")


class _AtmTrkVPI_Type(Integer32):
    """Custom type atmTrkVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmTrkVPI_Type.__name__ = "Integer32"
_AtmTrkVPI_Object = MibTableColumn
atmTrkVPI = _AtmTrkVPI_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 10),
    _AtmTrkVPI_Type()
)
atmTrkVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkVPI.setStatus("mandatory")
_AtmTrkResChans_Type = Integer32
_AtmTrkResChans_Object = MibTableColumn
atmTrkResChans = _AtmTrkResChans_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 11),
    _AtmTrkResChans_Type()
)
atmTrkResChans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkResChans.setStatus("mandatory")
_AtmTrkTrafCls_Type = Integer32
_AtmTrkTrafCls_Object = MibTableColumn
atmTrkTrafCls = _AtmTrkTrafCls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 12),
    _AtmTrkTrafCls_Type()
)
atmTrkTrafCls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkTrafCls.setStatus("mandatory")


class _AtmTrkOeNdType_Type(Integer32):
    """Custom type atmTrkOeNdType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("ndTypeOther", 1),
          ("ndTypeIPX", 2),
          ("ndTypeBPX", 3),
          ("ndTypeIPXAF", 4),
          ("ndTypeAXIS", 5),
          ("ndTypeIGX", 6),
          ("ndTypeIGXAF", 7),
          ("ndTypeESP", 8),
          ("ndTypePAR", 9),
          ("ndType8450", 16))
    )


_AtmTrkOeNdType_Type.__name__ = "Integer32"
_AtmTrkOeNdType_Object = MibTableColumn
atmTrkOeNdType = _AtmTrkOeNdType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 13),
    _AtmTrkOeNdType_Type()
)
atmTrkOeNdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeNdType.setStatus("mandatory")
_AtmTrkOeName_Type = DisplayString
_AtmTrkOeName_Object = MibTableColumn
atmTrkOeName = _AtmTrkOeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 14),
    _AtmTrkOeName_Type()
)
atmTrkOeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeName.setStatus("mandatory")
_AtmTrkOeIpAddr_Type = IpAddress
_AtmTrkOeIpAddr_Object = MibTableColumn
atmTrkOeIpAddr = _AtmTrkOeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 15),
    _AtmTrkOeIpAddr_Type()
)
atmTrkOeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeIpAddr.setStatus("mandatory")
_AtmTrkOeIfIndex_Type = Integer32
_AtmTrkOeIfIndex_Object = MibTableColumn
atmTrkOeIfIndex = _AtmTrkOeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 16),
    _AtmTrkOeIfIndex_Type()
)
atmTrkOeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeIfIndex.setStatus("mandatory")
_AtmTrkOeDomain_Type = Integer32
_AtmTrkOeDomain_Object = MibTableColumn
atmTrkOeDomain = _AtmTrkOeDomain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 17),
    _AtmTrkOeDomain_Type()
)
atmTrkOeDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeDomain.setStatus("mandatory")
_AtmTrkSvcChannels_Type = Integer32
_AtmTrkSvcChannels_Object = MibTableColumn
atmTrkSvcChannels = _AtmTrkSvcChannels_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 18),
    _AtmTrkSvcChannels_Type()
)
atmTrkSvcChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcChannels.setStatus("mandatory")


class _AtmTrkShareLcn_Type(Integer32):
    """Custom type atmTrkShareLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("cardBased", 2))
    )


_AtmTrkShareLcn_Type.__name__ = "Integer32"
_AtmTrkShareLcn_Object = MibTableColumn
atmTrkShareLcn = _AtmTrkShareLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 19),
    _AtmTrkShareLcn_Type()
)
atmTrkShareLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkShareLcn.setStatus("mandatory")
_AtmTrkSvcLcnLow_Type = Integer32
_AtmTrkSvcLcnLow_Object = MibTableColumn
atmTrkSvcLcnLow = _AtmTrkSvcLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 20),
    _AtmTrkSvcLcnLow_Type()
)
atmTrkSvcLcnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcLcnLow.setStatus("mandatory")
_AtmTrkSvcLcnHigh_Type = Integer32
_AtmTrkSvcLcnHigh_Object = MibTableColumn
atmTrkSvcLcnHigh = _AtmTrkSvcLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 21),
    _AtmTrkSvcLcnHigh_Type()
)
atmTrkSvcLcnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcLcnHigh.setStatus("mandatory")
_AtmTrkSvcVpiLow_Type = Integer32
_AtmTrkSvcVpiLow_Object = MibTableColumn
atmTrkSvcVpiLow = _AtmTrkSvcVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 22),
    _AtmTrkSvcVpiLow_Type()
)
atmTrkSvcVpiLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcVpiLow.setStatus("mandatory")
_AtmTrkSvcVpiHigh_Type = Integer32
_AtmTrkSvcVpiHigh_Object = MibTableColumn
atmTrkSvcVpiHigh = _AtmTrkSvcVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 23),
    _AtmTrkSvcVpiHigh_Type()
)
atmTrkSvcVpiHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcVpiHigh.setStatus("mandatory")
_AtmTrkSvcVciLow_Type = Integer32
_AtmTrkSvcVciLow_Object = MibTableColumn
atmTrkSvcVciLow = _AtmTrkSvcVciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 24),
    _AtmTrkSvcVciLow_Type()
)
atmTrkSvcVciLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTrkSvcVciLow.setStatus("deprecated")
_AtmTrkSvcVciHigh_Type = Integer32
_AtmTrkSvcVciHigh_Object = MibTableColumn
atmTrkSvcVciHigh = _AtmTrkSvcVciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 25),
    _AtmTrkSvcVciHigh_Type()
)
atmTrkSvcVciHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTrkSvcVciHigh.setStatus("deprecated")
_AtmTrkSvcQbinBitMap_Type = OctetString
_AtmTrkSvcQbinBitMap_Object = MibTableColumn
atmTrkSvcQbinBitMap = _AtmTrkSvcQbinBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 26),
    _AtmTrkSvcQbinBitMap_Type()
)
atmTrkSvcQbinBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcQbinBitMap.setStatus("mandatory")
_AtmTrkSvcQbinSz_Type = Integer32
_AtmTrkSvcQbinSz_Object = MibTableColumn
atmTrkSvcQbinSz = _AtmTrkSvcQbinSz_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 27),
    _AtmTrkSvcQbinSz_Type()
)
atmTrkSvcQbinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcQbinSz.setStatus("mandatory")
_AtmTrkSvcBw_Type = Integer32
_AtmTrkSvcBw_Object = MibTableColumn
atmTrkSvcBw = _AtmTrkSvcBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 28),
    _AtmTrkSvcBw_Type()
)
atmTrkSvcBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcBw.setStatus("mandatory")


class _AtmTrkSvcInUse_Type(Integer32):
    """Custom type atmTrkSvcInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_AtmTrkSvcInUse_Type.__name__ = "Integer32"
_AtmTrkSvcInUse_Object = MibTableColumn
atmTrkSvcInUse = _AtmTrkSvcInUse_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 29),
    _AtmTrkSvcInUse_Type()
)
atmTrkSvcInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkSvcInUse.setStatus("mandatory")
_AtmTrkXmitRate_Type = Integer32
_AtmTrkXmitRate_Object = MibTableColumn
atmTrkXmitRate = _AtmTrkXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 30),
    _AtmTrkXmitRate_Type()
)
atmTrkXmitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkXmitRate.setStatus("mandatory")


class _AtmTrkPassSync_Type(Integer32):
    """Custom type atmTrkPassSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtmTrkPassSync_Type.__name__ = "Integer32"
_AtmTrkPassSync_Object = MibTableColumn
atmTrkPassSync = _AtmTrkPassSync_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 31),
    _AtmTrkPassSync_Type()
)
atmTrkPassSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkPassSync.setStatus("mandatory")
_AtmTrkStatRes_Type = Integer32
_AtmTrkStatRes_Object = MibTableColumn
atmTrkStatRes = _AtmTrkStatRes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 32),
    _AtmTrkStatRes_Type()
)
atmTrkStatRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkStatRes.setStatus("mandatory")


class _AtmTrkLoopClock_Type(Integer32):
    """Custom type atmTrkLoopClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtmTrkLoopClock_Type.__name__ = "Integer32"
_AtmTrkLoopClock_Object = MibTableColumn
atmTrkLoopClock = _AtmTrkLoopClock_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 33),
    _AtmTrkLoopClock_Type()
)
atmTrkLoopClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkLoopClock.setStatus("mandatory")


class _AtmTrkBdataBTxQlen_Type(Integer32):
    """Custom type atmTrkBdataBTxQlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBTxQlen_Type.__name__ = "Integer32"
_AtmTrkBdataBTxQlen_Object = MibTableColumn
atmTrkBdataBTxQlen = _AtmTrkBdataBTxQlen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 34),
    _AtmTrkBdataBTxQlen_Type()
)
atmTrkBdataBTxQlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxQlen.setStatus("mandatory")


class _AtmTrkBdataBRxQlen_Type(Integer32):
    """Custom type atmTrkBdataBRxQlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBRxQlen_Type.__name__ = "Integer32"
_AtmTrkBdataBRxQlen_Object = MibTableColumn
atmTrkBdataBRxQlen = _AtmTrkBdataBRxQlen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 35),
    _AtmTrkBdataBRxQlen_Type()
)
atmTrkBdataBRxQlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxQlen.setStatus("mandatory")


class _AtmTrkBdataBTxEfcn_Type(Integer32):
    """Custom type atmTrkBdataBTxEfcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBTxEfcn_Type.__name__ = "Integer32"
_AtmTrkBdataBTxEfcn_Object = MibTableColumn
atmTrkBdataBTxEfcn = _AtmTrkBdataBTxEfcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 36),
    _AtmTrkBdataBTxEfcn_Type()
)
atmTrkBdataBTxEfcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxEfcn.setStatus("mandatory")


class _AtmTrkBdataBRxEfcn_Type(Integer32):
    """Custom type atmTrkBdataBRxEfcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBRxEfcn_Type.__name__ = "Integer32"
_AtmTrkBdataBRxEfcn_Object = MibTableColumn
atmTrkBdataBRxEfcn = _AtmTrkBdataBRxEfcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 37),
    _AtmTrkBdataBRxEfcn_Type()
)
atmTrkBdataBRxEfcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxEfcn.setStatus("mandatory")


class _AtmTrkBdataBTxHiClp_Type(Integer32):
    """Custom type atmTrkBdataBTxHiClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBTxHiClp_Type.__name__ = "Integer32"
_AtmTrkBdataBTxHiClp_Object = MibTableColumn
atmTrkBdataBTxHiClp = _AtmTrkBdataBTxHiClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 38),
    _AtmTrkBdataBTxHiClp_Type()
)
atmTrkBdataBTxHiClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxHiClp.setStatus("mandatory")


class _AtmTrkBdataBRxHiClp_Type(Integer32):
    """Custom type atmTrkBdataBRxHiClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBRxHiClp_Type.__name__ = "Integer32"
_AtmTrkBdataBRxHiClp_Object = MibTableColumn
atmTrkBdataBRxHiClp = _AtmTrkBdataBRxHiClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 39),
    _AtmTrkBdataBRxHiClp_Type()
)
atmTrkBdataBRxHiClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxHiClp.setStatus("mandatory")


class _AtmTrkBdataBTxLoClp_Type(Integer32):
    """Custom type atmTrkBdataBTxLoClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBTxLoClp_Type.__name__ = "Integer32"
_AtmTrkBdataBTxLoClp_Object = MibTableColumn
atmTrkBdataBTxLoClp = _AtmTrkBdataBTxLoClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 40),
    _AtmTrkBdataBTxLoClp_Type()
)
atmTrkBdataBTxLoClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxLoClp.setStatus("mandatory")


class _AtmTrkBdataBRxLoClp_Type(Integer32):
    """Custom type atmTrkBdataBRxLoClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBRxLoClp_Type.__name__ = "Integer32"
_AtmTrkBdataBRxLoClp_Object = MibTableColumn
atmTrkBdataBRxLoClp = _AtmTrkBdataBRxLoClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 41),
    _AtmTrkBdataBRxLoClp_Type()
)
atmTrkBdataBRxLoClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxLoClp.setStatus("mandatory")


class _AtmTrkMaxChanPort_Type(Integer32):
    """Custom type atmTrkMaxChanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16320),
    )


_AtmTrkMaxChanPort_Type.__name__ = "Integer32"
_AtmTrkMaxChanPort_Object = MibTableColumn
atmTrkMaxChanPort = _AtmTrkMaxChanPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 42),
    _AtmTrkMaxChanPort_Type()
)
atmTrkMaxChanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkMaxChanPort.setStatus("mandatory")


class _AtmTrkLinkType_Type(Integer32):
    """Custom type atmTrkLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("terrestrial", 1),
          ("satellite", 2))
    )


_AtmTrkLinkType_Type.__name__ = "Integer32"
_AtmTrkLinkType_Object = MibTableColumn
atmTrkLinkType = _AtmTrkLinkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 43),
    _AtmTrkLinkType_Type()
)
atmTrkLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkLinkType.setStatus("mandatory")


class _AtmTrkDerouteDelayTimer_Type(Integer32):
    """Custom type atmTrkDerouteDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AtmTrkDerouteDelayTimer_Type.__name__ = "Integer32"
_AtmTrkDerouteDelayTimer_Object = MibTableColumn
atmTrkDerouteDelayTimer = _AtmTrkDerouteDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 44),
    _AtmTrkDerouteDelayTimer_Type()
)
atmTrkDerouteDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkDerouteDelayTimer.setStatus("mandatory")
_AtmTrkGtwyChCount_Type = Integer32
_AtmTrkGtwyChCount_Object = MibTableColumn
atmTrkGtwyChCount = _AtmTrkGtwyChCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 45),
    _AtmTrkGtwyChCount_Type()
)
atmTrkGtwyChCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkGtwyChCount.setStatus("mandatory")


class _AtmTrkRetainedLinks_Type(Integer32):
    """Custom type atmTrkRetainedLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmTrkRetainedLinks_Type.__name__ = "Integer32"
_AtmTrkRetainedLinks_Object = MibTableColumn
atmTrkRetainedLinks = _AtmTrkRetainedLinks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 46),
    _AtmTrkRetainedLinks_Type()
)
atmTrkRetainedLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkRetainedLinks.setStatus("mandatory")
_AtmTrkImaWindowSize_Type = Integer32
_AtmTrkImaWindowSize_Object = MibTableColumn
atmTrkImaWindowSize = _AtmTrkImaWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 47),
    _AtmTrkImaWindowSize_Type()
)
atmTrkImaWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkImaWindowSize.setStatus("mandatory")
_AtmTrkImaTrnsCnts_Type = Integer32
_AtmTrkImaTrnsCnts_Object = MibTableColumn
atmTrkImaTrnsCnts = _AtmTrkImaTrnsCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 48),
    _AtmTrkImaTrnsCnts_Type()
)
atmTrkImaTrnsCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkImaTrnsCnts.setStatus("mandatory")
_AtmTrkImaReenableTimer_Type = Integer32
_AtmTrkImaReenableTimer_Object = MibTableColumn
atmTrkImaReenableTimer = _AtmTrkImaReenableTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 49),
    _AtmTrkImaReenableTimer_Type()
)
atmTrkImaReenableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkImaReenableTimer.setStatus("mandatory")
_FpTrunkStatsTable_Object = MibTable
fpTrunkStatsTable = _FpTrunkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3)
)
if mibBuilder.loadTexts:
    fpTrunkStatsTable.setStatus("mandatory")
_FpTrkStatsEntry_Object = MibTableRow
fpTrkStatsEntry = _FpTrkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1)
)
fpTrkStatsEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    fpTrkStatsEntry.setStatus("mandatory")
_FpTrkStatsPktCrcs_Type = Counter32
_FpTrkStatsPktCrcs_Object = MibTableColumn
fpTrkStatsPktCrcs = _FpTrkStatsPktCrcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 1),
    _FpTrkStatsPktCrcs_Type()
)
fpTrkStatsPktCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsPktCrcs.setStatus("mandatory")
_FpTrkStatsPktOofs_Type = Counter32
_FpTrkStatsPktOofs_Object = MibTableColumn
fpTrkStatsPktOofs = _FpTrkStatsPktOofs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 2),
    _FpTrkStatsPktOofs_Type()
)
fpTrkStatsPktOofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsPktOofs.setStatus("mandatory")
_FpTrkStatsTxVoPktDrps_Type = Counter32
_FpTrkStatsTxVoPktDrps_Object = MibTableColumn
fpTrkStatsTxVoPktDrps = _FpTrkStatsTxVoPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 3),
    _FpTrkStatsTxVoPktDrps_Type()
)
fpTrkStatsTxVoPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTxVoPktDrps.setStatus("mandatory")
_FpTrkStatsTxTsPktDrps_Type = Counter32
_FpTrkStatsTxTsPktDrps_Object = MibTableColumn
fpTrkStatsTxTsPktDrps = _FpTrkStatsTxTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 4),
    _FpTrkStatsTxTsPktDrps_Type()
)
fpTrkStatsTxTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTxTsPktDrps.setStatus("mandatory")
_FpTrkStatsTxNonTsPktDrps_Type = Counter32
_FpTrkStatsTxNonTsPktDrps_Object = MibTableColumn
fpTrkStatsTxNonTsPktDrps = _FpTrkStatsTxNonTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 5),
    _FpTrkStatsTxNonTsPktDrps_Type()
)
fpTrkStatsTxNonTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTxNonTsPktDrps.setStatus("mandatory")
_FpTrkStatsTxHiPrioPktDrps_Type = Counter32
_FpTrkStatsTxHiPrioPktDrps_Object = MibTableColumn
fpTrkStatsTxHiPrioPktDrps = _FpTrkStatsTxHiPrioPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 6),
    _FpTrkStatsTxHiPrioPktDrps_Type()
)
fpTrkStatsTxHiPrioPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTxHiPrioPktDrps.setStatus("mandatory")
_FpTrkStatsTxBdataAPktDrps_Type = Counter32
_FpTrkStatsTxBdataAPktDrps_Object = MibTableColumn
fpTrkStatsTxBdataAPktDrps = _FpTrkStatsTxBdataAPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 7),
    _FpTrkStatsTxBdataAPktDrps_Type()
)
fpTrkStatsTxBdataAPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTxBdataAPktDrps.setStatus("mandatory")
_FpTrkStatsTxBdataBPktDrps_Type = Counter32
_FpTrkStatsTxBdataBPktDrps_Object = MibTableColumn
fpTrkStatsTxBdataBPktDrps = _FpTrkStatsTxBdataBPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 8),
    _FpTrkStatsTxBdataBPktDrps_Type()
)
fpTrkStatsTxBdataBPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTxBdataBPktDrps.setStatus("mandatory")
_FpTrkStatsTotalPktsTxtoLns_Type = Counter32
_FpTrkStatsTotalPktsTxtoLns_Object = MibTableColumn
fpTrkStatsTotalPktsTxtoLns = _FpTrkStatsTotalPktsTxtoLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 3, 1, 9),
    _FpTrkStatsTotalPktsTxtoLns_Type()
)
fpTrkStatsTotalPktsTxtoLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTrkStatsTotalPktsTxtoLns.setStatus("mandatory")
_AtmTrunkStatsTable_Object = MibTable
atmTrunkStatsTable = _AtmTrunkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4)
)
if mibBuilder.loadTexts:
    atmTrunkStatsTable.setStatus("mandatory")
_AtmTrkStatsEntry_Object = MibTableRow
atmTrkStatsEntry = _AtmTrkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1)
)
atmTrkStatsEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    atmTrkStatsEntry.setStatus("mandatory")
_AtmTrkStatsTxVoPktDrps_Type = Counter32
_AtmTrkStatsTxVoPktDrps_Object = MibTableColumn
atmTrkStatsTxVoPktDrps = _AtmTrkStatsTxVoPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 1),
    _AtmTrkStatsTxVoPktDrps_Type()
)
atmTrkStatsTxVoPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxVoPktDrps.setStatus("mandatory")
_AtmTrkStatsTxTsPktDrps_Type = Counter32
_AtmTrkStatsTxTsPktDrps_Object = MibTableColumn
atmTrkStatsTxTsPktDrps = _AtmTrkStatsTxTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 2),
    _AtmTrkStatsTxTsPktDrps_Type()
)
atmTrkStatsTxTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxTsPktDrps.setStatus("mandatory")
_AtmTrkStatsTxNonTsPktDrps_Type = Counter32
_AtmTrkStatsTxNonTsPktDrps_Object = MibTableColumn
atmTrkStatsTxNonTsPktDrps = _AtmTrkStatsTxNonTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 3),
    _AtmTrkStatsTxNonTsPktDrps_Type()
)
atmTrkStatsTxNonTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxNonTsPktDrps.setStatus("mandatory")
_AtmTrkStatsTxHiPrioPktDrps_Type = Counter32
_AtmTrkStatsTxHiPrioPktDrps_Object = MibTableColumn
atmTrkStatsTxHiPrioPktDrps = _AtmTrkStatsTxHiPrioPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 4),
    _AtmTrkStatsTxHiPrioPktDrps_Type()
)
atmTrkStatsTxHiPrioPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxHiPrioPktDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataAPktDrps_Type = Counter32
_AtmTrkStatsTxBdataAPktDrps_Object = MibTableColumn
atmTrkStatsTxBdataAPktDrps = _AtmTrkStatsTxBdataAPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 5),
    _AtmTrkStatsTxBdataAPktDrps_Type()
)
atmTrkStatsTxBdataAPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataAPktDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataBPktDrps_Type = Counter32
_AtmTrkStatsTxBdataBPktDrps_Object = MibTableColumn
atmTrkStatsTxBdataBPktDrps = _AtmTrkStatsTxBdataBPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 6),
    _AtmTrkStatsTxBdataBPktDrps_Type()
)
atmTrkStatsTxBdataBPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataBPktDrps.setStatus("mandatory")
_AtmTrkStatsRxVoPktDrps_Type = Counter32
_AtmTrkStatsRxVoPktDrps_Object = MibTableColumn
atmTrkStatsRxVoPktDrps = _AtmTrkStatsRxVoPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 7),
    _AtmTrkStatsRxVoPktDrps_Type()
)
atmTrkStatsRxVoPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxVoPktDrps.setStatus("mandatory")
_AtmTrkStatsRxTsPktDrps_Type = Counter32
_AtmTrkStatsRxTsPktDrps_Object = MibTableColumn
atmTrkStatsRxTsPktDrps = _AtmTrkStatsRxTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 8),
    _AtmTrkStatsRxTsPktDrps_Type()
)
atmTrkStatsRxTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxTsPktDrps.setStatus("mandatory")
_AtmTrkStatsRxNonTsPktDrps_Type = Counter32
_AtmTrkStatsRxNonTsPktDrps_Object = MibTableColumn
atmTrkStatsRxNonTsPktDrps = _AtmTrkStatsRxNonTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 9),
    _AtmTrkStatsRxNonTsPktDrps_Type()
)
atmTrkStatsRxNonTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxNonTsPktDrps.setStatus("mandatory")
_AtmTrkStatsRxHiPrioPktDrps_Type = Counter32
_AtmTrkStatsRxHiPrioPktDrps_Object = MibTableColumn
atmTrkStatsRxHiPrioPktDrps = _AtmTrkStatsRxHiPrioPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 10),
    _AtmTrkStatsRxHiPrioPktDrps_Type()
)
atmTrkStatsRxHiPrioPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxHiPrioPktDrps.setStatus("mandatory")
_AtmTrkStatsRxBdataAPktDrps_Type = Counter32
_AtmTrkStatsRxBdataAPktDrps_Object = MibTableColumn
atmTrkStatsRxBdataAPktDrps = _AtmTrkStatsRxBdataAPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 11),
    _AtmTrkStatsRxBdataAPktDrps_Type()
)
atmTrkStatsRxBdataAPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxBdataAPktDrps.setStatus("mandatory")
_AtmTrkStatsRxBdataBPktDrps_Type = Counter32
_AtmTrkStatsRxBdataBPktDrps_Object = MibTableColumn
atmTrkStatsRxBdataBPktDrps = _AtmTrkStatsRxBdataBPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 12),
    _AtmTrkStatsRxBdataBPktDrps_Type()
)
atmTrkStatsRxBdataBPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxBdataBPktDrps.setStatus("mandatory")
_AtmTrkStatsSpacerPktsDrps_Type = Counter32
_AtmTrkStatsSpacerPktsDrps_Object = MibTableColumn
atmTrkStatsSpacerPktsDrps = _AtmTrkStatsSpacerPktsDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 13),
    _AtmTrkStatsSpacerPktsDrps_Type()
)
atmTrkStatsSpacerPktsDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsSpacerPktsDrps.setStatus("mandatory")
_AtmTrkStatsTotalPktsTxtoLns_Type = Counter32
_AtmTrkStatsTotalPktsTxtoLns_Object = MibTableColumn
atmTrkStatsTotalPktsTxtoLns = _AtmTrkStatsTotalPktsTxtoLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 14),
    _AtmTrkStatsTotalPktsTxtoLns_Type()
)
atmTrkStatsTotalPktsTxtoLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalPktsTxtoLns.setStatus("mandatory")
_AtmTrkStatsTotalPktsRxFromLns_Type = Counter32
_AtmTrkStatsTotalPktsRxFromLns_Object = MibTableColumn
atmTrkStatsTotalPktsRxFromLns = _AtmTrkStatsTotalPktsRxFromLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 15),
    _AtmTrkStatsTotalPktsRxFromLns_Type()
)
atmTrkStatsTotalPktsRxFromLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalPktsRxFromLns.setStatus("mandatory")
_AtmTrkStatsTxVoCellDrps_Type = Counter32
_AtmTrkStatsTxVoCellDrps_Object = MibTableColumn
atmTrkStatsTxVoCellDrps = _AtmTrkStatsTxVoCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 16),
    _AtmTrkStatsTxVoCellDrps_Type()
)
atmTrkStatsTxVoCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxVoCellDrps.setStatus("mandatory")
_AtmTrkStatsTxTsCellDrps_Type = Counter32
_AtmTrkStatsTxTsCellDrps_Object = MibTableColumn
atmTrkStatsTxTsCellDrps = _AtmTrkStatsTxTsCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 17),
    _AtmTrkStatsTxTsCellDrps_Type()
)
atmTrkStatsTxTsCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxTsCellDrps.setStatus("mandatory")
_AtmTrkStatsTxNonTsCellDrps_Type = Counter32
_AtmTrkStatsTxNonTsCellDrps_Object = MibTableColumn
atmTrkStatsTxNonTsCellDrps = _AtmTrkStatsTxNonTsCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 18),
    _AtmTrkStatsTxNonTsCellDrps_Type()
)
atmTrkStatsTxNonTsCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxNonTsCellDrps.setStatus("mandatory")
_AtmTrkStatsTxHiPrioCellDrps_Type = Counter32
_AtmTrkStatsTxHiPrioCellDrps_Object = MibTableColumn
atmTrkStatsTxHiPrioCellDrps = _AtmTrkStatsTxHiPrioCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 19),
    _AtmTrkStatsTxHiPrioCellDrps_Type()
)
atmTrkStatsTxHiPrioCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxHiPrioCellDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataACellDrps_Type = Counter32
_AtmTrkStatsTxBdataACellDrps_Object = MibTableColumn
atmTrkStatsTxBdataACellDrps = _AtmTrkStatsTxBdataACellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 20),
    _AtmTrkStatsTxBdataACellDrps_Type()
)
atmTrkStatsTxBdataACellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataACellDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataBCellDrps_Type = Counter32
_AtmTrkStatsTxBdataBCellDrps_Object = MibTableColumn
atmTrkStatsTxBdataBCellDrps = _AtmTrkStatsTxBdataBCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 21),
    _AtmTrkStatsTxBdataBCellDrps_Type()
)
atmTrkStatsTxBdataBCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataBCellDrps.setStatus("mandatory")
_AtmTrkStatsTxCbrCellDrps_Type = Counter32
_AtmTrkStatsTxCbrCellDrps_Object = MibTableColumn
atmTrkStatsTxCbrCellDrps = _AtmTrkStatsTxCbrCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 22),
    _AtmTrkStatsTxCbrCellDrps_Type()
)
atmTrkStatsTxCbrCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxCbrCellDrps.setStatus("mandatory")
_AtmTrkStatsTxVbrCellDrps_Type = Counter32
_AtmTrkStatsTxVbrCellDrps_Object = MibTableColumn
atmTrkStatsTxVbrCellDrps = _AtmTrkStatsTxVbrCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 23),
    _AtmTrkStatsTxVbrCellDrps_Type()
)
atmTrkStatsTxVbrCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxVbrCellDrps.setStatus("mandatory")
_AtmTrkStatsTxAbrCellDrps_Type = Counter32
_AtmTrkStatsTxAbrCellDrps_Object = MibTableColumn
atmTrkStatsTxAbrCellDrps = _AtmTrkStatsTxAbrCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 24),
    _AtmTrkStatsTxAbrCellDrps_Type()
)
atmTrkStatsTxAbrCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxAbrCellDrps.setStatus("mandatory")
_AtmTrkStatsTotalCellsTxtoLns_Type = Counter32
_AtmTrkStatsTotalCellsTxtoLns_Object = MibTableColumn
atmTrkStatsTotalCellsTxtoLns = _AtmTrkStatsTotalCellsTxtoLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 25),
    _AtmTrkStatsTotalCellsTxtoLns_Type()
)
atmTrkStatsTotalCellsTxtoLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalCellsTxtoLns.setStatus("mandatory")
_AtmTrkStatsTotalCellsRxFromPorts_Type = Counter32
_AtmTrkStatsTotalCellsRxFromPorts_Object = MibTableColumn
atmTrkStatsTotalCellsRxFromPorts = _AtmTrkStatsTotalCellsRxFromPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 26),
    _AtmTrkStatsTotalCellsRxFromPorts_Type()
)
atmTrkStatsTotalCellsRxFromPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalCellsRxFromPorts.setStatus("mandatory")
_LineServiceObjects_ObjectIdentity = ObjectIdentity
lineServiceObjects = _LineServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5)
)
_LineChanTable_Object = MibTable
lineChanTable = _LineChanTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lineChanTable.setStatus("mandatory")
_LineChanEntry_Object = MibTableRow
lineChanEntry = _LineChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1)
)
lineChanEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
    (0, "STRATACOM-MIB", "lineChanChannelIndex"),
)
if mibBuilder.loadTexts:
    lineChanEntry.setStatus("mandatory")


class _LineChanChannelIndex_Type(Integer32):
    """Custom type lineChanChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LineChanChannelIndex_Type.__name__ = "Integer32"
_LineChanChannelIndex_Object = MibTableColumn
lineChanChannelIndex = _LineChanChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 1),
    _LineChanChannelIndex_Type()
)
lineChanChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineChanChannelIndex.setStatus("mandatory")
_LineChanEndptPtr_Type = ObjectIdentifier
_LineChanEndptPtr_Object = MibTableColumn
lineChanEndptPtr = _LineChanEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 2),
    _LineChanEndptPtr_Type()
)
lineChanEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineChanEndptPtr.setStatus("mandatory")


class _LineChanIfType_Type(Integer32):
    """Custom type lineChanIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1", 2),
          ("e1", 3))
    )


_LineChanIfType_Type.__name__ = "Integer32"
_LineChanIfType_Object = MibTableColumn
lineChanIfType = _LineChanIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 3),
    _LineChanIfType_Type()
)
lineChanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineChanIfType.setStatus("mandatory")


class _LineChanAdapVoice_Type(Integer32):
    """Custom type lineChanAdapVoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_LineChanAdapVoice_Type.__name__ = "Integer32"
_LineChanAdapVoice_Object = MibTableColumn
lineChanAdapVoice = _LineChanAdapVoice_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 4),
    _LineChanAdapVoice_Type()
)
lineChanAdapVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanAdapVoice.setStatus("mandatory")


class _LineChanDialType_Type(Integer32):
    """Custom type lineChanDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("pulse", 2),
          ("userConfigured", 3))
    )


_LineChanDialType_Type.__name__ = "Integer32"
_LineChanDialType_Object = MibTableColumn
lineChanDialType = _LineChanDialType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 5),
    _LineChanDialType_Type()
)
lineChanDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanDialType.setStatus("mandatory")


class _LineChanDtSignallingDelay_Type(Integer32):
    """Custom type lineChanDtSignallingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 96),
    )


_LineChanDtSignallingDelay_Type.__name__ = "Integer32"
_LineChanDtSignallingDelay_Object = MibTableColumn
lineChanDtSignallingDelay = _LineChanDtSignallingDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 6),
    _LineChanDtSignallingDelay_Type()
)
lineChanDtSignallingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanDtSignallingDelay.setStatus("mandatory")


class _LineChanDtMinWink_Type(Integer32):
    """Custom type lineChanDtMinWink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 300),
    )


_LineChanDtMinWink_Type.__name__ = "Integer32"
_LineChanDtMinWink_Object = MibTableColumn
lineChanDtMinWink = _LineChanDtMinWink_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 7),
    _LineChanDtMinWink_Type()
)
lineChanDtMinWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanDtMinWink.setStatus("mandatory")


class _LineChanDtPlayOutDelay_Type(Integer32):
    """Custom type lineChanDtPlayOutDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_LineChanDtPlayOutDelay_Type.__name__ = "Integer32"
_LineChanDtPlayOutDelay_Object = MibTableColumn
lineChanDtPlayOutDelay = _LineChanDtPlayOutDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 8),
    _LineChanDtPlayOutDelay_Type()
)
lineChanDtPlayOutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanDtPlayOutDelay.setStatus("mandatory")


class _LineChanRecvSigABit_Type(Integer32):
    """Custom type lineChanRecvSigABit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanRecvSigABit_Type.__name__ = "Integer32"
_LineChanRecvSigABit_Object = MibTableColumn
lineChanRecvSigABit = _LineChanRecvSigABit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 9),
    _LineChanRecvSigABit_Type()
)
lineChanRecvSigABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanRecvSigABit.setStatus("mandatory")


class _LineChanRecvSigBBit_Type(Integer32):
    """Custom type lineChanRecvSigBBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanRecvSigBBit_Type.__name__ = "Integer32"
_LineChanRecvSigBBit_Object = MibTableColumn
lineChanRecvSigBBit = _LineChanRecvSigBBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 10),
    _LineChanRecvSigBBit_Type()
)
lineChanRecvSigBBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanRecvSigBBit.setStatus("mandatory")


class _LineChanRecvSigCBit_Type(Integer32):
    """Custom type lineChanRecvSigCBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanRecvSigCBit_Type.__name__ = "Integer32"
_LineChanRecvSigCBit_Object = MibTableColumn
lineChanRecvSigCBit = _LineChanRecvSigCBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 11),
    _LineChanRecvSigCBit_Type()
)
lineChanRecvSigCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanRecvSigCBit.setStatus("mandatory")


class _LineChanRecvSigDBit_Type(Integer32):
    """Custom type lineChanRecvSigDBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanRecvSigDBit_Type.__name__ = "Integer32"
_LineChanRecvSigDBit_Object = MibTableColumn
lineChanRecvSigDBit = _LineChanRecvSigDBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 12),
    _LineChanRecvSigDBit_Type()
)
lineChanRecvSigDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanRecvSigDBit.setStatus("mandatory")


class _LineChanXmitSigABit_Type(Integer32):
    """Custom type lineChanXmitSigABit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanXmitSigABit_Type.__name__ = "Integer32"
_LineChanXmitSigABit_Object = MibTableColumn
lineChanXmitSigABit = _LineChanXmitSigABit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 13),
    _LineChanXmitSigABit_Type()
)
lineChanXmitSigABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanXmitSigABit.setStatus("mandatory")


class _LineChanXmitSigBBit_Type(Integer32):
    """Custom type lineChanXmitSigBBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanXmitSigBBit_Type.__name__ = "Integer32"
_LineChanXmitSigBBit_Object = MibTableColumn
lineChanXmitSigBBit = _LineChanXmitSigBBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 14),
    _LineChanXmitSigBBit_Type()
)
lineChanXmitSigBBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanXmitSigBBit.setStatus("mandatory")


class _LineChanXmitSigCBit_Type(Integer32):
    """Custom type lineChanXmitSigCBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanXmitSigCBit_Type.__name__ = "Integer32"
_LineChanXmitSigCBit_Object = MibTableColumn
lineChanXmitSigCBit = _LineChanXmitSigCBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 15),
    _LineChanXmitSigCBit_Type()
)
lineChanXmitSigCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanXmitSigCBit.setStatus("mandatory")


class _LineChanXmitSigDBit_Type(Integer32):
    """Custom type lineChanXmitSigDBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("xmitTransparent", 3),
          ("donotXmit", 4),
          ("revSigBit", 5))
    )


_LineChanXmitSigDBit_Type.__name__ = "Integer32"
_LineChanXmitSigDBit_Object = MibTableColumn
lineChanXmitSigDBit = _LineChanXmitSigDBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 16),
    _LineChanXmitSigDBit_Type()
)
lineChanXmitSigDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanXmitSigDBit.setStatus("mandatory")


class _LineChanIfTypeName_Type(Integer32):
    """Custom type lineChanIfTypeName based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("userConfig", 1),
          ("unConfig", 2),
          ("noSig", 3),
          ("forceSig", 4),
          ("twoWireENM", 5),
          ("fourWireENM", 6),
          ("fXO", 7),
          ("fXSGS", 8),
          ("fXSLS", 9),
          ("dP0", 10),
          ("dPT", 11),
          ("rP0", 12),
          ("rPT", 13),
          ("sDP0", 14),
          ("dX", 15),
          ("eT0", 16),
          ("pLAR", 17),
          ("pLR", 18),
          ("rD", 19),
          ("r1", 20),
          ("sSDC5A", 21),
          ("r2Backward", 22),
          ("r2Forward", 23))
    )


_LineChanIfTypeName_Type.__name__ = "Integer32"
_LineChanIfTypeName_Object = MibTableColumn
lineChanIfTypeName = _LineChanIfTypeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 17),
    _LineChanIfTypeName_Type()
)
lineChanIfTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanIfTypeName.setStatus("mandatory")


class _LineChanIfOnhkABit_Type(Integer32):
    """Custom type lineChanIfOnhkABit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("donotCare", 3),
          ("unKnown", 4),
          ("notUsed", 5))
    )


_LineChanIfOnhkABit_Type.__name__ = "Integer32"
_LineChanIfOnhkABit_Object = MibTableColumn
lineChanIfOnhkABit = _LineChanIfOnhkABit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 18),
    _LineChanIfOnhkABit_Type()
)
lineChanIfOnhkABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanIfOnhkABit.setStatus("mandatory")


class _LineChanIfOnhkBBit_Type(Integer32):
    """Custom type lineChanIfOnhkBBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("donotCare", 3),
          ("unKnown", 4),
          ("notUsed", 5))
    )


_LineChanIfOnhkBBit_Type.__name__ = "Integer32"
_LineChanIfOnhkBBit_Object = MibTableColumn
lineChanIfOnhkBBit = _LineChanIfOnhkBBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 19),
    _LineChanIfOnhkBBit_Type()
)
lineChanIfOnhkBBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanIfOnhkBBit.setStatus("mandatory")


class _LineChanIfOnhkCBit_Type(Integer32):
    """Custom type lineChanIfOnhkCBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("donotCare", 3),
          ("unKnown", 4),
          ("notUsed", 5))
    )


_LineChanIfOnhkCBit_Type.__name__ = "Integer32"
_LineChanIfOnhkCBit_Object = MibTableColumn
lineChanIfOnhkCBit = _LineChanIfOnhkCBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 20),
    _LineChanIfOnhkCBit_Type()
)
lineChanIfOnhkCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanIfOnhkCBit.setStatus("mandatory")


class _LineChanIfOnhkDBit_Type(Integer32):
    """Custom type lineChanIfOnhkDBit based on Integer32"""
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
        *(("zero", 1),
          ("one", 2),
          ("donotCare", 3),
          ("unKnown", 4),
          ("notUsed", 5))
    )


_LineChanIfOnhkDBit_Type.__name__ = "Integer32"
_LineChanIfOnhkDBit_Object = MibTableColumn
lineChanIfOnhkDBit = _LineChanIfOnhkDBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 21),
    _LineChanIfOnhkDBit_Type()
)
lineChanIfOnhkDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanIfOnhkDBit.setStatus("mandatory")


class _LineChanIfCondIndex_Type(Integer32):
    """Custom type lineChanIfCondIndex based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6))
    )


_LineChanIfCondIndex_Type.__name__ = "Integer32"
_LineChanIfCondIndex_Object = MibTableColumn
lineChanIfCondIndex = _LineChanIfCondIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 22),
    _LineChanIfCondIndex_Type()
)
lineChanIfCondIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanIfCondIndex.setStatus("mandatory")


class _LineChanEchoCancel_Type(Integer32):
    """Custom type lineChanEchoCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LineChanEchoCancel_Type.__name__ = "Integer32"
_LineChanEchoCancel_Object = MibTableColumn
lineChanEchoCancel = _LineChanEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 23),
    _LineChanEchoCancel_Type()
)
lineChanEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoCancel.setStatus("mandatory")


class _LineChanEchoRtnLoss_Type(Integer32):
    """Custom type lineChanEchoRtnLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_LineChanEchoRtnLoss_Type.__name__ = "Integer32"
_LineChanEchoRtnLoss_Object = MibTableColumn
lineChanEchoRtnLoss = _LineChanEchoRtnLoss_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 24),
    _LineChanEchoRtnLoss_Type()
)
lineChanEchoRtnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoRtnLoss.setStatus("mandatory")


class _LineChanEchoTone_Type(Integer32):
    """Custom type lineChanEchoTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LineChanEchoTone_Type.__name__ = "Integer32"
_LineChanEchoTone_Object = MibTableColumn
lineChanEchoTone = _LineChanEchoTone_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 25),
    _LineChanEchoTone_Type()
)
lineChanEchoTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoTone.setStatus("mandatory")


class _LineChanEchoConv_Type(Integer32):
    """Custom type lineChanEchoConv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LineChanEchoConv_Type.__name__ = "Integer32"
_LineChanEchoConv_Object = MibTableColumn
lineChanEchoConv = _LineChanEchoConv_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 26),
    _LineChanEchoConv_Type()
)
lineChanEchoConv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoConv.setStatus("mandatory")


class _LineChanEchoNlp_Type(Integer32):
    """Custom type lineChanEchoNlp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LineChanEchoNlp_Type.__name__ = "Integer32"
_LineChanEchoNlp_Object = MibTableColumn
lineChanEchoNlp = _LineChanEchoNlp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 27),
    _LineChanEchoNlp_Type()
)
lineChanEchoNlp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoNlp.setStatus("mandatory")


class _LineChanInGain_Type(Integer32):
    """Custom type lineChanInGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_LineChanInGain_Type.__name__ = "Integer32"
_LineChanInGain_Object = MibTableColumn
lineChanInGain = _LineChanInGain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 28),
    _LineChanInGain_Type()
)
lineChanInGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanInGain.setStatus("mandatory")


class _LineChanOutGain_Type(Integer32):
    """Custom type lineChanOutGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_LineChanOutGain_Type.__name__ = "Integer32"
_LineChanOutGain_Object = MibTableColumn
lineChanOutGain = _LineChanOutGain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 29),
    _LineChanOutGain_Type()
)
lineChanOutGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanOutGain.setStatus("mandatory")


class _LineChanUtil_Type(Integer32):
    """Custom type lineChanUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LineChanUtil_Type.__name__ = "Integer32"
_LineChanUtil_Object = MibTableColumn
lineChanUtil = _LineChanUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 30),
    _LineChanUtil_Type()
)
lineChanUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanUtil.setStatus("mandatory")


class _LineChanEchoBgFilter_Type(Integer32):
    """Custom type lineChanEchoBgFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LineChanEchoBgFilter_Type.__name__ = "Integer32"
_LineChanEchoBgFilter_Object = MibTableColumn
lineChanEchoBgFilter = _LineChanEchoBgFilter_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 31),
    _LineChanEchoBgFilter_Type()
)
lineChanEchoBgFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoBgFilter.setStatus("mandatory")


class _LineChanEchoBackCard_Type(Integer32):
    """Custom type lineChanEchoBackCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LineChanEchoBackCard_Type.__name__ = "Integer32"
_LineChanEchoBackCard_Object = MibTableColumn
lineChanEchoBackCard = _LineChanEchoBackCard_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 32),
    _LineChanEchoBackCard_Type()
)
lineChanEchoBackCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEchoBackCard.setStatus("mandatory")


class _LineChanDataDceDte_Type(Integer32):
    """Custom type lineChanDataDceDte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dce", 2),
          ("dte", 3))
    )


_LineChanDataDceDte_Type.__name__ = "Integer32"
_LineChanDataDceDte_Object = MibTableColumn
lineChanDataDceDte = _LineChanDataDceDte_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 33),
    _LineChanDataDceDte_Type()
)
lineChanDataDceDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanDataDceDte.setStatus("mandatory")


class _LineChanDataUcs_Type(Integer32):
    """Custom type lineChanDataUcs based on Integer32"""
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
        *(("other", 1),
          ("t1-ucs", 2),
          ("ds0a", 3),
          ("e1-ucs", 4))
    )


_LineChanDataUcs_Type.__name__ = "Integer32"
_LineChanDataUcs_Object = MibTableColumn
lineChanDataUcs = _LineChanDataUcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 34),
    _LineChanDataUcs_Type()
)
lineChanDataUcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanDataUcs.setStatus("mandatory")
_LineChanConnPtr_Type = ObjectIdentifier
_LineChanConnPtr_Object = MibTableColumn
lineChanConnPtr = _LineChanConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 35),
    _LineChanConnPtr_Type()
)
lineChanConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineChanConnPtr.setStatus("mandatory")


class _LineChanEiaUpdt_Type(Integer32):
    """Custom type lineChanEiaUpdt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_LineChanEiaUpdt_Type.__name__ = "Integer32"
_LineChanEiaUpdt_Object = MibTableColumn
lineChanEiaUpdt = _LineChanEiaUpdt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 36),
    _LineChanEiaUpdt_Type()
)
lineChanEiaUpdt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEiaUpdt.setStatus("mandatory")


class _LineChanTimeSlot_Type(Integer32):
    """Custom type lineChanTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LineChanTimeSlot_Type.__name__ = "Integer32"
_LineChanTimeSlot_Object = MibTableColumn
lineChanTimeSlot = _LineChanTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 37),
    _LineChanTimeSlot_Type()
)
lineChanTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanTimeSlot.setStatus("mandatory")


class _LineChanEndState_Type(Integer32):
    """Custom type lineChanEndState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_LineChanEndState_Type.__name__ = "Integer32"
_LineChanEndState_Object = MibTableColumn
lineChanEndState = _LineChanEndState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 1, 1, 38),
    _LineChanEndState_Type()
)
lineChanEndState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineChanEndState.setStatus("mandatory")
_CircuitLines_Object = MibTable
circuitLines = _CircuitLines_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2)
)
if mibBuilder.loadTexts:
    circuitLines.setStatus("mandatory")
_CircuitLineEntry_Object = MibTableRow
circuitLineEntry = _CircuitLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1)
)
circuitLineEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    circuitLineEntry.setStatus("mandatory")


class _CirLineCnfStatus_Type(Integer32):
    """Custom type cirLineCnfStatus based on Integer32"""
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
        *(("other", 1),
          ("passing", 2),
          ("blocking", 3),
          ("inserting", 4),
          ("external", 5))
    )


_CirLineCnfStatus_Type.__name__ = "Integer32"
_CirLineCnfStatus_Object = MibTableColumn
cirLineCnfStatus = _CirLineCnfStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 1),
    _CirLineCnfStatus_Type()
)
cirLineCnfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineCnfStatus.setStatus("mandatory")
_CirLinePassOe_Type = Integer32
_CirLinePassOe_Object = MibTableColumn
cirLinePassOe = _CirLinePassOe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 2),
    _CirLinePassOe_Type()
)
cirLinePassOe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLinePassOe.setStatus("mandatory")


class _CirLineCasswMode_Type(Integer32):
    """Custom type cirLineCasswMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("server-end", 2),
          ("pbx-end", 3))
    )


_CirLineCasswMode_Type.__name__ = "Integer32"
_CirLineCasswMode_Object = MibTableColumn
cirLineCasswMode = _CirLineCasswMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 3),
    _CirLineCasswMode_Type()
)
cirLineCasswMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCasswMode.setStatus("mandatory")


class _CirLineCasConType_Type(Integer32):
    """Custom type cirLineCasConType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("a32", 1),
          ("a24", 2),
          ("a16", 3),
          ("a16z", 4),
          ("a32d", 5),
          ("c32", 6),
          ("c24", 7),
          ("c16", 8),
          ("c16z", 9),
          ("c32d", 10),
          ("p", 11),
          ("t", 12),
          ("v", 13),
          ("l16", 14),
          ("l16v", 15),
          ("l8", 16),
          ("l8v", 17),
          ("td", 18))
    )


_CirLineCasConType_Type.__name__ = "Integer32"
_CirLineCasConType_Object = MibTableColumn
cirLineCasConType = _CirLineCasConType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 4),
    _CirLineCasConType_Type()
)
cirLineCasConType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCasConType.setStatus("mandatory")


class _CirLineCCSType_Type(Integer32):
    """Custom type cirLineCCSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CirLineCCSType_Type.__name__ = "Integer32"
_CirLineCCSType_Object = MibTableColumn
cirLineCCSType = _CirLineCCSType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 5),
    _CirLineCCSType_Type()
)
cirLineCCSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCCSType.setStatus("mandatory")


class _CirLineCASType_Type(Integer32):
    """Custom type cirLineCASType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CirLineCASType_Type.__name__ = "Integer32"
_CirLineCASType_Object = MibTableColumn
cirLineCASType = _CirLineCASType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 6),
    _CirLineCASType_Type()
)
cirLineCASType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASType.setStatus("mandatory")


class _CirLineCASParm1_Type(Integer32):
    """Custom type cirLineCASParm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm1_Type.__name__ = "Integer32"
_CirLineCASParm1_Object = MibTableColumn
cirLineCASParm1 = _CirLineCASParm1_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 7),
    _CirLineCASParm1_Type()
)
cirLineCASParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm1.setStatus("mandatory")


class _CirLineCASParm2_Type(Integer32):
    """Custom type cirLineCASParm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm2_Type.__name__ = "Integer32"
_CirLineCASParm2_Object = MibTableColumn
cirLineCASParm2 = _CirLineCASParm2_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 8),
    _CirLineCASParm2_Type()
)
cirLineCASParm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm2.setStatus("mandatory")


class _CirLineCASParm3_Type(Integer32):
    """Custom type cirLineCASParm3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm3_Type.__name__ = "Integer32"
_CirLineCASParm3_Object = MibTableColumn
cirLineCASParm3 = _CirLineCASParm3_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 9),
    _CirLineCASParm3_Type()
)
cirLineCASParm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm3.setStatus("mandatory")


class _CirLineCASParm4_Type(Integer32):
    """Custom type cirLineCASParm4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm4_Type.__name__ = "Integer32"
_CirLineCASParm4_Object = MibTableColumn
cirLineCASParm4 = _CirLineCASParm4_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 10),
    _CirLineCASParm4_Type()
)
cirLineCASParm4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm4.setStatus("mandatory")


class _CirLineCASParm5_Type(Integer32):
    """Custom type cirLineCASParm5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm5_Type.__name__ = "Integer32"
_CirLineCASParm5_Object = MibTableColumn
cirLineCASParm5 = _CirLineCASParm5_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 11),
    _CirLineCASParm5_Type()
)
cirLineCASParm5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm5.setStatus("mandatory")


class _CirLineCASParm6_Type(Integer32):
    """Custom type cirLineCASParm6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm6_Type.__name__ = "Integer32"
_CirLineCASParm6_Object = MibTableColumn
cirLineCASParm6 = _CirLineCASParm6_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 12),
    _CirLineCASParm6_Type()
)
cirLineCASParm6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm6.setStatus("mandatory")


class _CirLineCASParm7_Type(Integer32):
    """Custom type cirLineCASParm7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm7_Type.__name__ = "Integer32"
_CirLineCASParm7_Object = MibTableColumn
cirLineCASParm7 = _CirLineCASParm7_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 13),
    _CirLineCASParm7_Type()
)
cirLineCASParm7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm7.setStatus("mandatory")


class _CirLineCASParm8_Type(Integer32):
    """Custom type cirLineCASParm8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm8_Type.__name__ = "Integer32"
_CirLineCASParm8_Object = MibTableColumn
cirLineCASParm8 = _CirLineCASParm8_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 14),
    _CirLineCASParm8_Type()
)
cirLineCASParm8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm8.setStatus("mandatory")


class _CirLineCASParm9_Type(Integer32):
    """Custom type cirLineCASParm9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm9_Type.__name__ = "Integer32"
_CirLineCASParm9_Object = MibTableColumn
cirLineCASParm9 = _CirLineCASParm9_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 15),
    _CirLineCASParm9_Type()
)
cirLineCASParm9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm9.setStatus("mandatory")


class _CirLineCASParm10_Type(Integer32):
    """Custom type cirLineCASParm10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm10_Type.__name__ = "Integer32"
_CirLineCASParm10_Object = MibTableColumn
cirLineCASParm10 = _CirLineCASParm10_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 16),
    _CirLineCASParm10_Type()
)
cirLineCASParm10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm10.setStatus("mandatory")


class _CirLineCASParm11_Type(Integer32):
    """Custom type cirLineCASParm11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm11_Type.__name__ = "Integer32"
_CirLineCASParm11_Object = MibTableColumn
cirLineCASParm11 = _CirLineCASParm11_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 17),
    _CirLineCASParm11_Type()
)
cirLineCASParm11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm11.setStatus("mandatory")


class _CirLineCASParm12_Type(Integer32):
    """Custom type cirLineCASParm12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm12_Type.__name__ = "Integer32"
_CirLineCASParm12_Object = MibTableColumn
cirLineCASParm12 = _CirLineCASParm12_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 18),
    _CirLineCASParm12_Type()
)
cirLineCASParm12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm12.setStatus("mandatory")


class _CirLineCASParm13_Type(Integer32):
    """Custom type cirLineCASParm13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm13_Type.__name__ = "Integer32"
_CirLineCASParm13_Object = MibTableColumn
cirLineCASParm13 = _CirLineCASParm13_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 19),
    _CirLineCASParm13_Type()
)
cirLineCASParm13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm13.setStatus("mandatory")


class _CirLineCASParm14_Type(Integer32):
    """Custom type cirLineCASParm14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm14_Type.__name__ = "Integer32"
_CirLineCASParm14_Object = MibTableColumn
cirLineCASParm14 = _CirLineCASParm14_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 20),
    _CirLineCASParm14_Type()
)
cirLineCASParm14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm14.setStatus("mandatory")


class _CirLineCASParm15_Type(Integer32):
    """Custom type cirLineCASParm15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm15_Type.__name__ = "Integer32"
_CirLineCASParm15_Object = MibTableColumn
cirLineCASParm15 = _CirLineCASParm15_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 21),
    _CirLineCASParm15_Type()
)
cirLineCASParm15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm15.setStatus("mandatory")


class _CirLineCASParm16_Type(Integer32):
    """Custom type cirLineCASParm16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm16_Type.__name__ = "Integer32"
_CirLineCASParm16_Object = MibTableColumn
cirLineCASParm16 = _CirLineCASParm16_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 22),
    _CirLineCASParm16_Type()
)
cirLineCASParm16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm16.setStatus("mandatory")


class _CirLineCASParm17_Type(Integer32):
    """Custom type cirLineCASParm17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm17_Type.__name__ = "Integer32"
_CirLineCASParm17_Object = MibTableColumn
cirLineCASParm17 = _CirLineCASParm17_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 23),
    _CirLineCASParm17_Type()
)
cirLineCASParm17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm17.setStatus("mandatory")


class _CirLineCASParm18_Type(Integer32):
    """Custom type cirLineCASParm18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CirLineCASParm18_Type.__name__ = "Integer32"
_CirLineCASParm18_Object = MibTableColumn
cirLineCASParm18 = _CirLineCASParm18_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 24),
    _CirLineCASParm18_Type()
)
cirLineCASParm18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCASParm18.setStatus("mandatory")


class _CirLineCachedSVC_Type(Integer32):
    """Custom type cirLineCachedSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CirLineCachedSVC_Type.__name__ = "Integer32"
_CirLineCachedSVC_Object = MibTableColumn
cirLineCachedSVC = _CirLineCachedSVC_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 5, 2, 1, 25),
    _CirLineCachedSVC_Type()
)
cirLineCachedSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirLineCachedSVC.setStatus("mandatory")
_RsrcServiceObjects_ObjectIdentity = ObjectIdentity
rsrcServiceObjects = _RsrcServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6)
)
_RsrcPartiTable_Object = MibTable
rsrcPartiTable = _RsrcPartiTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    rsrcPartiTable.setStatus("mandatory")
_RsrcPartiEntry_Object = MibTableRow
rsrcPartiEntry = _RsrcPartiEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1)
)
rsrcPartiEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
    (0, "STRATACOM-MIB", "rsrcPartiId"),
)
if mibBuilder.loadTexts:
    rsrcPartiEntry.setStatus("mandatory")


class _RsrcPartiId_Type(Integer32):
    """Custom type rsrcPartiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RsrcPartiId_Type.__name__ = "Integer32"
_RsrcPartiId_Object = MibTableColumn
rsrcPartiId = _RsrcPartiId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 1),
    _RsrcPartiId_Type()
)
rsrcPartiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrcPartiId.setStatus("mandatory")


class _RsrcPartiAdminStatus_Type(Integer32):
    """Custom type rsrcPartiAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("writeOnly", 3))
    )


_RsrcPartiAdminStatus_Type.__name__ = "Integer32"
_RsrcPartiAdminStatus_Object = MibTableColumn
rsrcPartiAdminStatus = _RsrcPartiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 2),
    _RsrcPartiAdminStatus_Type()
)
rsrcPartiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiAdminStatus.setStatus("mandatory")


class _RsrcPartiOperStatus_Type(Integer32):
    """Custom type rsrcPartiOperStatus based on Integer32"""
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


_RsrcPartiOperStatus_Type.__name__ = "Integer32"
_RsrcPartiOperStatus_Object = MibTableColumn
rsrcPartiOperStatus = _RsrcPartiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 3),
    _RsrcPartiOperStatus_Type()
)
rsrcPartiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrcPartiOperStatus.setStatus("mandatory")


class _RsrcPartiPvcMaxLcns_Type(Integer32):
    """Custom type rsrcPartiPvcMaxLcns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsrcPartiPvcMaxLcns_Type.__name__ = "Integer32"
_RsrcPartiPvcMaxLcns_Object = MibTableColumn
rsrcPartiPvcMaxLcns = _RsrcPartiPvcMaxLcns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 4),
    _RsrcPartiPvcMaxLcns_Type()
)
rsrcPartiPvcMaxLcns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiPvcMaxLcns.setStatus("mandatory")


class _RsrcPartiPvcMaxBw_Type(Integer32):
    """Custom type rsrcPartiPvcMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412830),
    )


_RsrcPartiPvcMaxBw_Type.__name__ = "Integer32"
_RsrcPartiPvcMaxBw_Object = MibTableColumn
rsrcPartiPvcMaxBw = _RsrcPartiPvcMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 5),
    _RsrcPartiPvcMaxBw_Type()
)
rsrcPartiPvcMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiPvcMaxBw.setStatus("mandatory")


class _RsrcPartiVsiMinLcns_Type(Integer32):
    """Custom type rsrcPartiVsiMinLcns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsrcPartiVsiMinLcns_Type.__name__ = "Integer32"
_RsrcPartiVsiMinLcns_Object = MibTableColumn
rsrcPartiVsiMinLcns = _RsrcPartiVsiMinLcns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 6),
    _RsrcPartiVsiMinLcns_Type()
)
rsrcPartiVsiMinLcns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiVsiMinLcns.setStatus("mandatory")


class _RsrcPartiVsiMaxLcns_Type(Integer32):
    """Custom type rsrcPartiVsiMaxLcns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsrcPartiVsiMaxLcns_Type.__name__ = "Integer32"
_RsrcPartiVsiMaxLcns_Object = MibTableColumn
rsrcPartiVsiMaxLcns = _RsrcPartiVsiMaxLcns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 7),
    _RsrcPartiVsiMaxLcns_Type()
)
rsrcPartiVsiMaxLcns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiVsiMaxLcns.setStatus("mandatory")


class _RsrcPartiVsiVpiStart_Type(Integer32):
    """Custom type rsrcPartiVsiVpiStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RsrcPartiVsiVpiStart_Type.__name__ = "Integer32"
_RsrcPartiVsiVpiStart_Object = MibTableColumn
rsrcPartiVsiVpiStart = _RsrcPartiVsiVpiStart_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 8),
    _RsrcPartiVsiVpiStart_Type()
)
rsrcPartiVsiVpiStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiVsiVpiStart.setStatus("mandatory")


class _RsrcPartiVsiVpiEnd_Type(Integer32):
    """Custom type rsrcPartiVsiVpiEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RsrcPartiVsiVpiEnd_Type.__name__ = "Integer32"
_RsrcPartiVsiVpiEnd_Object = MibTableColumn
rsrcPartiVsiVpiEnd = _RsrcPartiVsiVpiEnd_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 9),
    _RsrcPartiVsiVpiEnd_Type()
)
rsrcPartiVsiVpiEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiVsiVpiEnd.setStatus("mandatory")


class _RsrcPartiVsiMinBw_Type(Integer32):
    """Custom type rsrcPartiVsiMinBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412830),
    )


_RsrcPartiVsiMinBw_Type.__name__ = "Integer32"
_RsrcPartiVsiMinBw_Object = MibTableColumn
rsrcPartiVsiMinBw = _RsrcPartiVsiMinBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 10),
    _RsrcPartiVsiMinBw_Type()
)
rsrcPartiVsiMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiVsiMinBw.setStatus("mandatory")


class _RsrcPartiVsiMaxBw_Type(Integer32):
    """Custom type rsrcPartiVsiMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412830),
    )


_RsrcPartiVsiMaxBw_Type.__name__ = "Integer32"
_RsrcPartiVsiMaxBw_Object = MibTableColumn
rsrcPartiVsiMaxBw = _RsrcPartiVsiMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 1, 1, 11),
    _RsrcPartiVsiMaxBw_Type()
)
rsrcPartiVsiMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsrcPartiVsiMaxBw.setStatus("mandatory")
_AtmQbinTable_Object = MibTable
atmQbinTable = _AtmQbinTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2)
)
if mibBuilder.loadTexts:
    atmQbinTable.setStatus("mandatory")
_AtmQbinEntry_Object = MibTableRow
atmQbinEntry = _AtmQbinEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1)
)
atmQbinEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
    (0, "STRATACOM-MIB", "atmQbinId"),
)
if mibBuilder.loadTexts:
    atmQbinEntry.setStatus("mandatory")


class _AtmQbinId_Type(Integer32):
    """Custom type atmQbinId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmQbinId_Type.__name__ = "Integer32"
_AtmQbinId_Object = MibTableColumn
atmQbinId = _AtmQbinId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 1),
    _AtmQbinId_Type()
)
atmQbinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmQbinId.setStatus("mandatory")


class _AtmQbinAdminStatus_Type(Integer32):
    """Custom type atmQbinAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("writeOnly", 3))
    )


_AtmQbinAdminStatus_Type.__name__ = "Integer32"
_AtmQbinAdminStatus_Object = MibTableColumn
atmQbinAdminStatus = _AtmQbinAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 2),
    _AtmQbinAdminStatus_Type()
)
atmQbinAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQbinAdminStatus.setStatus("mandatory")


class _AtmQbinOperStatus_Type(Integer32):
    """Custom type atmQbinOperStatus based on Integer32"""
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


_AtmQbinOperStatus_Type.__name__ = "Integer32"
_AtmQbinOperStatus_Object = MibTableColumn
atmQbinOperStatus = _AtmQbinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 3),
    _AtmQbinOperStatus_Type()
)
atmQbinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmQbinOperStatus.setStatus("mandatory")


class _AtmQbinMinBw_Type(Integer32):
    """Custom type atmQbinMinBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412830),
    )


_AtmQbinMinBw_Type.__name__ = "Integer32"
_AtmQbinMinBw_Object = MibTableColumn
atmQbinMinBw = _AtmQbinMinBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 4),
    _AtmQbinMinBw_Type()
)
atmQbinMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQbinMinBw.setStatus("mandatory")


class _AtmQbinDepth_Type(Integer32):
    """Custom type atmQbinDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_AtmQbinDepth_Type.__name__ = "Integer32"
_AtmQbinDepth_Object = MibTableColumn
atmQbinDepth = _AtmQbinDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 5),
    _AtmQbinDepth_Type()
)
atmQbinDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQbinDepth.setStatus("mandatory")


class _AtmQbinLoClp_Type(Integer32):
    """Custom type atmQbinLoClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmQbinLoClp_Type.__name__ = "Integer32"
_AtmQbinLoClp_Object = MibTableColumn
atmQbinLoClp = _AtmQbinLoClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 6),
    _AtmQbinLoClp_Type()
)
atmQbinLoClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQbinLoClp.setStatus("mandatory")


class _AtmQbinHiClp_Type(Integer32):
    """Custom type atmQbinHiClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmQbinHiClp_Type.__name__ = "Integer32"
_AtmQbinHiClp_Object = MibTableColumn
atmQbinHiClp = _AtmQbinHiClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 7),
    _AtmQbinHiClp_Type()
)
atmQbinHiClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQbinHiClp.setStatus("mandatory")


class _AtmQbinEfci_Type(Integer32):
    """Custom type atmQbinEfci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmQbinEfci_Type.__name__ = "Integer32"
_AtmQbinEfci_Object = MibTableColumn
atmQbinEfci = _AtmQbinEfci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 6, 2, 1, 8),
    _AtmQbinEfci_Type()
)
atmQbinEfci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQbinEfci.setStatus("mandatory")
_SwitchConnection_ObjectIdentity = ObjectIdentity
switchConnection = _SwitchConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3)
)
_ConnNextEndptIndex_Type = Integer32
_ConnNextEndptIndex_Object = MibScalar
connNextEndptIndex = _ConnNextEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 1),
    _ConnNextEndptIndex_Type()
)
connNextEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connNextEndptIndex.setStatus("mandatory")
_ErrStatusLastIndex_Type = Integer32
_ErrStatusLastIndex_Object = MibScalar
errStatusLastIndex = _ErrStatusLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 2),
    _ErrStatusLastIndex_Type()
)
errStatusLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errStatusLastIndex.setStatus("obsolete")
_ErrStatusTable_Object = MibTable
errStatusTable = _ErrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3)
)
if mibBuilder.loadTexts:
    errStatusTable.setStatus("deprecated")
_ErrStatusTableEntry_Object = MibTableRow
errStatusTableEntry = _ErrStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1)
)
errStatusTableEntry.setIndexNames(
    (0, "STRATACOM-MIB", "errReqId"),
)
if mibBuilder.loadTexts:
    errStatusTableEntry.setStatus("deprecated")
_ErrReqId_Type = Integer32
_ErrReqId_Object = MibTableColumn
errReqId = _ErrReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1, 1),
    _ErrReqId_Type()
)
errReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errReqId.setStatus("deprecated")


class _ErrCode_Type(Integer32):
    """Custom type errCode based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("existErr", 2),
          ("syntaxErr", 3),
          ("resourceErr", 4),
          ("databaseLocked", 5),
          ("otherErr", 6),
          ("wrongType", 7),
          ("wrongLength", 8),
          ("wrongEncoding", 9),
          ("wrongValue", 10),
          ("noCreation", 11),
          ("inconsistentValue", 12),
          ("resourceUnavailable", 13),
          ("commitFailed", 14),
          ("undoFailed", 15),
          ("authorizationError", 16),
          ("notWritable", 17),
          ("inconsistentName", 18),
          ("featureDisabled", 19),
          ("m32Problem", 20),
          ("sarProblem", 21),
          ("bnmProblem", 22),
          ("ascUpdFailed", 23),
          ("lineEnabled", 24),
          ("lineDisabled", 25),
          ("lmMismatch", 26),
          ("lineHasPorts", 27),
          ("portEnabled", 28),
          ("portDisable", 29),
          ("portHasChan", 30),
          ("chanEnabled", 31),
          ("chanDisabled", 32),
          ("dlciEnabled", 33),
          ("dlciDisabled", 34))
    )


_ErrCode_Type.__name__ = "Integer32"
_ErrCode_Object = MibTableColumn
errCode = _ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1, 2),
    _ErrCode_Type()
)
errCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errCode.setStatus("deprecated")
_ErrStatusDesc_Type = DisplayString
_ErrStatusDesc_Object = MibTableColumn
errStatusDesc = _ErrStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1, 3),
    _ErrStatusDesc_Type()
)
errStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errStatusDesc.setStatus("deprecated")
_ConnTable_Object = MibTable
connTable = _ConnTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4)
)
if mibBuilder.loadTexts:
    connTable.setStatus("mandatory")
_ConnTableEntry_Object = MibTableRow
connTableEntry = _ConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1)
)
connTableEntry.setIndexNames(
    (0, "STRATACOM-MIB", "connIndex"),
)
if mibBuilder.loadTexts:
    connTableEntry.setStatus("mandatory")
_ConnIndex_Type = Integer32
_ConnIndex_Object = MibTableColumn
connIndex = _ConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 1),
    _ConnIndex_Type()
)
connIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connIndex.setStatus("mandatory")
_ConnLclEndptDesc_Type = DisplayString
_ConnLclEndptDesc_Object = MibTableColumn
connLclEndptDesc = _ConnLclEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 2),
    _ConnLclEndptDesc_Type()
)
connLclEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLclEndptDesc.setStatus("mandatory")


class _ConnType_Type(Integer32):
    """Custom type connType based on Integer32"""
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
        *(("frameRelay", 1),
          ("atf", 2),
          ("atm", 3),
          ("voice", 4),
          ("unknown", 5),
          ("data", 6))
    )


_ConnType_Type.__name__ = "Integer32"
_ConnType_Object = MibTableColumn
connType = _ConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 3),
    _ConnType_Type()
)
connType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connType.setStatus("mandatory")
_ConnOeIndex_Type = Integer32
_ConnOeIndex_Object = MibTableColumn
connOeIndex = _ConnOeIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 4),
    _ConnOeIndex_Type()
)
connOeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOeIndex.setStatus("mandatory")
_ConnRmtEndptDesc_Type = DisplayString
_ConnRmtEndptDesc_Object = MibTableColumn
connRmtEndptDesc = _ConnRmtEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 5),
    _ConnRmtEndptDesc_Type()
)
connRmtEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRmtEndptDesc.setStatus("mandatory")


class _ConnMasterFlag_Type(Integer32):
    """Custom type connMasterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnMasterFlag_Type.__name__ = "Integer32"
_ConnMasterFlag_Object = MibTableColumn
connMasterFlag = _ConnMasterFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 6),
    _ConnMasterFlag_Type()
)
connMasterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMasterFlag.setStatus("mandatory")


class _ConnClassOfService_Type(Integer32):
    """Custom type connClassOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ConnClassOfService_Type.__name__ = "Integer32"
_ConnClassOfService_Object = MibTableColumn
connClassOfService = _ConnClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 7),
    _ConnClassOfService_Type()
)
connClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connClassOfService.setStatus("mandatory")


class _ConnGroupFlag_Type(Integer32):
    """Custom type connGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnGroupFlag_Type.__name__ = "Integer32"
_ConnGroupFlag_Object = MibTableColumn
connGroupFlag = _ConnGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 8),
    _ConnGroupFlag_Type()
)
connGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connGroupFlag.setStatus("deprecated")


class _ConnAdminStatus_Type(Integer32):
    """Custom type connAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("modify", 3),
          ("writeOnly", 4),
          ("createGroup", 5),
          ("deleteGroup", 6))
    )


_ConnAdminStatus_Type.__name__ = "Integer32"
_ConnAdminStatus_Object = MibTableColumn
connAdminStatus = _ConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 9),
    _ConnAdminStatus_Type()
)
connAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connAdminStatus.setStatus("mandatory")


class _ConnOperStatus_Type(Integer32):
    """Custom type connOperStatus based on Integer32"""
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
        *(("ok", 1),
          ("okPendingDown", 2),
          ("down", 3),
          ("failed", 4),
          ("okPendingRoute", 5),
          ("unknown", 6))
    )


_ConnOperStatus_Type.__name__ = "Integer32"
_ConnOperStatus_Object = MibTableColumn
connOperStatus = _ConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 10),
    _ConnOperStatus_Type()
)
connOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOperStatus.setStatus("mandatory")


class _ConnNoRouteFoundFailure_Type(Integer32):
    """Custom type connNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnNoRouteFoundFailure_Type.__name__ = "Integer32"
_ConnNoRouteFoundFailure_Object = MibTableColumn
connNoRouteFoundFailure = _ConnNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 11),
    _ConnNoRouteFoundFailure_Type()
)
connNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connNoRouteFoundFailure.setStatus("mandatory")


class _ConnBumpFailure_Type(Integer32):
    """Custom type connBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnBumpFailure_Type.__name__ = "Integer32"
_ConnBumpFailure_Object = MibTableColumn
connBumpFailure = _ConnBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 12),
    _ConnBumpFailure_Type()
)
connBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connBumpFailure.setStatus("mandatory")
_ConnFirstEndptPtr_Type = ObjectIdentifier
_ConnFirstEndptPtr_Object = MibTableColumn
connFirstEndptPtr = _ConnFirstEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 13),
    _ConnFirstEndptPtr_Type()
)
connFirstEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFirstEndptPtr.setStatus("mandatory")


class _ConnCurrRouteDesc_Type(DisplayString):
    """Custom type connCurrRouteDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConnCurrRouteDesc_Type.__name__ = "DisplayString"
_ConnCurrRouteDesc_Object = MibTableColumn
connCurrRouteDesc = _ConnCurrRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 14),
    _ConnCurrRouteDesc_Type()
)
connCurrRouteDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCurrRouteDesc.setStatus("mandatory")


class _ConnPrefRouteDesc_Type(DisplayString):
    """Custom type connPrefRouteDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConnPrefRouteDesc_Type.__name__ = "DisplayString"
_ConnPrefRouteDesc_Object = MibTableColumn
connPrefRouteDesc = _ConnPrefRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 15),
    _ConnPrefRouteDesc_Type()
)
connPrefRouteDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPrefRouteDesc.setStatus("mandatory")


class _ConnMstOSpacePkts_Type(Integer32):
    """Custom type connMstOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnMstOSpacePkts_Type.__name__ = "Integer32"
_ConnMstOSpacePkts_Object = MibTableColumn
connMstOSpacePkts = _ConnMstOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 16),
    _ConnMstOSpacePkts_Type()
)
connMstOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpacePkts.setStatus("mandatory")


class _ConnMstOSpaceCells_Type(Integer32):
    """Custom type connMstOSpaceCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnMstOSpaceCells_Type.__name__ = "Integer32"
_ConnMstOSpaceCells_Object = MibTableColumn
connMstOSpaceCells = _ConnMstOSpaceCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 17),
    _ConnMstOSpaceCells_Type()
)
connMstOSpaceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpaceCells.setStatus("mandatory")


class _ConnMstOSpaceBdaCmax_Type(Integer32):
    """Custom type connMstOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnMstOSpaceBdaCmax_Type.__name__ = "Integer32"
_ConnMstOSpaceBdaCmax_Object = MibTableColumn
connMstOSpaceBdaCmax = _ConnMstOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 18),
    _ConnMstOSpaceBdaCmax_Type()
)
connMstOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpaceBdaCmax.setStatus("mandatory")


class _ConnMstOSpaceBdbCmax_Type(Integer32):
    """Custom type connMstOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnMstOSpaceBdbCmax_Type.__name__ = "Integer32"
_ConnMstOSpaceBdbCmax_Object = MibTableColumn
connMstOSpaceBdbCmax = _ConnMstOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 19),
    _ConnMstOSpaceBdbCmax_Type()
)
connMstOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpaceBdbCmax.setStatus("mandatory")


class _ConnSlvOSpacePkts_Type(Integer32):
    """Custom type connSlvOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnSlvOSpacePkts_Type.__name__ = "Integer32"
_ConnSlvOSpacePkts_Object = MibTableColumn
connSlvOSpacePkts = _ConnSlvOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 20),
    _ConnSlvOSpacePkts_Type()
)
connSlvOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpacePkts.setStatus("mandatory")


class _ConnSlvOSpaceCells_Type(Integer32):
    """Custom type connSlvOSpaceCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnSlvOSpaceCells_Type.__name__ = "Integer32"
_ConnSlvOSpaceCells_Object = MibTableColumn
connSlvOSpaceCells = _ConnSlvOSpaceCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 21),
    _ConnSlvOSpaceCells_Type()
)
connSlvOSpaceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpaceCells.setStatus("mandatory")


class _ConnSlvOSpaceBdaCmax_Type(Integer32):
    """Custom type connSlvOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnSlvOSpaceBdaCmax_Type.__name__ = "Integer32"
_ConnSlvOSpaceBdaCmax_Object = MibTableColumn
connSlvOSpaceBdaCmax = _ConnSlvOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 22),
    _ConnSlvOSpaceBdaCmax_Type()
)
connSlvOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpaceBdaCmax.setStatus("mandatory")


class _ConnSlvOSpaceBdbCmax_Type(Integer32):
    """Custom type connSlvOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnSlvOSpaceBdbCmax_Type.__name__ = "Integer32"
_ConnSlvOSpaceBdbCmax_Object = MibTableColumn
connSlvOSpaceBdbCmax = _ConnSlvOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 23),
    _ConnSlvOSpaceBdbCmax_Type()
)
connSlvOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpaceBdbCmax.setStatus("mandatory")
_ConnIcaRTD_Type = Integer32
_ConnIcaRTD_Object = MibTableColumn
connIcaRTD = _ConnIcaRTD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 24),
    _ConnIcaRTD_Type()
)
connIcaRTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connIcaRTD.setStatus("mandatory")
_ConnGroupDesc_Type = DisplayString
_ConnGroupDesc_Object = MibTableColumn
connGroupDesc = _ConnGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 25),
    _ConnGroupDesc_Type()
)
connGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connGroupDesc.setStatus("deprecated")
_FrEndptTable_Object = MibTable
frEndptTable = _FrEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5)
)
if mibBuilder.loadTexts:
    frEndptTable.setStatus("mandatory")
_FrEndptEntry_Object = MibTableRow
frEndptEntry = _FrEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1)
)
frEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndptIndex"),
)
if mibBuilder.loadTexts:
    frEndptEntry.setStatus("mandatory")
_FrEndptIndex_Type = Integer32
_FrEndptIndex_Object = MibTableColumn
frEndptIndex = _FrEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 1),
    _FrEndptIndex_Type()
)
frEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptIndex.setStatus("mandatory")
_FrEndptDesc_Type = DisplayString
_FrEndptDesc_Object = MibTableColumn
frEndptDesc = _FrEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 2),
    _FrEndptDesc_Type()
)
frEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptDesc.setStatus("mandatory")
_FrOtherEndptIndex_Type = Integer32
_FrOtherEndptIndex_Object = MibTableColumn
frOtherEndptIndex = _FrOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 3),
    _FrOtherEndptIndex_Type()
)
frOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frOtherEndptIndex.setStatus("mandatory")
_FrOtherEndptDesc_Type = DisplayString
_FrOtherEndptDesc_Object = MibTableColumn
frOtherEndptDesc = _FrOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 4),
    _FrOtherEndptDesc_Type()
)
frOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frOtherEndptDesc.setStatus("mandatory")


class _FrEndptAdminStatus_Type(Integer32):
    """Custom type frEndptAdminStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3),
          ("test", 4),
          ("writeOnly", 5))
    )


_FrEndptAdminStatus_Type.__name__ = "Integer32"
_FrEndptAdminStatus_Object = MibTableColumn
frEndptAdminStatus = _FrEndptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 5),
    _FrEndptAdminStatus_Type()
)
frEndptAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptAdminStatus.setStatus("mandatory")


class _FrEndptOperStatus_Type(Integer32):
    """Custom type frEndptOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("okPendingDown", 2),
          ("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("okPendingRoute", 6),
          ("okPendingDelete", 7),
          ("looped", 8),
          ("unknown", 9))
    )


_FrEndptOperStatus_Type.__name__ = "Integer32"
_FrEndptOperStatus_Object = MibTableColumn
frEndptOperStatus = _FrEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 6),
    _FrEndptOperStatus_Type()
)
frEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptOperStatus.setStatus("mandatory")


class _FrNoRouteFoundFailure_Type(Integer32):
    """Custom type frNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrNoRouteFoundFailure_Type.__name__ = "Integer32"
_FrNoRouteFoundFailure_Object = MibTableColumn
frNoRouteFoundFailure = _FrNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 7),
    _FrNoRouteFoundFailure_Type()
)
frNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNoRouteFoundFailure.setStatus("mandatory")


class _FrBumpFailure_Type(Integer32):
    """Custom type frBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrBumpFailure_Type.__name__ = "Integer32"
_FrBumpFailure_Object = MibTableColumn
frBumpFailure = _FrBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 8),
    _FrBumpFailure_Type()
)
frBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBumpFailure.setStatus("mandatory")


class _FrEndPointFailure_Type(Integer32):
    """Custom type frEndPointFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrEndPointFailure_Type.__name__ = "Integer32"
_FrEndPointFailure_Object = MibTableColumn
frEndPointFailure = _FrEndPointFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 9),
    _FrEndPointFailure_Type()
)
frEndPointFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointFailure.setStatus("mandatory")


class _FrTestFailure_Type(Integer32):
    """Custom type frTestFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrTestFailure_Type.__name__ = "Integer32"
_FrTestFailure_Object = MibTableColumn
frTestFailure = _FrTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 10),
    _FrTestFailure_Type()
)
frTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frTestFailure.setStatus("mandatory")
_FrConnPtr_Type = ObjectIdentifier
_FrConnPtr_Object = MibTableColumn
frConnPtr = _FrConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 11),
    _FrConnPtr_Type()
)
frConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frConnPtr.setStatus("mandatory")
_FrNextPtr_Type = ObjectIdentifier
_FrNextPtr_Object = MibTableColumn
frNextPtr = _FrNextPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 12),
    _FrNextPtr_Type()
)
frNextPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNextPtr.setStatus("deprecated")
_FrNextOnPortPtr_Type = ObjectIdentifier
_FrNextOnPortPtr_Object = MibTableColumn
frNextOnPortPtr = _FrNextOnPortPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 13),
    _FrNextOnPortPtr_Type()
)
frNextOnPortPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNextOnPortPtr.setStatus("mandatory")


class _FrEndptConnDesc_Type(DisplayString):
    """Custom type frEndptConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FrEndptConnDesc_Type.__name__ = "DisplayString"
_FrEndptConnDesc_Object = MibTableColumn
frEndptConnDesc = _FrEndptConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 14),
    _FrEndptConnDesc_Type()
)
frEndptConnDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frEndptConnDesc.setStatus("obsolete")


class _FrEndptTrkAvoidType_Type(Integer32):
    """Custom type frEndptTrkAvoidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_FrEndptTrkAvoidType_Type.__name__ = "Integer32"
_FrEndptTrkAvoidType_Object = MibTableColumn
frEndptTrkAvoidType = _FrEndptTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 15),
    _FrEndptTrkAvoidType_Type()
)
frEndptTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptTrkAvoidType.setStatus("mandatory")


class _FrEndptTrkAvoidZCS_Type(Integer32):
    """Custom type frEndptTrkAvoidZCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrEndptTrkAvoidZCS_Type.__name__ = "Integer32"
_FrEndptTrkAvoidZCS_Object = MibTableColumn
frEndptTrkAvoidZCS = _FrEndptTrkAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 16),
    _FrEndptTrkAvoidZCS_Type()
)
frEndptTrkAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptTrkAvoidZCS.setStatus("mandatory")


class _FrEndptSubType_Type(Integer32):
    """Custom type frEndptSubType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 1),
          ("atf", 2),
          ("unknown", 3),
          ("cbr", 4),
          ("vbr", 5),
          ("abr", 6),
          ("atft", 7),
          ("atfx", 8))
    )


_FrEndptSubType_Type.__name__ = "Integer32"
_FrEndptSubType_Object = MibTableColumn
frEndptSubType = _FrEndptSubType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 17),
    _FrEndptSubType_Type()
)
frEndptSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptSubType.setStatus("mandatory")


class _FrEndptBWClass_Type(Integer32):
    """Custom type frEndptBWClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrEndptBWClass_Type.__name__ = "Integer32"
_FrEndptBWClass_Object = MibTableColumn
frEndptBWClass = _FrEndptBWClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 18),
    _FrEndptBWClass_Type()
)
frEndptBWClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptBWClass.setStatus("mandatory")


class _FrEndptMIR_Type(Integer32):
    """Custom type frEndptMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrEndptMIR_Type.__name__ = "Integer32"
_FrEndptMIR_Object = MibTableColumn
frEndptMIR = _FrEndptMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 19),
    _FrEndptMIR_Type()
)
frEndptMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptMIR.setStatus("mandatory")


class _FrEndptCIR_Type(Integer32):
    """Custom type frEndptCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384000),
    )


_FrEndptCIR_Type.__name__ = "Integer32"
_FrEndptCIR_Object = MibTableColumn
frEndptCIR = _FrEndptCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 20),
    _FrEndptCIR_Type()
)
frEndptCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptCIR.setStatus("mandatory")


class _FrEndptBc_Type(Integer32):
    """Custom type frEndptBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrEndptBc_Type.__name__ = "Integer32"
_FrEndptBc_Object = MibTableColumn
frEndptBc = _FrEndptBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 21),
    _FrEndptBc_Type()
)
frEndptBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptBc.setStatus("mandatory")


class _FrEndptBe_Type(Integer32):
    """Custom type frEndptBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptBe_Type.__name__ = "Integer32"
_FrEndptBe_Object = MibTableColumn
frEndptBe = _FrEndptBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 22),
    _FrEndptBe_Type()
)
frEndptBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptBe.setStatus("mandatory")


class _FrEndptVcQSize_Type(Integer32):
    """Custom type frEndptVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrEndptVcQSize_Type.__name__ = "Integer32"
_FrEndptVcQSize_Object = MibTableColumn
frEndptVcQSize = _FrEndptVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 23),
    _FrEndptVcQSize_Type()
)
frEndptVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptVcQSize.setStatus("mandatory")


class _FrEndptPIR_Type(Integer32):
    """Custom type frEndptPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrEndptPIR_Type.__name__ = "Integer32"
_FrEndptPIR_Object = MibTableColumn
frEndptPIR = _FrEndptPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 24),
    _FrEndptPIR_Type()
)
frEndptPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptPIR.setStatus("mandatory")


class _FrEndptCMAX_Type(Integer32):
    """Custom type frEndptCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrEndptCMAX_Type.__name__ = "Integer32"
_FrEndptCMAX_Object = MibTableColumn
frEndptCMAX = _FrEndptCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 25),
    _FrEndptCMAX_Type()
)
frEndptCMAX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptCMAX.setStatus("mandatory")


class _FrEndptEcnQSize_Type(Integer32):
    """Custom type frEndptEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptEcnQSize_Type.__name__ = "Integer32"
_FrEndptEcnQSize_Object = MibTableColumn
frEndptEcnQSize = _FrEndptEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 26),
    _FrEndptEcnQSize_Type()
)
frEndptEcnQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptEcnQSize.setStatus("mandatory")


class _FrEndptQIR_Type(Integer32):
    """Custom type frEndptQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrEndptQIR_Type.__name__ = "Integer32"
_FrEndptQIR_Object = MibTableColumn
frEndptQIR = _FrEndptQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 27),
    _FrEndptQIR_Type()
)
frEndptQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptQIR.setStatus("mandatory")


class _FrEndptPercUtil_Type(Integer32):
    """Custom type frEndptPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrEndptPercUtil_Type.__name__ = "Integer32"
_FrEndptPercUtil_Object = MibTableColumn
frEndptPercUtil = _FrEndptPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 28),
    _FrEndptPercUtil_Type()
)
frEndptPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptPercUtil.setStatus("mandatory")


class _FrEndptOeMIR_Type(Integer32):
    """Custom type frEndptOeMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrEndptOeMIR_Type.__name__ = "Integer32"
_FrEndptOeMIR_Object = MibTableColumn
frEndptOeMIR = _FrEndptOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 29),
    _FrEndptOeMIR_Type()
)
frEndptOeMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeMIR.setStatus("mandatory")


class _FrEndptOeCIR_Type(Integer32):
    """Custom type frEndptOeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384000),
    )


_FrEndptOeCIR_Type.__name__ = "Integer32"
_FrEndptOeCIR_Object = MibTableColumn
frEndptOeCIR = _FrEndptOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 30),
    _FrEndptOeCIR_Type()
)
frEndptOeCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeCIR.setStatus("mandatory")


class _FrEndptOeBc_Type(Integer32):
    """Custom type frEndptOeBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptOeBc_Type.__name__ = "Integer32"
_FrEndptOeBc_Object = MibTableColumn
frEndptOeBc = _FrEndptOeBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 31),
    _FrEndptOeBc_Type()
)
frEndptOeBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeBc.setStatus("mandatory")


class _FrEndptOeBe_Type(Integer32):
    """Custom type frEndptOeBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptOeBe_Type.__name__ = "Integer32"
_FrEndptOeBe_Object = MibTableColumn
frEndptOeBe = _FrEndptOeBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 32),
    _FrEndptOeBe_Type()
)
frEndptOeBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeBe.setStatus("mandatory")


class _FrEndptOeVcQSize_Type(Integer32):
    """Custom type frEndptOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072000),
    )


_FrEndptOeVcQSize_Type.__name__ = "Integer32"
_FrEndptOeVcQSize_Object = MibTableColumn
frEndptOeVcQSize = _FrEndptOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 33),
    _FrEndptOeVcQSize_Type()
)
frEndptOeVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeVcQSize.setStatus("mandatory")


class _FrEndptOePIR_Type(Integer32):
    """Custom type frEndptOePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrEndptOePIR_Type.__name__ = "Integer32"
_FrEndptOePIR_Object = MibTableColumn
frEndptOePIR = _FrEndptOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 34),
    _FrEndptOePIR_Type()
)
frEndptOePIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOePIR.setStatus("mandatory")


class _FrEndptOeCMAX_Type(Integer32):
    """Custom type frEndptOeCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 57600),
    )


_FrEndptOeCMAX_Type.__name__ = "Integer32"
_FrEndptOeCMAX_Object = MibTableColumn
frEndptOeCMAX = _FrEndptOeCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 35),
    _FrEndptOeCMAX_Type()
)
frEndptOeCMAX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeCMAX.setStatus("mandatory")


class _FrEndptOeEcnQSize_Type(Integer32):
    """Custom type frEndptOeEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptOeEcnQSize_Type.__name__ = "Integer32"
_FrEndptOeEcnQSize_Object = MibTableColumn
frEndptOeEcnQSize = _FrEndptOeEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 36),
    _FrEndptOeEcnQSize_Type()
)
frEndptOeEcnQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeEcnQSize.setStatus("mandatory")


class _FrEndptOeQIR_Type(Integer32):
    """Custom type frEndptOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrEndptOeQIR_Type.__name__ = "Integer32"
_FrEndptOeQIR_Object = MibTableColumn
frEndptOeQIR = _FrEndptOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 37),
    _FrEndptOeQIR_Type()
)
frEndptOeQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeQIR.setStatus("mandatory")


class _FrEndptOePercUtil_Type(Integer32):
    """Custom type frEndptOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrEndptOePercUtil_Type.__name__ = "Integer32"
_FrEndptOePercUtil_Object = MibTableColumn
frEndptOePercUtil = _FrEndptOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 38),
    _FrEndptOePercUtil_Type()
)
frEndptOePercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOePercUtil.setStatus("mandatory")


class _FrEndptEnableFST_Type(Integer32):
    """Custom type frEndptEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrEndptEnableFST_Type.__name__ = "Integer32"
_FrEndptEnableFST_Object = MibTableColumn
frEndptEnableFST = _FrEndptEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 39),
    _FrEndptEnableFST_Type()
)
frEndptEnableFST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptEnableFST.setStatus("mandatory")


class _FrEndptConnPrio_Type(Integer32):
    """Custom type frEndptConnPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FrEndptConnPrio_Type.__name__ = "Integer32"
_FrEndptConnPrio_Object = MibTableColumn
frEndptConnPrio = _FrEndptConnPrio_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 40),
    _FrEndptConnPrio_Type()
)
frEndptConnPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptConnPrio.setStatus("mandatory")


class _FrEndptGroupFlag_Type(Integer32):
    """Custom type frEndptGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrEndptGroupFlag_Type.__name__ = "Integer32"
_FrEndptGroupFlag_Object = MibTableColumn
frEndptGroupFlag = _FrEndptGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 41),
    _FrEndptGroupFlag_Type()
)
frEndptGroupFlag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frEndptGroupFlag.setStatus("deprecated")


class _FrEndptLocLpbkState_Type(Integer32):
    """Custom type frEndptLocLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrEndptLocLpbkState_Type.__name__ = "Integer32"
_FrEndptLocLpbkState_Object = MibTableColumn
frEndptLocLpbkState = _FrEndptLocLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 42),
    _FrEndptLocLpbkState_Type()
)
frEndptLocLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptLocLpbkState.setStatus("mandatory")


class _FrEndptLocRmtLpbkState_Type(Integer32):
    """Custom type frEndptLocRmtLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrEndptLocRmtLpbkState_Type.__name__ = "Integer32"
_FrEndptLocRmtLpbkState_Object = MibTableColumn
frEndptLocRmtLpbkState = _FrEndptLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 43),
    _FrEndptLocRmtLpbkState_Type()
)
frEndptLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptLocRmtLpbkState.setStatus("mandatory")
_FrEndptLpbkStatus_Type = Integer32
_FrEndptLpbkStatus_Object = MibTableColumn
frEndptLpbkStatus = _FrEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 44),
    _FrEndptLpbkStatus_Type()
)
frEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptLpbkStatus.setStatus("mandatory")


class _FrEndptTestType_Type(Integer32):
    """Custom type frEndptTestType based on Integer32"""
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
        *(("test", 1),
          ("testDelay", 2),
          ("testNoLoop", 3),
          ("testDelayNoLoop", 4),
          ("writeOnly", 5))
    )


_FrEndptTestType_Type.__name__ = "Integer32"
_FrEndptTestType_Object = MibTableColumn
frEndptTestType = _FrEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 45),
    _FrEndptTestType_Type()
)
frEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptTestType.setStatus("mandatory")
_FrEndptRtdTestDelay_Type = Integer32
_FrEndptRtdTestDelay_Object = MibTableColumn
frEndptRtdTestDelay = _FrEndptRtdTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 46),
    _FrEndptRtdTestDelay_Type()
)
frEndptRtdTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRtdTestDelay.setStatus("mandatory")
_FrEndptGroupDesc_Type = DisplayString
_FrEndptGroupDesc_Object = MibTableColumn
frEndptGroupDesc = _FrEndptGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 47),
    _FrEndptGroupDesc_Type()
)
frEndptGroupDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frEndptGroupDesc.setStatus("deprecated")
_FrEndptStatTable_Object = MibTable
frEndptStatTable = _FrEndptStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6)
)
if mibBuilder.loadTexts:
    frEndptStatTable.setStatus("mandatory")
_FrEndptStatEntry_Object = MibTableRow
frEndptStatEntry = _FrEndptStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1)
)
frEndptStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndptIndex"),
)
if mibBuilder.loadTexts:
    frEndptStatEntry.setStatus("mandatory")
_FrEndptRxBytes_Type = Counter32
_FrEndptRxBytes_Object = MibTableColumn
frEndptRxBytes = _FrEndptRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 1),
    _FrEndptRxBytes_Type()
)
frEndptRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytes.setStatus("mandatory")
_FrEndptRxBytesDscds_Type = Counter32
_FrEndptRxBytesDscds_Object = MibTableColumn
frEndptRxBytesDscds = _FrEndptRxBytesDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 2),
    _FrEndptRxBytesDscds_Type()
)
frEndptRxBytesDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytesDscds.setStatus("mandatory")
_FrEndptRxFrms_Type = Counter32
_FrEndptRxFrms_Object = MibTableColumn
frEndptRxFrms = _FrEndptRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 3),
    _FrEndptRxFrms_Type()
)
frEndptRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrms.setStatus("mandatory")
_FrEndptRxFrmsDscds_Type = Counter32
_FrEndptRxFrmsDscds_Object = MibTableColumn
frEndptRxFrmsDscds = _FrEndptRxFrmsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 4),
    _FrEndptRxFrmsDscds_Type()
)
frEndptRxFrmsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsDscds.setStatus("mandatory")
_FrEndptRxPkts_Type = Counter32
_FrEndptRxPkts_Object = MibTableColumn
frEndptRxPkts = _FrEndptRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 5),
    _FrEndptRxPkts_Type()
)
frEndptRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxPkts.setStatus("mandatory")
_FrEndptRxPktsDscds_Type = Counter32
_FrEndptRxPktsDscds_Object = MibTableColumn
frEndptRxPktsDscds = _FrEndptRxPktsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 6),
    _FrEndptRxPktsDscds_Type()
)
frEndptRxPktsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxPktsDscds.setStatus("mandatory")
_FrEndptTxBytes_Type = Counter32
_FrEndptTxBytes_Object = MibTableColumn
frEndptTxBytes = _FrEndptTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 7),
    _FrEndptTxBytes_Type()
)
frEndptTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxBytes.setStatus("mandatory")
_FrEndptTxBytesDscds_Type = Counter32
_FrEndptTxBytesDscds_Object = MibTableColumn
frEndptTxBytesDscds = _FrEndptTxBytesDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 8),
    _FrEndptTxBytesDscds_Type()
)
frEndptTxBytesDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxBytesDscds.setStatus("mandatory")
_FrEndptTxFrms_Type = Counter32
_FrEndptTxFrms_Object = MibTableColumn
frEndptTxFrms = _FrEndptTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 9),
    _FrEndptTxFrms_Type()
)
frEndptTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrms.setStatus("mandatory")
_FrEndptTxFrmsDscds_Type = Counter32
_FrEndptTxFrmsDscds_Object = MibTableColumn
frEndptTxFrmsDscds = _FrEndptTxFrmsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 10),
    _FrEndptTxFrmsDscds_Type()
)
frEndptTxFrmsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsDscds.setStatus("mandatory")
_FrEndptTxPkts_Type = Counter32
_FrEndptTxPkts_Object = MibTableColumn
frEndptTxPkts = _FrEndptTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 11),
    _FrEndptTxPkts_Type()
)
frEndptTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxPkts.setStatus("mandatory")
_FrEndptTxFrmsFecns_Type = Counter32
_FrEndptTxFrmsFecns_Object = MibTableColumn
frEndptTxFrmsFecns = _FrEndptTxFrmsFecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 12),
    _FrEndptTxFrmsFecns_Type()
)
frEndptTxFrmsFecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsFecns.setStatus("mandatory")
_FrEndptTxFrmsBecns_Type = Counter32
_FrEndptTxFrmsBecns_Object = MibTableColumn
frEndptTxFrmsBecns = _FrEndptTxFrmsBecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 13),
    _FrEndptTxFrmsBecns_Type()
)
frEndptTxFrmsBecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsBecns.setStatus("mandatory")
_FrEndptSecInServices_Type = Counter32
_FrEndptSecInServices_Object = MibTableColumn
frEndptSecInServices = _FrEndptSecInServices_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 14),
    _FrEndptSecInServices_Type()
)
frEndptSecInServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptSecInServices.setStatus("mandatory")
_FrEndptCongestMins_Type = Counter32
_FrEndptCongestMins_Object = MibTableColumn
frEndptCongestMins = _FrEndptCongestMins_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 15),
    _FrEndptCongestMins_Type()
)
frEndptCongestMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptCongestMins.setStatus("mandatory")
_FrEndptRxFrmsDes_Type = Counter32
_FrEndptRxFrmsDes_Object = MibTableColumn
frEndptRxFrmsDes = _FrEndptRxFrmsDes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 16),
    _FrEndptRxFrmsDes_Type()
)
frEndptRxFrmsDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsDes.setStatus("mandatory")
_FrEndptRxBytesDes_Type = Counter32
_FrEndptRxBytesDes_Object = MibTableColumn
frEndptRxBytesDes = _FrEndptRxBytesDes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 17),
    _FrEndptRxBytesDes_Type()
)
frEndptRxBytesDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytesDes.setStatus("mandatory")
_FrEndptTxFrmsDes_Type = Counter32
_FrEndptTxFrmsDes_Object = MibTableColumn
frEndptTxFrmsDes = _FrEndptTxFrmsDes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 18),
    _FrEndptTxFrmsDes_Type()
)
frEndptTxFrmsDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsDes.setStatus("mandatory")
_FrEndptRxFrmsDeDscds_Type = Counter32
_FrEndptRxFrmsDeDscds_Object = MibTableColumn
frEndptRxFrmsDeDscds = _FrEndptRxFrmsDeDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 19),
    _FrEndptRxFrmsDeDscds_Type()
)
frEndptRxFrmsDeDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsDeDscds.setStatus("mandatory")
_FrEndptRxFrmsCirs_Type = Counter32
_FrEndptRxFrmsCirs_Object = MibTableColumn
frEndptRxFrmsCirs = _FrEndptRxFrmsCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 20),
    _FrEndptRxFrmsCirs_Type()
)
frEndptRxFrmsCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsCirs.setStatus("mandatory")
_FrEndptRxBytesCirs_Type = Counter32
_FrEndptRxBytesCirs_Object = MibTableColumn
frEndptRxBytesCirs = _FrEndptRxBytesCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 21),
    _FrEndptRxBytesCirs_Type()
)
frEndptRxBytesCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytesCirs.setStatus("mandatory")
_FrEndptTxFrmsCirs_Type = Counter32
_FrEndptTxFrmsCirs_Object = MibTableColumn
frEndptTxFrmsCirs = _FrEndptTxFrmsCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 22),
    _FrEndptTxFrmsCirs_Type()
)
frEndptTxFrmsCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsCirs.setStatus("mandatory")
_FrEndptTxBytesCirs_Type = Counter32
_FrEndptTxBytesCirs_Object = MibTableColumn
frEndptTxBytesCirs = _FrEndptTxBytesCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 23),
    _FrEndptTxBytesCirs_Type()
)
frEndptTxBytesCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxBytesCirs.setStatus("mandatory")
_FrEndptUnknProtIngDscds_Type = Counter32
_FrEndptUnknProtIngDscds_Object = MibTableColumn
frEndptUnknProtIngDscds = _FrEndptUnknProtIngDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 24),
    _FrEndptUnknProtIngDscds_Type()
)
frEndptUnknProtIngDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptUnknProtIngDscds.setStatus("mandatory")
_FrEndptUnknProtEgrDscds_Type = Counter32
_FrEndptUnknProtEgrDscds_Object = MibTableColumn
frEndptUnknProtEgrDscds = _FrEndptUnknProtEgrDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 25),
    _FrEndptUnknProtEgrDscds_Type()
)
frEndptUnknProtEgrDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptUnknProtEgrDscds.setStatus("mandatory")
_FrBwClassTable_Object = MibTable
frBwClassTable = _FrBwClassTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7)
)
if mibBuilder.loadTexts:
    frBwClassTable.setStatus("mandatory")
_FrBwClassEntry_Object = MibTableRow
frBwClassEntry = _FrBwClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1)
)
frBwClassEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frBwClassIndex"),
)
if mibBuilder.loadTexts:
    frBwClassEntry.setStatus("mandatory")


class _FrBwClassIndex_Type(Integer32):
    """Custom type frBwClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrBwClassIndex_Type.__name__ = "Integer32"
_FrBwClassIndex_Object = MibTableColumn
frBwClassIndex = _FrBwClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 1),
    _FrBwClassIndex_Type()
)
frBwClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassIndex.setStatus("mandatory")


class _FrBwClassMIR_Type(Integer32):
    """Custom type frBwClassMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassMIR_Type.__name__ = "Integer32"
_FrBwClassMIR_Object = MibTableColumn
frBwClassMIR = _FrBwClassMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 2),
    _FrBwClassMIR_Type()
)
frBwClassMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassMIR.setStatus("mandatory")


class _FrBwClassCIR_Type(Integer32):
    """Custom type frBwClassCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassCIR_Type.__name__ = "Integer32"
_FrBwClassCIR_Object = MibTableColumn
frBwClassCIR = _FrBwClassCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 3),
    _FrBwClassCIR_Type()
)
frBwClassCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassCIR.setStatus("mandatory")


class _FrBwClassVcQSize_Type(Integer32):
    """Custom type frBwClassVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrBwClassVcQSize_Type.__name__ = "Integer32"
_FrBwClassVcQSize_Object = MibTableColumn
frBwClassVcQSize = _FrBwClassVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 4),
    _FrBwClassVcQSize_Type()
)
frBwClassVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassVcQSize.setStatus("mandatory")


class _FrBwClassBc_Type(Integer32):
    """Custom type frBwClassBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrBwClassBc_Type.__name__ = "Integer32"
_FrBwClassBc_Object = MibTableColumn
frBwClassBc = _FrBwClassBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 5),
    _FrBwClassBc_Type()
)
frBwClassBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassBc.setStatus("mandatory")


class _FrBwClassPIR_Type(Integer32):
    """Custom type frBwClassPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassPIR_Type.__name__ = "Integer32"
_FrBwClassPIR_Object = MibTableColumn
frBwClassPIR = _FrBwClassPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 6),
    _FrBwClassPIR_Type()
)
frBwClassPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassPIR.setStatus("mandatory")


class _FrBwClassBe_Type(Integer32):
    """Custom type frBwClassBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassBe_Type.__name__ = "Integer32"
_FrBwClassBe_Object = MibTableColumn
frBwClassBe = _FrBwClassBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 7),
    _FrBwClassBe_Type()
)
frBwClassBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassBe.setStatus("mandatory")


class _FrBwClassCMAX_Type(Integer32):
    """Custom type frBwClassCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrBwClassCMAX_Type.__name__ = "Integer32"
_FrBwClassCMAX_Object = MibTableColumn
frBwClassCMAX = _FrBwClassCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 8),
    _FrBwClassCMAX_Type()
)
frBwClassCMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassCMAX.setStatus("mandatory")


class _FrBwClassEcnQSize_Type(Integer32):
    """Custom type frBwClassEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassEcnQSize_Type.__name__ = "Integer32"
_FrBwClassEcnQSize_Object = MibTableColumn
frBwClassEcnQSize = _FrBwClassEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 9),
    _FrBwClassEcnQSize_Type()
)
frBwClassEcnQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassEcnQSize.setStatus("mandatory")


class _FrBwClassQIR_Type(Integer32):
    """Custom type frBwClassQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassQIR_Type.__name__ = "Integer32"
_FrBwClassQIR_Object = MibTableColumn
frBwClassQIR = _FrBwClassQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 10),
    _FrBwClassQIR_Type()
)
frBwClassQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassQIR.setStatus("mandatory")


class _FrBwClassPercUtil_Type(Integer32):
    """Custom type frBwClassPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrBwClassPercUtil_Type.__name__ = "Integer32"
_FrBwClassPercUtil_Object = MibTableColumn
frBwClassPercUtil = _FrBwClassPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 11),
    _FrBwClassPercUtil_Type()
)
frBwClassPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassPercUtil.setStatus("mandatory")


class _FrBwClassOeMIR_Type(Integer32):
    """Custom type frBwClassOeMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassOeMIR_Type.__name__ = "Integer32"
_FrBwClassOeMIR_Object = MibTableColumn
frBwClassOeMIR = _FrBwClassOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 12),
    _FrBwClassOeMIR_Type()
)
frBwClassOeMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeMIR.setStatus("mandatory")


class _FrBwClassOeCIR_Type(Integer32):
    """Custom type frBwClassOeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassOeCIR_Type.__name__ = "Integer32"
_FrBwClassOeCIR_Object = MibTableColumn
frBwClassOeCIR = _FrBwClassOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 13),
    _FrBwClassOeCIR_Type()
)
frBwClassOeCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeCIR.setStatus("mandatory")


class _FrBwClassOeVcQSize_Type(Integer32):
    """Custom type frBwClassOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072000),
    )


_FrBwClassOeVcQSize_Type.__name__ = "Integer32"
_FrBwClassOeVcQSize_Object = MibTableColumn
frBwClassOeVcQSize = _FrBwClassOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 14),
    _FrBwClassOeVcQSize_Type()
)
frBwClassOeVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeVcQSize.setStatus("mandatory")


class _FrBwClassOeBc_Type(Integer32):
    """Custom type frBwClassOeBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassOeBc_Type.__name__ = "Integer32"
_FrBwClassOeBc_Object = MibTableColumn
frBwClassOeBc = _FrBwClassOeBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 15),
    _FrBwClassOeBc_Type()
)
frBwClassOeBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeBc.setStatus("mandatory")


class _FrBwClassOePIR_Type(Integer32):
    """Custom type frBwClassOePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassOePIR_Type.__name__ = "Integer32"
_FrBwClassOePIR_Object = MibTableColumn
frBwClassOePIR = _FrBwClassOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 16),
    _FrBwClassOePIR_Type()
)
frBwClassOePIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOePIR.setStatus("mandatory")


class _FrBwClassOeBe_Type(Integer32):
    """Custom type frBwClassOeBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassOeBe_Type.__name__ = "Integer32"
_FrBwClassOeBe_Object = MibTableColumn
frBwClassOeBe = _FrBwClassOeBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 17),
    _FrBwClassOeBe_Type()
)
frBwClassOeBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeBe.setStatus("mandatory")


class _FrBwClassOeCMAX_Type(Integer32):
    """Custom type frBwClassOeCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 57600),
    )


_FrBwClassOeCMAX_Type.__name__ = "Integer32"
_FrBwClassOeCMAX_Object = MibTableColumn
frBwClassOeCMAX = _FrBwClassOeCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 18),
    _FrBwClassOeCMAX_Type()
)
frBwClassOeCMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeCMAX.setStatus("mandatory")


class _FrBwClassOeEcnQSize_Type(Integer32):
    """Custom type frBwClassOeEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassOeEcnQSize_Type.__name__ = "Integer32"
_FrBwClassOeEcnQSize_Object = MibTableColumn
frBwClassOeEcnQSize = _FrBwClassOeEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 19),
    _FrBwClassOeEcnQSize_Type()
)
frBwClassOeEcnQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeEcnQSize.setStatus("mandatory")


class _FrBwClassOeQIR_Type(Integer32):
    """Custom type frBwClassOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 16384000),
    )


_FrBwClassOeQIR_Type.__name__ = "Integer32"
_FrBwClassOeQIR_Object = MibTableColumn
frBwClassOeQIR = _FrBwClassOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 20),
    _FrBwClassOeQIR_Type()
)
frBwClassOeQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeQIR.setStatus("mandatory")


class _FrBwClassOePercUtil_Type(Integer32):
    """Custom type frBwClassOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrBwClassOePercUtil_Type.__name__ = "Integer32"
_FrBwClassOePercUtil_Object = MibTableColumn
frBwClassOePercUtil = _FrBwClassOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 21),
    _FrBwClassOePercUtil_Type()
)
frBwClassOePercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOePercUtil.setStatus("mandatory")


class _FrBwClassEnableFST_Type(Integer32):
    """Custom type frBwClassEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrBwClassEnableFST_Type.__name__ = "Integer32"
_FrBwClassEnableFST_Object = MibTableColumn
frBwClassEnableFST = _FrBwClassEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 22),
    _FrBwClassEnableFST_Type()
)
frBwClassEnableFST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassEnableFST.setStatus("mandatory")


class _FrBwClassDescription_Type(DisplayString):
    """Custom type frBwClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_FrBwClassDescription_Type.__name__ = "DisplayString"
_FrBwClassDescription_Object = MibTableColumn
frBwClassDescription = _FrBwClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 23),
    _FrBwClassDescription_Type()
)
frBwClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassDescription.setStatus("mandatory")
_AtmEndptTable_Object = MibTable
atmEndptTable = _AtmEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8)
)
if mibBuilder.loadTexts:
    atmEndptTable.setStatus("mandatory")
_AtmEndptEntry_Object = MibTableRow
atmEndptEntry = _AtmEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1)
)
atmEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndptIndex"),
)
if mibBuilder.loadTexts:
    atmEndptEntry.setStatus("mandatory")


class _AtmEndptIndex_Type(Integer32):
    """Custom type atmEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AtmEndptIndex_Type.__name__ = "Integer32"
_AtmEndptIndex_Object = MibTableColumn
atmEndptIndex = _AtmEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 1),
    _AtmEndptIndex_Type()
)
atmEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptIndex.setStatus("mandatory")
_AtmEndptDesc_Type = DisplayString
_AtmEndptDesc_Object = MibTableColumn
atmEndptDesc = _AtmEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 2),
    _AtmEndptDesc_Type()
)
atmEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptDesc.setStatus("mandatory")


class _AtmOtherEndptIndex_Type(Integer32):
    """Custom type atmOtherEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AtmOtherEndptIndex_Type.__name__ = "Integer32"
_AtmOtherEndptIndex_Object = MibTableColumn
atmOtherEndptIndex = _AtmOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 3),
    _AtmOtherEndptIndex_Type()
)
atmOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOtherEndptIndex.setStatus("mandatory")
_AtmOtherEndptDesc_Type = DisplayString
_AtmOtherEndptDesc_Object = MibTableColumn
atmOtherEndptDesc = _AtmOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 4),
    _AtmOtherEndptDesc_Type()
)
atmOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOtherEndptDesc.setStatus("mandatory")


class _AtmEndptAdminStatus_Type(Integer32):
    """Custom type atmEndptAdminStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3),
          ("test", 4),
          ("writeOnly", 5))
    )


_AtmEndptAdminStatus_Type.__name__ = "Integer32"
_AtmEndptAdminStatus_Object = MibTableColumn
atmEndptAdminStatus = _AtmEndptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 5),
    _AtmEndptAdminStatus_Type()
)
atmEndptAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptAdminStatus.setStatus("mandatory")


class _AtmEndptOperStatus_Type(Integer32):
    """Custom type atmEndptOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("okPendingDown", 2),
          ("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("okPendingRoute", 6),
          ("okPendingDelete", 7),
          ("looped", 8),
          ("unknown", 9))
    )


_AtmEndptOperStatus_Type.__name__ = "Integer32"
_AtmEndptOperStatus_Object = MibTableColumn
atmEndptOperStatus = _AtmEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 6),
    _AtmEndptOperStatus_Type()
)
atmEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptOperStatus.setStatus("mandatory")


class _AtmNoRouteFoundFailure_Type(Integer32):
    """Custom type atmNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmNoRouteFoundFailure_Type.__name__ = "Integer32"
_AtmNoRouteFoundFailure_Object = MibTableColumn
atmNoRouteFoundFailure = _AtmNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 7),
    _AtmNoRouteFoundFailure_Type()
)
atmNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNoRouteFoundFailure.setStatus("mandatory")


class _AtmBumpFailure_Type(Integer32):
    """Custom type atmBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmBumpFailure_Type.__name__ = "Integer32"
_AtmBumpFailure_Object = MibTableColumn
atmBumpFailure = _AtmBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 8),
    _AtmBumpFailure_Type()
)
atmBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBumpFailure.setStatus("mandatory")


class _AtmEndPointFailure_Type(Integer32):
    """Custom type atmEndPointFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmEndPointFailure_Type.__name__ = "Integer32"
_AtmEndPointFailure_Object = MibTableColumn
atmEndPointFailure = _AtmEndPointFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 9),
    _AtmEndPointFailure_Type()
)
atmEndPointFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointFailure.setStatus("mandatory")


class _AtmTestFailure_Type(Integer32):
    """Custom type atmTestFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmTestFailure_Type.__name__ = "Integer32"
_AtmTestFailure_Object = MibTableColumn
atmTestFailure = _AtmTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 10),
    _AtmTestFailure_Type()
)
atmTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTestFailure.setStatus("mandatory")
_AtmConnPtr_Type = ObjectIdentifier
_AtmConnPtr_Object = MibTableColumn
atmConnPtr = _AtmConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 11),
    _AtmConnPtr_Type()
)
atmConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConnPtr.setStatus("mandatory")
_AtmNextPtr_Type = ObjectIdentifier
_AtmNextPtr_Object = MibTableColumn
atmNextPtr = _AtmNextPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 12),
    _AtmNextPtr_Type()
)
atmNextPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNextPtr.setStatus("deprecated")
_AtmNextOnPortPtr_Type = ObjectIdentifier
_AtmNextOnPortPtr_Object = MibTableColumn
atmNextOnPortPtr = _AtmNextOnPortPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 13),
    _AtmNextOnPortPtr_Type()
)
atmNextOnPortPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNextOnPortPtr.setStatus("mandatory")


class _AtmEndptConnDesc_Type(DisplayString):
    """Custom type atmEndptConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmEndptConnDesc_Type.__name__ = "DisplayString"
_AtmEndptConnDesc_Object = MibTableColumn
atmEndptConnDesc = _AtmEndptConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 14),
    _AtmEndptConnDesc_Type()
)
atmEndptConnDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptConnDesc.setStatus("obsolete")


class _AtmEndptTrkAvoidType_Type(Integer32):
    """Custom type atmEndptTrkAvoidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_AtmEndptTrkAvoidType_Type.__name__ = "Integer32"
_AtmEndptTrkAvoidType_Object = MibTableColumn
atmEndptTrkAvoidType = _AtmEndptTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 15),
    _AtmEndptTrkAvoidType_Type()
)
atmEndptTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTrkAvoidType.setStatus("mandatory")


class _AtmEndptTrkAvoidZCS_Type(Integer32):
    """Custom type atmEndptTrkAvoidZCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmEndptTrkAvoidZCS_Type.__name__ = "Integer32"
_AtmEndptTrkAvoidZCS_Object = MibTableColumn
atmEndptTrkAvoidZCS = _AtmEndptTrkAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 16),
    _AtmEndptTrkAvoidZCS_Type()
)
atmEndptTrkAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTrkAvoidZCS.setStatus("mandatory")


class _AtmEndptSubType_Type(Integer32):
    """Custom type atmEndptSubType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("atf", 1),
          ("vbr", 2),
          ("cbr", 3),
          ("unknown", 4),
          ("abrstd", 5),
          ("atfst", 6),
          ("atft", 7),
          ("atftfst", 8),
          ("atfx", 9),
          ("atfxfst", 10),
          ("ubr", 11),
          ("abrfst", 12))
    )


_AtmEndptSubType_Type.__name__ = "Integer32"
_AtmEndptSubType_Object = MibTableColumn
atmEndptSubType = _AtmEndptSubType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 17),
    _AtmEndptSubType_Type()
)
atmEndptSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptSubType.setStatus("mandatory")


class _AtmEndptBWClass_Type(Integer32):
    """Custom type atmEndptBWClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmEndptBWClass_Type.__name__ = "Integer32"
_AtmEndptBWClass_Object = MibTableColumn
atmEndptBWClass = _AtmEndptBWClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 18),
    _AtmEndptBWClass_Type()
)
atmEndptBWClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptBWClass.setStatus("mandatory")
_AtmEndptMIR_Type = Integer32
_AtmEndptMIR_Object = MibTableColumn
atmEndptMIR = _AtmEndptMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 19),
    _AtmEndptMIR_Type()
)
atmEndptMIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptMIR.setStatus("obsolete")
_AtmEndptCIR_Type = Integer32
_AtmEndptCIR_Object = MibTableColumn
atmEndptCIR = _AtmEndptCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 20),
    _AtmEndptCIR_Type()
)
atmEndptCIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptCIR.setStatus("obsolete")


class _AtmEndptVcQSize_Type(Integer32):
    """Custom type atmEndptVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmEndptVcQSize_Type.__name__ = "Integer32"
_AtmEndptVcQSize_Object = MibTableColumn
atmEndptVcQSize = _AtmEndptVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 21),
    _AtmEndptVcQSize_Type()
)
atmEndptVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptVcQSize.setStatus("mandatory")
_AtmEndptPIR_Type = Integer32
_AtmEndptPIR_Object = MibTableColumn
atmEndptPIR = _AtmEndptPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 22),
    _AtmEndptPIR_Type()
)
atmEndptPIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptPIR.setStatus("obsolete")


class _AtmEndptEfciQSize_Type(Integer32):
    """Custom type atmEndptEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptEfciQSize_Type.__name__ = "Integer32"
_AtmEndptEfciQSize_Object = MibTableColumn
atmEndptEfciQSize = _AtmEndptEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 23),
    _AtmEndptEfciQSize_Type()
)
atmEndptEfciQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptEfciQSize.setStatus("mandatory")


class _AtmEndptQIR_Type(Integer32):
    """Custom type atmEndptQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1412832),
    )


_AtmEndptQIR_Type.__name__ = "Integer32"
_AtmEndptQIR_Object = MibTableColumn
atmEndptQIR = _AtmEndptQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 24),
    _AtmEndptQIR_Type()
)
atmEndptQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptQIR.setStatus("mandatory")


class _AtmEndptPercUtil_Type(Integer32):
    """Custom type atmEndptPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AtmEndptPercUtil_Type.__name__ = "Integer32"
_AtmEndptPercUtil_Object = MibTableColumn
atmEndptPercUtil = _AtmEndptPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 25),
    _AtmEndptPercUtil_Type()
)
atmEndptPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPercUtil.setStatus("mandatory")


class _AtmEndptCBS_Type(Integer32):
    """Custom type atmEndptCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000000),
    )


_AtmEndptCBS_Type.__name__ = "Integer32"
_AtmEndptCBS_Object = MibTableColumn
atmEndptCBS = _AtmEndptCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 26),
    _AtmEndptCBS_Type()
)
atmEndptCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCBS.setStatus("mandatory")


class _AtmEndptIBS_Type(Integer32):
    """Custom type atmEndptIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmEndptIBS_Type.__name__ = "Integer32"
_AtmEndptIBS_Object = MibTableColumn
atmEndptIBS = _AtmEndptIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 27),
    _AtmEndptIBS_Type()
)
atmEndptIBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptIBS.setStatus("mandatory")
_AtmEndptMFS_Type = Integer32
_AtmEndptMFS_Object = MibTableColumn
atmEndptMFS = _AtmEndptMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 28),
    _AtmEndptMFS_Type()
)
atmEndptMFS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptMFS.setStatus("obsolete")


class _AtmEndptCCDV_Type(Integer32):
    """Custom type atmEndptCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_AtmEndptCCDV_Type.__name__ = "Integer32"
_AtmEndptCCDV_Object = MibTableColumn
atmEndptCCDV = _AtmEndptCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 29),
    _AtmEndptCCDV_Type()
)
atmEndptCCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCCDV.setStatus("mandatory")


class _AtmEndptHiCLP_Type(Integer32):
    """Custom type atmEndptHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptHiCLP_Type.__name__ = "Integer32"
_AtmEndptHiCLP_Object = MibTableColumn
atmEndptHiCLP = _AtmEndptHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 30),
    _AtmEndptHiCLP_Type()
)
atmEndptHiCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptHiCLP.setStatus("mandatory")


class _AtmEndptLoCLP_Type(Integer32):
    """Custom type atmEndptLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptLoCLP_Type.__name__ = "Integer32"
_AtmEndptLoCLP_Object = MibTableColumn
atmEndptLoCLP = _AtmEndptLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 31),
    _AtmEndptLoCLP_Type()
)
atmEndptLoCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptLoCLP.setStatus("mandatory")
_AtmEndptOeMIR_Type = Integer32
_AtmEndptOeMIR_Object = MibTableColumn
atmEndptOeMIR = _AtmEndptOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 32),
    _AtmEndptOeMIR_Type()
)
atmEndptOeMIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOeMIR.setStatus("obsolete")
_AtmEndptOeCIR_Type = Integer32
_AtmEndptOeCIR_Object = MibTableColumn
atmEndptOeCIR = _AtmEndptOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 33),
    _AtmEndptOeCIR_Type()
)
atmEndptOeCIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOeCIR.setStatus("obsolete")


class _AtmEndptOeVcQSize_Type(Integer32):
    """Custom type atmEndptOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmEndptOeVcQSize_Type.__name__ = "Integer32"
_AtmEndptOeVcQSize_Object = MibTableColumn
atmEndptOeVcQSize = _AtmEndptOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 34),
    _AtmEndptOeVcQSize_Type()
)
atmEndptOeVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeVcQSize.setStatus("mandatory")
_AtmEndptOePIR_Type = Integer32
_AtmEndptOePIR_Object = MibTableColumn
atmEndptOePIR = _AtmEndptOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 35),
    _AtmEndptOePIR_Type()
)
atmEndptOePIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOePIR.setStatus("obsolete")


class _AtmEndptOeEfciQSize_Type(Integer32):
    """Custom type atmEndptOeEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOeEfciQSize_Type.__name__ = "Integer32"
_AtmEndptOeEfciQSize_Object = MibTableColumn
atmEndptOeEfciQSize = _AtmEndptOeEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 36),
    _AtmEndptOeEfciQSize_Type()
)
atmEndptOeEfciQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeEfciQSize.setStatus("mandatory")


class _AtmEndptOeQIR_Type(Integer32):
    """Custom type atmEndptOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1412832),
    )


_AtmEndptOeQIR_Type.__name__ = "Integer32"
_AtmEndptOeQIR_Object = MibTableColumn
atmEndptOeQIR = _AtmEndptOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 37),
    _AtmEndptOeQIR_Type()
)
atmEndptOeQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeQIR.setStatus("mandatory")


class _AtmEndptOePercUtil_Type(Integer32):
    """Custom type atmEndptOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AtmEndptOePercUtil_Type.__name__ = "Integer32"
_AtmEndptOePercUtil_Object = MibTableColumn
atmEndptOePercUtil = _AtmEndptOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 38),
    _AtmEndptOePercUtil_Type()
)
atmEndptOePercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOePercUtil.setStatus("mandatory")


class _AtmEndptOeCBS_Type(Integer32):
    """Custom type atmEndptOeCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000000),
    )


_AtmEndptOeCBS_Type.__name__ = "Integer32"
_AtmEndptOeCBS_Object = MibTableColumn
atmEndptOeCBS = _AtmEndptOeCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 39),
    _AtmEndptOeCBS_Type()
)
atmEndptOeCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeCBS.setStatus("mandatory")


class _AtmEndptOeIBS_Type(Integer32):
    """Custom type atmEndptOeIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmEndptOeIBS_Type.__name__ = "Integer32"
_AtmEndptOeIBS_Object = MibTableColumn
atmEndptOeIBS = _AtmEndptOeIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 40),
    _AtmEndptOeIBS_Type()
)
atmEndptOeIBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeIBS.setStatus("mandatory")
_AtmEndptOeMFS_Type = Integer32
_AtmEndptOeMFS_Object = MibTableColumn
atmEndptOeMFS = _AtmEndptOeMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 41),
    _AtmEndptOeMFS_Type()
)
atmEndptOeMFS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOeMFS.setStatus("obsolete")


class _AtmEndptOeCCDV_Type(Integer32):
    """Custom type atmEndptOeCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_AtmEndptOeCCDV_Type.__name__ = "Integer32"
_AtmEndptOeCCDV_Object = MibTableColumn
atmEndptOeCCDV = _AtmEndptOeCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 42),
    _AtmEndptOeCCDV_Type()
)
atmEndptOeCCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeCCDV.setStatus("mandatory")


class _AtmEndptOeHiCLP_Type(Integer32):
    """Custom type atmEndptOeHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOeHiCLP_Type.__name__ = "Integer32"
_AtmEndptOeHiCLP_Object = MibTableColumn
atmEndptOeHiCLP = _AtmEndptOeHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 43),
    _AtmEndptOeHiCLP_Type()
)
atmEndptOeHiCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeHiCLP.setStatus("mandatory")


class _AtmEndptOeLoCLP_Type(Integer32):
    """Custom type atmEndptOeLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOeLoCLP_Type.__name__ = "Integer32"
_AtmEndptOeLoCLP_Object = MibTableColumn
atmEndptOeLoCLP = _AtmEndptOeLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 44),
    _AtmEndptOeLoCLP_Type()
)
atmEndptOeLoCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeLoCLP.setStatus("mandatory")


class _AtmEndptCLPTagging_Type(Integer32):
    """Custom type atmEndptCLPTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptCLPTagging_Type.__name__ = "Integer32"
_AtmEndptCLPTagging_Object = MibTableColumn
atmEndptCLPTagging = _AtmEndptCLPTagging_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 45),
    _AtmEndptCLPTagging_Type()
)
atmEndptCLPTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCLPTagging.setStatus("mandatory")
_AtmEndptUPC_Type = Integer32
_AtmEndptUPC_Object = MibTableColumn
atmEndptUPC = _AtmEndptUPC_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 46),
    _AtmEndptUPC_Type()
)
atmEndptUPC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptUPC.setStatus("obsolete")


class _AtmEndptEnableFST_Type(Integer32):
    """Custom type atmEndptEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptEnableFST_Type.__name__ = "Integer32"
_AtmEndptEnableFST_Object = MibTableColumn
atmEndptEnableFST = _AtmEndptEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 47),
    _AtmEndptEnableFST_Type()
)
atmEndptEnableFST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptEnableFST.setStatus("mandatory")


class _AtmEndptRateUpICA_Type(Integer32):
    """Custom type atmEndptRateUpICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412832),
    )


_AtmEndptRateUpICA_Type.__name__ = "Integer32"
_AtmEndptRateUpICA_Object = MibTableColumn
atmEndptRateUpICA = _AtmEndptRateUpICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 48),
    _AtmEndptRateUpICA_Type()
)
atmEndptRateUpICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptRateUpICA.setStatus("mandatory")


class _AtmEndptRateDnICA_Type(Integer32):
    """Custom type atmEndptRateDnICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_AtmEndptRateDnICA_Type.__name__ = "Integer32"
_AtmEndptRateDnICA_Object = MibTableColumn
atmEndptRateDnICA = _AtmEndptRateDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 49),
    _AtmEndptRateDnICA_Type()
)
atmEndptRateDnICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptRateDnICA.setStatus("mandatory")
_AtmEndptFastDnICA_Type = Integer32
_AtmEndptFastDnICA_Object = MibTableColumn
atmEndptFastDnICA = _AtmEndptFastDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 50),
    _AtmEndptFastDnICA_Type()
)
atmEndptFastDnICA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptFastDnICA.setStatus("obsolete")


class _AtmEndptToQIR_Type(Integer32):
    """Custom type atmEndptToQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(62, 255000),
    )


_AtmEndptToQIR_Type.__name__ = "Integer32"
_AtmEndptToQIR_Object = MibTableColumn
atmEndptToQIR = _AtmEndptToQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 51),
    _AtmEndptToQIR_Type()
)
atmEndptToQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptToQIR.setStatus("mandatory")


class _AtmEndptMinAdjustICA_Type(Integer32):
    """Custom type atmEndptMinAdjustICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmEndptMinAdjustICA_Type.__name__ = "Integer32"
_AtmEndptMinAdjustICA_Object = MibTableColumn
atmEndptMinAdjustICA = _AtmEndptMinAdjustICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 52),
    _AtmEndptMinAdjustICA_Type()
)
atmEndptMinAdjustICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptMinAdjustICA.setStatus("mandatory")


class _AtmEndptGroupFlag_Type(Integer32):
    """Custom type atmEndptGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmEndptGroupFlag_Type.__name__ = "Integer32"
_AtmEndptGroupFlag_Object = MibTableColumn
atmEndptGroupFlag = _AtmEndptGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 53),
    _AtmEndptGroupFlag_Type()
)
atmEndptGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptGroupFlag.setStatus("deprecated")


class _AtmEndptOamStatus_Type(Integer32):
    """Custom type atmEndptOamStatus based on Integer32"""
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
        *(("unknown", 1),
          ("clear", 2),
          ("aisDetected", 3),
          ("ferfDetected", 4))
    )


_AtmEndptOamStatus_Type.__name__ = "Integer32"
_AtmEndptOamStatus_Object = MibTableColumn
atmEndptOamStatus = _AtmEndptOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 54),
    _AtmEndptOamStatus_Type()
)
atmEndptOamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptOamStatus.setStatus("mandatory")


class _AtmEndptBCM_Type(Integer32):
    """Custom type atmEndptBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptBCM_Type.__name__ = "Integer32"
_AtmEndptBCM_Object = MibTableColumn
atmEndptBCM = _AtmEndptBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 55),
    _AtmEndptBCM_Type()
)
atmEndptBCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptBCM.setStatus("mandatory")


class _AtmEndptFGCRA_Type(Integer32):
    """Custom type atmEndptFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptFGCRA_Type.__name__ = "Integer32"
_AtmEndptFGCRA_Object = MibTableColumn
atmEndptFGCRA = _AtmEndptFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 56),
    _AtmEndptFGCRA_Type()
)
atmEndptFGCRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptFGCRA.setStatus("mandatory")


class _AtmEndptLocLpbkState_Type(Integer32):
    """Custom type atmEndptLocLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptLocLpbkState_Type.__name__ = "Integer32"
_AtmEndptLocLpbkState_Object = MibTableColumn
atmEndptLocLpbkState = _AtmEndptLocLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 57),
    _AtmEndptLocLpbkState_Type()
)
atmEndptLocLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptLocLpbkState.setStatus("mandatory")
_AtmEndptLpbkStatus_Type = Integer32
_AtmEndptLpbkStatus_Object = MibTableColumn
atmEndptLpbkStatus = _AtmEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 58),
    _AtmEndptLpbkStatus_Type()
)
atmEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptLpbkStatus.setStatus("mandatory")


class _AtmEndptTestType_Type(Integer32):
    """Custom type atmEndptTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testDelay", 1),
          ("writeOnly", 2))
    )


_AtmEndptTestType_Type.__name__ = "Integer32"
_AtmEndptTestType_Object = MibTableColumn
atmEndptTestType = _AtmEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 59),
    _AtmEndptTestType_Type()
)
atmEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTestType.setStatus("mandatory")
_AtmEndptRtdTestDelay_Type = Integer32
_AtmEndptRtdTestDelay_Object = MibTableColumn
atmEndptRtdTestDelay = _AtmEndptRtdTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 60),
    _AtmEndptRtdTestDelay_Type()
)
atmEndptRtdTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptRtdTestDelay.setStatus("mandatory")


class _AtmEndptOeBCM_Type(Integer32):
    """Custom type atmEndptOeBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptOeBCM_Type.__name__ = "Integer32"
_AtmEndptOeBCM_Object = MibTableColumn
atmEndptOeBCM = _AtmEndptOeBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 61),
    _AtmEndptOeBCM_Type()
)
atmEndptOeBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptOeBCM.setStatus("mandatory")


class _AtmEndptOeFGCRA_Type(Integer32):
    """Custom type atmEndptOeFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptOeFGCRA_Type.__name__ = "Integer32"
_AtmEndptOeFGCRA_Object = MibTableColumn
atmEndptOeFGCRA = _AtmEndptOeFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 62),
    _AtmEndptOeFGCRA_Type()
)
atmEndptOeFGCRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptOeFGCRA.setStatus("mandatory")
_AtmEndptGroupDesc_Type = DisplayString
_AtmEndptGroupDesc_Object = MibTableColumn
atmEndptGroupDesc = _AtmEndptGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 63),
    _AtmEndptGroupDesc_Type()
)
atmEndptGroupDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptGroupDesc.setStatus("obsolete")


class _AtmEndptLocRmtLpbkState_Type(Integer32):
    """Custom type atmEndptLocRmtLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptLocRmtLpbkState_Type.__name__ = "Integer32"
_AtmEndptLocRmtLpbkState_Object = MibTableColumn
atmEndptLocRmtLpbkState = _AtmEndptLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 64),
    _AtmEndptLocRmtLpbkState_Type()
)
atmEndptLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptLocRmtLpbkState.setStatus("mandatory")
_AtmEndptScrPlc_Type = Integer32
_AtmEndptScrPlc_Object = MibTableColumn
atmEndptScrPlc = _AtmEndptScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 65),
    _AtmEndptScrPlc_Type()
)
atmEndptScrPlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptScrPlc.setStatus("obsolete")
_AtmEndptOeScrPlc_Type = Integer32
_AtmEndptOeScrPlc_Object = MibTableColumn
atmEndptOeScrPlc = _AtmEndptOeScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 66),
    _AtmEndptOeScrPlc_Type()
)
atmEndptOeScrPlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOeScrPlc.setStatus("obsolete")
_AtmEndptPCR0_Type = Integer32
_AtmEndptPCR0_Object = MibTableColumn
atmEndptPCR0 = _AtmEndptPCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 67),
    _AtmEndptPCR0_Type()
)
atmEndptPCR0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptPCR0.setStatus("obsolete")
_AtmEndptOePCR0_Type = Integer32
_AtmEndptOePCR0_Object = MibTableColumn
atmEndptOePCR0 = _AtmEndptOePCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 68),
    _AtmEndptOePCR0_Type()
)
atmEndptOePCR0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOePCR0.setStatus("obsolete")
_AtmEndptCDVT0_Type = Integer32
_AtmEndptCDVT0_Object = MibTableColumn
atmEndptCDVT0 = _AtmEndptCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 69),
    _AtmEndptCDVT0_Type()
)
atmEndptCDVT0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptCDVT0.setStatus("obsolete")
_AtmEndptOeCDVT0_Type = Integer32
_AtmEndptOeCDVT0_Object = MibTableColumn
atmEndptOeCDVT0 = _AtmEndptOeCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 70),
    _AtmEndptOeCDVT0_Type()
)
atmEndptOeCDVT0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmEndptOeCDVT0.setStatus("obsolete")


class _AtmEndptNRM_Type(Integer32):
    """Custom type atmEndptNRM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_AtmEndptNRM_Type.__name__ = "Integer32"
_AtmEndptNRM_Object = MibTableColumn
atmEndptNRM = _AtmEndptNRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 71),
    _AtmEndptNRM_Type()
)
atmEndptNRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptNRM.setStatus("mandatory")


class _AtmEndptFRTT_Type(Integer32):
    """Custom type atmEndptFRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16700),
    )


_AtmEndptFRTT_Type.__name__ = "Integer32"
_AtmEndptFRTT_Object = MibTableColumn
atmEndptFRTT = _AtmEndptFRTT_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 72),
    _AtmEndptFRTT_Type()
)
atmEndptFRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptFRTT.setStatus("mandatory")


class _AtmEndptTBE_Type(Integer32):
    """Custom type atmEndptTBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048320),
    )


_AtmEndptTBE_Type.__name__ = "Integer32"
_AtmEndptTBE_Object = MibTableColumn
atmEndptTBE = _AtmEndptTBE_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 73),
    _AtmEndptTBE_Type()
)
atmEndptTBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTBE.setStatus("mandatory")


class _AtmEndptVSVD_Type(Integer32):
    """Custom type atmEndptVSVD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptVSVD_Type.__name__ = "Integer32"
_AtmEndptVSVD_Object = MibTableColumn
atmEndptVSVD = _AtmEndptVSVD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 74),
    _AtmEndptVSVD_Type()
)
atmEndptVSVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptVSVD.setStatus("mandatory")


class _AtmEndptPolicing_Type(Integer32):
    """Custom type atmEndptPolicing based on Integer32"""
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
        *(("vbr1", 1),
          ("vbr2", 2),
          ("vbr3", 3),
          ("pcrplc", 4),
          ("none", 5))
    )


_AtmEndptPolicing_Type.__name__ = "Integer32"
_AtmEndptPolicing_Object = MibTableColumn
atmEndptPolicing = _AtmEndptPolicing_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 75),
    _AtmEndptPolicing_Type()
)
atmEndptPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPolicing.setStatus("mandatory")


class _AtmEndptPCR_Type(Integer32):
    """Custom type atmEndptPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1412832),
    )


_AtmEndptPCR_Type.__name__ = "Integer32"
_AtmEndptPCR_Object = MibTableColumn
atmEndptPCR = _AtmEndptPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 76),
    _AtmEndptPCR_Type()
)
atmEndptPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPCR.setStatus("mandatory")


class _AtmEndptOePCR_Type(Integer32):
    """Custom type atmEndptOePCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1412832),
    )


_AtmEndptOePCR_Type.__name__ = "Integer32"
_AtmEndptOePCR_Object = MibTableColumn
atmEndptOePCR = _AtmEndptOePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 77),
    _AtmEndptOePCR_Type()
)
atmEndptOePCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOePCR.setStatus("mandatory")


class _AtmEndptSCR_Type(Integer32):
    """Custom type atmEndptSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 1412832),
    )


_AtmEndptSCR_Type.__name__ = "Integer32"
_AtmEndptSCR_Object = MibTableColumn
atmEndptSCR = _AtmEndptSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 78),
    _AtmEndptSCR_Type()
)
atmEndptSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptSCR.setStatus("mandatory")


class _AtmEndptOeSCR_Type(Integer32):
    """Custom type atmEndptOeSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 1412832),
    )


_AtmEndptOeSCR_Type.__name__ = "Integer32"
_AtmEndptOeSCR_Object = MibTableColumn
atmEndptOeSCR = _AtmEndptOeSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 79),
    _AtmEndptOeSCR_Type()
)
atmEndptOeSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeSCR.setStatus("mandatory")


class _AtmEndptMCR_Type(Integer32):
    """Custom type atmEndptMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412832),
    )


_AtmEndptMCR_Type.__name__ = "Integer32"
_AtmEndptMCR_Object = MibTableColumn
atmEndptMCR = _AtmEndptMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 80),
    _AtmEndptMCR_Type()
)
atmEndptMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptMCR.setStatus("mandatory")


class _AtmEndptOeMCR_Type(Integer32):
    """Custom type atmEndptOeMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412832),
    )


_AtmEndptOeMCR_Type.__name__ = "Integer32"
_AtmEndptOeMCR_Object = MibTableColumn
atmEndptOeMCR = _AtmEndptOeMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 81),
    _AtmEndptOeMCR_Type()
)
atmEndptOeMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeMCR.setStatus("mandatory")


class _AtmEndptCellRouting_Type(Integer32):
    """Custom type atmEndptCellRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndptCellRouting_Type.__name__ = "Integer32"
_AtmEndptCellRouting_Object = MibTableColumn
atmEndptCellRouting = _AtmEndptCellRouting_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 82),
    _AtmEndptCellRouting_Type()
)
atmEndptCellRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCellRouting.setStatus("mandatory")
_AtmBwClassTable_Object = MibTable
atmBwClassTable = _AtmBwClassTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9)
)
if mibBuilder.loadTexts:
    atmBwClassTable.setStatus("mandatory")
_AtmBwClassEntry_Object = MibTableRow
atmBwClassEntry = _AtmBwClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1)
)
atmBwClassEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmBwClassIndex"),
)
if mibBuilder.loadTexts:
    atmBwClassEntry.setStatus("mandatory")


class _AtmBwClassIndex_Type(Integer32):
    """Custom type atmBwClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmBwClassIndex_Type.__name__ = "Integer32"
_AtmBwClassIndex_Object = MibTableColumn
atmBwClassIndex = _AtmBwClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 1),
    _AtmBwClassIndex_Type()
)
atmBwClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassIndex.setStatus("mandatory")
_AtmBwClassMIR_Type = Integer32
_AtmBwClassMIR_Object = MibTableColumn
atmBwClassMIR = _AtmBwClassMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 2),
    _AtmBwClassMIR_Type()
)
atmBwClassMIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassMIR.setStatus("obsolete")
_AtmBwClassCIR_Type = Integer32
_AtmBwClassCIR_Object = MibTableColumn
atmBwClassCIR = _AtmBwClassCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 3),
    _AtmBwClassCIR_Type()
)
atmBwClassCIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassCIR.setStatus("obsolete")


class _AtmBwClassVcQSize_Type(Integer32):
    """Custom type atmBwClassVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmBwClassVcQSize_Type.__name__ = "Integer32"
_AtmBwClassVcQSize_Object = MibTableColumn
atmBwClassVcQSize = _AtmBwClassVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 4),
    _AtmBwClassVcQSize_Type()
)
atmBwClassVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassVcQSize.setStatus("mandatory")
_AtmBwClassPIR_Type = Integer32
_AtmBwClassPIR_Object = MibTableColumn
atmBwClassPIR = _AtmBwClassPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 5),
    _AtmBwClassPIR_Type()
)
atmBwClassPIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassPIR.setStatus("obsolete")


class _AtmBwClassEfciQSize_Type(Integer32):
    """Custom type atmBwClassEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassEfciQSize_Type.__name__ = "Integer32"
_AtmBwClassEfciQSize_Object = MibTableColumn
atmBwClassEfciQSize = _AtmBwClassEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 6),
    _AtmBwClassEfciQSize_Type()
)
atmBwClassEfciQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassEfciQSize.setStatus("mandatory")


class _AtmBwClassQIR_Type(Integer32):
    """Custom type atmBwClassQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000),
    )


_AtmBwClassQIR_Type.__name__ = "Integer32"
_AtmBwClassQIR_Object = MibTableColumn
atmBwClassQIR = _AtmBwClassQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 7),
    _AtmBwClassQIR_Type()
)
atmBwClassQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassQIR.setStatus("mandatory")


class _AtmBwClassPercUtil_Type(Integer32):
    """Custom type atmBwClassPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassPercUtil_Type.__name__ = "Integer32"
_AtmBwClassPercUtil_Object = MibTableColumn
atmBwClassPercUtil = _AtmBwClassPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 8),
    _AtmBwClassPercUtil_Type()
)
atmBwClassPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassPercUtil.setStatus("mandatory")


class _AtmBwClassCBS_Type(Integer32):
    """Custom type atmBwClassCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmBwClassCBS_Type.__name__ = "Integer32"
_AtmBwClassCBS_Object = MibTableColumn
atmBwClassCBS = _AtmBwClassCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 9),
    _AtmBwClassCBS_Type()
)
atmBwClassCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCBS.setStatus("mandatory")


class _AtmBwClassIBS_Type(Integer32):
    """Custom type atmBwClassIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmBwClassIBS_Type.__name__ = "Integer32"
_AtmBwClassIBS_Object = MibTableColumn
atmBwClassIBS = _AtmBwClassIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 10),
    _AtmBwClassIBS_Type()
)
atmBwClassIBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassIBS.setStatus("mandatory")


class _AtmBwClassMFS_Type(Integer32):
    """Custom type atmBwClassMFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmBwClassMFS_Type.__name__ = "Integer32"
_AtmBwClassMFS_Object = MibTableColumn
atmBwClassMFS = _AtmBwClassMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 11),
    _AtmBwClassMFS_Type()
)
atmBwClassMFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassMFS.setStatus("deprecated")


class _AtmBwClassCCDV_Type(Integer32):
    """Custom type atmBwClassCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_AtmBwClassCCDV_Type.__name__ = "Integer32"
_AtmBwClassCCDV_Object = MibTableColumn
atmBwClassCCDV = _AtmBwClassCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 12),
    _AtmBwClassCCDV_Type()
)
atmBwClassCCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCCDV.setStatus("mandatory")


class _AtmBwClassHiCLP_Type(Integer32):
    """Custom type atmBwClassHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassHiCLP_Type.__name__ = "Integer32"
_AtmBwClassHiCLP_Object = MibTableColumn
atmBwClassHiCLP = _AtmBwClassHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 13),
    _AtmBwClassHiCLP_Type()
)
atmBwClassHiCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassHiCLP.setStatus("mandatory")


class _AtmBwClassLoCLP_Type(Integer32):
    """Custom type atmBwClassLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassLoCLP_Type.__name__ = "Integer32"
_AtmBwClassLoCLP_Object = MibTableColumn
atmBwClassLoCLP = _AtmBwClassLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 14),
    _AtmBwClassLoCLP_Type()
)
atmBwClassLoCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassLoCLP.setStatus("mandatory")
_AtmBwClassOeMIR_Type = Integer32
_AtmBwClassOeMIR_Object = MibTableColumn
atmBwClassOeMIR = _AtmBwClassOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 15),
    _AtmBwClassOeMIR_Type()
)
atmBwClassOeMIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassOeMIR.setStatus("obsolete")
_AtmBwClassOeCIR_Type = Integer32
_AtmBwClassOeCIR_Object = MibTableColumn
atmBwClassOeCIR = _AtmBwClassOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 16),
    _AtmBwClassOeCIR_Type()
)
atmBwClassOeCIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassOeCIR.setStatus("obsolete")


class _AtmBwClassOeVcQSize_Type(Integer32):
    """Custom type atmBwClassOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmBwClassOeVcQSize_Type.__name__ = "Integer32"
_AtmBwClassOeVcQSize_Object = MibTableColumn
atmBwClassOeVcQSize = _AtmBwClassOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 17),
    _AtmBwClassOeVcQSize_Type()
)
atmBwClassOeVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeVcQSize.setStatus("mandatory")
_AtmBwClassOePIR_Type = Integer32
_AtmBwClassOePIR_Object = MibTableColumn
atmBwClassOePIR = _AtmBwClassOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 18),
    _AtmBwClassOePIR_Type()
)
atmBwClassOePIR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassOePIR.setStatus("obsolete")


class _AtmBwClassOeEfciQSize_Type(Integer32):
    """Custom type atmBwClassOeEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOeEfciQSize_Type.__name__ = "Integer32"
_AtmBwClassOeEfciQSize_Object = MibTableColumn
atmBwClassOeEfciQSize = _AtmBwClassOeEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 19),
    _AtmBwClassOeEfciQSize_Type()
)
atmBwClassOeEfciQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeEfciQSize.setStatus("mandatory")


class _AtmBwClassOeQIR_Type(Integer32):
    """Custom type atmBwClassOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000),
    )


_AtmBwClassOeQIR_Type.__name__ = "Integer32"
_AtmBwClassOeQIR_Object = MibTableColumn
atmBwClassOeQIR = _AtmBwClassOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 20),
    _AtmBwClassOeQIR_Type()
)
atmBwClassOeQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeQIR.setStatus("mandatory")


class _AtmBwClassOePercUtil_Type(Integer32):
    """Custom type atmBwClassOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOePercUtil_Type.__name__ = "Integer32"
_AtmBwClassOePercUtil_Object = MibTableColumn
atmBwClassOePercUtil = _AtmBwClassOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 21),
    _AtmBwClassOePercUtil_Type()
)
atmBwClassOePercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOePercUtil.setStatus("mandatory")


class _AtmBwClassOeCBS_Type(Integer32):
    """Custom type atmBwClassOeCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmBwClassOeCBS_Type.__name__ = "Integer32"
_AtmBwClassOeCBS_Object = MibTableColumn
atmBwClassOeCBS = _AtmBwClassOeCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 22),
    _AtmBwClassOeCBS_Type()
)
atmBwClassOeCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeCBS.setStatus("mandatory")


class _AtmBwClassOeIBS_Type(Integer32):
    """Custom type atmBwClassOeIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmBwClassOeIBS_Type.__name__ = "Integer32"
_AtmBwClassOeIBS_Object = MibTableColumn
atmBwClassOeIBS = _AtmBwClassOeIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 23),
    _AtmBwClassOeIBS_Type()
)
atmBwClassOeIBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeIBS.setStatus("mandatory")


class _AtmBwClassOeMFS_Type(Integer32):
    """Custom type atmBwClassOeMFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmBwClassOeMFS_Type.__name__ = "Integer32"
_AtmBwClassOeMFS_Object = MibTableColumn
atmBwClassOeMFS = _AtmBwClassOeMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 24),
    _AtmBwClassOeMFS_Type()
)
atmBwClassOeMFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeMFS.setStatus("deprecated")


class _AtmBwClassOeCCDV_Type(Integer32):
    """Custom type atmBwClassOeCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_AtmBwClassOeCCDV_Type.__name__ = "Integer32"
_AtmBwClassOeCCDV_Object = MibTableColumn
atmBwClassOeCCDV = _AtmBwClassOeCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 25),
    _AtmBwClassOeCCDV_Type()
)
atmBwClassOeCCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeCCDV.setStatus("mandatory")


class _AtmBwClassOeHiCLP_Type(Integer32):
    """Custom type atmBwClassOeHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOeHiCLP_Type.__name__ = "Integer32"
_AtmBwClassOeHiCLP_Object = MibTableColumn
atmBwClassOeHiCLP = _AtmBwClassOeHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 26),
    _AtmBwClassOeHiCLP_Type()
)
atmBwClassOeHiCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeHiCLP.setStatus("mandatory")


class _AtmBwClassOeLoCLP_Type(Integer32):
    """Custom type atmBwClassOeLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOeLoCLP_Type.__name__ = "Integer32"
_AtmBwClassOeLoCLP_Object = MibTableColumn
atmBwClassOeLoCLP = _AtmBwClassOeLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 27),
    _AtmBwClassOeLoCLP_Type()
)
atmBwClassOeLoCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeLoCLP.setStatus("mandatory")


class _AtmBwClassCLPTagging_Type(Integer32):
    """Custom type atmBwClassCLPTagging based on Integer32"""
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


_AtmBwClassCLPTagging_Type.__name__ = "Integer32"
_AtmBwClassCLPTagging_Object = MibTableColumn
atmBwClassCLPTagging = _AtmBwClassCLPTagging_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 28),
    _AtmBwClassCLPTagging_Type()
)
atmBwClassCLPTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCLPTagging.setStatus("mandatory")


class _AtmBwClassUPC_Type(Integer32):
    """Custom type atmBwClassUPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBwClassUPC_Type.__name__ = "Integer32"
_AtmBwClassUPC_Object = MibTableColumn
atmBwClassUPC = _AtmBwClassUPC_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 29),
    _AtmBwClassUPC_Type()
)
atmBwClassUPC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassUPC.setStatus("obsolete")


class _AtmBwClassEnableFST_Type(Integer32):
    """Custom type atmBwClassEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBwClassEnableFST_Type.__name__ = "Integer32"
_AtmBwClassEnableFST_Object = MibTableColumn
atmBwClassEnableFST = _AtmBwClassEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 30),
    _AtmBwClassEnableFST_Type()
)
atmBwClassEnableFST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassEnableFST.setStatus("mandatory")


class _AtmBwClassRateUpICA_Type(Integer32):
    """Custom type atmBwClassRateUpICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_AtmBwClassRateUpICA_Type.__name__ = "Integer32"
_AtmBwClassRateUpICA_Object = MibTableColumn
atmBwClassRateUpICA = _AtmBwClassRateUpICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 31),
    _AtmBwClassRateUpICA_Type()
)
atmBwClassRateUpICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassRateUpICA.setStatus("mandatory")


class _AtmBwClassRateDnICA_Type(Integer32):
    """Custom type atmBwClassRateDnICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassRateDnICA_Type.__name__ = "Integer32"
_AtmBwClassRateDnICA_Object = MibTableColumn
atmBwClassRateDnICA = _AtmBwClassRateDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 32),
    _AtmBwClassRateDnICA_Type()
)
atmBwClassRateDnICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassRateDnICA.setStatus("mandatory")
_AtmBwClassFastDnICA_Type = Integer32
_AtmBwClassFastDnICA_Object = MibTableColumn
atmBwClassFastDnICA = _AtmBwClassFastDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 33),
    _AtmBwClassFastDnICA_Type()
)
atmBwClassFastDnICA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassFastDnICA.setStatus("obsolete")


class _AtmBwClassToQIR_Type(Integer32):
    """Custom type atmBwClassToQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmBwClassToQIR_Type.__name__ = "Integer32"
_AtmBwClassToQIR_Object = MibTableColumn
atmBwClassToQIR = _AtmBwClassToQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 34),
    _AtmBwClassToQIR_Type()
)
atmBwClassToQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassToQIR.setStatus("mandatory")


class _AtmBwClassMinAdjustICA_Type(Integer32):
    """Custom type atmBwClassMinAdjustICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 250),
    )


_AtmBwClassMinAdjustICA_Type.__name__ = "Integer32"
_AtmBwClassMinAdjustICA_Object = MibTableColumn
atmBwClassMinAdjustICA = _AtmBwClassMinAdjustICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 35),
    _AtmBwClassMinAdjustICA_Type()
)
atmBwClassMinAdjustICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassMinAdjustICA.setStatus("mandatory")


class _AtmBwClassDescription_Type(DisplayString):
    """Custom type atmBwClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AtmBwClassDescription_Type.__name__ = "DisplayString"
_AtmBwClassDescription_Object = MibTableColumn
atmBwClassDescription = _AtmBwClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 36),
    _AtmBwClassDescription_Type()
)
atmBwClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassDescription.setStatus("mandatory")


class _AtmBwClassBCM_Type(Integer32):
    """Custom type atmBwClassBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBwClassBCM_Type.__name__ = "Integer32"
_AtmBwClassBCM_Object = MibTableColumn
atmBwClassBCM = _AtmBwClassBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 37),
    _AtmBwClassBCM_Type()
)
atmBwClassBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassBCM.setStatus("mandatory")


class _AtmBwClassFGCRA_Type(Integer32):
    """Custom type atmBwClassFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBwClassFGCRA_Type.__name__ = "Integer32"
_AtmBwClassFGCRA_Object = MibTableColumn
atmBwClassFGCRA = _AtmBwClassFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 38),
    _AtmBwClassFGCRA_Type()
)
atmBwClassFGCRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassFGCRA.setStatus("mandatory")


class _AtmBwClassOeBCM_Type(Integer32):
    """Custom type atmBwClassOeBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBwClassOeBCM_Type.__name__ = "Integer32"
_AtmBwClassOeBCM_Object = MibTableColumn
atmBwClassOeBCM = _AtmBwClassOeBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 39),
    _AtmBwClassOeBCM_Type()
)
atmBwClassOeBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeBCM.setStatus("mandatory")


class _AtmBwClassOeFGCRA_Type(Integer32):
    """Custom type atmBwClassOeFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBwClassOeFGCRA_Type.__name__ = "Integer32"
_AtmBwClassOeFGCRA_Object = MibTableColumn
atmBwClassOeFGCRA = _AtmBwClassOeFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 40),
    _AtmBwClassOeFGCRA_Type()
)
atmBwClassOeFGCRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeFGCRA.setStatus("mandatory")


class _AtmBwClassConType_Type(Integer32):
    """Custom type atmBwClassConType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atf", 1),
          ("vbr", 2),
          ("cbr", 3),
          ("unknown", 4),
          ("abr", 5),
          ("atft", 6),
          ("atfx", 7))
    )


_AtmBwClassConType_Type.__name__ = "Integer32"
_AtmBwClassConType_Object = MibTableColumn
atmBwClassConType = _AtmBwClassConType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 41),
    _AtmBwClassConType_Type()
)
atmBwClassConType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassConType.setStatus("mandatory")
_AtmBwClassScrPlc_Type = Integer32
_AtmBwClassScrPlc_Object = MibTableColumn
atmBwClassScrPlc = _AtmBwClassScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 42),
    _AtmBwClassScrPlc_Type()
)
atmBwClassScrPlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassScrPlc.setStatus("obsolete")
_AtmBwClassOeScrPlc_Type = Integer32
_AtmBwClassOeScrPlc_Object = MibTableColumn
atmBwClassOeScrPlc = _AtmBwClassOeScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 43),
    _AtmBwClassOeScrPlc_Type()
)
atmBwClassOeScrPlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassOeScrPlc.setStatus("obsolete")
_AtmBwClassPCR0_Type = Integer32
_AtmBwClassPCR0_Object = MibTableColumn
atmBwClassPCR0 = _AtmBwClassPCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 44),
    _AtmBwClassPCR0_Type()
)
atmBwClassPCR0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassPCR0.setStatus("obsolete")
_AtmBwClassOePCR0_Type = Integer32
_AtmBwClassOePCR0_Object = MibTableColumn
atmBwClassOePCR0 = _AtmBwClassOePCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 45),
    _AtmBwClassOePCR0_Type()
)
atmBwClassOePCR0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassOePCR0.setStatus("obsolete")
_AtmBwClassCDVT0_Type = Integer32
_AtmBwClassCDVT0_Object = MibTableColumn
atmBwClassCDVT0 = _AtmBwClassCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 46),
    _AtmBwClassCDVT0_Type()
)
atmBwClassCDVT0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassCDVT0.setStatus("obsolete")
_AtmBwClassOeCDVT0_Type = Integer32
_AtmBwClassOeCDVT0_Object = MibTableColumn
atmBwClassOeCDVT0 = _AtmBwClassOeCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 47),
    _AtmBwClassOeCDVT0_Type()
)
atmBwClassOeCDVT0.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmBwClassOeCDVT0.setStatus("obsolete")
_AtmBWClassNRM_Type = Integer32
_AtmBWClassNRM_Object = MibTableColumn
atmBWClassNRM = _AtmBWClassNRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 48),
    _AtmBWClassNRM_Type()
)
atmBWClassNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassNRM.setStatus("mandatory")
_AtmBWClassFRTT_Type = Integer32
_AtmBWClassFRTT_Object = MibTableColumn
atmBWClassFRTT = _AtmBWClassFRTT_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 49),
    _AtmBWClassFRTT_Type()
)
atmBWClassFRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassFRTT.setStatus("mandatory")
_AtmBWClassTBE_Type = Integer32
_AtmBWClassTBE_Object = MibTableColumn
atmBWClassTBE = _AtmBWClassTBE_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 50),
    _AtmBWClassTBE_Type()
)
atmBWClassTBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassTBE.setStatus("mandatory")


class _AtmBWClassVSVD_Type(Integer32):
    """Custom type atmBWClassVSVD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmBWClassVSVD_Type.__name__ = "Integer32"
_AtmBWClassVSVD_Object = MibTableColumn
atmBWClassVSVD = _AtmBWClassVSVD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 51),
    _AtmBWClassVSVD_Type()
)
atmBWClassVSVD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassVSVD.setStatus("mandatory")


class _AtmBWClassPolicing_Type(Integer32):
    """Custom type atmBWClassPolicing based on Integer32"""
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
        *(("vbr1", 1),
          ("vbr2", 2),
          ("vbr3", 3),
          ("pcrplc", 4),
          ("none", 5))
    )


_AtmBWClassPolicing_Type.__name__ = "Integer32"
_AtmBWClassPolicing_Object = MibTableColumn
atmBWClassPolicing = _AtmBWClassPolicing_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 52),
    _AtmBWClassPolicing_Type()
)
atmBWClassPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmBWClassPolicing.setStatus("mandatory")
_AtmBWClassPCR_Type = Integer32
_AtmBWClassPCR_Object = MibTableColumn
atmBWClassPCR = _AtmBWClassPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 53),
    _AtmBWClassPCR_Type()
)
atmBWClassPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassPCR.setStatus("mandatory")
_AtmBWClassOePCR_Type = Integer32
_AtmBWClassOePCR_Object = MibTableColumn
atmBWClassOePCR = _AtmBWClassOePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 54),
    _AtmBWClassOePCR_Type()
)
atmBWClassOePCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassOePCR.setStatus("mandatory")
_AtmBWClassSCR_Type = Integer32
_AtmBWClassSCR_Object = MibTableColumn
atmBWClassSCR = _AtmBWClassSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 55),
    _AtmBWClassSCR_Type()
)
atmBWClassSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassSCR.setStatus("mandatory")
_AtmBWClassOeSCR_Type = Integer32
_AtmBWClassOeSCR_Object = MibTableColumn
atmBWClassOeSCR = _AtmBWClassOeSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 56),
    _AtmBWClassOeSCR_Type()
)
atmBWClassOeSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassOeSCR.setStatus("mandatory")
_AtmBWClassMCR_Type = Integer32
_AtmBWClassMCR_Object = MibTableColumn
atmBWClassMCR = _AtmBWClassMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 57),
    _AtmBWClassMCR_Type()
)
atmBWClassMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassMCR.setStatus("mandatory")
_AtmBWClassOeMCR_Type = Integer32
_AtmBWClassOeMCR_Object = MibTableColumn
atmBWClassOeMCR = _AtmBWClassOeMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 58),
    _AtmBWClassOeMCR_Type()
)
atmBWClassOeMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBWClassOeMCR.setStatus("mandatory")
_FrEndptMapTable_Object = MibTable
frEndptMapTable = _FrEndptMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10)
)
if mibBuilder.loadTexts:
    frEndptMapTable.setStatus("mandatory")
_FrEndptMapEntry_Object = MibTableRow
frEndptMapEntry = _FrEndptMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1)
)
frEndptMapEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndptMapSlot"),
    (0, "STRATACOM-MIB", "frEndptMapPort"),
    (0, "STRATACOM-MIB", "frEndptMapDlci"),
)
if mibBuilder.loadTexts:
    frEndptMapEntry.setStatus("mandatory")


class _FrEndptMapSlot_Type(Integer32):
    """Custom type frEndptMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrEndptMapSlot_Type.__name__ = "Integer32"
_FrEndptMapSlot_Object = MibTableColumn
frEndptMapSlot = _FrEndptMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 1),
    _FrEndptMapSlot_Type()
)
frEndptMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapSlot.setStatus("mandatory")


class _FrEndptMapPort_Type(Integer32):
    """Custom type frEndptMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrEndptMapPort_Type.__name__ = "Integer32"
_FrEndptMapPort_Object = MibTableColumn
frEndptMapPort = _FrEndptMapPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 2),
    _FrEndptMapPort_Type()
)
frEndptMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapPort.setStatus("mandatory")
_FrEndptMapDlci_Type = Integer32
_FrEndptMapDlci_Object = MibTableColumn
frEndptMapDlci = _FrEndptMapDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 3),
    _FrEndptMapDlci_Type()
)
frEndptMapDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapDlci.setStatus("mandatory")
_FrEndptMapEndptPtr_Type = ObjectIdentifier
_FrEndptMapEndptPtr_Object = MibTableColumn
frEndptMapEndptPtr = _FrEndptMapEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 4),
    _FrEndptMapEndptPtr_Type()
)
frEndptMapEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapEndptPtr.setStatus("mandatory")
_FrEndptMapConnPtr_Type = ObjectIdentifier
_FrEndptMapConnPtr_Object = MibTableColumn
frEndptMapConnPtr = _FrEndptMapConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 5),
    _FrEndptMapConnPtr_Type()
)
frEndptMapConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapConnPtr.setStatus("mandatory")
_AtmEndptMapTable_Object = MibTable
atmEndptMapTable = _AtmEndptMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11)
)
if mibBuilder.loadTexts:
    atmEndptMapTable.setStatus("mandatory")
_AtmEndptMapEntry_Object = MibTableRow
atmEndptMapEntry = _AtmEndptMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1)
)
atmEndptMapEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndptMapSlot"),
    (0, "STRATACOM-MIB", "atmEndptMapPort"),
    (0, "STRATACOM-MIB", "atmEndptMapVpi"),
    (0, "STRATACOM-MIB", "atmEndptMapVci"),
)
if mibBuilder.loadTexts:
    atmEndptMapEntry.setStatus("mandatory")


class _AtmEndptMapSlot_Type(Integer32):
    """Custom type atmEndptMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmEndptMapSlot_Type.__name__ = "Integer32"
_AtmEndptMapSlot_Object = MibTableColumn
atmEndptMapSlot = _AtmEndptMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 1),
    _AtmEndptMapSlot_Type()
)
atmEndptMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapSlot.setStatus("mandatory")


class _AtmEndptMapPort_Type(Integer32):
    """Custom type atmEndptMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmEndptMapPort_Type.__name__ = "Integer32"
_AtmEndptMapPort_Object = MibTableColumn
atmEndptMapPort = _AtmEndptMapPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 2),
    _AtmEndptMapPort_Type()
)
atmEndptMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapPort.setStatus("mandatory")
_AtmEndptMapVpi_Type = Integer32
_AtmEndptMapVpi_Object = MibTableColumn
atmEndptMapVpi = _AtmEndptMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 3),
    _AtmEndptMapVpi_Type()
)
atmEndptMapVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapVpi.setStatus("mandatory")
_AtmEndptMapVci_Type = Integer32
_AtmEndptMapVci_Object = MibTableColumn
atmEndptMapVci = _AtmEndptMapVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 4),
    _AtmEndptMapVci_Type()
)
atmEndptMapVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapVci.setStatus("mandatory")
_AtmEndptMapEndptPtr_Type = ObjectIdentifier
_AtmEndptMapEndptPtr_Object = MibTableColumn
atmEndptMapEndptPtr = _AtmEndptMapEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 5),
    _AtmEndptMapEndptPtr_Type()
)
atmEndptMapEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapEndptPtr.setStatus("mandatory")
_AtmEndptMapConnPtr_Type = ObjectIdentifier
_AtmEndptMapConnPtr_Object = MibTableColumn
atmEndptMapConnPtr = _AtmEndptMapConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 6),
    _AtmEndptMapConnPtr_Type()
)
atmEndptMapConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapConnPtr.setStatus("mandatory")
_AtmEndptStatTable_Object = MibTable
atmEndptStatTable = _AtmEndptStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12)
)
if mibBuilder.loadTexts:
    atmEndptStatTable.setStatus("mandatory")
_AtmEndptStatEntry_Object = MibTableRow
atmEndptStatEntry = _AtmEndptStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1)
)
atmEndptStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndptIndex"),
)
if mibBuilder.loadTexts:
    atmEndptStatEntry.setStatus("mandatory")
_AtmCellsRxPorts_Type = Counter32
_AtmCellsRxPorts_Object = MibTableColumn
atmCellsRxPorts = _AtmCellsRxPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 1),
    _AtmCellsRxPorts_Type()
)
atmCellsRxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsRxPorts.setStatus("mandatory")
_AtmFramesRxPorts_Type = Counter32
_AtmFramesRxPorts_Object = MibTableColumn
atmFramesRxPorts = _AtmFramesRxPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 2),
    _AtmFramesRxPorts_Type()
)
atmFramesRxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFramesRxPorts.setStatus("mandatory")
_AtmCellsTxNets_Type = Counter32
_AtmCellsTxNets_Object = MibTableColumn
atmCellsTxNets = _AtmCellsTxNets_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 3),
    _AtmCellsTxNets_Type()
)
atmCellsTxNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsTxNets.setStatus("mandatory")
_AtmClpRxs_Type = Counter32
_AtmClpRxs_Object = MibTableColumn
atmClpRxs = _AtmClpRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 4),
    _AtmClpRxs_Type()
)
atmClpRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmClpRxs.setStatus("mandatory")
_AtmViolRxs_Type = Counter32
_AtmViolRxs_Object = MibTableColumn
atmViolRxs = _AtmViolRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 5),
    _AtmViolRxs_Type()
)
atmViolRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmViolRxs.setStatus("mandatory")
_AtmDiscardVcqClpThs_Type = Counter32
_AtmDiscardVcqClpThs_Object = MibTableColumn
atmDiscardVcqClpThs = _AtmDiscardVcqClpThs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 6),
    _AtmDiscardVcqClpThs_Type()
)
atmDiscardVcqClpThs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardVcqClpThs.setStatus("mandatory")
_AtmDiscardVcqFulls_Type = Counter32
_AtmDiscardVcqFulls_Object = MibTableColumn
atmDiscardVcqFulls = _AtmDiscardVcqFulls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 7),
    _AtmDiscardVcqFulls_Type()
)
atmDiscardVcqFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardVcqFulls.setStatus("mandatory")
_AtmEfciRxs_Type = Counter32
_AtmEfciRxs_Object = MibTableColumn
atmEfciRxs = _AtmEfciRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 8),
    _AtmEfciRxs_Type()
)
atmEfciRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEfciRxs.setStatus("mandatory")
_AtmNonCompRxs_Type = Counter32
_AtmNonCompRxs_Object = MibTableColumn
atmNonCompRxs = _AtmNonCompRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 9),
    _AtmNonCompRxs_Type()
)
atmNonCompRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNonCompRxs.setStatus("mandatory")
_AtmDiscardFails_Type = Counter32
_AtmDiscardFails_Object = MibTableColumn
atmDiscardFails = _AtmDiscardFails_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 10),
    _AtmDiscardFails_Type()
)
atmDiscardFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardFails.setStatus("mandatory")
_AtmAvgVcqDepths_Type = Counter32
_AtmAvgVcqDepths_Object = MibTableColumn
atmAvgVcqDepths = _AtmAvgVcqDepths_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 11),
    _AtmAvgVcqDepths_Type()
)
atmAvgVcqDepths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAvgVcqDepths.setStatus("mandatory")
_AtmDiscardRsrcOflows_Type = Counter32
_AtmDiscardRsrcOflows_Object = MibTableColumn
atmDiscardRsrcOflows = _AtmDiscardRsrcOflows_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 12),
    _AtmDiscardRsrcOflows_Type()
)
atmDiscardRsrcOflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardRsrcOflows.setStatus("mandatory")
_AtmDiscardSbinFulls_Type = Counter32
_AtmDiscardSbinFulls_Object = MibTableColumn
atmDiscardSbinFulls = _AtmDiscardSbinFulls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 13),
    _AtmDiscardSbinFulls_Type()
)
atmDiscardSbinFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardSbinFulls.setStatus("mandatory")
_AtmBcmRxs_Type = Counter32
_AtmBcmRxs_Object = MibTableColumn
atmBcmRxs = _AtmBcmRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 14),
    _AtmBcmRxs_Type()
)
atmBcmRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBcmRxs.setStatus("mandatory")
_AtmBcmTxs_Type = Counter32
_AtmBcmTxs_Object = MibTableColumn
atmBcmTxs = _AtmBcmTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 15),
    _AtmBcmTxs_Type()
)
atmBcmTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBcmTxs.setStatus("mandatory")
_AtmOamTxs_Type = Counter32
_AtmOamTxs_Object = MibTableColumn
atmOamTxs = _AtmOamTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 16),
    _AtmOamTxs_Type()
)
atmOamTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamTxs.setStatus("mandatory")
_AtmDiscardQbinFulls_Type = Counter32
_AtmDiscardQbinFulls_Object = MibTableColumn
atmDiscardQbinFulls = _AtmDiscardQbinFulls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 17),
    _AtmDiscardQbinFulls_Type()
)
atmDiscardQbinFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardQbinFulls.setStatus("mandatory")
_AtmDiscardQbinClpThs_Type = Counter32
_AtmDiscardQbinClpThs_Object = MibTableColumn
atmDiscardQbinClpThs = _AtmDiscardQbinClpThs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 18),
    _AtmDiscardQbinClpThs_Type()
)
atmDiscardQbinClpThs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardQbinClpThs.setStatus("mandatory")
_AtmCellsRxNets_Type = Counter32
_AtmCellsRxNets_Object = MibTableColumn
atmCellsRxNets = _AtmCellsRxNets_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 19),
    _AtmCellsRxNets_Type()
)
atmCellsRxNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsRxNets.setStatus("mandatory")
_AtmClpTxs_Type = Counter32
_AtmClpTxs_Object = MibTableColumn
atmClpTxs = _AtmClpTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 20),
    _AtmClpTxs_Type()
)
atmClpTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmClpTxs.setStatus("mandatory")
_AtmEfciTxs_Type = Counter32
_AtmEfciTxs_Object = MibTableColumn
atmEfciTxs = _AtmEfciTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 21),
    _AtmEfciTxs_Type()
)
atmEfciTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEfciTxs.setStatus("mandatory")
_AtmCellsTxPorts_Type = Counter32
_AtmCellsTxPorts_Object = MibTableColumn
atmCellsTxPorts = _AtmCellsTxPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 22),
    _AtmCellsTxPorts_Type()
)
atmCellsTxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsTxPorts.setStatus("mandatory")
_AtmAisRxs_Type = Counter32
_AtmAisRxs_Object = MibTableColumn
atmAisRxs = _AtmAisRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 23),
    _AtmAisRxs_Type()
)
atmAisRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAisRxs.setStatus("mandatory")
_AtmFerfRxs_Type = Counter32
_AtmFerfRxs_Object = MibTableColumn
atmFerfRxs = _AtmFerfRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 24),
    _AtmFerfRxs_Type()
)
atmFerfRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFerfRxs.setStatus("mandatory")
_VoiceEndptTable_Object = MibTable
voiceEndptTable = _VoiceEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13)
)
if mibBuilder.loadTexts:
    voiceEndptTable.setStatus("mandatory")
_VoiceEndptEntry_Object = MibTableRow
voiceEndptEntry = _VoiceEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1)
)
voiceEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "voiceEndptIndex"),
)
if mibBuilder.loadTexts:
    voiceEndptEntry.setStatus("mandatory")
_VoiceEndptIndex_Type = Integer32
_VoiceEndptIndex_Object = MibTableColumn
voiceEndptIndex = _VoiceEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 1),
    _VoiceEndptIndex_Type()
)
voiceEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptIndex.setStatus("mandatory")
_VoiceOtherEndptIndex_Type = Integer32
_VoiceOtherEndptIndex_Object = MibTableColumn
voiceOtherEndptIndex = _VoiceOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 2),
    _VoiceOtherEndptIndex_Type()
)
voiceOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceOtherEndptIndex.setStatus("mandatory")
_VoiceEndptDesc_Type = DisplayString
_VoiceEndptDesc_Object = MibTableColumn
voiceEndptDesc = _VoiceEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 3),
    _VoiceEndptDesc_Type()
)
voiceEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptDesc.setStatus("mandatory")
_VoiceOtherEndptDesc_Type = DisplayString
_VoiceOtherEndptDesc_Object = MibTableColumn
voiceOtherEndptDesc = _VoiceOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 4),
    _VoiceOtherEndptDesc_Type()
)
voiceOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceOtherEndptDesc.setStatus("mandatory")


class _VoiceEndptConnDesc_Type(DisplayString):
    """Custom type voiceEndptConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VoiceEndptConnDesc_Type.__name__ = "DisplayString"
_VoiceEndptConnDesc_Object = MibTableColumn
voiceEndptConnDesc = _VoiceEndptConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 5),
    _VoiceEndptConnDesc_Type()
)
voiceEndptConnDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voiceEndptConnDesc.setStatus("obsolete")


class _VoiceEndptAdminStatus_Type(Integer32):
    """Custom type voiceEndptAdminStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3),
          ("test", 4),
          ("writeOnly", 5))
    )


_VoiceEndptAdminStatus_Type.__name__ = "Integer32"
_VoiceEndptAdminStatus_Object = MibTableColumn
voiceEndptAdminStatus = _VoiceEndptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 6),
    _VoiceEndptAdminStatus_Type()
)
voiceEndptAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptAdminStatus.setStatus("mandatory")


class _VoiceEndptOperStatus_Type(Integer32):
    """Custom type voiceEndptOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("okPendingDown", 2),
          ("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("okPendingRoute", 6),
          ("okPendingDelete", 7),
          ("looped", 8),
          ("unknown", 9))
    )


_VoiceEndptOperStatus_Type.__name__ = "Integer32"
_VoiceEndptOperStatus_Object = MibTableColumn
voiceEndptOperStatus = _VoiceEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 7),
    _VoiceEndptOperStatus_Type()
)
voiceEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptOperStatus.setStatus("mandatory")


class _VoiceEndptRateType_Type(Integer32):
    """Custom type voiceEndptRateType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("a32", 1),
          ("a24", 2),
          ("a16", 3),
          ("a16z", 4),
          ("a32d", 5),
          ("c32", 6),
          ("c24", 7),
          ("c16", 8),
          ("c16z", 9),
          ("c32d", 10),
          ("p", 11),
          ("t", 12),
          ("v", 13),
          ("l16", 14),
          ("l16v", 15),
          ("g729r8", 16),
          ("g729r8v", 17),
          ("g729ar8", 18),
          ("g729ar8v", 19),
          ("td", 20))
    )


_VoiceEndptRateType_Type.__name__ = "Integer32"
_VoiceEndptRateType_Object = MibTableColumn
voiceEndptRateType = _VoiceEndptRateType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 8),
    _VoiceEndptRateType_Type()
)
voiceEndptRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptRateType.setStatus("mandatory")


class _VoiceEndPointFailure_Type(Integer32):
    """Custom type voiceEndPointFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndPointFailure_Type.__name__ = "Integer32"
_VoiceEndPointFailure_Object = MibTableColumn
voiceEndPointFailure = _VoiceEndPointFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 9),
    _VoiceEndPointFailure_Type()
)
voiceEndPointFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointFailure.setStatus("mandatory")


class _VoiceNoRouteFoundFailure_Type(Integer32):
    """Custom type voiceNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceNoRouteFoundFailure_Type.__name__ = "Integer32"
_VoiceNoRouteFoundFailure_Object = MibTableColumn
voiceNoRouteFoundFailure = _VoiceNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 10),
    _VoiceNoRouteFoundFailure_Type()
)
voiceNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceNoRouteFoundFailure.setStatus("mandatory")


class _VoiceBumpFailure_Type(Integer32):
    """Custom type voiceBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceBumpFailure_Type.__name__ = "Integer32"
_VoiceBumpFailure_Object = MibTableColumn
voiceBumpFailure = _VoiceBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 11),
    _VoiceBumpFailure_Type()
)
voiceBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceBumpFailure.setStatus("mandatory")


class _VoiceTestFailure_Type(Integer32):
    """Custom type voiceTestFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceTestFailure_Type.__name__ = "Integer32"
_VoiceTestFailure_Object = MibTableColumn
voiceTestFailure = _VoiceTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 12),
    _VoiceTestFailure_Type()
)
voiceTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceTestFailure.setStatus("mandatory")


class _VoiceEndptTestType_Type(Integer32):
    """Custom type voiceEndptTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("testCon", 1),
          ("testNoLoop", 3),
          ("writeOnly", 5))
    )


_VoiceEndptTestType_Type.__name__ = "Integer32"
_VoiceEndptTestType_Object = MibTableColumn
voiceEndptTestType = _VoiceEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 13),
    _VoiceEndptTestType_Type()
)
voiceEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptTestType.setStatus("mandatory")
_VoiceEndptLpbkStatus_Type = Integer32
_VoiceEndptLpbkStatus_Object = MibTableColumn
voiceEndptLpbkStatus = _VoiceEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 14),
    _VoiceEndptLpbkStatus_Type()
)
voiceEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptLpbkStatus.setStatus("mandatory")
_VoiceConnPtr_Type = ObjectIdentifier
_VoiceConnPtr_Object = MibTableColumn
voiceConnPtr = _VoiceConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 15),
    _VoiceConnPtr_Type()
)
voiceConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceConnPtr.setStatus("mandatory")
_VoiceChannelPtr_Type = ObjectIdentifier
_VoiceChannelPtr_Object = MibTableColumn
voiceChannelPtr = _VoiceChannelPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 16),
    _VoiceChannelPtr_Type()
)
voiceChannelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelPtr.setStatus("mandatory")


class _VoiceEndptTrkAvoidType_Type(Integer32):
    """Custom type voiceEndptTrkAvoidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_VoiceEndptTrkAvoidType_Type.__name__ = "Integer32"
_VoiceEndptTrkAvoidType_Object = MibTableColumn
voiceEndptTrkAvoidType = _VoiceEndptTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 17),
    _VoiceEndptTrkAvoidType_Type()
)
voiceEndptTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptTrkAvoidType.setStatus("mandatory")


class _VoiceEndptAvoidZCS_Type(Integer32):
    """Custom type voiceEndptAvoidZCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndptAvoidZCS_Type.__name__ = "Integer32"
_VoiceEndptAvoidZCS_Object = MibTableColumn
voiceEndptAvoidZCS = _VoiceEndptAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 18),
    _VoiceEndptAvoidZCS_Type()
)
voiceEndptAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptAvoidZCS.setStatus("mandatory")


class _VoiceEndptState_Type(Integer32):
    """Custom type voiceEndptState based on Integer32"""
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
        *(("offhook", 1),
          ("onhook", 2),
          ("slowmodem", 3),
          ("fastmodem", 4),
          ("notConnected", 5))
    )


_VoiceEndptState_Type.__name__ = "Integer32"
_VoiceEndptState_Object = MibTableColumn
voiceEndptState = _VoiceEndptState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 19),
    _VoiceEndptState_Type()
)
voiceEndptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptState.setStatus("mandatory")


class _VoiceEndptAdv_Type(Integer32):
    """Custom type voiceEndptAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndptAdv_Type.__name__ = "Integer32"
_VoiceEndptAdv_Object = MibTableColumn
voiceEndptAdv = _VoiceEndptAdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 20),
    _VoiceEndptAdv_Type()
)
voiceEndptAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptAdv.setStatus("mandatory")


class _VoiceOtherEndptAdv_Type(Integer32):
    """Custom type voiceOtherEndptAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceOtherEndptAdv_Type.__name__ = "Integer32"
_VoiceOtherEndptAdv_Object = MibTableColumn
voiceOtherEndptAdv = _VoiceOtherEndptAdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 21),
    _VoiceOtherEndptAdv_Type()
)
voiceOtherEndptAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceOtherEndptAdv.setStatus("mandatory")


class _VoiceEndptEncoding_Type(Integer32):
    """Custom type voiceEndptEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2))
    )


_VoiceEndptEncoding_Type.__name__ = "Integer32"
_VoiceEndptEncoding_Object = MibTableColumn
voiceEndptEncoding = _VoiceEndptEncoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 22),
    _VoiceEndptEncoding_Type()
)
voiceEndptEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptEncoding.setStatus("mandatory")


class _VoiceOtherEndptEncoding_Type(Integer32):
    """Custom type voiceOtherEndptEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2))
    )


_VoiceOtherEndptEncoding_Type.__name__ = "Integer32"
_VoiceOtherEndptEncoding_Object = MibTableColumn
voiceOtherEndptEncoding = _VoiceOtherEndptEncoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 23),
    _VoiceOtherEndptEncoding_Type()
)
voiceOtherEndptEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceOtherEndptEncoding.setStatus("mandatory")


class _VoiceEndptEndptType_Type(Integer32):
    """Custom type voiceEndptEndptType based on Integer32"""
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
        *(("pcm", 1),
          ("adpcm", 2),
          ("adpno", 3),
          ("transp", 4),
          ("unknown", 5),
          ("ldcelp", 6))
    )


_VoiceEndptEndptType_Type.__name__ = "Integer32"
_VoiceEndptEndptType_Object = MibTableColumn
voiceEndptEndptType = _VoiceEndptEndptType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 24),
    _VoiceEndptEndptType_Type()
)
voiceEndptEndptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptEndptType.setStatus("mandatory")


class _VoiceEndptLocLpbkState_Type(Integer32):
    """Custom type voiceEndptLocLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VoiceEndptLocLpbkState_Type.__name__ = "Integer32"
_VoiceEndptLocLpbkState_Object = MibTableColumn
voiceEndptLocLpbkState = _VoiceEndptLocLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 25),
    _VoiceEndptLocLpbkState_Type()
)
voiceEndptLocLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptLocLpbkState.setStatus("mandatory")


class _VoiceEndptSvcId_Type(Integer32):
    """Custom type voiceEndptSvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VoiceEndptSvcId_Type.__name__ = "Integer32"
_VoiceEndptSvcId_Object = MibTableColumn
voiceEndptSvcId = _VoiceEndptSvcId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 26),
    _VoiceEndptSvcId_Type()
)
voiceEndptSvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptSvcId.setStatus("mandatory")


class _VoiceEndptIsSVC_Type(Integer32):
    """Custom type voiceEndptIsSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndptIsSVC_Type.__name__ = "Integer32"
_VoiceEndptIsSVC_Object = MibTableColumn
voiceEndptIsSVC = _VoiceEndptIsSVC_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 27),
    _VoiceEndptIsSVC_Type()
)
voiceEndptIsSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptIsSVC.setStatus("mandatory")


class _VoiceEndptFaxModem_Type(Integer32):
    """Custom type voiceEndptFaxModem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VoiceEndptFaxModem_Type.__name__ = "Integer32"
_VoiceEndptFaxModem_Object = MibTableColumn
voiceEndptFaxModem = _VoiceEndptFaxModem_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 28),
    _VoiceEndptFaxModem_Type()
)
voiceEndptFaxModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptFaxModem.setStatus("mandatory")


class _VoiceEndptLocRmtLpbk_Type(Integer32):
    """Custom type voiceEndptLocRmtLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VoiceEndptLocRmtLpbk_Type.__name__ = "Integer32"
_VoiceEndptLocRmtLpbk_Object = MibTableColumn
voiceEndptLocRmtLpbk = _VoiceEndptLocRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 29),
    _VoiceEndptLocRmtLpbk_Type()
)
voiceEndptLocRmtLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptLocRmtLpbk.setStatus("mandatory")
_VoiceStatTable_Object = MibTable
voiceStatTable = _VoiceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14)
)
if mibBuilder.loadTexts:
    voiceStatTable.setStatus("mandatory")
_VoiceStatEntry_Object = MibTableRow
voiceStatEntry = _VoiceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1)
)
voiceStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "voiceEndptIndex"),
)
if mibBuilder.loadTexts:
    voiceStatEntry.setStatus("mandatory")
_VoiceStatPktsRxs_Type = Counter32
_VoiceStatPktsRxs_Object = MibTableColumn
voiceStatPktsRxs = _VoiceStatPktsRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 1),
    _VoiceStatPktsRxs_Type()
)
voiceStatPktsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatPktsRxs.setStatus("mandatory")
_VoiceStatPktsXmits_Type = Counter32
_VoiceStatPktsXmits_Object = MibTableColumn
voiceStatPktsXmits = _VoiceStatPktsXmits_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 2),
    _VoiceStatPktsXmits_Type()
)
voiceStatPktsXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatPktsXmits.setStatus("mandatory")
_VoiceStatRxPktsDscds_Type = Counter32
_VoiceStatRxPktsDscds_Object = MibTableColumn
voiceStatRxPktsDscds = _VoiceStatRxPktsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 3),
    _VoiceStatRxPktsDscds_Type()
)
voiceStatRxPktsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatRxPktsDscds.setStatus("mandatory")
_VoiceStatSprvPktsXmits_Type = Counter32
_VoiceStatSprvPktsXmits_Object = MibTableColumn
voiceStatSprvPktsXmits = _VoiceStatSprvPktsXmits_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 4),
    _VoiceStatSprvPktsXmits_Type()
)
voiceStatSprvPktsXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatSprvPktsXmits.setStatus("mandatory")
_VoiceStatSprvPktsRcvs_Type = Counter32
_VoiceStatSprvPktsRcvs_Object = MibTableColumn
voiceStatSprvPktsRcvs = _VoiceStatSprvPktsRcvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 5),
    _VoiceStatSprvPktsRcvs_Type()
)
voiceStatSprvPktsRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatSprvPktsRcvs.setStatus("mandatory")
_VoiceStatV25ModemOns_Type = Counter32
_VoiceStatV25ModemOns_Object = MibTableColumn
voiceStatV25ModemOns = _VoiceStatV25ModemOns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 6),
    _VoiceStatV25ModemOns_Type()
)
voiceStatV25ModemOns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatV25ModemOns.setStatus("mandatory")
_VoiceStatDsiOns_Type = Counter32
_VoiceStatDsiOns_Object = MibTableColumn
voiceStatDsiOns = _VoiceStatDsiOns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 7),
    _VoiceStatDsiOns_Type()
)
voiceStatDsiOns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatDsiOns.setStatus("mandatory")
_VoiceStatOffhks_Type = Counter32
_VoiceStatOffhks_Object = MibTableColumn
voiceStatOffhks = _VoiceStatOffhks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 8),
    _VoiceStatOffhks_Type()
)
voiceStatOffhks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatOffhks.setStatus("mandatory")
_VoiceStatInservices_Type = Counter32
_VoiceStatInservices_Object = MibTableColumn
voiceStatInservices = _VoiceStatInservices_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 9),
    _VoiceStatInservices_Type()
)
voiceStatInservices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatInservices.setStatus("mandatory")
_VoiceEndptConnMapTable_Object = MibTable
voiceEndptConnMapTable = _VoiceEndptConnMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 16)
)
if mibBuilder.loadTexts:
    voiceEndptConnMapTable.setStatus("mandatory")
_VoiceEndptConnMapEntry_Object = MibTableRow
voiceEndptConnMapEntry = _VoiceEndptConnMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 16, 1)
)
voiceEndptConnMapEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
    (0, "STRATACOM-MIB", "voiceEndptConnMapChannel"),
)
if mibBuilder.loadTexts:
    voiceEndptConnMapEntry.setStatus("mandatory")


class _VoiceEndptConnMapChannel_Type(Integer32):
    """Custom type voiceEndptConnMapChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_VoiceEndptConnMapChannel_Type.__name__ = "Integer32"
_VoiceEndptConnMapChannel_Object = MibTableColumn
voiceEndptConnMapChannel = _VoiceEndptConnMapChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 16, 1, 1),
    _VoiceEndptConnMapChannel_Type()
)
voiceEndptConnMapChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptConnMapChannel.setStatus("mandatory")
_VoiceEndptConnMapEndptPtr_Type = ObjectIdentifier
_VoiceEndptConnMapEndptPtr_Object = MibTableColumn
voiceEndptConnMapEndptPtr = _VoiceEndptConnMapEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 16, 1, 2),
    _VoiceEndptConnMapEndptPtr_Type()
)
voiceEndptConnMapEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptConnMapEndptPtr.setStatus("mandatory")
_VoiceEndptConnMapConnPtr_Type = ObjectIdentifier
_VoiceEndptConnMapConnPtr_Object = MibTableColumn
voiceEndptConnMapConnPtr = _VoiceEndptConnMapConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 16, 1, 3),
    _VoiceEndptConnMapConnPtr_Type()
)
voiceEndptConnMapConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptConnMapConnPtr.setStatus("mandatory")
_DataEndptTable_Object = MibTable
dataEndptTable = _DataEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17)
)
if mibBuilder.loadTexts:
    dataEndptTable.setStatus("mandatory")
_DataEndptEntry_Object = MibTableRow
dataEndptEntry = _DataEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1)
)
dataEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "dataEndptIndex"),
)
if mibBuilder.loadTexts:
    dataEndptEntry.setStatus("mandatory")
_DataEndptIndex_Type = Integer32
_DataEndptIndex_Object = MibTableColumn
dataEndptIndex = _DataEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 1),
    _DataEndptIndex_Type()
)
dataEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptIndex.setStatus("mandatory")
_DataOtherEndptIndex_Type = Integer32
_DataOtherEndptIndex_Object = MibTableColumn
dataOtherEndptIndex = _DataOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 2),
    _DataOtherEndptIndex_Type()
)
dataOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataOtherEndptIndex.setStatus("mandatory")
_DataEndptDesc_Type = DisplayString
_DataEndptDesc_Object = MibTableColumn
dataEndptDesc = _DataEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 3),
    _DataEndptDesc_Type()
)
dataEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptDesc.setStatus("mandatory")
_DataOtherEndptDesc_Type = DisplayString
_DataOtherEndptDesc_Object = MibTableColumn
dataOtherEndptDesc = _DataOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 4),
    _DataOtherEndptDesc_Type()
)
dataOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataOtherEndptDesc.setStatus("mandatory")


class _DataEndptAdmStatus_Type(Integer32):
    """Custom type dataEndptAdmStatus based on Integer32"""
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
        *(("added", 1),
          ("deleted", 2),
          ("configured", 3),
          ("testing", 4))
    )


_DataEndptAdmStatus_Type.__name__ = "Integer32"
_DataEndptAdmStatus_Object = MibTableColumn
dataEndptAdmStatus = _DataEndptAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 5),
    _DataEndptAdmStatus_Type()
)
dataEndptAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptAdmStatus.setStatus("mandatory")


class _DataEndptOperStatus_Type(Integer32):
    """Custom type dataEndptOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("okPendingDown", 2),
          ("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("okPendingRoute", 6),
          ("okPendingDelete", 7),
          ("looped", 8),
          ("unknown", 9))
    )


_DataEndptOperStatus_Type.__name__ = "Integer32"
_DataEndptOperStatus_Object = MibTableColumn
dataEndptOperStatus = _DataEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 6),
    _DataEndptOperStatus_Type()
)
dataEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptOperStatus.setStatus("mandatory")
_DataEndptRate_Type = Integer32
_DataEndptRate_Object = MibTableColumn
dataEndptRate = _DataEndptRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 7),
    _DataEndptRate_Type()
)
dataEndptRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptRate.setStatus("mandatory")


class _DataEndPtRemoteFail_Type(Integer32):
    """Custom type dataEndPtRemoteFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DataEndPtRemoteFail_Type.__name__ = "Integer32"
_DataEndPtRemoteFail_Object = MibTableColumn
dataEndPtRemoteFail = _DataEndPtRemoteFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 8),
    _DataEndPtRemoteFail_Type()
)
dataEndPtRemoteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndPtRemoteFail.setStatus("mandatory")


class _DataEndptNoRouteFail_Type(Integer32):
    """Custom type dataEndptNoRouteFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DataEndptNoRouteFail_Type.__name__ = "Integer32"
_DataEndptNoRouteFail_Object = MibTableColumn
dataEndptNoRouteFail = _DataEndptNoRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 9),
    _DataEndptNoRouteFail_Type()
)
dataEndptNoRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptNoRouteFail.setStatus("mandatory")


class _DataEndptTestFail_Type(Integer32):
    """Custom type dataEndptTestFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DataEndptTestFail_Type.__name__ = "Integer32"
_DataEndptTestFail_Object = MibTableColumn
dataEndptTestFail = _DataEndptTestFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 10),
    _DataEndptTestFail_Type()
)
dataEndptTestFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptTestFail.setStatus("mandatory")


class _DataEndptTestType_Type(Integer32):
    """Custom type dataEndptTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("test", 1),
          ("testNolp", 3),
          ("noTest", 5))
    )


_DataEndptTestType_Type.__name__ = "Integer32"
_DataEndptTestType_Object = MibTableColumn
dataEndptTestType = _DataEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 11),
    _DataEndptTestType_Type()
)
dataEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptTestType.setStatus("mandatory")
_DataEndptLpbkStatus_Type = Integer32
_DataEndptLpbkStatus_Object = MibTableColumn
dataEndptLpbkStatus = _DataEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 12),
    _DataEndptLpbkStatus_Type()
)
dataEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptLpbkStatus.setStatus("mandatory")


class _DataEndptLocLpbkEnable_Type(Integer32):
    """Custom type dataEndptLocLpbkEnable based on Integer32"""
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


_DataEndptLocLpbkEnable_Type.__name__ = "Integer32"
_DataEndptLocLpbkEnable_Object = MibTableColumn
dataEndptLocLpbkEnable = _DataEndptLocLpbkEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 13),
    _DataEndptLocLpbkEnable_Type()
)
dataEndptLocLpbkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptLocLpbkEnable.setStatus("mandatory")


class _DataEndptLocRmtLpbk_Type(Integer32):
    """Custom type dataEndptLocRmtLpbk based on Integer32"""
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


_DataEndptLocRmtLpbk_Type.__name__ = "Integer32"
_DataEndptLocRmtLpbk_Object = MibTableColumn
dataEndptLocRmtLpbk = _DataEndptLocRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 14),
    _DataEndptLocRmtLpbk_Type()
)
dataEndptLocRmtLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptLocRmtLpbk.setStatus("mandatory")
_DataEndptConnPtr_Type = ObjectIdentifier
_DataEndptConnPtr_Object = MibTableColumn
dataEndptConnPtr = _DataEndptConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 15),
    _DataEndptConnPtr_Type()
)
dataEndptConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptConnPtr.setStatus("mandatory")
_DataEndptPortPtr_Type = ObjectIdentifier
_DataEndptPortPtr_Object = MibTableColumn
dataEndptPortPtr = _DataEndptPortPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 16),
    _DataEndptPortPtr_Type()
)
dataEndptPortPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptPortPtr.setStatus("mandatory")


class _DataEndptTrkAvoid_Type(Integer32):
    """Custom type dataEndptTrkAvoid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_DataEndptTrkAvoid_Type.__name__ = "Integer32"
_DataEndptTrkAvoid_Object = MibTableColumn
dataEndptTrkAvoid = _DataEndptTrkAvoid_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 17),
    _DataEndptTrkAvoid_Type()
)
dataEndptTrkAvoid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptTrkAvoid.setStatus("mandatory")


class _DataEndptZCSAvoid_Type(Integer32):
    """Custom type dataEndptZCSAvoid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DataEndptZCSAvoid_Type.__name__ = "Integer32"
_DataEndptZCSAvoid_Object = MibTableColumn
dataEndptZCSAvoid = _DataEndptZCSAvoid_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 18),
    _DataEndptZCSAvoid_Type()
)
dataEndptZCSAvoid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptZCSAvoid.setStatus("mandatory")


class _DataEndptFastEia_Type(Integer32):
    """Custom type dataEndptFastEia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DataEndptFastEia_Type.__name__ = "Integer32"
_DataEndptFastEia_Object = MibTableColumn
dataEndptFastEia = _DataEndptFastEia_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 19),
    _DataEndptFastEia_Type()
)
dataEndptFastEia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptFastEia.setStatus("mandatory")


class _DataEndptEiaUpdt_Type(Integer32):
    """Custom type dataEndptEiaUpdt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_DataEndptEiaUpdt_Type.__name__ = "Integer32"
_DataEndptEiaUpdt_Object = MibTableColumn
dataEndptEiaUpdt = _DataEndptEiaUpdt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 20),
    _DataEndptEiaUpdt_Type()
)
dataEndptEiaUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptEiaUpdt.setStatus("mandatory")


class _DataEndptSampPerPkt_Type(Integer32):
    """Custom type dataEndptSampPerPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1),
          ("two-bytes", 2),
          ("four-bytes", 4),
          ("five-bytes", 5),
          ("ten-bytes", 10))
    )


_DataEndptSampPerPkt_Type.__name__ = "Integer32"
_DataEndptSampPerPkt_Object = MibTableColumn
dataEndptSampPerPkt = _DataEndptSampPerPkt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 21),
    _DataEndptSampPerPkt_Type()
)
dataEndptSampPerPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptSampPerPkt.setStatus("mandatory")


class _DataEndptTspnt_Type(Integer32):
    """Custom type dataEndptTspnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DataEndptTspnt_Type.__name__ = "Integer32"
_DataEndptTspnt_Object = MibTableColumn
dataEndptTspnt = _DataEndptTspnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 22),
    _DataEndptTspnt_Type()
)
dataEndptTspnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptTspnt.setStatus("mandatory")


class _DataEndptSuperRateN_Type(Integer32):
    """Custom type dataEndptSuperRateN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DataEndptSuperRateN_Type.__name__ = "Integer32"
_DataEndptSuperRateN_Object = MibTableColumn
dataEndptSuperRateN = _DataEndptSuperRateN_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 23),
    _DataEndptSuperRateN_Type()
)
dataEndptSuperRateN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptSuperRateN.setStatus("mandatory")


class _DataEndptCoding_Type(Integer32):
    """Custom type dataEndptCoding based on Integer32"""
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
        *(("dataCode78", 1),
          ("dataCode88", 2),
          ("dataCode88I", 3),
          ("dataCode78E", 4))
    )


_DataEndptCoding_Type.__name__ = "Integer32"
_DataEndptCoding_Object = MibTableColumn
dataEndptCoding = _DataEndptCoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 24),
    _DataEndptCoding_Type()
)
dataEndptCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptCoding.setStatus("mandatory")


class _DataEndptDfmEnable_Type(Integer32):
    """Custom type dataEndptDfmEnable based on Integer32"""
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


_DataEndptDfmEnable_Type.__name__ = "Integer32"
_DataEndptDfmEnable_Object = MibTableColumn
dataEndptDfmEnable = _DataEndptDfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 25),
    _DataEndptDfmEnable_Type()
)
dataEndptDfmEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptDfmEnable.setStatus("mandatory")


class _DataEndptDfmLen_Type(Integer32):
    """Custom type dataEndptDfmLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dataEndptDfmOther", 1),
          ("dataEndptDfm7", 7),
          ("dataEndptDfm8", 8),
          ("dataEndptDfm16", 16))
    )


_DataEndptDfmLen_Type.__name__ = "Integer32"
_DataEndptDfmLen_Object = MibTableColumn
dataEndptDfmLen = _DataEndptDfmLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 26),
    _DataEndptDfmLen_Type()
)
dataEndptDfmLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndptDfmLen.setStatus("mandatory")


class _DataEndptOeDceDte_Type(Integer32):
    """Custom type dataEndptOeDceDte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dce", 2),
          ("dte", 3))
    )


_DataEndptOeDceDte_Type.__name__ = "Integer32"
_DataEndptOeDceDte_Object = MibTableColumn
dataEndptOeDceDte = _DataEndptOeDceDte_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 27),
    _DataEndptOeDceDte_Type()
)
dataEndptOeDceDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptOeDceDte.setStatus("mandatory")


class _DataEndptOeClk_Type(Integer32):
    """Custom type dataEndptOeClk based on Integer32"""
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
        *(("other", 1),
          ("normal", 2),
          ("split", 3),
          ("looped", 4))
    )


_DataEndptOeClk_Type.__name__ = "Integer32"
_DataEndptOeClk_Object = MibTableColumn
dataEndptOeClk = _DataEndptOeClk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 17, 1, 28),
    _DataEndptOeClk_Type()
)
dataEndptOeClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndptOeClk.setStatus("mandatory")
_SwitchShelf_ObjectIdentity = ObjectIdentity
switchShelf = _SwitchShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4)
)
_ShelfCnfgObjects_ObjectIdentity = ObjectIdentity
shelfCnfgObjects = _ShelfCnfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1)
)
_ShelfCnfgStatMaster_Type = IpAddress
_ShelfCnfgStatMaster_Object = MibScalar
shelfCnfgStatMaster = _ShelfCnfgStatMaster_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 1),
    _ShelfCnfgStatMaster_Type()
)
shelfCnfgStatMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatMaster.setStatus("mandatory")
_ShelfCnfgStatCollIntvl_Type = Integer32
_ShelfCnfgStatCollIntvl_Object = MibScalar
shelfCnfgStatCollIntvl = _ShelfCnfgStatCollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 2),
    _ShelfCnfgStatCollIntvl_Type()
)
shelfCnfgStatCollIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatCollIntvl.setStatus("mandatory")
_ShelfCnfgStatBcktIntvl_Type = Integer32
_ShelfCnfgStatBcktIntvl_Object = MibScalar
shelfCnfgStatBcktIntvl = _ShelfCnfgStatBcktIntvl_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 3),
    _ShelfCnfgStatBcktIntvl_Type()
)
shelfCnfgStatBcktIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatBcktIntvl.setStatus("mandatory")
_ShelfCnfgStatTimeSync_Type = DisplayString
_ShelfCnfgStatTimeSync_Object = MibScalar
shelfCnfgStatTimeSync = _ShelfCnfgStatTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 4),
    _ShelfCnfgStatTimeSync_Type()
)
shelfCnfgStatTimeSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatTimeSync.setStatus("mandatory")


class _ShelfCnfgSwError_Type(Integer32):
    """Custom type shelfCnfgSwError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ShelfCnfgSwError_Type.__name__ = "Integer32"
_ShelfCnfgSwError_Object = MibScalar
shelfCnfgSwError = _ShelfCnfgSwError_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 5),
    _ShelfCnfgSwError_Type()
)
shelfCnfgSwError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgSwError.setStatus("mandatory")


class _ShelfCnfgCardError_Type(Integer32):
    """Custom type shelfCnfgCardError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ShelfCnfgCardError_Type.__name__ = "Integer32"
_ShelfCnfgCardError_Object = MibScalar
shelfCnfgCardError = _ShelfCnfgCardError_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 6),
    _ShelfCnfgCardError_Type()
)
shelfCnfgCardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgCardError.setStatus("mandatory")
_ShelfCnfgEthIPAddr_Type = IpAddress
_ShelfCnfgEthIPAddr_Object = MibScalar
shelfCnfgEthIPAddr = _ShelfCnfgEthIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 7),
    _ShelfCnfgEthIPAddr_Type()
)
shelfCnfgEthIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgEthIPAddr.setStatus("mandatory")
_ShelfCnfgEthIPMask_Type = IpAddress
_ShelfCnfgEthIPMask_Object = MibScalar
shelfCnfgEthIPMask = _ShelfCnfgEthIPMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 8),
    _ShelfCnfgEthIPMask_Type()
)
shelfCnfgEthIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgEthIPMask.setStatus("mandatory")
_ShelfCnfgEthMacAddr_Type = OctetString
_ShelfCnfgEthMacAddr_Object = MibScalar
shelfCnfgEthMacAddr = _ShelfCnfgEthMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 9),
    _ShelfCnfgEthMacAddr_Type()
)
shelfCnfgEthMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgEthMacAddr.setStatus("mandatory")
_ShelfCnfgEthGWAddr_Type = IpAddress
_ShelfCnfgEthGWAddr_Object = MibScalar
shelfCnfgEthGWAddr = _ShelfCnfgEthGWAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 10),
    _ShelfCnfgEthGWAddr_Type()
)
shelfCnfgEthGWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgEthGWAddr.setStatus("mandatory")
_ShelfCnfgNwIPAddr_Type = IpAddress
_ShelfCnfgNwIPAddr_Object = MibScalar
shelfCnfgNwIPAddr = _ShelfCnfgNwIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 11),
    _ShelfCnfgNwIPAddr_Type()
)
shelfCnfgNwIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgNwIPAddr.setStatus("mandatory")
_ShelfCnfgNwIPMask_Type = IpAddress
_ShelfCnfgNwIPMask_Object = MibScalar
shelfCnfgNwIPMask = _ShelfCnfgNwIPMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 12),
    _ShelfCnfgNwIPMask_Type()
)
shelfCnfgNwIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgNwIPMask.setStatus("mandatory")
_ShelfCnfgNodeName_Type = DisplayString
_ShelfCnfgNodeName_Object = MibScalar
shelfCnfgNodeName = _ShelfCnfgNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 13),
    _ShelfCnfgNodeName_Type()
)
shelfCnfgNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgNodeName.setStatus("mandatory")
_ShelfCnfgNodeNumber_Type = Integer32
_ShelfCnfgNodeNumber_Object = MibScalar
shelfCnfgNodeNumber = _ShelfCnfgNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 14),
    _ShelfCnfgNodeNumber_Type()
)
shelfCnfgNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgNodeNumber.setStatus("mandatory")
_ShelfCnfgDomainNumber_Type = Integer32
_ShelfCnfgDomainNumber_Object = MibScalar
shelfCnfgDomainNumber = _ShelfCnfgDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 15),
    _ShelfCnfgDomainNumber_Type()
)
shelfCnfgDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgDomainNumber.setStatus("mandatory")


class _ShelfCnfgNodeType_Type(Integer32):
    """Custom type shelfCnfgNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipx", 1),
          ("bpx", 2),
          ("igx", 3),
          ("igx8450", 16))
    )


_ShelfCnfgNodeType_Type.__name__ = "Integer32"
_ShelfCnfgNodeType_Object = MibScalar
shelfCnfgNodeType = _ShelfCnfgNodeType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 16),
    _ShelfCnfgNodeType_Type()
)
shelfCnfgNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgNodeType.setStatus("mandatory")


class _ShelfCnfgAlarmStatus_Type(Integer32):
    """Custom type shelfCnfgAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor", 2),
          ("major", 3))
    )


_ShelfCnfgAlarmStatus_Type.__name__ = "Integer32"
_ShelfCnfgAlarmStatus_Object = MibScalar
shelfCnfgAlarmStatus = _ShelfCnfgAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 17),
    _ShelfCnfgAlarmStatus_Type()
)
shelfCnfgAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgAlarmStatus.setStatus("mandatory")
_ShelfCnfgPrimSwRevision_Type = DisplayString
_ShelfCnfgPrimSwRevision_Object = MibScalar
shelfCnfgPrimSwRevision = _ShelfCnfgPrimSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 18),
    _ShelfCnfgPrimSwRevision_Type()
)
shelfCnfgPrimSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgPrimSwRevision.setStatus("mandatory")
_ShelfCnfgSecSwRevision_Type = DisplayString
_ShelfCnfgSecSwRevision_Object = MibScalar
shelfCnfgSecSwRevision = _ShelfCnfgSecSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 19),
    _ShelfCnfgSecSwRevision_Type()
)
shelfCnfgSecSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgSecSwRevision.setStatus("mandatory")


class _ShelfCnfgTimeZone_Type(Integer32):
    """Custom type shelfCnfgTimeZone based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("gplus12", 1),
          ("gplus11", 2),
          ("gplus10", 3),
          ("gplus09", 4),
          ("gplus08", 5),
          ("gplus07", 6),
          ("gplus06", 7),
          ("gplus05", 8),
          ("gplus04", 9),
          ("gplus03", 10),
          ("gplus02", 11),
          ("gplus01", 12),
          ("gmt", 13),
          ("gminus01", 14),
          ("gminus02", 15),
          ("gminus04", 16),
          ("gminus05", 17),
          ("est", 18),
          ("cst", 19),
          ("pdt", 20),
          ("pst", 21),
          ("yst", 22),
          ("gminus10", 23),
          ("gminus11", 24),
          ("gminus12", 25))
    )


_ShelfCnfgTimeZone_Type.__name__ = "Integer32"
_ShelfCnfgTimeZone_Object = MibScalar
shelfCnfgTimeZone = _ShelfCnfgTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 20),
    _ShelfCnfgTimeZone_Type()
)
shelfCnfgTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgTimeZone.setStatus("mandatory")


class _ShelfCnfgTrapSeverity_Type(Integer32):
    """Custom type shelfCnfgTrapSeverity based on Integer32"""
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
        *(("minor", 1),
          ("major", 2),
          ("info", 3),
          ("notReadable", 4))
    )


_ShelfCnfgTrapSeverity_Type.__name__ = "Integer32"
_ShelfCnfgTrapSeverity_Object = MibScalar
shelfCnfgTrapSeverity = _ShelfCnfgTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 21),
    _ShelfCnfgTrapSeverity_Type()
)
shelfCnfgTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgTrapSeverity.setStatus("mandatory")


class _ShelfCnfgRebuildStatus_Type(Integer32):
    """Custom type shelfCnfgRebuildStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rebuild", 1),
          ("active", 2))
    )


_ShelfCnfgRebuildStatus_Type.__name__ = "Integer32"
_ShelfCnfgRebuildStatus_Object = MibScalar
shelfCnfgRebuildStatus = _ShelfCnfgRebuildStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 22),
    _ShelfCnfgRebuildStatus_Type()
)
shelfCnfgRebuildStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCnfgRebuildStatus.setStatus("mandatory")


class _ShelfCnfgJunctNode_Type(Integer32):
    """Custom type shelfCnfgJunctNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ShelfCnfgJunctNode_Type.__name__ = "Integer32"
_ShelfCnfgJunctNode_Object = MibScalar
shelfCnfgJunctNode = _ShelfCnfgJunctNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 23),
    _ShelfCnfgJunctNode_Type()
)
shelfCnfgJunctNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgJunctNode.setStatus("mandatory")


class _ShelfCnfgVcPollRate_Type(Integer32):
    """Custom type shelfCnfgVcPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_ShelfCnfgVcPollRate_Type.__name__ = "Integer32"
_ShelfCnfgVcPollRate_Object = MibScalar
shelfCnfgVcPollRate = _ShelfCnfgVcPollRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 24),
    _ShelfCnfgVcPollRate_Type()
)
shelfCnfgVcPollRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgVcPollRate.setStatus("mandatory")
_ShelfInfoObjects_ObjectIdentity = ObjectIdentity
shelfInfoObjects = _ShelfInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2)
)
_ShelfSlotInfoTable_Object = MibTable
shelfSlotInfoTable = _ShelfSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    shelfSlotInfoTable.setStatus("mandatory")
_ShelfSlotInfoEntry_Object = MibTableRow
shelfSlotInfoEntry = _ShelfSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1)
)
shelfSlotInfoEntry.setIndexNames(
    (0, "STRATACOM-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    shelfSlotInfoEntry.setStatus("mandatory")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("mandatory")


class _SlotCardYred_Type(Integer32):
    """Custom type slotCardYred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("null", 3))
    )


_SlotCardYred_Type.__name__ = "Integer32"
_SlotCardYred_Object = MibTableColumn
slotCardYred = _SlotCardYred_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 2),
    _SlotCardYred_Type()
)
slotCardYred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardYred.setStatus("mandatory")
_SlotCardYredSlot_Type = Integer32
_SlotCardYredSlot_Object = MibTableColumn
slotCardYredSlot = _SlotCardYredSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 3),
    _SlotCardYredSlot_Type()
)
slotCardYredSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardYredSlot.setStatus("mandatory")


class _SlotCardStatus_Type(Integer32):
    """Custom type slotCardStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              60)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("disabled", 2),
          ("standby", 3),
          ("active", 4),
          ("failed", 5),
          ("stbypccupdt", 6),
          ("ucstatus", 7),
          ("unavailable", 8),
          ("downloading", 9),
          ("downloader", 10),
          ("downloaded", 11),
          ("frozen", 12),
          ("mismatch", 13),
          ("fwdnldfailed", 14),
          ("program", 15),
          ("upgrading", 16),
          ("upgraded", 17),
          ("hwerr", 18),
          ("testcard", 19),
          ("backcardmissing", 60))
    )


_SlotCardStatus_Type.__name__ = "Integer32"
_SlotCardStatus_Object = MibTableColumn
slotCardStatus = _SlotCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 4),
    _SlotCardStatus_Type()
)
slotCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardStatus.setStatus("mandatory")


class _SlotCardFail_Type(Integer32):
    """Custom type slotCardFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SlotCardFail_Type.__name__ = "Integer32"
_SlotCardFail_Object = MibTableColumn
slotCardFail = _SlotCardFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 5),
    _SlotCardFail_Type()
)
slotCardFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFail.setStatus("mandatory")


class _SlotCardFailInt_Type(Integer32):
    """Custom type slotCardFailInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SlotCardFailInt_Type.__name__ = "Integer32"
_SlotCardFailInt_Object = MibTableColumn
slotCardFailInt = _SlotCardFailInt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 6),
    _SlotCardFailInt_Type()
)
slotCardFailInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFailInt.setStatus("mandatory")


class _SlotCardStFail_Type(Integer32):
    """Custom type slotCardStFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SlotCardStFail_Type.__name__ = "Integer32"
_SlotCardStFail_Object = MibTableColumn
slotCardStFail = _SlotCardStFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 7),
    _SlotCardStFail_Type()
)
slotCardStFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardStFail.setStatus("mandatory")


class _SlotCardStFailInt_Type(Integer32):
    """Custom type slotCardStFailInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SlotCardStFailInt_Type.__name__ = "Integer32"
_SlotCardStFailInt_Object = MibTableColumn
slotCardStFailInt = _SlotCardStFailInt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 8),
    _SlotCardStFailInt_Type()
)
slotCardStFailInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardStFailInt.setStatus("mandatory")


class _SlotCardBusFail_Type(Integer32):
    """Custom type slotCardBusFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SlotCardBusFail_Type.__name__ = "Integer32"
_SlotCardBusFail_Object = MibTableColumn
slotCardBusFail = _SlotCardBusFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 9),
    _SlotCardBusFail_Type()
)
slotCardBusFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardBusFail.setStatus("mandatory")


class _SlotFrontType_Type(Integer32):
    """Custom type slotFrontType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              118,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              256)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("pcc", 2),
          ("vdp", 3),
          ("txr", 4),
          ("pic", 5),
          ("vcd", 6),
          ("vdpvcd", 7),
          ("powerSupplyMonitor", 8),
          ("powersupply", 9),
          ("sdp", 10),
          ("ipxBslot", 11),
          ("mt3T3", 12),
          ("adpSDI", 13),
          ("txr2", 14),
          ("xdp", 15),
          ("ldp", 16),
          ("xdpsdi", 17),
          ("ldpldi", 18),
          ("sdi", 19),
          ("ldi", 20),
          ("fdp", 21),
          ("cip", 22),
          ("ntc", 23),
          ("uback", 24),
          ("uni", 25),
          ("frp", 26),
          ("fri", 27),
          ("frpFRI", 28),
          ("mt3", 29),
          ("cdp", 30),
          ("e1T1", 31),
          ("atm", 32),
          ("npc", 33),
          ("arc", 34),
          ("ait", 35),
          ("ftc", 36),
          ("fpc", 37),
          ("ufm1", 38),
          ("ufm1U", 39),
          ("btmHP", 40),
          ("uvm", 41),
          ("uxm", 42),
          ("bcc", 102),
          ("asm", 103),
          ("bniT3", 104),
          ("bniE3", 105),
          ("mfrp", 106),
          ("asiT3", 107),
          ("asiE3", 108),
          ("asi0T3", 109),
          ("asi0E3", 110),
          ("bniOC3", 111),
          ("asiOC3", 112),
          ("bslot", 113),
          ("bcc3", 114),
          ("bxm", 118),
          ("hdm", 201),
          ("hdmHDI", 202),
          ("ldm", 203),
          ("ldmLDI", 204),
          ("hdi", 205),
          ("ntm", 206),
          ("frm", 207),
          ("frmFRI", 208),
          ("cvm", 209),
          ("npm", 210),
          ("arm", 211),
          ("btm", 212),
          ("ftm", 213),
          ("unknown", 256))
    )


_SlotFrontType_Type.__name__ = "Integer32"
_SlotFrontType_Object = MibTableColumn
slotFrontType = _SlotFrontType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 10),
    _SlotFrontType_Type()
)
slotFrontType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFrontType.setStatus("mandatory")
_SlotFrontSerial_Type = DisplayString
_SlotFrontSerial_Object = MibTableColumn
slotFrontSerial = _SlotFrontSerial_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 11),
    _SlotFrontSerial_Type()
)
slotFrontSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFrontSerial.setStatus("mandatory")


class _SlotBackInstalled_Type(Integer32):
    """Custom type slotBackInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SlotBackInstalled_Type.__name__ = "Integer32"
_SlotBackInstalled_Object = MibTableColumn
slotBackInstalled = _SlotBackInstalled_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 12),
    _SlotBackInstalled_Type()
)
slotBackInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBackInstalled.setStatus("mandatory")


class _SlotBackType_Type(Integer32):
    """Custom type slotBackType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              201,
              202,
              203,
              204)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("rs232", 2),
          ("rs449", 3),
          ("v35", 4),
          ("rs232D", 5),
          ("rs2328", 6),
          ("rs2324", 7),
          ("friV35", 8),
          ("e1", 9),
          ("t1", 10),
          ("pccb", 11),
          ("dds4", 12),
          ("dds8", 13),
          ("sr", 14),
          ("mt3", 15),
          ("friE1", 16),
          ("friT1", 17),
          ("j1", 18),
          ("y1", 19),
          ("t3", 20),
          ("e3", 21),
          ("friX21", 22),
          ("ari", 23),
          ("aitT3", 24),
          ("aitE3", 25),
          ("fpcV35", 26),
          ("fpcX21", 27),
          ("fpcE1", 28),
          ("fpcT1", 29),
          ("aitE2", 30),
          ("aitHSSI", 31),
          ("ufm1T1DB15", 32),
          ("ufm1E1DB15", 33),
          ("ufm1E1BNC", 34),
          ("ufm1UHSSI", 35),
          ("ufm1UV35", 36),
          ("ufm1UX21", 37),
          ("uai1T3", 38),
          ("uai1E3", 39),
          ("t1-2", 40),
          ("e1-2", 41),
          ("j1-2", 42),
          ("uaiT1", 43),
          ("uaiE1", 44),
          ("uaiOC3", 45),
          ("btiE1", 46),
          ("uaiT3", 47),
          ("uaiE3", 48),
          ("lmBCC", 102),
          ("lmAS", 103),
          ("t33", 104),
          ("e33", 105),
          ("t32", 106),
          ("e32", 107),
          ("smf2", 108),
          ("mmf2", 109),
          ("bcclm2", 110),
          ("stm1", 111),
          ("utp", 112),
          ("stp", 113),
          ("lmbxm", 114),
          ("smflr", 115),
          ("unknown", 116),
          ("init", 117),
          ("btmT3", 201),
          ("btmE3", 202),
          ("btmE2", 203),
          ("btmHSSI", 204))
    )


_SlotBackType_Type.__name__ = "Integer32"
_SlotBackType_Object = MibTableColumn
slotBackType = _SlotBackType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 13),
    _SlotBackType_Type()
)
slotBackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBackType.setStatus("mandatory")
_SlotBackSerial_Type = DisplayString
_SlotBackSerial_Object = MibTableColumn
slotBackSerial = _SlotBackSerial_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 14),
    _SlotBackSerial_Type()
)
slotBackSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBackSerial.setStatus("mandatory")
_SlotCardRAMId_Type = DisplayString
_SlotCardRAMId_Object = MibTableColumn
slotCardRAMId = _SlotCardRAMId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 15),
    _SlotCardRAMId_Type()
)
slotCardRAMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardRAMId.setStatus("mandatory")
_SlotCardROMId_Type = DisplayString
_SlotCardROMId_Object = MibTableColumn
slotCardROMId = _SlotCardROMId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 16),
    _SlotCardROMId_Type()
)
slotCardROMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardROMId.setStatus("mandatory")
_SlotCardBRAMId_Type = DisplayString
_SlotCardBRAMId_Object = MibTableColumn
slotCardBRAMId = _SlotCardBRAMId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 17),
    _SlotCardBRAMId_Type()
)
slotCardBRAMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardBRAMId.setStatus("mandatory")
_SlotCardBOOTId_Type = DisplayString
_SlotCardBOOTId_Object = MibTableColumn
slotCardBOOTId = _SlotCardBOOTId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 18),
    _SlotCardBOOTId_Type()
)
slotCardBOOTId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardBOOTId.setStatus("mandatory")
_SlotCardRAMSize_Type = Integer32
_SlotCardRAMSize_Object = MibTableColumn
slotCardRAMSize = _SlotCardRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 19),
    _SlotCardRAMSize_Type()
)
slotCardRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardRAMSize.setStatus("mandatory")


class _SlotCardFEPROMSize_Type(Integer32):
    """Custom type slotCardFEPROMSize based on Integer32"""
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
        *(("meg4", 1),
          ("meg3", 2),
          ("meg2", 3),
          ("unknown", 4),
          ("meg8", 5))
    )


_SlotCardFEPROMSize_Type.__name__ = "Integer32"
_SlotCardFEPROMSize_Object = MibTableColumn
slotCardFEPROMSize = _SlotCardFEPROMSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 20),
    _SlotCardFEPROMSize_Type()
)
slotCardFEPROMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFEPROMSize.setStatus("mandatory")
_SlotCardBRAMSize_Type = Integer32
_SlotCardBRAMSize_Object = MibTableColumn
slotCardBRAMSize = _SlotCardBRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 21),
    _SlotCardBRAMSize_Type()
)
slotCardBRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardBRAMSize.setStatus("mandatory")
_SlotCardFrontRev_Type = DisplayString
_SlotCardFrontRev_Object = MibTableColumn
slotCardFrontRev = _SlotCardFrontRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 22),
    _SlotCardFrontRev_Type()
)
slotCardFrontRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFrontRev.setStatus("mandatory")
_SlotCardBackRev_Type = DisplayString
_SlotCardBackRev_Object = MibTableColumn
slotCardBackRev = _SlotCardBackRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 23),
    _SlotCardBackRev_Type()
)
slotCardBackRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardBackRev.setStatus("mandatory")
_SlotCardActivateTime_Type = Integer32
_SlotCardActivateTime_Object = MibTableColumn
slotCardActivateTime = _SlotCardActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 24),
    _SlotCardActivateTime_Type()
)
slotCardActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardActivateTime.setStatus("mandatory")


class _SlotFrontNumPort_Type(Integer32):
    """Custom type slotFrontNumPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SlotFrontNumPort_Type.__name__ = "Integer32"
_SlotFrontNumPort_Object = MibTableColumn
slotFrontNumPort = _SlotFrontNumPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 25),
    _SlotFrontNumPort_Type()
)
slotFrontNumPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFrontNumPort.setStatus("mandatory")


class _SlotFrontQueue_Type(Integer32):
    """Custom type slotFrontQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256000),
    )


_SlotFrontQueue_Type.__name__ = "Integer32"
_SlotFrontQueue_Object = MibTableColumn
slotFrontQueue = _SlotFrontQueue_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 26),
    _SlotFrontQueue_Type()
)
slotFrontQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFrontQueue.setStatus("mandatory")


class _SlotFrontLnFormat_Type(Integer32):
    """Custom type slotFrontLnFormat based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("e1", 2),
          ("t1", 3),
          ("subrate", 4),
          ("t3", 5),
          ("e3", 6),
          ("oc3", 7),
          ("oc12", 8))
    )


_SlotFrontLnFormat_Type.__name__ = "Integer32"
_SlotFrontLnFormat_Object = MibTableColumn
slotFrontLnFormat = _SlotFrontLnFormat_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 27),
    _SlotFrontLnFormat_Type()
)
slotFrontLnFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFrontLnFormat.setStatus("mandatory")
_SlotFrontChCount_Type = Integer32
_SlotFrontChCount_Object = MibTableColumn
slotFrontChCount = _SlotFrontChCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 28),
    _SlotFrontChCount_Type()
)
slotFrontChCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFrontChCount.setStatus("mandatory")


class _SlotBackNumPort_Type(Integer32):
    """Custom type slotBackNumPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SlotBackNumPort_Type.__name__ = "Integer32"
_SlotBackNumPort_Object = MibTableColumn
slotBackNumPort = _SlotBackNumPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 29),
    _SlotBackNumPort_Type()
)
slotBackNumPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBackNumPort.setStatus("mandatory")


class _SlotBackLnFormat_Type(Integer32):
    """Custom type slotBackLnFormat based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("e1", 2),
          ("t1", 3),
          ("subrate", 4),
          ("t3", 5),
          ("e3", 6),
          ("oc3", 7),
          ("oc12", 8),
          ("bxmt3e3", 9),
          ("e2", 10),
          ("hssi", 11))
    )


_SlotBackLnFormat_Type.__name__ = "Integer32"
_SlotBackLnFormat_Object = MibTableColumn
slotBackLnFormat = _SlotBackLnFormat_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 30),
    _SlotBackLnFormat_Type()
)
slotBackLnFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBackLnFormat.setStatus("mandatory")


class _SlotBackSonetMode_Type(Integer32):
    """Custom type slotBackSonetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("smf", 1),
          ("mmf", 2),
          ("smflr", 3),
          ("null", 4),
          ("snm", 5),
          ("stm1e", 6),
          ("xlr", 7))
    )


_SlotBackSonetMode_Type.__name__ = "Integer32"
_SlotBackSonetMode_Object = MibTableColumn
slotBackSonetMode = _SlotBackSonetMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 31),
    _SlotBackSonetMode_Type()
)
slotBackSonetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBackSonetMode.setStatus("mandatory")


class _SlotFSTSupport_Type(Integer32):
    """Custom type slotFSTSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SlotFSTSupport_Type.__name__ = "Integer32"
_SlotFSTSupport_Object = MibTableColumn
slotFSTSupport = _SlotFSTSupport_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 32),
    _SlotFSTSupport_Type()
)
slotFSTSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFSTSupport.setStatus("mandatory")


class _SlotCardMuxBusUtil_Type(Integer32):
    """Custom type slotCardMuxBusUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 250),
    )


_SlotCardMuxBusUtil_Type.__name__ = "Integer32"
_SlotCardMuxBusUtil_Object = MibTableColumn
slotCardMuxBusUtil = _SlotCardMuxBusUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 33),
    _SlotCardMuxBusUtil_Type()
)
slotCardMuxBusUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCardMuxBusUtil.setStatus("mandatory")
_SlotCardFrontName_Type = DisplayString
_SlotCardFrontName_Object = MibTableColumn
slotCardFrontName = _SlotCardFrontName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 34),
    _SlotCardFrontName_Type()
)
slotCardFrontName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFrontName.setStatus("mandatory")
_SlotCardMinReqBusBWCell_Type = Integer32
_SlotCardMinReqBusBWCell_Object = MibTableColumn
slotCardMinReqBusBWCell = _SlotCardMinReqBusBWCell_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 35),
    _SlotCardMinReqBusBWCell_Type()
)
slotCardMinReqBusBWCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardMinReqBusBWCell.setStatus("mandatory")
_SlotCardMaxPortBusBW_Type = Integer32
_SlotCardMaxPortBusBW_Object = MibTableColumn
slotCardMaxPortBusBW = _SlotCardMaxPortBusBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 36),
    _SlotCardMaxPortBusBW_Type()
)
slotCardMaxPortBusBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardMaxPortBusBW.setStatus("mandatory")
_SlotCardAvgUsedBusBWCell_Type = Integer32
_SlotCardAvgUsedBusBWCell_Object = MibTableColumn
slotCardAvgUsedBusBWCell = _SlotCardAvgUsedBusBWCell_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 37),
    _SlotCardAvgUsedBusBWCell_Type()
)
slotCardAvgUsedBusBWCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardAvgUsedBusBWCell.setStatus("mandatory")
_SlotCardUsedPeakBusBWCell_Type = Integer32
_SlotCardUsedPeakBusBWCell_Object = MibTableColumn
slotCardUsedPeakBusBWCell = _SlotCardUsedPeakBusBWCell_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 38),
    _SlotCardUsedPeakBusBWCell_Type()
)
slotCardUsedPeakBusBWCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardUsedPeakBusBWCell.setStatus("mandatory")
_SlotCardAllocBusUBU_Type = Integer32
_SlotCardAllocBusUBU_Object = MibTableColumn
slotCardAllocBusUBU = _SlotCardAllocBusUBU_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 39),
    _SlotCardAllocBusUBU_Type()
)
slotCardAllocBusUBU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCardAllocBusUBU.setStatus("mandatory")
_SlotCardTrunkPorts_Type = Integer32
_SlotCardTrunkPorts_Object = MibTableColumn
slotCardTrunkPorts = _SlotCardTrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 40),
    _SlotCardTrunkPorts_Type()
)
slotCardTrunkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCardTrunkPorts.setStatus("mandatory")
_SlotCardMinBusUBU_Type = Integer32
_SlotCardMinBusUBU_Object = MibTableColumn
slotCardMinBusUBU = _SlotCardMinBusUBU_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 41),
    _SlotCardMinBusUBU_Type()
)
slotCardMinBusUBU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCardMinBusUBU.setStatus("mandatory")
_SlotCardMinReqBusBWFpkt_Type = Integer32
_SlotCardMinReqBusBWFpkt_Object = MibTableColumn
slotCardMinReqBusBWFpkt = _SlotCardMinReqBusBWFpkt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 42),
    _SlotCardMinReqBusBWFpkt_Type()
)
slotCardMinReqBusBWFpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardMinReqBusBWFpkt.setStatus("mandatory")
_SlotCardAvgUsedBusBWFpkt_Type = Integer32
_SlotCardAvgUsedBusBWFpkt_Object = MibTableColumn
slotCardAvgUsedBusBWFpkt = _SlotCardAvgUsedBusBWFpkt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 43),
    _SlotCardAvgUsedBusBWFpkt_Type()
)
slotCardAvgUsedBusBWFpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardAvgUsedBusBWFpkt.setStatus("mandatory")
_SlotCardUsedPeakBusBWFpkt_Type = Integer32
_SlotCardUsedPeakBusBWFpkt_Object = MibTableColumn
slotCardUsedPeakBusBWFpkt = _SlotCardUsedPeakBusBWFpkt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 2, 1, 1, 44),
    _SlotCardUsedPeakBusBWFpkt_Type()
)
slotCardUsedPeakBusBWFpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardUsedPeakBusBWFpkt.setStatus("mandatory")
_ShelfTrapObjects_ObjectIdentity = ObjectIdentity
shelfTrapObjects = _ShelfTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 3)
)
_SwitchMedia_ObjectIdentity = ObjectIdentity
switchMedia = _SwitchMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5)
)
_Ds1LineTable_Object = MibTable
ds1LineTable = _Ds1LineTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ds1LineTable.setStatus("mandatory")
_Ds1LineEntry_Object = MibTableRow
ds1LineEntry = _Ds1LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1, 1)
)
ds1LineEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    ds1LineEntry.setStatus("mandatory")


class _Ds1LineStatus_Type(Integer32):
    """Custom type ds1LineStatus based on Integer32"""
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
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("down", 4),
          ("deact", 5))
    )


_Ds1LineStatus_Type.__name__ = "Integer32"
_Ds1LineStatus_Object = MibTableColumn
ds1LineStatus = _Ds1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1, 1, 1),
    _Ds1LineStatus_Type()
)
ds1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineStatus.setStatus("mandatory")


class _Ds1LineAlmType_Type(Integer32):
    """Custom type ds1LineAlmType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("lineAlmTypeOTHER", 1),
          ("lineAlmTypeOK", 2),
          ("lineAlmTypeDEACT", 3),
          ("lineAlmTypeACT", 4),
          ("lineAlmTypeBPV", 5),
          ("lineAlmTypeFS", 6),
          ("lineAlmTypeFER", 7),
          ("lineAlmTypePKOOF", 8),
          ("lineAlmTypeOOF", 9),
          ("lineAlmTypeLOS", 10),
          ("lineAlmTypeBADCLK", 11),
          ("lineAlmTypeCRC", 12),
          ("lineAlmTypePKCRC", 13),
          ("lineAlmTypeOOM", 14),
          ("lineAlmTypeAIS", 15),
          ("lineAlmTypeLCV", 16),
          ("lineAlmTypePCVL", 17),
          ("lineAlmTypePCVP", 18),
          ("lineAlmTypeBCV", 19),
          ("lineAlmTypeATMCRC", 20),
          ("lineAlmTypePLCPOOF", 21),
          ("lineAlmTypeCDMISS", 22),
          ("lineAlmTypeNET", 23))
    )


_Ds1LineAlmType_Type.__name__ = "Integer32"
_Ds1LineAlmType_Object = MibTableColumn
ds1LineAlmType = _Ds1LineAlmType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1, 1, 2),
    _Ds1LineAlmType_Type()
)
ds1LineAlmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineAlmType.setStatus("mandatory")


class _Ds1LineType_Type(Integer32):
    """Custom type ds1LineType based on Integer32"""
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
        *(("other", 1),
          ("ds1ESF", 2),
          ("ds1D4", 3),
          ("ds1E1", 4),
          ("ds1E1CRC", 5))
    )


_Ds1LineType_Type.__name__ = "Integer32"
_Ds1LineType_Object = MibTableColumn
ds1LineType = _Ds1LineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1, 1, 3),
    _Ds1LineType_Type()
)
ds1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineType.setStatus("mandatory")


class _Ds1LineCode_Type(Integer32):
    """Custom type ds1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ds1JBZS", 1),
          ("ds1B8ZS", 2),
          ("ds1HDB3", 3),
          ("ds1ZBTSI", 4),
          ("ds1AMI", 5),
          ("other", 6),
          ("ds1ZCS", 7))
    )


_Ds1LineCode_Type.__name__ = "Integer32"
_Ds1LineCode_Object = MibTableColumn
ds1LineCode = _Ds1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1, 1, 4),
    _Ds1LineCode_Type()
)
ds1LineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineCode.setStatus("mandatory")


class _Ds1ClkSource_Type(Integer32):
    """Custom type ds1ClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3))
    )


_Ds1ClkSource_Type.__name__ = "Integer32"
_Ds1ClkSource_Object = MibTableColumn
ds1ClkSource = _Ds1ClkSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 1, 1, 5),
    _Ds1ClkSource_Type()
)
ds1ClkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ClkSource.setStatus("mandatory")
_Ds3LineTable_Object = MibTable
ds3LineTable = _Ds3LineTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ds3LineTable.setStatus("mandatory")
_Ds3LineEntry_Object = MibTableRow
ds3LineEntry = _Ds3LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1)
)
ds3LineEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    ds3LineEntry.setStatus("mandatory")


class _Ds3LineStatus_Type(Integer32):
    """Custom type ds3LineStatus based on Integer32"""
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
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("down", 4),
          ("deact", 5))
    )


_Ds3LineStatus_Type.__name__ = "Integer32"
_Ds3LineStatus_Object = MibTableColumn
ds3LineStatus = _Ds3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 1),
    _Ds3LineStatus_Type()
)
ds3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineStatus.setStatus("mandatory")


class _Ds3LineAlmType_Type(Integer32):
    """Custom type ds3LineAlmType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("lineAlmTypeOTHER", 1),
          ("lineAlmTypeOK", 2),
          ("lineAlmTypeDEACT", 3),
          ("lineAlmTypeACT", 4),
          ("lineAlmTypeBPV", 5),
          ("lineAlmTypeFS", 6),
          ("lineAlmTypeFER", 7),
          ("lineAlmTypePKOOF", 8),
          ("lineAlmTypeOOF", 9),
          ("lineAlmTypeLOS", 10),
          ("lineAlmTypeBADCLK", 11),
          ("lineAlmTypeCRC", 12),
          ("lineAlmTypePKCRC", 13),
          ("lineAlmTypeOOM", 14),
          ("lineAlmTypeAIS", 15),
          ("lineAlmTypeLCV", 16),
          ("lineAlmTypePCVL", 17),
          ("lineAlmTypePCVP", 18),
          ("lineAlmTypeBCV", 19),
          ("lineAlmTypeATMCRC", 20),
          ("lineAlmTypePLCPOOF", 21),
          ("lineAlmTypeCDMISS", 22),
          ("lineAlmTypeNET", 23))
    )


_Ds3LineAlmType_Type.__name__ = "Integer32"
_Ds3LineAlmType_Object = MibTableColumn
ds3LineAlmType = _Ds3LineAlmType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 2),
    _Ds3LineAlmType_Type()
)
ds3LineAlmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineAlmType.setStatus("mandatory")


class _Ds3LineType_Type(Integer32):
    """Custom type ds3LineType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ds3other", 1),
          ("ds3M23", 2),
          ("ds3SYNTRAN", 3),
          ("ds3CbitPar", 4),
          ("ds3ClearChan", 5),
          ("e3other", 6),
          ("e3Framed", 7),
          ("e3Plcp", 8))
    )


_Ds3LineType_Type.__name__ = "Integer32"
_Ds3LineType_Object = MibTableColumn
ds3LineType = _Ds3LineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 3),
    _Ds3LineType_Type()
)
ds3LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineType.setStatus("mandatory")


class _Ds3LineCode_Type(Integer32):
    """Custom type ds3LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3Other", 1),
          ("ds3B3ZS", 2),
          ("e3HDB3", 3))
    )


_Ds3LineCode_Type.__name__ = "Integer32"
_Ds3LineCode_Object = MibTableColumn
ds3LineCode = _Ds3LineCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 4),
    _Ds3LineCode_Type()
)
ds3LineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineCode.setStatus("mandatory")


class _Ds3ClkSource_Type(Integer32):
    """Custom type ds3ClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3))
    )


_Ds3ClkSource_Type.__name__ = "Integer32"
_Ds3ClkSource_Object = MibTableColumn
ds3ClkSource = _Ds3ClkSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 5),
    _Ds3ClkSource_Type()
)
ds3ClkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ClkSource.setStatus("mandatory")


class _Ds3LineLclLpbk_Type(Integer32):
    """Custom type ds3LineLclLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Ds3LineLclLpbk_Type.__name__ = "Integer32"
_Ds3LineLclLpbk_Object = MibTableColumn
ds3LineLclLpbk = _Ds3LineLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 6),
    _Ds3LineLclLpbk_Type()
)
ds3LineLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LineLclLpbk.setStatus("mandatory")


class _Ds3LineLclRmtLpbk_Type(Integer32):
    """Custom type ds3LineLclRmtLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Ds3LineLclRmtLpbk_Type.__name__ = "Integer32"
_Ds3LineLclRmtLpbk_Object = MibTableColumn
ds3LineLclRmtLpbk = _Ds3LineLclRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 2, 1, 7),
    _Ds3LineLclRmtLpbk_Type()
)
ds3LineLclRmtLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LineLclRmtLpbk.setStatus("mandatory")
_SonetIfTable_Object = MibTable
sonetIfTable = _SonetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3)
)
if mibBuilder.loadTexts:
    sonetIfTable.setStatus("mandatory")
_SonetIfEntry_Object = MibTableRow
sonetIfEntry = _SonetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1)
)
sonetIfEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    sonetIfEntry.setStatus("mandatory")


class _SonetIfStatus_Type(Integer32):
    """Custom type sonetIfStatus based on Integer32"""
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
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("down", 4),
          ("deact", 5))
    )


_SonetIfStatus_Type.__name__ = "Integer32"
_SonetIfStatus_Object = MibTableColumn
sonetIfStatus = _SonetIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 1),
    _SonetIfStatus_Type()
)
sonetIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetIfStatus.setStatus("mandatory")


class _SonetIfAlmType_Type(Integer32):
    """Custom type sonetIfAlmType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("lineAlmTypeOTHER", 1),
          ("lineAlmTypeOK", 2),
          ("lineAlmTypeDEACT", 3),
          ("lineAlmTypeACT", 4),
          ("lineAlmTypeBPV", 5),
          ("lineAlmTypeFS", 6),
          ("lineAlmTypeFER", 7),
          ("lineAlmTypePKOOF", 8),
          ("lineAlmTypeOOF", 9),
          ("lineAlmTypeLOS", 10),
          ("lineAlmTypeBADCLK", 11),
          ("lineAlmTypeCRC", 12),
          ("lineAlmTypePKCRC", 13),
          ("lineAlmTypeOOM", 14),
          ("lineAlmTypeAIS", 15),
          ("lineAlmTypeLCV", 16),
          ("lineAlmTypePCVL", 17),
          ("lineAlmTypePCVP", 18),
          ("lineAlmTypeBCV", 19),
          ("lineAlmTypeATMCRC", 20),
          ("lineAlmTypePLCPOOF", 21),
          ("lineAlmTypeCDMISS", 22),
          ("lineAlmTypeNET", 23))
    )


_SonetIfAlmType_Type.__name__ = "Integer32"
_SonetIfAlmType_Object = MibTableColumn
sonetIfAlmType = _SonetIfAlmType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 2),
    _SonetIfAlmType_Type()
)
sonetIfAlmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetIfAlmType.setStatus("mandatory")


class _SonetIfType_Type(Integer32):
    """Custom type sonetIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sonetOther", 1),
          ("sonetShortSingleMode", 2),
          ("sonetLongSingleMode", 3),
          ("sonetMultiMode", 4),
          ("sonetCoax", 5),
          ("sonetUTP", 6),
          ("sonetXLongSingleMode", 7))
    )


_SonetIfType_Type.__name__ = "Integer32"
_SonetIfType_Object = MibTableColumn
sonetIfType = _SonetIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 3),
    _SonetIfType_Type()
)
sonetIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetIfType.setStatus("mandatory")


class _SonetIfFrame_Type(Integer32):
    """Custom type sonetIfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonetOther", 1),
          ("sonetSTS-3C", 2),
          ("sonetSTM-1", 3))
    )


_SonetIfFrame_Type.__name__ = "Integer32"
_SonetIfFrame_Object = MibTableColumn
sonetIfFrame = _SonetIfFrame_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 4),
    _SonetIfFrame_Type()
)
sonetIfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetIfFrame.setStatus("mandatory")
_SonetIfHiSpeed_Type = Integer32
_SonetIfHiSpeed_Object = MibTableColumn
sonetIfHiSpeed = _SonetIfHiSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 5),
    _SonetIfHiSpeed_Type()
)
sonetIfHiSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetIfHiSpeed.setStatus("mandatory")


class _SonetIfClkSource_Type(Integer32):
    """Custom type sonetIfClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3))
    )


_SonetIfClkSource_Type.__name__ = "Integer32"
_SonetIfClkSource_Object = MibTableColumn
sonetIfClkSource = _SonetIfClkSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 6),
    _SonetIfClkSource_Type()
)
sonetIfClkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetIfClkSource.setStatus("mandatory")


class _SonetIfLclLpbk_Type(Integer32):
    """Custom type sonetIfLclLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SonetIfLclLpbk_Type.__name__ = "Integer32"
_SonetIfLclLpbk_Object = MibTableColumn
sonetIfLclLpbk = _SonetIfLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 7),
    _SonetIfLclLpbk_Type()
)
sonetIfLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetIfLclLpbk.setStatus("mandatory")


class _SonetIfLclRmtLpbk_Type(Integer32):
    """Custom type sonetIfLclRmtLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SonetIfLclRmtLpbk_Type.__name__ = "Integer32"
_SonetIfLclRmtLpbk_Object = MibTableColumn
sonetIfLclRmtLpbk = _SonetIfLclRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 3, 1, 8),
    _SonetIfLclRmtLpbk_Type()
)
sonetIfLclRmtLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetIfLclRmtLpbk.setStatus("mandatory")
_Ds1LineStatsTable_Object = MibTable
ds1LineStatsTable = _Ds1LineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4)
)
if mibBuilder.loadTexts:
    ds1LineStatsTable.setStatus("mandatory")
_Ds1LineStatsEntry_Object = MibTableRow
ds1LineStatsEntry = _Ds1LineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1)
)
ds1LineStatsEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    ds1LineStatsEntry.setStatus("mandatory")
_Ds1StatsBpvs_Type = Counter32
_Ds1StatsBpvs_Object = MibTableColumn
ds1StatsBpvs = _Ds1StatsBpvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 1),
    _Ds1StatsBpvs_Type()
)
ds1StatsBpvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsBpvs.setStatus("mandatory")
_Ds1StatsFs_Type = Counter32
_Ds1StatsFs_Object = MibTableColumn
ds1StatsFs = _Ds1StatsFs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 2),
    _Ds1StatsFs_Type()
)
ds1StatsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsFs.setStatus("mandatory")
_Ds1StatsOofs_Type = Counter32
_Ds1StatsOofs_Object = MibTableColumn
ds1StatsOofs = _Ds1StatsOofs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 3),
    _Ds1StatsOofs_Type()
)
ds1StatsOofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsOofs.setStatus("mandatory")
_Ds1StatsLoss_Type = Counter32
_Ds1StatsLoss_Object = MibTableColumn
ds1StatsLoss = _Ds1StatsLoss_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 4),
    _Ds1StatsLoss_Type()
)
ds1StatsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsLoss.setStatus("mandatory")
_Ds1StatsFers_Type = Counter32
_Ds1StatsFers_Object = MibTableColumn
ds1StatsFers = _Ds1StatsFers_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 5),
    _Ds1StatsFers_Type()
)
ds1StatsFers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsFers.setStatus("mandatory")
_Ds1StatsCrcs_Type = Counter32
_Ds1StatsCrcs_Object = MibTableColumn
ds1StatsCrcs = _Ds1StatsCrcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 6),
    _Ds1StatsCrcs_Type()
)
ds1StatsCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsCrcs.setStatus("mandatory")
_Ds1StatsOoms_Type = Counter32
_Ds1StatsOoms_Object = MibTableColumn
ds1StatsOoms = _Ds1StatsOoms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 7),
    _Ds1StatsOoms_Type()
)
ds1StatsOoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsOoms.setStatus("mandatory")
_Ds1StatsAis16s_Type = Counter32
_Ds1StatsAis16s_Object = MibTableColumn
ds1StatsAis16s = _Ds1StatsAis16s_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 4, 1, 8),
    _Ds1StatsAis16s_Type()
)
ds1StatsAis16s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1StatsAis16s.setStatus("mandatory")
_Ds3LineStatsTable_Object = MibTable
ds3LineStatsTable = _Ds3LineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5)
)
if mibBuilder.loadTexts:
    ds3LineStatsTable.setStatus("mandatory")
_Ds3LineStatsEntry_Object = MibTableRow
ds3LineStatsEntry = _Ds3LineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1)
)
ds3LineStatsEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    ds3LineStatsEntry.setStatus("mandatory")
_Ds3StatsOofs_Type = Counter32
_Ds3StatsOofs_Object = MibTableColumn
ds3StatsOofs = _Ds3StatsOofs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 1),
    _Ds3StatsOofs_Type()
)
ds3StatsOofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsOofs.setStatus("mandatory")
_Ds3StatsLoss_Type = Counter32
_Ds3StatsLoss_Object = MibTableColumn
ds3StatsLoss = _Ds3StatsLoss_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 2),
    _Ds3StatsLoss_Type()
)
ds3StatsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsLoss.setStatus("mandatory")
_Ds3StatsLcvs_Type = Counter32
_Ds3StatsLcvs_Object = MibTableColumn
ds3StatsLcvs = _Ds3StatsLcvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 3),
    _Ds3StatsLcvs_Type()
)
ds3StatsLcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsLcvs.setStatus("mandatory")
_Ds3StatsCPcvs_Type = Counter32
_Ds3StatsCPcvs_Object = MibTableColumn
ds3StatsCPcvs = _Ds3StatsCPcvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 4),
    _Ds3StatsCPcvs_Type()
)
ds3StatsCPcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsCPcvs.setStatus("mandatory")
_Ds3StatsPPcvs_Type = Counter32
_Ds3StatsPPcvs_Object = MibTableColumn
ds3StatsPPcvs = _Ds3StatsPPcvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 5),
    _Ds3StatsPPcvs_Type()
)
ds3StatsPPcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsPPcvs.setStatus("mandatory")
_Ds3StatsPlcpBcvs_Type = Counter32
_Ds3StatsPlcpBcvs_Object = MibTableColumn
ds3StatsPlcpBcvs = _Ds3StatsPlcpBcvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 6),
    _Ds3StatsPlcpBcvs_Type()
)
ds3StatsPlcpBcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsPlcpBcvs.setStatus("mandatory")
_Ds3StatsAtmCrcs_Type = Counter32
_Ds3StatsAtmCrcs_Object = MibTableColumn
ds3StatsAtmCrcs = _Ds3StatsAtmCrcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 7),
    _Ds3StatsAtmCrcs_Type()
)
ds3StatsAtmCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsAtmCrcs.setStatus("mandatory")
_Ds3StatsPktCrcs_Type = Counter32
_Ds3StatsPktCrcs_Object = MibTableColumn
ds3StatsPktCrcs = _Ds3StatsPktCrcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 8),
    _Ds3StatsPktCrcs_Type()
)
ds3StatsPktCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsPktCrcs.setStatus("mandatory")
_Ds3StatsPlcpOofs_Type = Counter32
_Ds3StatsPlcpOofs_Object = MibTableColumn
ds3StatsPlcpOofs = _Ds3StatsPlcpOofs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 5, 1, 9),
    _Ds3StatsPlcpOofs_Type()
)
ds3StatsPlcpOofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3StatsPlcpOofs.setStatus("mandatory")
_SonetStatsTable_Object = MibTable
sonetStatsTable = _SonetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 6)
)
if mibBuilder.loadTexts:
    sonetStatsTable.setStatus("mandatory")
_SonetStatsEntry_Object = MibTableRow
sonetStatsEntry = _SonetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 6, 1)
)
sonetStatsEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    sonetStatsEntry.setStatus("mandatory")
_SonetStatsOofs_Type = Counter32
_SonetStatsOofs_Object = MibTableColumn
sonetStatsOofs = _SonetStatsOofs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 6, 1, 1),
    _SonetStatsOofs_Type()
)
sonetStatsOofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetStatsOofs.setStatus("mandatory")
_SonetStatsLoss_Type = Counter32
_SonetStatsLoss_Object = MibTableColumn
sonetStatsLoss = _SonetStatsLoss_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 6, 1, 2),
    _SonetStatsLoss_Type()
)
sonetStatsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetStatsLoss.setStatus("mandatory")
_SonetStatsAtmCrcs_Type = Counter32
_SonetStatsAtmCrcs_Object = MibTableColumn
sonetStatsAtmCrcs = _SonetStatsAtmCrcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 6, 1, 3),
    _SonetStatsAtmCrcs_Type()
)
sonetStatsAtmCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetStatsAtmCrcs.setStatus("mandatory")
_SerialPortTable_Object = MibTable
serialPortTable = _SerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7)
)
if mibBuilder.loadTexts:
    serialPortTable.setStatus("mandatory")
_SerialPortEntry_Object = MibTableRow
serialPortEntry = _SerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1)
)
serialPortEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    serialPortEntry.setStatus("mandatory")


class _SerialPortIfType_Type(Integer32):
    """Custom type serialPortIfType based on Integer32"""
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
        *(("other", 1),
          ("rs232", 2),
          ("rs449", 3),
          ("x21", 4),
          ("v35", 5),
          ("hssi", 6))
    )


_SerialPortIfType_Type.__name__ = "Integer32"
_SerialPortIfType_Object = MibTableColumn
serialPortIfType = _SerialPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 1),
    _SerialPortIfType_Type()
)
serialPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortIfType.setStatus("mandatory")


class _SerialPortStatus_Type(Integer32):
    """Custom type serialPortStatus based on Integer32"""
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
        *(("other", 1),
          ("up", 2),
          ("down", 3),
          ("failed", 4))
    )


_SerialPortStatus_Type.__name__ = "Integer32"
_SerialPortStatus_Object = MibTableColumn
serialPortStatus = _SerialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 2),
    _SerialPortStatus_Type()
)
serialPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortStatus.setStatus("mandatory")


class _SerialPortDceDte_Type(Integer32):
    """Custom type serialPortDceDte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dce", 2),
          ("dte", 3))
    )


_SerialPortDceDte_Type.__name__ = "Integer32"
_SerialPortDceDte_Object = MibTableColumn
serialPortDceDte = _SerialPortDceDte_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 3),
    _SerialPortDceDte_Type()
)
serialPortDceDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortDceDte.setStatus("mandatory")


class _SerialPortClk_Type(Integer32):
    """Custom type serialPortClk based on Integer32"""
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
        *(("other", 1),
          ("normal", 2),
          ("split", 3),
          ("looped", 4))
    )


_SerialPortClk_Type.__name__ = "Integer32"
_SerialPortClk_Object = MibTableColumn
serialPortClk = _SerialPortClk_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 4),
    _SerialPortClk_Type()
)
serialPortClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortClk.setStatus("mandatory")


class _SerialPortUtil_Type(Integer32):
    """Custom type serialPortUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SerialPortUtil_Type.__name__ = "Integer32"
_SerialPortUtil_Object = MibTableColumn
serialPortUtil = _SerialPortUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 5),
    _SerialPortUtil_Type()
)
serialPortUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortUtil.setStatus("mandatory")
_SerialPortEndptPtr_Type = ObjectIdentifier
_SerialPortEndptPtr_Object = MibTableColumn
serialPortEndptPtr = _SerialPortEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 6),
    _SerialPortEndptPtr_Type()
)
serialPortEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortEndptPtr.setStatus("mandatory")
_SerialPortConnPtr_Type = ObjectIdentifier
_SerialPortConnPtr_Object = MibTableColumn
serialPortConnPtr = _SerialPortConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 7),
    _SerialPortConnPtr_Type()
)
serialPortConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortConnPtr.setStatus("mandatory")


class _SerialPortEiaUpdt_Type(Integer32):
    """Custom type serialPortEiaUpdt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SerialPortEiaUpdt_Type.__name__ = "Integer32"
_SerialPortEiaUpdt_Object = MibTableColumn
serialPortEiaUpdt = _SerialPortEiaUpdt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 8),
    _SerialPortEiaUpdt_Type()
)
serialPortEiaUpdt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortEiaUpdt.setStatus("mandatory")


class _SerialPortDfmEnable_Type(Integer32):
    """Custom type serialPortDfmEnable based on Integer32"""
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


_SerialPortDfmEnable_Type.__name__ = "Integer32"
_SerialPortDfmEnable_Object = MibTableColumn
serialPortDfmEnable = _SerialPortDfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 9),
    _SerialPortDfmEnable_Type()
)
serialPortDfmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortDfmEnable.setStatus("mandatory")


class _SerialPortDfmLen_Type(Integer32):
    """Custom type serialPortDfmLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("serialPortDfmOther", 1),
          ("serialPortDfm7", 7),
          ("serialPortDfm8", 8),
          ("serialPortDfm16", 16))
    )


_SerialPortDfmLen_Type.__name__ = "Integer32"
_SerialPortDfmLen_Object = MibTableColumn
serialPortDfmLen = _SerialPortDfmLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 5, 7, 1, 10),
    _SerialPortDfmLen_Type()
)
serialPortDfmLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortDfmLen.setStatus("mandatory")
_StrmErrors_ObjectIdentity = ObjectIdentity
strmErrors = _StrmErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 910)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATACOM-MIB",
    **{"stratacom": stratacom,
       "snmpAgents": snmpAgents,
       "strmSwitchMIB": strmSwitchMIB,
       "switchInterfaces": switchInterfaces,
       "switchIfTable": switchIfTable,
       "switchIfEntry": switchIfEntry,
       "switchIfIndex": switchIfIndex,
       "switchIfSlot": switchIfSlot,
       "switchIfPort": switchIfPort,
       "switchIfSubPort": switchIfSubPort,
       "switchIfMediaType": switchIfMediaType,
       "switchIfService": switchIfService,
       "switchIfAdmStatus": switchIfAdmStatus,
       "switchIfOperStatus": switchIfOperStatus,
       "switchIfPhysPort": switchIfPhysPort,
       "switchIfPartiId": switchIfPartiId,
       "switchIfCtrlerId": switchIfCtrlerId,
       "switchServiceObjects": switchServiceObjects,
       "frServiceObjects": frServiceObjects,
       "frLportCnfTable": frLportCnfTable,
       "frLportCnfEntry": frLportCnfEntry,
       "frLportSlotIndex": frLportSlotIndex,
       "frLportPortIndex": frLportPortIndex,
       "frLportPortDLCI": frLportPortDLCI,
       "frLportAdminStatus": frLportAdminStatus,
       "frLportOperStatus": frLportOperStatus,
       "frLportPortSpeed": frLportPortSpeed,
       "frLportClockType": frLportClockType,
       "frLportPortType": frLportPortType,
       "frLportVcCount": frLportVcCount,
       "frLportFirstVcPtr": frLportFirstVcPtr,
       "frLportAggrChCnt": frLportAggrChCnt,
       "frLportChSpeed": frLportChSpeed,
       "frLportMaxTxQDepth": frLportMaxTxQDepth,
       "frLportECNQThresh": frLportECNQThresh,
       "frLportDEThresh": frLportDEThresh,
       "frLportIDEMap": frLportIDEMap,
       "frLportSigProt": frLportSigProt,
       "frLportNNIStatus": frLportNNIStatus,
       "frLportAsynStatus": frLportAsynStatus,
       "frLportPolVerTmr": frLportPolVerTmr,
       "frLportErrThresh": frLportErrThresh,
       "frLportMonEveCnt": frLportMonEveCnt,
       "frLportCommPri": frLportCommPri,
       "frLportUpRNR": frLportUpRNR,
       "frLportLowRNR": frLportLowRNR,
       "frLportMinFrmFlgs": frLportMinFrmFlgs,
       "frLportOamThresh": frLportOamThresh,
       "frLportLinkTimer": frLportLinkTimer,
       "frLportPollCycle": frLportPollCycle,
       "frLportCLLMTimer": frLportCLLMTimer,
       "frLportEFCItoBECN": frLportEFCItoBECN,
       "frLportSrRTS": frLportSrRTS,
       "frLportSrDTR": frLportSrDTR,
       "frLportSrDCD": frLportSrDCD,
       "frLportSrCTS": frLportSrCTS,
       "frLportSrDSR": frLportSrDSR,
       "frLportLoopBack": frLportLoopBack,
       "frLportExtConFail": frLportExtConFail,
       "frLportLine": frLportLine,
       "frLportStartCh": frLportStartCh,
       "frLportExtProt": frLportExtProt,
       "frLportDte": frLportDte,
       "frLportStatTable": frLportStatTable,
       "frLportStatEntry": frLportStatEntry,
       "frLportRxBytes": frLportRxBytes,
       "frLportRxFrms": frLportRxFrms,
       "frLportTxBytes": frLportTxBytes,
       "frLportTxFrms": frLportTxFrms,
       "frLportTxFrmsFecns": frLportTxFrmsFecns,
       "frLportTxFrmsBecns": frLportTxFrmsBecns,
       "frLportCrcErrors": frLportCrcErrors,
       "frLportBadFmts": frLportBadFmts,
       "frLportAlgnErrors": frLportAlgnErrors,
       "frLportIllegLengths": frLportIllegLengths,
       "frLportDmaOvruns": frLportDmaOvruns,
       "frLportStatEnqUnis": frLportStatEnqUnis,
       "frLportStatTxUnis": frLportStatTxUnis,
       "frLportUpdtTxUnis": frLportUpdtTxUnis,
       "frLportInvldReqCnts": frLportInvldReqCnts,
       "frLportToutCntUnis": frLportToutCntUnis,
       "frLportSeqnmErrUnis": frLportSeqnmErrUnis,
       "frLportUnknDlcis": frLportUnknDlcis,
       "frLportDeFrmsDrops": frLportDeFrmsDrops,
       "frLportStatEnqNnis": frLportStatEnqNnis,
       "frLportStatRxNnis": frLportStatRxNnis,
       "frLportUpdtRxNnis": frLportUpdtRxNnis,
       "frLportToutCntNnis": frLportToutCntNnis,
       "frLportSeqnmErrNnis": frLportSeqnmErrNnis,
       "frLportCllmTxFrms": frLportCllmTxFrms,
       "frLportCllmTxBytes": frLportCllmTxBytes,
       "frLportCllmRxFrms": frLportCllmRxFrms,
       "frLportCllmRxBytes": frLportCllmRxBytes,
       "frLportCllmFailures": frLportCllmFailures,
       "frLportDscdQTxFrms": frLportDscdQTxFrms,
       "frLportDscdQTxBytes": frLportDscdQTxBytes,
       "frLportLmiFailFrms": frLportLmiFailFrms,
       "frLportLmiFailBytes": frLportLmiFailBytes,
       "atmServiceObjects": atmServiceObjects,
       "atmPortTable": atmPortTable,
       "atmPortEntry": atmPortEntry,
       "atmPortSlot": atmPortSlot,
       "atmPortPort": atmPortPort,
       "atmPortAdminStatus": atmPortAdminStatus,
       "atmPortOperStatus": atmPortOperStatus,
       "atmPortType": atmPortType,
       "atmPortIfType": atmPortIfType,
       "atmPortSpeed": atmPortSpeed,
       "atmPortAxis": atmPortAxis,
       "atmPortVcCount": atmPortVcCount,
       "atmPortFirstVcPtr": atmPortFirstVcPtr,
       "atmPortMetro": atmPortMetro,
       "atmPortMgmtProto": atmPortMgmtProto,
       "atmPortIlmiVpi": atmPortIlmiVpi,
       "atmPortIlmiVci": atmPortIlmiVci,
       "atmPortIlmiPollEnable": atmPortIlmiPollEnable,
       "atmPortIlmiTrapEnable": atmPortIlmiTrapEnable,
       "atmPortIlmiPollIntrvl": atmPortIlmiPollIntrvl,
       "atmPortIlmiErrorThresh": atmPortIlmiErrorThresh,
       "atmPortIlmiEventThresh": atmPortIlmiEventThresh,
       "atmPortLmiVpi": atmPortLmiVpi,
       "atmPortLmiVci": atmPortLmiVci,
       "atmPortLmiPollEnable": atmPortLmiPollEnable,
       "atmPortLmiStatEnqTimer": atmPortLmiStatEnqTimer,
       "atmPortLmiUpdStatTimer": atmPortLmiUpdStatTimer,
       "atmPortLmiStatEnqRetry": atmPortLmiStatEnqRetry,
       "atmPortLmiUpdStatRetry": atmPortLmiUpdStatRetry,
       "atmPortLmiPollTimer": atmPortLmiPollTimer,
       "atmPortPercUtil": atmPortPercUtil,
       "atmPortSvcChannels": atmPortSvcChannels,
       "atmPortShareLcn": atmPortShareLcn,
       "atmPortSvcLcnLow": atmPortSvcLcnLow,
       "atmPortSvcLcnHigh": atmPortSvcLcnHigh,
       "atmPortSvcVpiLow": atmPortSvcVpiLow,
       "atmPortSvcVpiHigh": atmPortSvcVpiHigh,
       "atmPortSvcVciLow": atmPortSvcVciLow,
       "atmPortSvcVciHigh": atmPortSvcVciHigh,
       "atmPortSvcQbinBitMap": atmPortSvcQbinBitMap,
       "atmPortSvcQbinSz": atmPortSvcQbinSz,
       "atmPortSvcBw": atmPortSvcBw,
       "atmPortSvcInUse": atmPortSvcInUse,
       "atmPortPvcInUse": atmPortPvcInUse,
       "atmPortIlmiAddrReg": atmPortIlmiAddrReg,
       "atmPortCACOverride": atmPortCACOverride,
       "atmPortLoad": atmPortLoad,
       "atmPortQueueTable": atmPortQueueTable,
       "atmPortQueueEntry": atmPortQueueEntry,
       "atmPortQueueIndex": atmPortQueueIndex,
       "atmPortQueueAdminStatus": atmPortQueueAdminStatus,
       "atmPortQueueType": atmPortQueueType,
       "atmPortQueueDepth": atmPortQueueDepth,
       "atmPortQueueClpHi": atmPortQueueClpHi,
       "atmPortQueueClpLo": atmPortQueueClpLo,
       "atmPortQueueEfciTh": atmPortQueueEfciTh,
       "atmPortQueueAlgorithm": atmPortQueueAlgorithm,
       "atmPortStatTable": atmPortStatTable,
       "atmPortStatEntry": atmPortStatEntry,
       "atmPortStatUnknVpiVcis": atmPortStatUnknVpiVcis,
       "atmPortStatBufferOvfls": atmPortStatBufferOvfls,
       "atmPortStatNonZeroGfcs": atmPortStatNonZeroGfcs,
       "atmPortStatIsuDiscards": atmPortStatIsuDiscards,
       "atmPortStatIsuEmptys": atmPortStatIsuEmptys,
       "atmPortStatAisRxs": atmPortStatAisRxs,
       "atmPortStatFerfRxs": atmPortStatFerfRxs,
       "atmPortStatCellsRxs": atmPortStatCellsRxs,
       "atmPortStatClpRxs": atmPortStatClpRxs,
       "atmPortStatEfciRxs": atmPortStatEfciRxs,
       "atmPortStatBcmRxs": atmPortStatBcmRxs,
       "atmPortStatCellsTxs": atmPortStatCellsTxs,
       "atmPortStatOamRxs": atmPortStatOamRxs,
       "atmPortStatPayldErrs": atmPortStatPayldErrs,
       "atmPortStatClpTxs": atmPortStatClpTxs,
       "atmPortStatEfciTxs": atmPortStatEfciTxs,
       "atmPortStatHdrDiscards": atmPortStatHdrDiscards,
       "atmPortStatIlmiGetRxs": atmPortStatIlmiGetRxs,
       "atmPortStatIlmiGetNextRxs": atmPortStatIlmiGetNextRxs,
       "atmPortStatIlmiGetNextTxs": atmPortStatIlmiGetNextTxs,
       "atmPortStatIlmiSetRxs": atmPortStatIlmiSetRxs,
       "atmPortStatIlmiTrapRxs": atmPortStatIlmiTrapRxs,
       "atmPortStatIlmiGetRspRxs": atmPortStatIlmiGetRspRxs,
       "atmPortStatIlmiGetTxs": atmPortStatIlmiGetTxs,
       "atmPortStatIlmiGetRspTxs": atmPortStatIlmiGetRspTxs,
       "atmPortStatIlmiTrapTxs": atmPortStatIlmiTrapTxs,
       "atmPortStatIlmiUnkRxs": atmPortStatIlmiUnkRxs,
       "atmPortStatLmiStatTxs": atmPortStatLmiStatTxs,
       "atmPortStatLmiUpdtStatTxs": atmPortStatLmiUpdtStatTxs,
       "atmPortStatLmiStatAckTxs": atmPortStatLmiStatAckTxs,
       "atmPortStatLmiStatEnqTxs": atmPortStatLmiStatEnqTxs,
       "atmPortStatLmiStatEnqRxs": atmPortStatLmiStatEnqRxs,
       "atmPortStatLmiStatRxs": atmPortStatLmiStatRxs,
       "atmPortStatLmiUpdStatRxs": atmPortStatLmiUpdStatRxs,
       "atmPortStatLmiStatAckRxs": atmPortStatLmiStatAckRxs,
       "voiceServiceObjects": voiceServiceObjects,
       "trunkServiceObjects": trunkServiceObjects,
       "fpRoutingTrunks": fpRoutingTrunks,
       "fpRteTrkEntry": fpRteTrkEntry,
       "fpRteTrkStatus": fpRteTrkStatus,
       "fpRteTrkAlmEnable": fpRteTrkAlmEnable,
       "fpRteTrkComStatus": fpRteTrkComStatus,
       "fpRteTrkTrnsCap": fpRteTrkTrnsCap,
       "fpRteTrkTrnsLoad": fpRteTrkTrnsLoad,
       "fpRteTrkRcvCap": fpRteTrkRcvCap,
       "fpRteTrkRcvLoad": fpRteTrkRcvLoad,
       "fpRteTrkOeNdType": fpRteTrkOeNdType,
       "fpRteTrkOeName": fpRteTrkOeName,
       "fpRteTrkOeIpAddr": fpRteTrkOeIpAddr,
       "fpRteTrkOeIfIndex": fpRteTrkOeIfIndex,
       "fpRteTrkOeDomain": fpRteTrkOeDomain,
       "fpRteTrkXmitRate": fpRteTrkXmitRate,
       "fpRteTrkPassSync": fpRteTrkPassSync,
       "fpRteTrkStatRes": fpRteTrkStatRes,
       "fpRteTrkLoopClock": fpRteTrkLoopClock,
       "fpRteTrkBdataBTxQlen": fpRteTrkBdataBTxQlen,
       "fpRteTrkBdataBTxEfcn": fpRteTrkBdataBTxEfcn,
       "fpRteTrkBdataBTxHiClp": fpRteTrkBdataBTxHiClp,
       "fpRteTrkBdataBTxLoClp": fpRteTrkBdataBTxLoClp,
       "fpRteTrkLinkType": fpRteTrkLinkType,
       "atmTrunks": atmTrunks,
       "atmTrkEntry": atmTrkEntry,
       "atmTrkStatus": atmTrkStatus,
       "atmTrkAlmEnable": atmTrkAlmEnable,
       "atmTrkComStatus": atmTrkComStatus,
       "atmTrkRcvRate": atmTrkRcvRate,
       "atmTrkTrnsCap": atmTrkTrnsCap,
       "atmTrkTrnsLoad": atmTrkTrnsLoad,
       "atmTrkRcvCap": atmTrkRcvCap,
       "atmTrkRcvLoad": atmTrkRcvLoad,
       "atmTrkType": atmTrkType,
       "atmTrkVPI": atmTrkVPI,
       "atmTrkResChans": atmTrkResChans,
       "atmTrkTrafCls": atmTrkTrafCls,
       "atmTrkOeNdType": atmTrkOeNdType,
       "atmTrkOeName": atmTrkOeName,
       "atmTrkOeIpAddr": atmTrkOeIpAddr,
       "atmTrkOeIfIndex": atmTrkOeIfIndex,
       "atmTrkOeDomain": atmTrkOeDomain,
       "atmTrkSvcChannels": atmTrkSvcChannels,
       "atmTrkShareLcn": atmTrkShareLcn,
       "atmTrkSvcLcnLow": atmTrkSvcLcnLow,
       "atmTrkSvcLcnHigh": atmTrkSvcLcnHigh,
       "atmTrkSvcVpiLow": atmTrkSvcVpiLow,
       "atmTrkSvcVpiHigh": atmTrkSvcVpiHigh,
       "atmTrkSvcVciLow": atmTrkSvcVciLow,
       "atmTrkSvcVciHigh": atmTrkSvcVciHigh,
       "atmTrkSvcQbinBitMap": atmTrkSvcQbinBitMap,
       "atmTrkSvcQbinSz": atmTrkSvcQbinSz,
       "atmTrkSvcBw": atmTrkSvcBw,
       "atmTrkSvcInUse": atmTrkSvcInUse,
       "atmTrkXmitRate": atmTrkXmitRate,
       "atmTrkPassSync": atmTrkPassSync,
       "atmTrkStatRes": atmTrkStatRes,
       "atmTrkLoopClock": atmTrkLoopClock,
       "atmTrkBdataBTxQlen": atmTrkBdataBTxQlen,
       "atmTrkBdataBRxQlen": atmTrkBdataBRxQlen,
       "atmTrkBdataBTxEfcn": atmTrkBdataBTxEfcn,
       "atmTrkBdataBRxEfcn": atmTrkBdataBRxEfcn,
       "atmTrkBdataBTxHiClp": atmTrkBdataBTxHiClp,
       "atmTrkBdataBRxHiClp": atmTrkBdataBRxHiClp,
       "atmTrkBdataBTxLoClp": atmTrkBdataBTxLoClp,
       "atmTrkBdataBRxLoClp": atmTrkBdataBRxLoClp,
       "atmTrkMaxChanPort": atmTrkMaxChanPort,
       "atmTrkLinkType": atmTrkLinkType,
       "atmTrkDerouteDelayTimer": atmTrkDerouteDelayTimer,
       "atmTrkGtwyChCount": atmTrkGtwyChCount,
       "atmTrkRetainedLinks": atmTrkRetainedLinks,
       "atmTrkImaWindowSize": atmTrkImaWindowSize,
       "atmTrkImaTrnsCnts": atmTrkImaTrnsCnts,
       "atmTrkImaReenableTimer": atmTrkImaReenableTimer,
       "fpTrunkStatsTable": fpTrunkStatsTable,
       "fpTrkStatsEntry": fpTrkStatsEntry,
       "fpTrkStatsPktCrcs": fpTrkStatsPktCrcs,
       "fpTrkStatsPktOofs": fpTrkStatsPktOofs,
       "fpTrkStatsTxVoPktDrps": fpTrkStatsTxVoPktDrps,
       "fpTrkStatsTxTsPktDrps": fpTrkStatsTxTsPktDrps,
       "fpTrkStatsTxNonTsPktDrps": fpTrkStatsTxNonTsPktDrps,
       "fpTrkStatsTxHiPrioPktDrps": fpTrkStatsTxHiPrioPktDrps,
       "fpTrkStatsTxBdataAPktDrps": fpTrkStatsTxBdataAPktDrps,
       "fpTrkStatsTxBdataBPktDrps": fpTrkStatsTxBdataBPktDrps,
       "fpTrkStatsTotalPktsTxtoLns": fpTrkStatsTotalPktsTxtoLns,
       "atmTrunkStatsTable": atmTrunkStatsTable,
       "atmTrkStatsEntry": atmTrkStatsEntry,
       "atmTrkStatsTxVoPktDrps": atmTrkStatsTxVoPktDrps,
       "atmTrkStatsTxTsPktDrps": atmTrkStatsTxTsPktDrps,
       "atmTrkStatsTxNonTsPktDrps": atmTrkStatsTxNonTsPktDrps,
       "atmTrkStatsTxHiPrioPktDrps": atmTrkStatsTxHiPrioPktDrps,
       "atmTrkStatsTxBdataAPktDrps": atmTrkStatsTxBdataAPktDrps,
       "atmTrkStatsTxBdataBPktDrps": atmTrkStatsTxBdataBPktDrps,
       "atmTrkStatsRxVoPktDrps": atmTrkStatsRxVoPktDrps,
       "atmTrkStatsRxTsPktDrps": atmTrkStatsRxTsPktDrps,
       "atmTrkStatsRxNonTsPktDrps": atmTrkStatsRxNonTsPktDrps,
       "atmTrkStatsRxHiPrioPktDrps": atmTrkStatsRxHiPrioPktDrps,
       "atmTrkStatsRxBdataAPktDrps": atmTrkStatsRxBdataAPktDrps,
       "atmTrkStatsRxBdataBPktDrps": atmTrkStatsRxBdataBPktDrps,
       "atmTrkStatsSpacerPktsDrps": atmTrkStatsSpacerPktsDrps,
       "atmTrkStatsTotalPktsTxtoLns": atmTrkStatsTotalPktsTxtoLns,
       "atmTrkStatsTotalPktsRxFromLns": atmTrkStatsTotalPktsRxFromLns,
       "atmTrkStatsTxVoCellDrps": atmTrkStatsTxVoCellDrps,
       "atmTrkStatsTxTsCellDrps": atmTrkStatsTxTsCellDrps,
       "atmTrkStatsTxNonTsCellDrps": atmTrkStatsTxNonTsCellDrps,
       "atmTrkStatsTxHiPrioCellDrps": atmTrkStatsTxHiPrioCellDrps,
       "atmTrkStatsTxBdataACellDrps": atmTrkStatsTxBdataACellDrps,
       "atmTrkStatsTxBdataBCellDrps": atmTrkStatsTxBdataBCellDrps,
       "atmTrkStatsTxCbrCellDrps": atmTrkStatsTxCbrCellDrps,
       "atmTrkStatsTxVbrCellDrps": atmTrkStatsTxVbrCellDrps,
       "atmTrkStatsTxAbrCellDrps": atmTrkStatsTxAbrCellDrps,
       "atmTrkStatsTotalCellsTxtoLns": atmTrkStatsTotalCellsTxtoLns,
       "atmTrkStatsTotalCellsRxFromPorts": atmTrkStatsTotalCellsRxFromPorts,
       "lineServiceObjects": lineServiceObjects,
       "lineChanTable": lineChanTable,
       "lineChanEntry": lineChanEntry,
       "lineChanChannelIndex": lineChanChannelIndex,
       "lineChanEndptPtr": lineChanEndptPtr,
       "lineChanIfType": lineChanIfType,
       "lineChanAdapVoice": lineChanAdapVoice,
       "lineChanDialType": lineChanDialType,
       "lineChanDtSignallingDelay": lineChanDtSignallingDelay,
       "lineChanDtMinWink": lineChanDtMinWink,
       "lineChanDtPlayOutDelay": lineChanDtPlayOutDelay,
       "lineChanRecvSigABit": lineChanRecvSigABit,
       "lineChanRecvSigBBit": lineChanRecvSigBBit,
       "lineChanRecvSigCBit": lineChanRecvSigCBit,
       "lineChanRecvSigDBit": lineChanRecvSigDBit,
       "lineChanXmitSigABit": lineChanXmitSigABit,
       "lineChanXmitSigBBit": lineChanXmitSigBBit,
       "lineChanXmitSigCBit": lineChanXmitSigCBit,
       "lineChanXmitSigDBit": lineChanXmitSigDBit,
       "lineChanIfTypeName": lineChanIfTypeName,
       "lineChanIfOnhkABit": lineChanIfOnhkABit,
       "lineChanIfOnhkBBit": lineChanIfOnhkBBit,
       "lineChanIfOnhkCBit": lineChanIfOnhkCBit,
       "lineChanIfOnhkDBit": lineChanIfOnhkDBit,
       "lineChanIfCondIndex": lineChanIfCondIndex,
       "lineChanEchoCancel": lineChanEchoCancel,
       "lineChanEchoRtnLoss": lineChanEchoRtnLoss,
       "lineChanEchoTone": lineChanEchoTone,
       "lineChanEchoConv": lineChanEchoConv,
       "lineChanEchoNlp": lineChanEchoNlp,
       "lineChanInGain": lineChanInGain,
       "lineChanOutGain": lineChanOutGain,
       "lineChanUtil": lineChanUtil,
       "lineChanEchoBgFilter": lineChanEchoBgFilter,
       "lineChanEchoBackCard": lineChanEchoBackCard,
       "lineChanDataDceDte": lineChanDataDceDte,
       "lineChanDataUcs": lineChanDataUcs,
       "lineChanConnPtr": lineChanConnPtr,
       "lineChanEiaUpdt": lineChanEiaUpdt,
       "lineChanTimeSlot": lineChanTimeSlot,
       "lineChanEndState": lineChanEndState,
       "circuitLines": circuitLines,
       "circuitLineEntry": circuitLineEntry,
       "cirLineCnfStatus": cirLineCnfStatus,
       "cirLinePassOe": cirLinePassOe,
       "cirLineCasswMode": cirLineCasswMode,
       "cirLineCasConType": cirLineCasConType,
       "cirLineCCSType": cirLineCCSType,
       "cirLineCASType": cirLineCASType,
       "cirLineCASParm1": cirLineCASParm1,
       "cirLineCASParm2": cirLineCASParm2,
       "cirLineCASParm3": cirLineCASParm3,
       "cirLineCASParm4": cirLineCASParm4,
       "cirLineCASParm5": cirLineCASParm5,
       "cirLineCASParm6": cirLineCASParm6,
       "cirLineCASParm7": cirLineCASParm7,
       "cirLineCASParm8": cirLineCASParm8,
       "cirLineCASParm9": cirLineCASParm9,
       "cirLineCASParm10": cirLineCASParm10,
       "cirLineCASParm11": cirLineCASParm11,
       "cirLineCASParm12": cirLineCASParm12,
       "cirLineCASParm13": cirLineCASParm13,
       "cirLineCASParm14": cirLineCASParm14,
       "cirLineCASParm15": cirLineCASParm15,
       "cirLineCASParm16": cirLineCASParm16,
       "cirLineCASParm17": cirLineCASParm17,
       "cirLineCASParm18": cirLineCASParm18,
       "cirLineCachedSVC": cirLineCachedSVC,
       "rsrcServiceObjects": rsrcServiceObjects,
       "rsrcPartiTable": rsrcPartiTable,
       "rsrcPartiEntry": rsrcPartiEntry,
       "rsrcPartiId": rsrcPartiId,
       "rsrcPartiAdminStatus": rsrcPartiAdminStatus,
       "rsrcPartiOperStatus": rsrcPartiOperStatus,
       "rsrcPartiPvcMaxLcns": rsrcPartiPvcMaxLcns,
       "rsrcPartiPvcMaxBw": rsrcPartiPvcMaxBw,
       "rsrcPartiVsiMinLcns": rsrcPartiVsiMinLcns,
       "rsrcPartiVsiMaxLcns": rsrcPartiVsiMaxLcns,
       "rsrcPartiVsiVpiStart": rsrcPartiVsiVpiStart,
       "rsrcPartiVsiVpiEnd": rsrcPartiVsiVpiEnd,
       "rsrcPartiVsiMinBw": rsrcPartiVsiMinBw,
       "rsrcPartiVsiMaxBw": rsrcPartiVsiMaxBw,
       "atmQbinTable": atmQbinTable,
       "atmQbinEntry": atmQbinEntry,
       "atmQbinId": atmQbinId,
       "atmQbinAdminStatus": atmQbinAdminStatus,
       "atmQbinOperStatus": atmQbinOperStatus,
       "atmQbinMinBw": atmQbinMinBw,
       "atmQbinDepth": atmQbinDepth,
       "atmQbinLoClp": atmQbinLoClp,
       "atmQbinHiClp": atmQbinHiClp,
       "atmQbinEfci": atmQbinEfci,
       "switchConnection": switchConnection,
       "connNextEndptIndex": connNextEndptIndex,
       "errStatusLastIndex": errStatusLastIndex,
       "errStatusTable": errStatusTable,
       "errStatusTableEntry": errStatusTableEntry,
       "errReqId": errReqId,
       "errCode": errCode,
       "errStatusDesc": errStatusDesc,
       "connTable": connTable,
       "connTableEntry": connTableEntry,
       "connIndex": connIndex,
       "connLclEndptDesc": connLclEndptDesc,
       "connType": connType,
       "connOeIndex": connOeIndex,
       "connRmtEndptDesc": connRmtEndptDesc,
       "connMasterFlag": connMasterFlag,
       "connClassOfService": connClassOfService,
       "connGroupFlag": connGroupFlag,
       "connAdminStatus": connAdminStatus,
       "connOperStatus": connOperStatus,
       "connNoRouteFoundFailure": connNoRouteFoundFailure,
       "connBumpFailure": connBumpFailure,
       "connFirstEndptPtr": connFirstEndptPtr,
       "connCurrRouteDesc": connCurrRouteDesc,
       "connPrefRouteDesc": connPrefRouteDesc,
       "connMstOSpacePkts": connMstOSpacePkts,
       "connMstOSpaceCells": connMstOSpaceCells,
       "connMstOSpaceBdaCmax": connMstOSpaceBdaCmax,
       "connMstOSpaceBdbCmax": connMstOSpaceBdbCmax,
       "connSlvOSpacePkts": connSlvOSpacePkts,
       "connSlvOSpaceCells": connSlvOSpaceCells,
       "connSlvOSpaceBdaCmax": connSlvOSpaceBdaCmax,
       "connSlvOSpaceBdbCmax": connSlvOSpaceBdbCmax,
       "connIcaRTD": connIcaRTD,
       "connGroupDesc": connGroupDesc,
       "frEndptTable": frEndptTable,
       "frEndptEntry": frEndptEntry,
       "frEndptIndex": frEndptIndex,
       "frEndptDesc": frEndptDesc,
       "frOtherEndptIndex": frOtherEndptIndex,
       "frOtherEndptDesc": frOtherEndptDesc,
       "frEndptAdminStatus": frEndptAdminStatus,
       "frEndptOperStatus": frEndptOperStatus,
       "frNoRouteFoundFailure": frNoRouteFoundFailure,
       "frBumpFailure": frBumpFailure,
       "frEndPointFailure": frEndPointFailure,
       "frTestFailure": frTestFailure,
       "frConnPtr": frConnPtr,
       "frNextPtr": frNextPtr,
       "frNextOnPortPtr": frNextOnPortPtr,
       "frEndptConnDesc": frEndptConnDesc,
       "frEndptTrkAvoidType": frEndptTrkAvoidType,
       "frEndptTrkAvoidZCS": frEndptTrkAvoidZCS,
       "frEndptSubType": frEndptSubType,
       "frEndptBWClass": frEndptBWClass,
       "frEndptMIR": frEndptMIR,
       "frEndptCIR": frEndptCIR,
       "frEndptBc": frEndptBc,
       "frEndptBe": frEndptBe,
       "frEndptVcQSize": frEndptVcQSize,
       "frEndptPIR": frEndptPIR,
       "frEndptCMAX": frEndptCMAX,
       "frEndptEcnQSize": frEndptEcnQSize,
       "frEndptQIR": frEndptQIR,
       "frEndptPercUtil": frEndptPercUtil,
       "frEndptOeMIR": frEndptOeMIR,
       "frEndptOeCIR": frEndptOeCIR,
       "frEndptOeBc": frEndptOeBc,
       "frEndptOeBe": frEndptOeBe,
       "frEndptOeVcQSize": frEndptOeVcQSize,
       "frEndptOePIR": frEndptOePIR,
       "frEndptOeCMAX": frEndptOeCMAX,
       "frEndptOeEcnQSize": frEndptOeEcnQSize,
       "frEndptOeQIR": frEndptOeQIR,
       "frEndptOePercUtil": frEndptOePercUtil,
       "frEndptEnableFST": frEndptEnableFST,
       "frEndptConnPrio": frEndptConnPrio,
       "frEndptGroupFlag": frEndptGroupFlag,
       "frEndptLocLpbkState": frEndptLocLpbkState,
       "frEndptLocRmtLpbkState": frEndptLocRmtLpbkState,
       "frEndptLpbkStatus": frEndptLpbkStatus,
       "frEndptTestType": frEndptTestType,
       "frEndptRtdTestDelay": frEndptRtdTestDelay,
       "frEndptGroupDesc": frEndptGroupDesc,
       "frEndptStatTable": frEndptStatTable,
       "frEndptStatEntry": frEndptStatEntry,
       "frEndptRxBytes": frEndptRxBytes,
       "frEndptRxBytesDscds": frEndptRxBytesDscds,
       "frEndptRxFrms": frEndptRxFrms,
       "frEndptRxFrmsDscds": frEndptRxFrmsDscds,
       "frEndptRxPkts": frEndptRxPkts,
       "frEndptRxPktsDscds": frEndptRxPktsDscds,
       "frEndptTxBytes": frEndptTxBytes,
       "frEndptTxBytesDscds": frEndptTxBytesDscds,
       "frEndptTxFrms": frEndptTxFrms,
       "frEndptTxFrmsDscds": frEndptTxFrmsDscds,
       "frEndptTxPkts": frEndptTxPkts,
       "frEndptTxFrmsFecns": frEndptTxFrmsFecns,
       "frEndptTxFrmsBecns": frEndptTxFrmsBecns,
       "frEndptSecInServices": frEndptSecInServices,
       "frEndptCongestMins": frEndptCongestMins,
       "frEndptRxFrmsDes": frEndptRxFrmsDes,
       "frEndptRxBytesDes": frEndptRxBytesDes,
       "frEndptTxFrmsDes": frEndptTxFrmsDes,
       "frEndptRxFrmsDeDscds": frEndptRxFrmsDeDscds,
       "frEndptRxFrmsCirs": frEndptRxFrmsCirs,
       "frEndptRxBytesCirs": frEndptRxBytesCirs,
       "frEndptTxFrmsCirs": frEndptTxFrmsCirs,
       "frEndptTxBytesCirs": frEndptTxBytesCirs,
       "frEndptUnknProtIngDscds": frEndptUnknProtIngDscds,
       "frEndptUnknProtEgrDscds": frEndptUnknProtEgrDscds,
       "frBwClassTable": frBwClassTable,
       "frBwClassEntry": frBwClassEntry,
       "frBwClassIndex": frBwClassIndex,
       "frBwClassMIR": frBwClassMIR,
       "frBwClassCIR": frBwClassCIR,
       "frBwClassVcQSize": frBwClassVcQSize,
       "frBwClassBc": frBwClassBc,
       "frBwClassPIR": frBwClassPIR,
       "frBwClassBe": frBwClassBe,
       "frBwClassCMAX": frBwClassCMAX,
       "frBwClassEcnQSize": frBwClassEcnQSize,
       "frBwClassQIR": frBwClassQIR,
       "frBwClassPercUtil": frBwClassPercUtil,
       "frBwClassOeMIR": frBwClassOeMIR,
       "frBwClassOeCIR": frBwClassOeCIR,
       "frBwClassOeVcQSize": frBwClassOeVcQSize,
       "frBwClassOeBc": frBwClassOeBc,
       "frBwClassOePIR": frBwClassOePIR,
       "frBwClassOeBe": frBwClassOeBe,
       "frBwClassOeCMAX": frBwClassOeCMAX,
       "frBwClassOeEcnQSize": frBwClassOeEcnQSize,
       "frBwClassOeQIR": frBwClassOeQIR,
       "frBwClassOePercUtil": frBwClassOePercUtil,
       "frBwClassEnableFST": frBwClassEnableFST,
       "frBwClassDescription": frBwClassDescription,
       "atmEndptTable": atmEndptTable,
       "atmEndptEntry": atmEndptEntry,
       "atmEndptIndex": atmEndptIndex,
       "atmEndptDesc": atmEndptDesc,
       "atmOtherEndptIndex": atmOtherEndptIndex,
       "atmOtherEndptDesc": atmOtherEndptDesc,
       "atmEndptAdminStatus": atmEndptAdminStatus,
       "atmEndptOperStatus": atmEndptOperStatus,
       "atmNoRouteFoundFailure": atmNoRouteFoundFailure,
       "atmBumpFailure": atmBumpFailure,
       "atmEndPointFailure": atmEndPointFailure,
       "atmTestFailure": atmTestFailure,
       "atmConnPtr": atmConnPtr,
       "atmNextPtr": atmNextPtr,
       "atmNextOnPortPtr": atmNextOnPortPtr,
       "atmEndptConnDesc": atmEndptConnDesc,
       "atmEndptTrkAvoidType": atmEndptTrkAvoidType,
       "atmEndptTrkAvoidZCS": atmEndptTrkAvoidZCS,
       "atmEndptSubType": atmEndptSubType,
       "atmEndptBWClass": atmEndptBWClass,
       "atmEndptMIR": atmEndptMIR,
       "atmEndptCIR": atmEndptCIR,
       "atmEndptVcQSize": atmEndptVcQSize,
       "atmEndptPIR": atmEndptPIR,
       "atmEndptEfciQSize": atmEndptEfciQSize,
       "atmEndptQIR": atmEndptQIR,
       "atmEndptPercUtil": atmEndptPercUtil,
       "atmEndptCBS": atmEndptCBS,
       "atmEndptIBS": atmEndptIBS,
       "atmEndptMFS": atmEndptMFS,
       "atmEndptCCDV": atmEndptCCDV,
       "atmEndptHiCLP": atmEndptHiCLP,
       "atmEndptLoCLP": atmEndptLoCLP,
       "atmEndptOeMIR": atmEndptOeMIR,
       "atmEndptOeCIR": atmEndptOeCIR,
       "atmEndptOeVcQSize": atmEndptOeVcQSize,
       "atmEndptOePIR": atmEndptOePIR,
       "atmEndptOeEfciQSize": atmEndptOeEfciQSize,
       "atmEndptOeQIR": atmEndptOeQIR,
       "atmEndptOePercUtil": atmEndptOePercUtil,
       "atmEndptOeCBS": atmEndptOeCBS,
       "atmEndptOeIBS": atmEndptOeIBS,
       "atmEndptOeMFS": atmEndptOeMFS,
       "atmEndptOeCCDV": atmEndptOeCCDV,
       "atmEndptOeHiCLP": atmEndptOeHiCLP,
       "atmEndptOeLoCLP": atmEndptOeLoCLP,
       "atmEndptCLPTagging": atmEndptCLPTagging,
       "atmEndptUPC": atmEndptUPC,
       "atmEndptEnableFST": atmEndptEnableFST,
       "atmEndptRateUpICA": atmEndptRateUpICA,
       "atmEndptRateDnICA": atmEndptRateDnICA,
       "atmEndptFastDnICA": atmEndptFastDnICA,
       "atmEndptToQIR": atmEndptToQIR,
       "atmEndptMinAdjustICA": atmEndptMinAdjustICA,
       "atmEndptGroupFlag": atmEndptGroupFlag,
       "atmEndptOamStatus": atmEndptOamStatus,
       "atmEndptBCM": atmEndptBCM,
       "atmEndptFGCRA": atmEndptFGCRA,
       "atmEndptLocLpbkState": atmEndptLocLpbkState,
       "atmEndptLpbkStatus": atmEndptLpbkStatus,
       "atmEndptTestType": atmEndptTestType,
       "atmEndptRtdTestDelay": atmEndptRtdTestDelay,
       "atmEndptOeBCM": atmEndptOeBCM,
       "atmEndptOeFGCRA": atmEndptOeFGCRA,
       "atmEndptGroupDesc": atmEndptGroupDesc,
       "atmEndptLocRmtLpbkState": atmEndptLocRmtLpbkState,
       "atmEndptScrPlc": atmEndptScrPlc,
       "atmEndptOeScrPlc": atmEndptOeScrPlc,
       "atmEndptPCR0": atmEndptPCR0,
       "atmEndptOePCR0": atmEndptOePCR0,
       "atmEndptCDVT0": atmEndptCDVT0,
       "atmEndptOeCDVT0": atmEndptOeCDVT0,
       "atmEndptNRM": atmEndptNRM,
       "atmEndptFRTT": atmEndptFRTT,
       "atmEndptTBE": atmEndptTBE,
       "atmEndptVSVD": atmEndptVSVD,
       "atmEndptPolicing": atmEndptPolicing,
       "atmEndptPCR": atmEndptPCR,
       "atmEndptOePCR": atmEndptOePCR,
       "atmEndptSCR": atmEndptSCR,
       "atmEndptOeSCR": atmEndptOeSCR,
       "atmEndptMCR": atmEndptMCR,
       "atmEndptOeMCR": atmEndptOeMCR,
       "atmEndptCellRouting": atmEndptCellRouting,
       "atmBwClassTable": atmBwClassTable,
       "atmBwClassEntry": atmBwClassEntry,
       "atmBwClassIndex": atmBwClassIndex,
       "atmBwClassMIR": atmBwClassMIR,
       "atmBwClassCIR": atmBwClassCIR,
       "atmBwClassVcQSize": atmBwClassVcQSize,
       "atmBwClassPIR": atmBwClassPIR,
       "atmBwClassEfciQSize": atmBwClassEfciQSize,
       "atmBwClassQIR": atmBwClassQIR,
       "atmBwClassPercUtil": atmBwClassPercUtil,
       "atmBwClassCBS": atmBwClassCBS,
       "atmBwClassIBS": atmBwClassIBS,
       "atmBwClassMFS": atmBwClassMFS,
       "atmBwClassCCDV": atmBwClassCCDV,
       "atmBwClassHiCLP": atmBwClassHiCLP,
       "atmBwClassLoCLP": atmBwClassLoCLP,
       "atmBwClassOeMIR": atmBwClassOeMIR,
       "atmBwClassOeCIR": atmBwClassOeCIR,
       "atmBwClassOeVcQSize": atmBwClassOeVcQSize,
       "atmBwClassOePIR": atmBwClassOePIR,
       "atmBwClassOeEfciQSize": atmBwClassOeEfciQSize,
       "atmBwClassOeQIR": atmBwClassOeQIR,
       "atmBwClassOePercUtil": atmBwClassOePercUtil,
       "atmBwClassOeCBS": atmBwClassOeCBS,
       "atmBwClassOeIBS": atmBwClassOeIBS,
       "atmBwClassOeMFS": atmBwClassOeMFS,
       "atmBwClassOeCCDV": atmBwClassOeCCDV,
       "atmBwClassOeHiCLP": atmBwClassOeHiCLP,
       "atmBwClassOeLoCLP": atmBwClassOeLoCLP,
       "atmBwClassCLPTagging": atmBwClassCLPTagging,
       "atmBwClassUPC": atmBwClassUPC,
       "atmBwClassEnableFST": atmBwClassEnableFST,
       "atmBwClassRateUpICA": atmBwClassRateUpICA,
       "atmBwClassRateDnICA": atmBwClassRateDnICA,
       "atmBwClassFastDnICA": atmBwClassFastDnICA,
       "atmBwClassToQIR": atmBwClassToQIR,
       "atmBwClassMinAdjustICA": atmBwClassMinAdjustICA,
       "atmBwClassDescription": atmBwClassDescription,
       "atmBwClassBCM": atmBwClassBCM,
       "atmBwClassFGCRA": atmBwClassFGCRA,
       "atmBwClassOeBCM": atmBwClassOeBCM,
       "atmBwClassOeFGCRA": atmBwClassOeFGCRA,
       "atmBwClassConType": atmBwClassConType,
       "atmBwClassScrPlc": atmBwClassScrPlc,
       "atmBwClassOeScrPlc": atmBwClassOeScrPlc,
       "atmBwClassPCR0": atmBwClassPCR0,
       "atmBwClassOePCR0": atmBwClassOePCR0,
       "atmBwClassCDVT0": atmBwClassCDVT0,
       "atmBwClassOeCDVT0": atmBwClassOeCDVT0,
       "atmBWClassNRM": atmBWClassNRM,
       "atmBWClassFRTT": atmBWClassFRTT,
       "atmBWClassTBE": atmBWClassTBE,
       "atmBWClassVSVD": atmBWClassVSVD,
       "atmBWClassPolicing": atmBWClassPolicing,
       "atmBWClassPCR": atmBWClassPCR,
       "atmBWClassOePCR": atmBWClassOePCR,
       "atmBWClassSCR": atmBWClassSCR,
       "atmBWClassOeSCR": atmBWClassOeSCR,
       "atmBWClassMCR": atmBWClassMCR,
       "atmBWClassOeMCR": atmBWClassOeMCR,
       "frEndptMapTable": frEndptMapTable,
       "frEndptMapEntry": frEndptMapEntry,
       "frEndptMapSlot": frEndptMapSlot,
       "frEndptMapPort": frEndptMapPort,
       "frEndptMapDlci": frEndptMapDlci,
       "frEndptMapEndptPtr": frEndptMapEndptPtr,
       "frEndptMapConnPtr": frEndptMapConnPtr,
       "atmEndptMapTable": atmEndptMapTable,
       "atmEndptMapEntry": atmEndptMapEntry,
       "atmEndptMapSlot": atmEndptMapSlot,
       "atmEndptMapPort": atmEndptMapPort,
       "atmEndptMapVpi": atmEndptMapVpi,
       "atmEndptMapVci": atmEndptMapVci,
       "atmEndptMapEndptPtr": atmEndptMapEndptPtr,
       "atmEndptMapConnPtr": atmEndptMapConnPtr,
       "atmEndptStatTable": atmEndptStatTable,
       "atmEndptStatEntry": atmEndptStatEntry,
       "atmCellsRxPorts": atmCellsRxPorts,
       "atmFramesRxPorts": atmFramesRxPorts,
       "atmCellsTxNets": atmCellsTxNets,
       "atmClpRxs": atmClpRxs,
       "atmViolRxs": atmViolRxs,
       "atmDiscardVcqClpThs": atmDiscardVcqClpThs,
       "atmDiscardVcqFulls": atmDiscardVcqFulls,
       "atmEfciRxs": atmEfciRxs,
       "atmNonCompRxs": atmNonCompRxs,
       "atmDiscardFails": atmDiscardFails,
       "atmAvgVcqDepths": atmAvgVcqDepths,
       "atmDiscardRsrcOflows": atmDiscardRsrcOflows,
       "atmDiscardSbinFulls": atmDiscardSbinFulls,
       "atmBcmRxs": atmBcmRxs,
       "atmBcmTxs": atmBcmTxs,
       "atmOamTxs": atmOamTxs,
       "atmDiscardQbinFulls": atmDiscardQbinFulls,
       "atmDiscardQbinClpThs": atmDiscardQbinClpThs,
       "atmCellsRxNets": atmCellsRxNets,
       "atmClpTxs": atmClpTxs,
       "atmEfciTxs": atmEfciTxs,
       "atmCellsTxPorts": atmCellsTxPorts,
       "atmAisRxs": atmAisRxs,
       "atmFerfRxs": atmFerfRxs,
       "voiceEndptTable": voiceEndptTable,
       "voiceEndptEntry": voiceEndptEntry,
       "voiceEndptIndex": voiceEndptIndex,
       "voiceOtherEndptIndex": voiceOtherEndptIndex,
       "voiceEndptDesc": voiceEndptDesc,
       "voiceOtherEndptDesc": voiceOtherEndptDesc,
       "voiceEndptConnDesc": voiceEndptConnDesc,
       "voiceEndptAdminStatus": voiceEndptAdminStatus,
       "voiceEndptOperStatus": voiceEndptOperStatus,
       "voiceEndptRateType": voiceEndptRateType,
       "voiceEndPointFailure": voiceEndPointFailure,
       "voiceNoRouteFoundFailure": voiceNoRouteFoundFailure,
       "voiceBumpFailure": voiceBumpFailure,
       "voiceTestFailure": voiceTestFailure,
       "voiceEndptTestType": voiceEndptTestType,
       "voiceEndptLpbkStatus": voiceEndptLpbkStatus,
       "voiceConnPtr": voiceConnPtr,
       "voiceChannelPtr": voiceChannelPtr,
       "voiceEndptTrkAvoidType": voiceEndptTrkAvoidType,
       "voiceEndptAvoidZCS": voiceEndptAvoidZCS,
       "voiceEndptState": voiceEndptState,
       "voiceEndptAdv": voiceEndptAdv,
       "voiceOtherEndptAdv": voiceOtherEndptAdv,
       "voiceEndptEncoding": voiceEndptEncoding,
       "voiceOtherEndptEncoding": voiceOtherEndptEncoding,
       "voiceEndptEndptType": voiceEndptEndptType,
       "voiceEndptLocLpbkState": voiceEndptLocLpbkState,
       "voiceEndptSvcId": voiceEndptSvcId,
       "voiceEndptIsSVC": voiceEndptIsSVC,
       "voiceEndptFaxModem": voiceEndptFaxModem,
       "voiceEndptLocRmtLpbk": voiceEndptLocRmtLpbk,
       "voiceStatTable": voiceStatTable,
       "voiceStatEntry": voiceStatEntry,
       "voiceStatPktsRxs": voiceStatPktsRxs,
       "voiceStatPktsXmits": voiceStatPktsXmits,
       "voiceStatRxPktsDscds": voiceStatRxPktsDscds,
       "voiceStatSprvPktsXmits": voiceStatSprvPktsXmits,
       "voiceStatSprvPktsRcvs": voiceStatSprvPktsRcvs,
       "voiceStatV25ModemOns": voiceStatV25ModemOns,
       "voiceStatDsiOns": voiceStatDsiOns,
       "voiceStatOffhks": voiceStatOffhks,
       "voiceStatInservices": voiceStatInservices,
       "voiceEndptConnMapTable": voiceEndptConnMapTable,
       "voiceEndptConnMapEntry": voiceEndptConnMapEntry,
       "voiceEndptConnMapChannel": voiceEndptConnMapChannel,
       "voiceEndptConnMapEndptPtr": voiceEndptConnMapEndptPtr,
       "voiceEndptConnMapConnPtr": voiceEndptConnMapConnPtr,
       "dataEndptTable": dataEndptTable,
       "dataEndptEntry": dataEndptEntry,
       "dataEndptIndex": dataEndptIndex,
       "dataOtherEndptIndex": dataOtherEndptIndex,
       "dataEndptDesc": dataEndptDesc,
       "dataOtherEndptDesc": dataOtherEndptDesc,
       "dataEndptAdmStatus": dataEndptAdmStatus,
       "dataEndptOperStatus": dataEndptOperStatus,
       "dataEndptRate": dataEndptRate,
       "dataEndPtRemoteFail": dataEndPtRemoteFail,
       "dataEndptNoRouteFail": dataEndptNoRouteFail,
       "dataEndptTestFail": dataEndptTestFail,
       "dataEndptTestType": dataEndptTestType,
       "dataEndptLpbkStatus": dataEndptLpbkStatus,
       "dataEndptLocLpbkEnable": dataEndptLocLpbkEnable,
       "dataEndptLocRmtLpbk": dataEndptLocRmtLpbk,
       "dataEndptConnPtr": dataEndptConnPtr,
       "dataEndptPortPtr": dataEndptPortPtr,
       "dataEndptTrkAvoid": dataEndptTrkAvoid,
       "dataEndptZCSAvoid": dataEndptZCSAvoid,
       "dataEndptFastEia": dataEndptFastEia,
       "dataEndptEiaUpdt": dataEndptEiaUpdt,
       "dataEndptSampPerPkt": dataEndptSampPerPkt,
       "dataEndptTspnt": dataEndptTspnt,
       "dataEndptSuperRateN": dataEndptSuperRateN,
       "dataEndptCoding": dataEndptCoding,
       "dataEndptDfmEnable": dataEndptDfmEnable,
       "dataEndptDfmLen": dataEndptDfmLen,
       "dataEndptOeDceDte": dataEndptOeDceDte,
       "dataEndptOeClk": dataEndptOeClk,
       "switchShelf": switchShelf,
       "shelfCnfgObjects": shelfCnfgObjects,
       "shelfCnfgStatMaster": shelfCnfgStatMaster,
       "shelfCnfgStatCollIntvl": shelfCnfgStatCollIntvl,
       "shelfCnfgStatBcktIntvl": shelfCnfgStatBcktIntvl,
       "shelfCnfgStatTimeSync": shelfCnfgStatTimeSync,
       "shelfCnfgSwError": shelfCnfgSwError,
       "shelfCnfgCardError": shelfCnfgCardError,
       "shelfCnfgEthIPAddr": shelfCnfgEthIPAddr,
       "shelfCnfgEthIPMask": shelfCnfgEthIPMask,
       "shelfCnfgEthMacAddr": shelfCnfgEthMacAddr,
       "shelfCnfgEthGWAddr": shelfCnfgEthGWAddr,
       "shelfCnfgNwIPAddr": shelfCnfgNwIPAddr,
       "shelfCnfgNwIPMask": shelfCnfgNwIPMask,
       "shelfCnfgNodeName": shelfCnfgNodeName,
       "shelfCnfgNodeNumber": shelfCnfgNodeNumber,
       "shelfCnfgDomainNumber": shelfCnfgDomainNumber,
       "shelfCnfgNodeType": shelfCnfgNodeType,
       "shelfCnfgAlarmStatus": shelfCnfgAlarmStatus,
       "shelfCnfgPrimSwRevision": shelfCnfgPrimSwRevision,
       "shelfCnfgSecSwRevision": shelfCnfgSecSwRevision,
       "shelfCnfgTimeZone": shelfCnfgTimeZone,
       "shelfCnfgTrapSeverity": shelfCnfgTrapSeverity,
       "shelfCnfgRebuildStatus": shelfCnfgRebuildStatus,
       "shelfCnfgJunctNode": shelfCnfgJunctNode,
       "shelfCnfgVcPollRate": shelfCnfgVcPollRate,
       "shelfInfoObjects": shelfInfoObjects,
       "shelfSlotInfoTable": shelfSlotInfoTable,
       "shelfSlotInfoEntry": shelfSlotInfoEntry,
       "slotIndex": slotIndex,
       "slotCardYred": slotCardYred,
       "slotCardYredSlot": slotCardYredSlot,
       "slotCardStatus": slotCardStatus,
       "slotCardFail": slotCardFail,
       "slotCardFailInt": slotCardFailInt,
       "slotCardStFail": slotCardStFail,
       "slotCardStFailInt": slotCardStFailInt,
       "slotCardBusFail": slotCardBusFail,
       "slotFrontType": slotFrontType,
       "slotFrontSerial": slotFrontSerial,
       "slotBackInstalled": slotBackInstalled,
       "slotBackType": slotBackType,
       "slotBackSerial": slotBackSerial,
       "slotCardRAMId": slotCardRAMId,
       "slotCardROMId": slotCardROMId,
       "slotCardBRAMId": slotCardBRAMId,
       "slotCardBOOTId": slotCardBOOTId,
       "slotCardRAMSize": slotCardRAMSize,
       "slotCardFEPROMSize": slotCardFEPROMSize,
       "slotCardBRAMSize": slotCardBRAMSize,
       "slotCardFrontRev": slotCardFrontRev,
       "slotCardBackRev": slotCardBackRev,
       "slotCardActivateTime": slotCardActivateTime,
       "slotFrontNumPort": slotFrontNumPort,
       "slotFrontQueue": slotFrontQueue,
       "slotFrontLnFormat": slotFrontLnFormat,
       "slotFrontChCount": slotFrontChCount,
       "slotBackNumPort": slotBackNumPort,
       "slotBackLnFormat": slotBackLnFormat,
       "slotBackSonetMode": slotBackSonetMode,
       "slotFSTSupport": slotFSTSupport,
       "slotCardMuxBusUtil": slotCardMuxBusUtil,
       "slotCardFrontName": slotCardFrontName,
       "slotCardMinReqBusBWCell": slotCardMinReqBusBWCell,
       "slotCardMaxPortBusBW": slotCardMaxPortBusBW,
       "slotCardAvgUsedBusBWCell": slotCardAvgUsedBusBWCell,
       "slotCardUsedPeakBusBWCell": slotCardUsedPeakBusBWCell,
       "slotCardAllocBusUBU": slotCardAllocBusUBU,
       "slotCardTrunkPorts": slotCardTrunkPorts,
       "slotCardMinBusUBU": slotCardMinBusUBU,
       "slotCardMinReqBusBWFpkt": slotCardMinReqBusBWFpkt,
       "slotCardAvgUsedBusBWFpkt": slotCardAvgUsedBusBWFpkt,
       "slotCardUsedPeakBusBWFpkt": slotCardUsedPeakBusBWFpkt,
       "shelfTrapObjects": shelfTrapObjects,
       "switchMedia": switchMedia,
       "ds1LineTable": ds1LineTable,
       "ds1LineEntry": ds1LineEntry,
       "ds1LineStatus": ds1LineStatus,
       "ds1LineAlmType": ds1LineAlmType,
       "ds1LineType": ds1LineType,
       "ds1LineCode": ds1LineCode,
       "ds1ClkSource": ds1ClkSource,
       "ds3LineTable": ds3LineTable,
       "ds3LineEntry": ds3LineEntry,
       "ds3LineStatus": ds3LineStatus,
       "ds3LineAlmType": ds3LineAlmType,
       "ds3LineType": ds3LineType,
       "ds3LineCode": ds3LineCode,
       "ds3ClkSource": ds3ClkSource,
       "ds3LineLclLpbk": ds3LineLclLpbk,
       "ds3LineLclRmtLpbk": ds3LineLclRmtLpbk,
       "sonetIfTable": sonetIfTable,
       "sonetIfEntry": sonetIfEntry,
       "sonetIfStatus": sonetIfStatus,
       "sonetIfAlmType": sonetIfAlmType,
       "sonetIfType": sonetIfType,
       "sonetIfFrame": sonetIfFrame,
       "sonetIfHiSpeed": sonetIfHiSpeed,
       "sonetIfClkSource": sonetIfClkSource,
       "sonetIfLclLpbk": sonetIfLclLpbk,
       "sonetIfLclRmtLpbk": sonetIfLclRmtLpbk,
       "ds1LineStatsTable": ds1LineStatsTable,
       "ds1LineStatsEntry": ds1LineStatsEntry,
       "ds1StatsBpvs": ds1StatsBpvs,
       "ds1StatsFs": ds1StatsFs,
       "ds1StatsOofs": ds1StatsOofs,
       "ds1StatsLoss": ds1StatsLoss,
       "ds1StatsFers": ds1StatsFers,
       "ds1StatsCrcs": ds1StatsCrcs,
       "ds1StatsOoms": ds1StatsOoms,
       "ds1StatsAis16s": ds1StatsAis16s,
       "ds3LineStatsTable": ds3LineStatsTable,
       "ds3LineStatsEntry": ds3LineStatsEntry,
       "ds3StatsOofs": ds3StatsOofs,
       "ds3StatsLoss": ds3StatsLoss,
       "ds3StatsLcvs": ds3StatsLcvs,
       "ds3StatsCPcvs": ds3StatsCPcvs,
       "ds3StatsPPcvs": ds3StatsPPcvs,
       "ds3StatsPlcpBcvs": ds3StatsPlcpBcvs,
       "ds3StatsAtmCrcs": ds3StatsAtmCrcs,
       "ds3StatsPktCrcs": ds3StatsPktCrcs,
       "ds3StatsPlcpOofs": ds3StatsPlcpOofs,
       "sonetStatsTable": sonetStatsTable,
       "sonetStatsEntry": sonetStatsEntry,
       "sonetStatsOofs": sonetStatsOofs,
       "sonetStatsLoss": sonetStatsLoss,
       "sonetStatsAtmCrcs": sonetStatsAtmCrcs,
       "serialPortTable": serialPortTable,
       "serialPortEntry": serialPortEntry,
       "serialPortIfType": serialPortIfType,
       "serialPortStatus": serialPortStatus,
       "serialPortDceDte": serialPortDceDte,
       "serialPortClk": serialPortClk,
       "serialPortUtil": serialPortUtil,
       "serialPortEndptPtr": serialPortEndptPtr,
       "serialPortConnPtr": serialPortConnPtr,
       "serialPortEiaUpdt": serialPortEiaUpdt,
       "serialPortDfmEnable": serialPortDfmEnable,
       "serialPortDfmLen": serialPortDfmLen,
       "strmErrors": strmErrors}
)
