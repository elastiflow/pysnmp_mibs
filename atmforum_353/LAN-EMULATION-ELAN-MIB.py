# SNMP MIB module (LAN-EMULATION-ELAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/LAN-EMULATION-ELAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:06:53 2025
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

(AtmLaneAddress,
 LecDataFrameFormat,
 LecDataFrameSize,
 VciInteger,
 VpiInteger,
 atmfLanEmulation) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress",
    "LecDataFrameFormat",
    "LecDataFrameSize",
    "VciInteger",
    "VpiInteger",
    "atmfLanEmulation")

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

(AutonomousType,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

elanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ElanLocalIndex(TextualConvention, Integer32):
    status = "current"


class AtmLaneMask(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20



class TlvSelectorIndexType(TextualConvention, Integer32):
    status = "current"


class PolicySelectorIndexType(TextualConvention, Integer32):
    status = "current"


class LecsErrLogIndexType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_ElanAdminGroup_ObjectIdentity = ObjectIdentity
elanAdminGroup = _ElanAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1)
)
_ElanAdminPolicyVal_ObjectIdentity = ObjectIdentity
elanAdminPolicyVal = _ElanAdminPolicyVal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1)
)
_ByAtmAddr_ObjectIdentity = ObjectIdentity
byAtmAddr = _ByAtmAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 1)
)
_ByMacAddr_ObjectIdentity = ObjectIdentity
byMacAddr = _ByMacAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 2)
)
_ByRouteDescriptor_ObjectIdentity = ObjectIdentity
byRouteDescriptor = _ByRouteDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 3)
)
_ByLanType_ObjectIdentity = ObjectIdentity
byLanType = _ByLanType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 4)
)
_ByPktSize_ObjectIdentity = ObjectIdentity
byPktSize = _ByPktSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 5)
)
_ByElanName_ObjectIdentity = ObjectIdentity
byElanName = _ByElanName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 6)
)
_ElanConfGroup_ObjectIdentity = ObjectIdentity
elanConfGroup = _ElanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2)
)
_ElanConfNextId_Type = ElanLocalIndex
_ElanConfNextId_Object = MibScalar
elanConfNextId = _ElanConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 1),
    _ElanConfNextId_Type()
)
elanConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elanConfNextId.setStatus("current")
_ElanConfTable_Object = MibTable
elanConfTable = _ElanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    elanConfTable.setStatus("current")
_ElanConfEntry_Object = MibTableRow
elanConfEntry = _ElanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1)
)
elanConfEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
)
if mibBuilder.loadTexts:
    elanConfEntry.setStatus("current")
_ElanConfIndex_Type = ElanLocalIndex
_ElanConfIndex_Object = MibTableColumn
elanConfIndex = _ElanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 1),
    _ElanConfIndex_Type()
)
elanConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanConfIndex.setStatus("current")


class _ElanConfName_Type(DisplayString):
    """Custom type elanConfName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ElanConfName_Type.__name__ = "DisplayString"
_ElanConfName_Object = MibTableColumn
elanConfName = _ElanConfName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 2),
    _ElanConfName_Type()
)
elanConfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanConfName.setStatus("current")
_ElanConfTlvIndex_Type = TlvSelectorIndexType
_ElanConfTlvIndex_Object = MibTableColumn
elanConfTlvIndex = _ElanConfTlvIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 3),
    _ElanConfTlvIndex_Type()
)
elanConfTlvIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanConfTlvIndex.setStatus("current")


class _ElanConfLanType_Type(LecDataFrameFormat):
    """Custom type elanConfLanType based on LecDataFrameFormat"""
    defaultValue = 1


_ElanConfLanType_Type.__name__ = "LecDataFrameFormat"
_ElanConfLanType_Object = MibTableColumn
elanConfLanType = _ElanConfLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 4),
    _ElanConfLanType_Type()
)
elanConfLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanConfLanType.setStatus("current")


class _ElanConfMaxFrameSize_Type(LecDataFrameSize):
    """Custom type elanConfMaxFrameSize based on LecDataFrameSize"""
    defaultValue = 1


_ElanConfMaxFrameSize_Type.__name__ = "LecDataFrameSize"
_ElanConfMaxFrameSize_Object = MibTableColumn
elanConfMaxFrameSize = _ElanConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 5),
    _ElanConfMaxFrameSize_Type()
)
elanConfMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanConfMaxFrameSize.setStatus("current")
_ElanConfRowStatus_Type = RowStatus
_ElanConfRowStatus_Object = MibTableColumn
elanConfRowStatus = _ElanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 6),
    _ElanConfRowStatus_Type()
)
elanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanConfRowStatus.setStatus("current")
_ElanLesTable_Object = MibTable
elanLesTable = _ElanLesTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    elanLesTable.setStatus("current")
_ElanLesEntry_Object = MibTableRow
elanLesEntry = _ElanLesEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1)
)
elanLesEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"),
)
if mibBuilder.loadTexts:
    elanLesEntry.setStatus("current")
_ElanLesIndex_Type = Integer32
_ElanLesIndex_Object = MibTableColumn
elanLesIndex = _ElanLesIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1, 1),
    _ElanLesIndex_Type()
)
elanLesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLesIndex.setStatus("current")


class _ElanLesAtmAddress_Type(AtmLaneAddress):
    """Custom type elanLesAtmAddress based on AtmLaneAddress"""
    defaultValue = OctetString("")


_ElanLesAtmAddress_Type.__name__ = "AtmLaneAddress"
_ElanLesAtmAddress_Object = MibTableColumn
elanLesAtmAddress = _ElanLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1, 2),
    _ElanLesAtmAddress_Type()
)
elanLesAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLesAtmAddress.setStatus("current")
_ElanLesRowStatus_Type = RowStatus
_ElanLesRowStatus_Object = MibTableColumn
elanLesRowStatus = _ElanLesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1, 3),
    _ElanLesRowStatus_Type()
)
elanLesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLesRowStatus.setStatus("current")
_ElanPolicyTable_Object = MibTable
elanPolicyTable = _ElanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    elanPolicyTable.setStatus("current")
_ElanPolicyEntry_Object = MibTableRow
elanPolicyEntry = _ElanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1)
)
elanPolicyEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanPolicySelectorIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanPolicyIndex"),
)
if mibBuilder.loadTexts:
    elanPolicyEntry.setStatus("current")
_ElanPolicySelectorIndex_Type = PolicySelectorIndexType
_ElanPolicySelectorIndex_Object = MibTableColumn
elanPolicySelectorIndex = _ElanPolicySelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 1),
    _ElanPolicySelectorIndex_Type()
)
elanPolicySelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanPolicySelectorIndex.setStatus("current")


class _ElanPolicyIndex_Type(Integer32):
    """Custom type elanPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_ElanPolicyIndex_Type.__name__ = "Integer32"
_ElanPolicyIndex_Object = MibTableColumn
elanPolicyIndex = _ElanPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 2),
    _ElanPolicyIndex_Type()
)
elanPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanPolicyIndex.setStatus("current")


class _ElanPolicyPriority_Type(Integer32):
    """Custom type elanPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_ElanPolicyPriority_Type.__name__ = "Integer32"
_ElanPolicyPriority_Object = MibTableColumn
elanPolicyPriority = _ElanPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 3),
    _ElanPolicyPriority_Type()
)
elanPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanPolicyPriority.setStatus("current")
_ElanPolicyType_Type = AutonomousType
_ElanPolicyType_Object = MibTableColumn
elanPolicyType = _ElanPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 4),
    _ElanPolicyType_Type()
)
elanPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanPolicyType.setStatus("current")
_ElanPolicyRowStatus_Type = RowStatus
_ElanPolicyRowStatus_Object = MibTableColumn
elanPolicyRowStatus = _ElanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 5),
    _ElanPolicyRowStatus_Type()
)
elanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanPolicyRowStatus.setStatus("current")
_ElanLecAtmAddrTable_Object = MibTable
elanLecAtmAddrTable = _ElanLecAtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    elanLecAtmAddrTable.setStatus("current")
_ElanLecAtmAddrEntry_Object = MibTableRow
elanLecAtmAddrEntry = _ElanLecAtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1)
)
elanLecAtmAddrEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecAtmAddress"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecAtmMask"),
)
if mibBuilder.loadTexts:
    elanLecAtmAddrEntry.setStatus("current")
_ElanLecAtmAddress_Type = AtmLaneAddress
_ElanLecAtmAddress_Object = MibTableColumn
elanLecAtmAddress = _ElanLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1, 1),
    _ElanLecAtmAddress_Type()
)
elanLecAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecAtmAddress.setStatus("current")
_ElanLecAtmMask_Type = AtmLaneAddress
_ElanLecAtmMask_Object = MibTableColumn
elanLecAtmMask = _ElanLecAtmMask_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1, 2),
    _ElanLecAtmMask_Type()
)
elanLecAtmMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecAtmMask.setStatus("current")
_ElanLecAtmRowStatus_Type = RowStatus
_ElanLecAtmRowStatus_Object = MibTableColumn
elanLecAtmRowStatus = _ElanLecAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1, 4),
    _ElanLecAtmRowStatus_Type()
)
elanLecAtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLecAtmRowStatus.setStatus("current")
_ElanLecMacAddrTable_Object = MibTable
elanLecMacAddrTable = _ElanLecMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    elanLecMacAddrTable.setStatus("current")
_ElanLecMacAddrEntry_Object = MibTableRow
elanLecMacAddrEntry = _ElanLecMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6, 1)
)
elanLecMacAddrEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecMacAddress"),
)
if mibBuilder.loadTexts:
    elanLecMacAddrEntry.setStatus("current")
_ElanLecMacAddress_Type = MacAddress
_ElanLecMacAddress_Object = MibTableColumn
elanLecMacAddress = _ElanLecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6, 1, 1),
    _ElanLecMacAddress_Type()
)
elanLecMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecMacAddress.setStatus("current")
_ElanLecMacRowStatus_Type = RowStatus
_ElanLecMacRowStatus_Object = MibTableColumn
elanLecMacRowStatus = _ElanLecMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6, 1, 2),
    _ElanLecMacRowStatus_Type()
)
elanLecMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLecMacRowStatus.setStatus("current")
_ElanLecRdTable_Object = MibTable
elanLecRdTable = _ElanLecRdTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7)
)
if mibBuilder.loadTexts:
    elanLecRdTable.setStatus("current")
_ElanLecRdEntry_Object = MibTableRow
elanLecRdEntry = _ElanLecRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1)
)
elanLecRdEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecRdSegId"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecRdBridgeNum"),
)
if mibBuilder.loadTexts:
    elanLecRdEntry.setStatus("current")


class _ElanLecRdSegId_Type(Integer32):
    """Custom type elanLecRdSegId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ElanLecRdSegId_Type.__name__ = "Integer32"
_ElanLecRdSegId_Object = MibTableColumn
elanLecRdSegId = _ElanLecRdSegId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1, 1),
    _ElanLecRdSegId_Type()
)
elanLecRdSegId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecRdSegId.setStatus("current")


class _ElanLecRdBridgeNum_Type(Integer32):
    """Custom type elanLecRdBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ElanLecRdBridgeNum_Type.__name__ = "Integer32"
_ElanLecRdBridgeNum_Object = MibTableColumn
elanLecRdBridgeNum = _ElanLecRdBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1, 2),
    _ElanLecRdBridgeNum_Type()
)
elanLecRdBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecRdBridgeNum.setStatus("current")
_ElanLecRdRowStatus_Type = RowStatus
_ElanLecRdRowStatus_Object = MibTableColumn
elanLecRdRowStatus = _ElanLecRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1, 4),
    _ElanLecRdRowStatus_Type()
)
elanLecRdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLecRdRowStatus.setStatus("current")
_ElanLecPktSizeTable_Object = MibTable
elanLecPktSizeTable = _ElanLecPktSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8)
)
if mibBuilder.loadTexts:
    elanLecPktSizeTable.setStatus("current")
_ElanLecPktSizeEntry_Object = MibTableRow
elanLecPktSizeEntry = _ElanLecPktSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8, 1)
)
elanLecPktSizeEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecFrameSize"),
)
if mibBuilder.loadTexts:
    elanLecPktSizeEntry.setStatus("current")
_ElanLecFrameSize_Type = LecDataFrameSize
_ElanLecFrameSize_Object = MibTableColumn
elanLecFrameSize = _ElanLecFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8, 1, 1),
    _ElanLecFrameSize_Type()
)
elanLecFrameSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecFrameSize.setStatus("current")
_ElanLecPktSizeRowStatus_Type = RowStatus
_ElanLecPktSizeRowStatus_Object = MibTableColumn
elanLecPktSizeRowStatus = _ElanLecPktSizeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8, 1, 2),
    _ElanLecPktSizeRowStatus_Type()
)
elanLecPktSizeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLecPktSizeRowStatus.setStatus("current")
_ElanLecNameTable_Object = MibTable
elanLecNameTable = _ElanLecNameTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9)
)
if mibBuilder.loadTexts:
    elanLecNameTable.setStatus("current")
_ElanLecNameEntry_Object = MibTableRow
elanLecNameEntry = _ElanLecNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9, 1)
)
elanLecNameEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "elanLecElanName"),
)
if mibBuilder.loadTexts:
    elanLecNameEntry.setStatus("current")


class _ElanLecElanName_Type(DisplayString):
    """Custom type elanLecElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ElanLecElanName_Type.__name__ = "DisplayString"
_ElanLecElanName_Object = MibTableColumn
elanLecElanName = _ElanLecElanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9, 1, 1),
    _ElanLecElanName_Type()
)
elanLecElanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elanLecElanName.setStatus("current")
_ElanLecNameRowStatus_Type = RowStatus
_ElanLecNameRowStatus_Object = MibTableColumn
elanLecNameRowStatus = _ElanLecNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9, 1, 2),
    _ElanLecNameRowStatus_Type()
)
elanLecNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elanLecNameRowStatus.setStatus("current")
_ElanLecsGroup_ObjectIdentity = ObjectIdentity
elanLecsGroup = _ElanLecsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3)
)
_ElanLecsConfGroup_ObjectIdentity = ObjectIdentity
elanLecsConfGroup = _ElanLecsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1)
)
_LecsConfNextId_Type = ElanLocalIndex
_LecsConfNextId_Object = MibScalar
lecsConfNextId = _LecsConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 1),
    _LecsConfNextId_Type()
)
lecsConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfNextId.setStatus("current")
_LecsConfTable_Object = MibTable
lecsConfTable = _LecsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lecsConfTable.setStatus("current")
_LecsConfEntry_Object = MibTableRow
lecsConfEntry = _LecsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1)
)
lecsConfEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    lecsConfEntry.setStatus("current")
_LecsConfIndex_Type = Integer32
_LecsConfIndex_Object = MibTableColumn
lecsConfIndex = _LecsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 1),
    _LecsConfIndex_Type()
)
lecsConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfIndex.setStatus("current")


class _LecsAtmIfIndex_Type(IfIndexOrZero):
    """Custom type lecsAtmIfIndex based on IfIndexOrZero"""
    defaultValue = 0


_LecsAtmIfIndex_Type.__name__ = "IfIndexOrZero"
_LecsAtmIfIndex_Object = MibTableColumn
lecsAtmIfIndex = _LecsAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 2),
    _LecsAtmIfIndex_Type()
)
lecsAtmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmIfIndex.setStatus("current")


class _LecsAtmAddrSpec_Type(AtmLaneAddress):
    """Custom type lecsAtmAddrSpec based on AtmLaneAddress"""
    defaultHexValue = "4700790000000000000000000000A03E00000100"


_LecsAtmAddrSpec_Type.__name__ = "AtmLaneAddress"
_LecsAtmAddrSpec_Object = MibTableColumn
lecsAtmAddrSpec = _LecsAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 3),
    _LecsAtmAddrSpec_Type()
)
lecsAtmAddrSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrSpec.setStatus("current")


class _LecsAtmAddrMask_Type(AtmLaneMask):
    """Custom type lecsAtmAddrMask based on AtmLaneMask"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"


_LecsAtmAddrMask_Type.__name__ = "AtmLaneMask"
_LecsAtmAddrMask_Object = MibTableColumn
lecsAtmAddrMask = _LecsAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 4),
    _LecsAtmAddrMask_Type()
)
lecsAtmAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrMask.setStatus("current")
_LecsAtmAddrActual_Type = AtmLaneAddress
_LecsAtmAddrActual_Object = MibTableColumn
lecsAtmAddrActual = _LecsAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 5),
    _LecsAtmAddrActual_Type()
)
lecsAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrActual.setStatus("current")
_LecsPolicySelIndex_Type = PolicySelectorIndexType
_LecsPolicySelIndex_Object = MibTableColumn
lecsPolicySelIndex = _LecsPolicySelIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 6),
    _LecsPolicySelIndex_Type()
)
lecsPolicySelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsPolicySelIndex.setStatus("current")
_LecsLastInitialized_Type = TimeStamp
_LecsLastInitialized_Object = MibTableColumn
lecsLastInitialized = _LecsLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 7),
    _LecsLastInitialized_Type()
)
lecsLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLastInitialized.setStatus("current")


class _LecsOperStatus_Type(Integer32):
    """Custom type lecsOperStatus based on Integer32"""
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
          ("up", 2),
          ("down", 3))
    )


_LecsOperStatus_Type.__name__ = "Integer32"
_LecsOperStatus_Object = MibTableColumn
lecsOperStatus = _LecsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 8),
    _LecsOperStatus_Type()
)
lecsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsOperStatus.setStatus("current")


class _LecsAdminStatus_Type(Integer32):
    """Custom type lecsAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_LecsAdminStatus_Type.__name__ = "Integer32"
_LecsAdminStatus_Object = MibTableColumn
lecsAdminStatus = _LecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 9),
    _LecsAdminStatus_Type()
)
lecsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAdminStatus.setStatus("current")
_LecsRowStatus_Type = RowStatus
_LecsRowStatus_Object = MibTableColumn
lecsRowStatus = _LecsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 10),
    _LecsRowStatus_Type()
)
lecsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsRowStatus.setStatus("current")
_LecsElanTable_Object = MibTable
lecsElanTable = _LecsElanTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lecsElanTable.setStatus("current")
_LecsElanEntry_Object = MibTableRow
lecsElanEntry = _LecsElanEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 3, 1)
)
lecsElanEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    lecsElanEntry.setStatus("current")
_LecsElanRowStatus_Type = RowStatus
_LecsElanRowStatus_Object = MibTableColumn
lecsElanRowStatus = _LecsElanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 3, 1, 1),
    _LecsElanRowStatus_Type()
)
lecsElanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsElanRowStatus.setStatus("current")
_LecsTlvTable_Object = MibTable
lecsTlvTable = _LecsTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    lecsTlvTable.setStatus("current")
_LecsTlvEntry_Object = MibTableRow
lecsTlvEntry = _LecsTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1)
)
lecsTlvEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsTlvSelectorIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsTlvTag"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsTlvIndex"),
)
if mibBuilder.loadTexts:
    lecsTlvEntry.setStatus("current")
_LecsTlvSelectorIndex_Type = TlvSelectorIndexType
_LecsTlvSelectorIndex_Object = MibTableColumn
lecsTlvSelectorIndex = _LecsTlvSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 1),
    _LecsTlvSelectorIndex_Type()
)
lecsTlvSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsTlvSelectorIndex.setStatus("current")


class _LecsTlvTag_Type(OctetString):
    """Custom type lecsTlvTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_LecsTlvTag_Type.__name__ = "OctetString"
_LecsTlvTag_Object = MibTableColumn
lecsTlvTag = _LecsTlvTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 2),
    _LecsTlvTag_Type()
)
lecsTlvTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsTlvTag.setStatus("current")


class _LecsTlvIndex_Type(Integer32):
    """Custom type lecsTlvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LecsTlvIndex_Type.__name__ = "Integer32"
_LecsTlvIndex_Object = MibTableColumn
lecsTlvIndex = _LecsTlvIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 3),
    _LecsTlvIndex_Type()
)
lecsTlvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsTlvIndex.setStatus("current")


class _LecsTlvVal_Type(OctetString):
    """Custom type lecsTlvVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_LecsTlvVal_Type.__name__ = "OctetString"
_LecsTlvVal_Object = MibTableColumn
lecsTlvVal = _LecsTlvVal_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 4),
    _LecsTlvVal_Type()
)
lecsTlvVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsTlvVal.setStatus("current")
_LecsTlvRowStatus_Type = RowStatus
_LecsTlvRowStatus_Object = MibTableColumn
lecsTlvRowStatus = _LecsTlvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 5),
    _LecsTlvRowStatus_Type()
)
lecsTlvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsTlvRowStatus.setStatus("current")
_LecsVccTable_Object = MibTable
lecsVccTable = _LecsVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    lecsVccTable.setStatus("current")
_LecsVccEntry_Object = MibTableRow
lecsVccEntry = _LecsVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1)
)
lecsVccEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsVccIfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsVccVpi"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsVccVci"),
)
if mibBuilder.loadTexts:
    lecsVccEntry.setStatus("current")
_LecsVccIfIndex_Type = IfIndexOrZero
_LecsVccIfIndex_Object = MibTableColumn
lecsVccIfIndex = _LecsVccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 1),
    _LecsVccIfIndex_Type()
)
lecsVccIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsVccIfIndex.setStatus("current")
_LecsVccVpi_Type = VpiInteger
_LecsVccVpi_Object = MibTableColumn
lecsVccVpi = _LecsVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 2),
    _LecsVccVpi_Type()
)
lecsVccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsVccVpi.setStatus("current")
_LecsVccVci_Type = VciInteger
_LecsVccVci_Object = MibTableColumn
lecsVccVci = _LecsVccVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 3),
    _LecsVccVci_Type()
)
lecsVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsVccVci.setStatus("current")
_LecsVccRowStatus_Type = RowStatus
_LecsVccRowStatus_Object = MibTableColumn
lecsVccRowStatus = _LecsVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 4),
    _LecsVccRowStatus_Type()
)
lecsVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsVccRowStatus.setStatus("current")
_ElanLecsFaultGroup_ObjectIdentity = ObjectIdentity
elanLecsFaultGroup = _ElanLecsFaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2)
)
_LecsErrCtlTable_Object = MibTable
lecsErrCtlTable = _LecsErrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lecsErrCtlTable.setStatus("current")
_LecsErrCtlEntry_Object = MibTableRow
lecsErrCtlEntry = _LecsErrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lecsErrCtlEntry.setStatus("current")


class _LecsErrCtlAdminStatus_Type(Integer32):
    """Custom type lecsErrCtlAdminStatus based on Integer32"""
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


_LecsErrCtlAdminStatus_Type.__name__ = "Integer32"
_LecsErrCtlAdminStatus_Object = MibTableColumn
lecsErrCtlAdminStatus = _LecsErrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 1),
    _LecsErrCtlAdminStatus_Type()
)
lecsErrCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsErrCtlAdminStatus.setStatus("current")


class _LecsErrCtlOperStatus_Type(Integer32):
    """Custom type lecsErrCtlOperStatus based on Integer32"""
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
          ("active", 2),
          ("outOfRes", 3),
          ("failed", 4),
          ("disabled", 5))
    )


_LecsErrCtlOperStatus_Type.__name__ = "Integer32"
_LecsErrCtlOperStatus_Object = MibTableColumn
lecsErrCtlOperStatus = _LecsErrCtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 2),
    _LecsErrCtlOperStatus_Type()
)
lecsErrCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsErrCtlOperStatus.setStatus("current")


class _LecsErrCtlClearLog_Type(Integer32):
    """Custom type lecsErrCtlClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("clear", 2))
    )


_LecsErrCtlClearLog_Type.__name__ = "Integer32"
_LecsErrCtlClearLog_Object = MibTableColumn
lecsErrCtlClearLog = _LecsErrCtlClearLog_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 3),
    _LecsErrCtlClearLog_Type()
)
lecsErrCtlClearLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsErrCtlClearLog.setStatus("current")


class _LecsErrCtlMaxEntries_Type(Integer32):
    """Custom type lecsErrCtlMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LecsErrCtlMaxEntries_Type.__name__ = "Integer32"
_LecsErrCtlMaxEntries_Object = MibTableColumn
lecsErrCtlMaxEntries = _LecsErrCtlMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 4),
    _LecsErrCtlMaxEntries_Type()
)
lecsErrCtlMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsErrCtlMaxEntries.setStatus("current")
_LecsErrCtlLastEntry_Type = LecsErrLogIndexType
_LecsErrCtlLastEntry_Object = MibTableColumn
lecsErrCtlLastEntry = _LecsErrCtlLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 5),
    _LecsErrCtlLastEntry_Type()
)
lecsErrCtlLastEntry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsErrCtlLastEntry.setStatus("current")
_LecsErrLogTable_Object = MibTable
lecsErrLogTable = _LecsErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    lecsErrLogTable.setStatus("current")
_LecsErrLogEntry_Object = MibTableRow
lecsErrLogEntry = _LecsErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1)
)
lecsErrLogEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
    (0, "LAN-EMULATION-ELAN-MIB", "lecsErrLogIndex"),
)
if mibBuilder.loadTexts:
    lecsErrLogEntry.setStatus("current")
_LecsErrLogIndex_Type = LecsErrLogIndexType
_LecsErrLogIndex_Object = MibTableColumn
lecsErrLogIndex = _LecsErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 1),
    _LecsErrLogIndex_Type()
)
lecsErrLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsErrLogIndex.setStatus("current")
_LecsErrLogAtmAddr_Type = AtmLaneAddress
_LecsErrLogAtmAddr_Object = MibTableColumn
lecsErrLogAtmAddr = _LecsErrLogAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 2),
    _LecsErrLogAtmAddr_Type()
)
lecsErrLogAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsErrLogAtmAddr.setStatus("current")


class _LecsErrLogErrCode_Type(Integer32):
    """Custom type lecsErrLogErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_LecsErrLogErrCode_Type.__name__ = "Integer32"
_LecsErrLogErrCode_Object = MibTableColumn
lecsErrLogErrCode = _LecsErrLogErrCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 3),
    _LecsErrLogErrCode_Type()
)
lecsErrLogErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsErrLogErrCode.setStatus("current")
_LecsErrLogTime_Type = TimeStamp
_LecsErrLogTime_Object = MibTableColumn
lecsErrLogTime = _LecsErrLogTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 4),
    _LecsErrLogTime_Type()
)
lecsErrLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsErrLogTime.setStatus("current")
_ElanLecsStatGroup_ObjectIdentity = ObjectIdentity
elanLecsStatGroup = _ElanLecsStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3)
)
_LecsStatsTable_Object = MibTable
lecsStatsTable = _LecsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lecsStatsTable.setStatus("current")
_LecsStatsEntry_Object = MibTableRow
lecsStatsEntry = _LecsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lecsStatsEntry.setStatus("current")
_LecsStatSuccessful_Type = Counter32
_LecsStatSuccessful_Object = MibTableColumn
lecsStatSuccessful = _LecsStatSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 1),
    _LecsStatSuccessful_Type()
)
lecsStatSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatSuccessful.setStatus("current")
_LecsStatInBadFrames_Type = Counter32
_LecsStatInBadFrames_Object = MibTableColumn
lecsStatInBadFrames = _LecsStatInBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 2),
    _LecsStatInBadFrames_Type()
)
lecsStatInBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInBadFrames.setStatus("current")
_LecsStatInvalidParam_Type = Counter32
_LecsStatInvalidParam_Object = MibTableColumn
lecsStatInvalidParam = _LecsStatInvalidParam_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 3),
    _LecsStatInvalidParam_Type()
)
lecsStatInvalidParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInvalidParam.setStatus("current")
_LecsStatInsufRes_Type = Counter32
_LecsStatInsufRes_Object = MibTableColumn
lecsStatInsufRes = _LecsStatInsufRes_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 4),
    _LecsStatInsufRes_Type()
)
lecsStatInsufRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInsufRes.setStatus("current")
_LecsStatAccDenied_Type = Counter32
_LecsStatAccDenied_Object = MibTableColumn
lecsStatAccDenied = _LecsStatAccDenied_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 5),
    _LecsStatAccDenied_Type()
)
lecsStatAccDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatAccDenied.setStatus("current")
_LecsStatInvalidReq_Type = Counter32
_LecsStatInvalidReq_Object = MibTableColumn
lecsStatInvalidReq = _LecsStatInvalidReq_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 6),
    _LecsStatInvalidReq_Type()
)
lecsStatInvalidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInvalidReq.setStatus("current")
_LecsStatInvalidDest_Type = Counter32
_LecsStatInvalidDest_Object = MibTableColumn
lecsStatInvalidDest = _LecsStatInvalidDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 7),
    _LecsStatInvalidDest_Type()
)
lecsStatInvalidDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInvalidDest.setStatus("current")
_LecsStatInvalidAddr_Type = Counter32
_LecsStatInvalidAddr_Object = MibTableColumn
lecsStatInvalidAddr = _LecsStatInvalidAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 8),
    _LecsStatInvalidAddr_Type()
)
lecsStatInvalidAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInvalidAddr.setStatus("current")
_LecsStatNoConf_Type = Counter32
_LecsStatNoConf_Object = MibTableColumn
lecsStatNoConf = _LecsStatNoConf_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 9),
    _LecsStatNoConf_Type()
)
lecsStatNoConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatNoConf.setStatus("current")
_LecsStatConfError_Type = Counter32
_LecsStatConfError_Object = MibTableColumn
lecsStatConfError = _LecsStatConfError_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 10),
    _LecsStatConfError_Type()
)
lecsStatConfError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatConfError.setStatus("current")
_LecsStatInsufInfo_Type = Counter32
_LecsStatInsufInfo_Object = MibTableColumn
lecsStatInsufInfo = _LecsStatInsufInfo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 11),
    _LecsStatInsufInfo_Type()
)
lecsStatInsufInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsStatInsufInfo.setStatus("current")
_ElanMIBConformance_ObjectIdentity = ObjectIdentity
elanMIBConformance = _ElanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4)
)
_ElanMIBGroups_ObjectIdentity = ObjectIdentity
elanMIBGroups = _ElanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1)
)
_ElanMIBCompliances_ObjectIdentity = ObjectIdentity
elanMIBCompliances = _ElanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 2)
)
lecsConfEntry.registerAugmentions(
    ("LAN-EMULATION-ELAN-MIB",
     "lecsErrCtlEntry")
)
lecsErrCtlEntry.setIndexNames(*lecsConfEntry.getIndexNames())
lecsConfEntry.registerAugmentions(
    ("LAN-EMULATION-ELAN-MIB",
     "lecsStatsEntry")
)
lecsStatsEntry.setIndexNames(*lecsConfEntry.getIndexNames())

# Managed Objects groups

elanCConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 1)
)
elanCConfGroup.setObjects(
      *(("LAN-EMULATION-ELAN-MIB", "elanConfNextId"),
        ("LAN-EMULATION-ELAN-MIB", "elanConfName"),
        ("LAN-EMULATION-ELAN-MIB", "elanConfTlvIndex"),
        ("LAN-EMULATION-ELAN-MIB", "elanConfLanType"),
        ("LAN-EMULATION-ELAN-MIB", "elanConfMaxFrameSize"),
        ("LAN-EMULATION-ELAN-MIB", "elanConfRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "elanLecPktSizeRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "elanLecNameRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "elanLesAtmAddress"),
        ("LAN-EMULATION-ELAN-MIB", "elanLesRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "elanPolicyPriority"),
        ("LAN-EMULATION-ELAN-MIB", "elanPolicyType"),
        ("LAN-EMULATION-ELAN-MIB", "elanPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    elanCConfGroup.setStatus("current")

elanLecAssignByAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 2)
)
elanLecAssignByAtmGroup.setObjects(
    ("LAN-EMULATION-ELAN-MIB", "elanLecAtmRowStatus")
)
if mibBuilder.loadTexts:
    elanLecAssignByAtmGroup.setStatus("current")

elanLecAssignByMacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 3)
)
elanLecAssignByMacGroup.setObjects(
    ("LAN-EMULATION-ELAN-MIB", "elanLecMacRowStatus")
)
if mibBuilder.loadTexts:
    elanLecAssignByMacGroup.setStatus("current")

elanLecAssignByRdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 4)
)
elanLecAssignByRdGroup.setObjects(
    ("LAN-EMULATION-ELAN-MIB", "elanLecRdRowStatus")
)
if mibBuilder.loadTexts:
    elanLecAssignByRdGroup.setStatus("current")

lecsCStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 5)
)
lecsCStatGroup.setObjects(
      *(("LAN-EMULATION-ELAN-MIB", "lecsStatSuccessful"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInBadFrames"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInvalidParam"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInsufRes"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatAccDenied"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInvalidReq"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInvalidDest"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInvalidAddr"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatNoConf"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatConfError"),
        ("LAN-EMULATION-ELAN-MIB", "lecsStatInsufInfo"))
)
if mibBuilder.loadTexts:
    lecsCStatGroup.setStatus("current")

lecsCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 6)
)
lecsCGroup.setObjects(
      *(("LAN-EMULATION-ELAN-MIB", "lecsConfNextId"),
        ("LAN-EMULATION-ELAN-MIB", "lecsAtmIfIndex"),
        ("LAN-EMULATION-ELAN-MIB", "lecsAtmAddrSpec"),
        ("LAN-EMULATION-ELAN-MIB", "lecsAtmAddrMask"),
        ("LAN-EMULATION-ELAN-MIB", "lecsAtmAddrActual"),
        ("LAN-EMULATION-ELAN-MIB", "lecsElanRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsPolicySelIndex"),
        ("LAN-EMULATION-ELAN-MIB", "lecsTlvVal"),
        ("LAN-EMULATION-ELAN-MIB", "lecsTlvRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsVccRowStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsLastInitialized"),
        ("LAN-EMULATION-ELAN-MIB", "lecsOperStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsAdminStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsRowStatus"))
)
if mibBuilder.loadTexts:
    lecsCGroup.setStatus("current")

lecsCFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 1, 7)
)
lecsCFaultGroup.setObjects(
      *(("LAN-EMULATION-ELAN-MIB", "lecsErrCtlAdminStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrCtlOperStatus"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrCtlClearLog"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrCtlMaxEntries"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrCtlLastEntry"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrLogTime"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrLogAtmAddr"),
        ("LAN-EMULATION-ELAN-MIB", "lecsErrLogErrCode"))
)
if mibBuilder.loadTexts:
    lecsCFaultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

elanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 4, 2, 1)
)
elanMIBCompliance.setObjects(
      *(("LAN-EMULATION-ELAN-MIB", "elanCConfGroup"),
        ("LAN-EMULATION-ELAN-MIB", "elanLecAssignByAtmGroup"),
        ("LAN-EMULATION-ELAN-MIB", "elanLecAssignByMacGroup"),
        ("LAN-EMULATION-ELAN-MIB", "elanLecAssignByRdGroup"),
        ("LAN-EMULATION-ELAN-MIB", "lecsCStatGroup"),
        ("LAN-EMULATION-ELAN-MIB", "lecsCGroup"),
        ("LAN-EMULATION-ELAN-MIB", "lecsCFaultGroup"))
)
if mibBuilder.loadTexts:
    elanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-EMULATION-ELAN-MIB",
    **{"IfIndexOrZero": IfIndexOrZero,
       "ElanLocalIndex": ElanLocalIndex,
       "AtmLaneMask": AtmLaneMask,
       "TlvSelectorIndexType": TlvSelectorIndexType,
       "PolicySelectorIndexType": PolicySelectorIndexType,
       "LecsErrLogIndexType": LecsErrLogIndexType,
       "elanMIB": elanMIB,
       "elanAdminGroup": elanAdminGroup,
       "elanAdminPolicyVal": elanAdminPolicyVal,
       "byAtmAddr": byAtmAddr,
       "byMacAddr": byMacAddr,
       "byRouteDescriptor": byRouteDescriptor,
       "byLanType": byLanType,
       "byPktSize": byPktSize,
       "byElanName": byElanName,
       "elanConfGroup": elanConfGroup,
       "elanConfNextId": elanConfNextId,
       "elanConfTable": elanConfTable,
       "elanConfEntry": elanConfEntry,
       "elanConfIndex": elanConfIndex,
       "elanConfName": elanConfName,
       "elanConfTlvIndex": elanConfTlvIndex,
       "elanConfLanType": elanConfLanType,
       "elanConfMaxFrameSize": elanConfMaxFrameSize,
       "elanConfRowStatus": elanConfRowStatus,
       "elanLesTable": elanLesTable,
       "elanLesEntry": elanLesEntry,
       "elanLesIndex": elanLesIndex,
       "elanLesAtmAddress": elanLesAtmAddress,
       "elanLesRowStatus": elanLesRowStatus,
       "elanPolicyTable": elanPolicyTable,
       "elanPolicyEntry": elanPolicyEntry,
       "elanPolicySelectorIndex": elanPolicySelectorIndex,
       "elanPolicyIndex": elanPolicyIndex,
       "elanPolicyPriority": elanPolicyPriority,
       "elanPolicyType": elanPolicyType,
       "elanPolicyRowStatus": elanPolicyRowStatus,
       "elanLecAtmAddrTable": elanLecAtmAddrTable,
       "elanLecAtmAddrEntry": elanLecAtmAddrEntry,
       "elanLecAtmAddress": elanLecAtmAddress,
       "elanLecAtmMask": elanLecAtmMask,
       "elanLecAtmRowStatus": elanLecAtmRowStatus,
       "elanLecMacAddrTable": elanLecMacAddrTable,
       "elanLecMacAddrEntry": elanLecMacAddrEntry,
       "elanLecMacAddress": elanLecMacAddress,
       "elanLecMacRowStatus": elanLecMacRowStatus,
       "elanLecRdTable": elanLecRdTable,
       "elanLecRdEntry": elanLecRdEntry,
       "elanLecRdSegId": elanLecRdSegId,
       "elanLecRdBridgeNum": elanLecRdBridgeNum,
       "elanLecRdRowStatus": elanLecRdRowStatus,
       "elanLecPktSizeTable": elanLecPktSizeTable,
       "elanLecPktSizeEntry": elanLecPktSizeEntry,
       "elanLecFrameSize": elanLecFrameSize,
       "elanLecPktSizeRowStatus": elanLecPktSizeRowStatus,
       "elanLecNameTable": elanLecNameTable,
       "elanLecNameEntry": elanLecNameEntry,
       "elanLecElanName": elanLecElanName,
       "elanLecNameRowStatus": elanLecNameRowStatus,
       "elanLecsGroup": elanLecsGroup,
       "elanLecsConfGroup": elanLecsConfGroup,
       "lecsConfNextId": lecsConfNextId,
       "lecsConfTable": lecsConfTable,
       "lecsConfEntry": lecsConfEntry,
       "lecsConfIndex": lecsConfIndex,
       "lecsAtmIfIndex": lecsAtmIfIndex,
       "lecsAtmAddrSpec": lecsAtmAddrSpec,
       "lecsAtmAddrMask": lecsAtmAddrMask,
       "lecsAtmAddrActual": lecsAtmAddrActual,
       "lecsPolicySelIndex": lecsPolicySelIndex,
       "lecsLastInitialized": lecsLastInitialized,
       "lecsOperStatus": lecsOperStatus,
       "lecsAdminStatus": lecsAdminStatus,
       "lecsRowStatus": lecsRowStatus,
       "lecsElanTable": lecsElanTable,
       "lecsElanEntry": lecsElanEntry,
       "lecsElanRowStatus": lecsElanRowStatus,
       "lecsTlvTable": lecsTlvTable,
       "lecsTlvEntry": lecsTlvEntry,
       "lecsTlvSelectorIndex": lecsTlvSelectorIndex,
       "lecsTlvTag": lecsTlvTag,
       "lecsTlvIndex": lecsTlvIndex,
       "lecsTlvVal": lecsTlvVal,
       "lecsTlvRowStatus": lecsTlvRowStatus,
       "lecsVccTable": lecsVccTable,
       "lecsVccEntry": lecsVccEntry,
       "lecsVccIfIndex": lecsVccIfIndex,
       "lecsVccVpi": lecsVccVpi,
       "lecsVccVci": lecsVccVci,
       "lecsVccRowStatus": lecsVccRowStatus,
       "elanLecsFaultGroup": elanLecsFaultGroup,
       "lecsErrCtlTable": lecsErrCtlTable,
       "lecsErrCtlEntry": lecsErrCtlEntry,
       "lecsErrCtlAdminStatus": lecsErrCtlAdminStatus,
       "lecsErrCtlOperStatus": lecsErrCtlOperStatus,
       "lecsErrCtlClearLog": lecsErrCtlClearLog,
       "lecsErrCtlMaxEntries": lecsErrCtlMaxEntries,
       "lecsErrCtlLastEntry": lecsErrCtlLastEntry,
       "lecsErrLogTable": lecsErrLogTable,
       "lecsErrLogEntry": lecsErrLogEntry,
       "lecsErrLogIndex": lecsErrLogIndex,
       "lecsErrLogAtmAddr": lecsErrLogAtmAddr,
       "lecsErrLogErrCode": lecsErrLogErrCode,
       "lecsErrLogTime": lecsErrLogTime,
       "elanLecsStatGroup": elanLecsStatGroup,
       "lecsStatsTable": lecsStatsTable,
       "lecsStatsEntry": lecsStatsEntry,
       "lecsStatSuccessful": lecsStatSuccessful,
       "lecsStatInBadFrames": lecsStatInBadFrames,
       "lecsStatInvalidParam": lecsStatInvalidParam,
       "lecsStatInsufRes": lecsStatInsufRes,
       "lecsStatAccDenied": lecsStatAccDenied,
       "lecsStatInvalidReq": lecsStatInvalidReq,
       "lecsStatInvalidDest": lecsStatInvalidDest,
       "lecsStatInvalidAddr": lecsStatInvalidAddr,
       "lecsStatNoConf": lecsStatNoConf,
       "lecsStatConfError": lecsStatConfError,
       "lecsStatInsufInfo": lecsStatInsufInfo,
       "elanMIBConformance": elanMIBConformance,
       "elanMIBGroups": elanMIBGroups,
       "elanCConfGroup": elanCConfGroup,
       "elanLecAssignByAtmGroup": elanLecAssignByAtmGroup,
       "elanLecAssignByMacGroup": elanLecAssignByMacGroup,
       "elanLecAssignByRdGroup": elanLecAssignByRdGroup,
       "lecsCStatGroup": lecsCStatGroup,
       "lecsCGroup": lecsCGroup,
       "lecsCFaultGroup": lecsCFaultGroup,
       "elanMIBCompliances": elanMIBCompliances,
       "elanMIBCompliance": elanMIBCompliance}
)
