# SNMP MIB module (LAN-EMULATION-LES-MIB) expressed in pysnmp data model.
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
 LeArpTableEntryType,
 VciInteger,
 VpiInteger,
 atmfLanEmulation) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress",
    "LeArpTableEntryType",
    "VciInteger",
    "VpiInteger",
    "atmfLanEmulation")

(AtmLaneMask,
 IfIndexOrZero) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "AtmLaneMask",
    "IfIndexOrZero")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

lesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LecId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )



class BusConfIndex(TextualConvention, Integer32):
    status = "current"


class LesLocalIndex(TextualConvention, Integer32):
    status = "current"


class LesLecDataFrameFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3))
    )



class LesLecDataFrameSize(TextualConvention, Integer32):
    status = "current"
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
        *(("max1516", 2),
          ("max4544", 3),
          ("max9234", 4),
          ("max18190", 5))
    )



class LesErrLogIndexType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_LesConfGroup_ObjectIdentity = ObjectIdentity
lesConfGroup = _LesConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1)
)
_LesConfNextId_Type = LesLocalIndex
_LesConfNextId_Object = MibScalar
lesConfNextId = _LesConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 1),
    _LesConfNextId_Type()
)
lesConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesConfNextId.setStatus("current")
_LesConfTable_Object = MibTable
lesConfTable = _LesConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lesConfTable.setStatus("current")
_LesConfEntry_Object = MibTableRow
lesConfEntry = _LesConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1)
)
lesConfEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    lesConfEntry.setStatus("current")
_LesConfIndex_Type = LesLocalIndex
_LesConfIndex_Object = MibTableColumn
lesConfIndex = _LesConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 1),
    _LesConfIndex_Type()
)
lesConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesConfIndex.setStatus("current")
_LesAtmAddrSpec_Type = AtmLaneAddress
_LesAtmAddrSpec_Object = MibTableColumn
lesAtmAddrSpec = _LesAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 2),
    _LesAtmAddrSpec_Type()
)
lesAtmAddrSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesAtmAddrSpec.setStatus("current")


class _LesAtmAddrMask_Type(AtmLaneMask):
    """Custom type lesAtmAddrMask based on AtmLaneMask"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"


_LesAtmAddrMask_Type.__name__ = "AtmLaneMask"
_LesAtmAddrMask_Object = MibTableColumn
lesAtmAddrMask = _LesAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 3),
    _LesAtmAddrMask_Type()
)
lesAtmAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesAtmAddrMask.setStatus("current")
_LesAtmAddrActual_Type = AtmLaneAddress
_LesAtmAddrActual_Object = MibTableColumn
lesAtmAddrActual = _LesAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 4),
    _LesAtmAddrActual_Type()
)
lesAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesAtmAddrActual.setStatus("current")


class _LesElanName_Type(DisplayString):
    """Custom type lesElanName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LesElanName_Type.__name__ = "DisplayString"
_LesElanName_Object = MibTableColumn
lesElanName = _LesElanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 5),
    _LesElanName_Type()
)
lesElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesElanName.setStatus("current")
_LesLanType_Type = LesLecDataFrameFormat
_LesLanType_Object = MibTableColumn
lesLanType = _LesLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 6),
    _LesLanType_Type()
)
lesLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLanType.setStatus("current")
_LesLastChange_Type = TimeStamp
_LesLastChange_Object = MibTableColumn
lesLastChange = _LesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 7),
    _LesLastChange_Type()
)
lesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLastChange.setStatus("current")
_LesMaxFrameSize_Type = LesLecDataFrameSize
_LesMaxFrameSize_Object = MibTableColumn
lesMaxFrameSize = _LesMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 8),
    _LesMaxFrameSize_Type()
)
lesMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesMaxFrameSize.setStatus("current")


class _LesControlTimeOut_Type(Integer32):
    """Custom type lesControlTimeOut based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LesControlTimeOut_Type.__name__ = "Integer32"
_LesControlTimeOut_Object = MibTableColumn
lesControlTimeOut = _LesControlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 9),
    _LesControlTimeOut_Type()
)
lesControlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesControlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    lesControlTimeOut.setUnits("seconds")


class _LesOperStatus_Type(Integer32):
    """Custom type lesOperStatus based on Integer32"""
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


_LesOperStatus_Type.__name__ = "Integer32"
_LesOperStatus_Object = MibTableColumn
lesOperStatus = _LesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 11),
    _LesOperStatus_Type()
)
lesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOperStatus.setStatus("current")


class _LesAdminStatus_Type(Integer32):
    """Custom type lesAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3))
    )


_LesAdminStatus_Type.__name__ = "Integer32"
_LesAdminStatus_Object = MibTableColumn
lesAdminStatus = _LesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 12),
    _LesAdminStatus_Type()
)
lesAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesAdminStatus.setStatus("current")
_LesRowStatus_Type = RowStatus
_LesRowStatus_Object = MibTableColumn
lesRowStatus = _LesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 2, 1, 13),
    _LesRowStatus_Type()
)
lesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesRowStatus.setStatus("current")
_LesVccTable_Object = MibTable
lesVccTable = _LesVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lesVccTable.setStatus("current")
_LesVccEntry_Object = MibTableRow
lesVccEntry = _LesVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1)
)
lesVccEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesVccAtmIfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesVccCtlDistVpi"),
    (0, "LAN-EMULATION-LES-MIB", "lesVccCtlDistVci"),
)
if mibBuilder.loadTexts:
    lesVccEntry.setStatus("current")
_LesVccAtmIfIndex_Type = IfIndexOrZero
_LesVccAtmIfIndex_Object = MibTableColumn
lesVccAtmIfIndex = _LesVccAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 1),
    _LesVccAtmIfIndex_Type()
)
lesVccAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesVccAtmIfIndex.setStatus("current")
_LesVccCtlDistVpi_Type = VpiInteger
_LesVccCtlDistVpi_Object = MibTableColumn
lesVccCtlDistVpi = _LesVccCtlDistVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 2),
    _LesVccCtlDistVpi_Type()
)
lesVccCtlDistVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesVccCtlDistVpi.setStatus("current")
_LesVccCtlDistVci_Type = VciInteger
_LesVccCtlDistVci_Object = MibTableColumn
lesVccCtlDistVci = _LesVccCtlDistVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 3),
    _LesVccCtlDistVci_Type()
)
lesVccCtlDistVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesVccCtlDistVci.setStatus("current")
_LesVccRowStatus_Type = RowStatus
_LesVccRowStatus_Object = MibTableColumn
lesVccRowStatus = _LesVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 3, 1, 4),
    _LesVccRowStatus_Type()
)
lesVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesVccRowStatus.setStatus("current")
_LesBusTable_Object = MibTable
lesBusTable = _LesBusTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    lesBusTable.setStatus("current")
_LesBusEntry_Object = MibTableRow
lesBusEntry = _LesBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4, 1)
)
lesBusEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesBusConfIndex"),
)
if mibBuilder.loadTexts:
    lesBusEntry.setStatus("current")
_LesBusConfIndex_Type = BusConfIndex
_LesBusConfIndex_Object = MibTableColumn
lesBusConfIndex = _LesBusConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4, 1, 1),
    _LesBusConfIndex_Type()
)
lesBusConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesBusConfIndex.setStatus("current")
_LesBusAddress_Type = AtmLaneAddress
_LesBusAddress_Object = MibTableColumn
lesBusAddress = _LesBusAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 4, 1, 2),
    _LesBusAddress_Type()
)
lesBusAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesBusAddress.setStatus("current")
_LesLeArpMacTable_Object = MibTable
lesLeArpMacTable = _LesLeArpMacTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    lesLeArpMacTable.setStatus("current")
_LesLeArpMacEntry_Object = MibTableRow
lesLeArpMacEntry = _LesLeArpMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1)
)
lesLeArpMacEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLeArpMacAddr"),
)
if mibBuilder.loadTexts:
    lesLeArpMacEntry.setStatus("current")
_LesLeArpMacAddr_Type = MacAddress
_LesLeArpMacAddr_Object = MibTableColumn
lesLeArpMacAddr = _LesLeArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 1),
    _LesLeArpMacAddr_Type()
)
lesLeArpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLeArpMacAddr.setStatus("current")
_LesLeArpLecId_Type = LecId
_LesLeArpLecId_Object = MibTableColumn
lesLeArpLecId = _LesLeArpLecId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 2),
    _LesLeArpLecId_Type()
)
lesLeArpLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeArpLecId.setStatus("current")
_LesLeArpAtmAddr_Type = AtmLaneAddress
_LesLeArpAtmAddr_Object = MibTableColumn
lesLeArpAtmAddr = _LesLeArpAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 3),
    _LesLeArpAtmAddr_Type()
)
lesLeArpAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLeArpAtmAddr.setStatus("current")


class _LesLeArpEntryType_Type(LeArpTableEntryType):
    """Custom type lesLeArpEntryType based on LeArpTableEntryType"""
    defaultValue = 4


_LesLeArpEntryType_Type.__name__ = "LeArpTableEntryType"
_LesLeArpEntryType_Object = MibTableColumn
lesLeArpEntryType = _LesLeArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 4),
    _LesLeArpEntryType_Type()
)
lesLeArpEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLeArpEntryType.setStatus("current")
_LesLeArpRowStatus_Type = RowStatus
_LesLeArpRowStatus_Object = MibTableColumn
lesLeArpRowStatus = _LesLeArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 5, 1, 5),
    _LesLeArpRowStatus_Type()
)
lesLeArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLeArpRowStatus.setStatus("current")
_LesLeArpRdTable_Object = MibTable
lesLeArpRdTable = _LesLeArpRdTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6)
)
if mibBuilder.loadTexts:
    lesLeArpRdTable.setStatus("current")
_LesLeArpRdEntry_Object = MibTableRow
lesLeArpRdEntry = _LesLeArpRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1)
)
lesLeArpRdEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLeArpRdSegId"),
    (0, "LAN-EMULATION-LES-MIB", "lesLeArpRdBridgeNum"),
)
if mibBuilder.loadTexts:
    lesLeArpRdEntry.setStatus("current")


class _LesLeArpRdSegId_Type(Integer32):
    """Custom type lesLeArpRdSegId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LesLeArpRdSegId_Type.__name__ = "Integer32"
_LesLeArpRdSegId_Object = MibTableColumn
lesLeArpRdSegId = _LesLeArpRdSegId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 1),
    _LesLeArpRdSegId_Type()
)
lesLeArpRdSegId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLeArpRdSegId.setStatus("current")


class _LesLeArpRdBridgeNum_Type(Integer32):
    """Custom type lesLeArpRdBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LesLeArpRdBridgeNum_Type.__name__ = "Integer32"
_LesLeArpRdBridgeNum_Object = MibTableColumn
lesLeArpRdBridgeNum = _LesLeArpRdBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 2),
    _LesLeArpRdBridgeNum_Type()
)
lesLeArpRdBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLeArpRdBridgeNum.setStatus("current")
_LesLeArpRdLecId_Type = LecId
_LesLeArpRdLecId_Object = MibTableColumn
lesLeArpRdLecId = _LesLeArpRdLecId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 3),
    _LesLeArpRdLecId_Type()
)
lesLeArpRdLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLeArpRdLecId.setStatus("current")
_LesLeArpRdAtmAddr_Type = AtmLaneAddress
_LesLeArpRdAtmAddr_Object = MibTableColumn
lesLeArpRdAtmAddr = _LesLeArpRdAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 4),
    _LesLeArpRdAtmAddr_Type()
)
lesLeArpRdAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLeArpRdAtmAddr.setStatus("current")


class _LesLeArpRdEntryType_Type(LeArpTableEntryType):
    """Custom type lesLeArpRdEntryType based on LeArpTableEntryType"""
    defaultValue = 4


_LesLeArpRdEntryType_Type.__name__ = "LeArpTableEntryType"
_LesLeArpRdEntryType_Object = MibTableColumn
lesLeArpRdEntryType = _LesLeArpRdEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 5),
    _LesLeArpRdEntryType_Type()
)
lesLeArpRdEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLeArpRdEntryType.setStatus("current")
_LesLeArpRdRowStatus_Type = RowStatus
_LesLeArpRdRowStatus_Object = MibTableColumn
lesLeArpRdRowStatus = _LesLeArpRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 6, 1, 6),
    _LesLeArpRdRowStatus_Type()
)
lesLeArpRdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLeArpRdRowStatus.setStatus("current")
_LesLecTableLastChange_Type = TimeStamp
_LesLecTableLastChange_Object = MibScalar
lesLecTableLastChange = _LesLecTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 7),
    _LesLecTableLastChange_Type()
)
lesLecTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecTableLastChange.setStatus("current")
_LesLecTable_Object = MibTable
lesLecTable = _LesLecTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8)
)
if mibBuilder.loadTexts:
    lesLecTable.setStatus("current")
_LesLecEntry_Object = MibTableRow
lesLecEntry = _LesLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1)
)
lesLecEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesLecIndex"),
)
if mibBuilder.loadTexts:
    lesLecEntry.setStatus("current")


class _LesLecIndex_Type(Integer32):
    """Custom type lesLecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LesLecIndex_Type.__name__ = "Integer32"
_LesLecIndex_Object = MibTableColumn
lesLecIndex = _LesLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 1),
    _LesLecIndex_Type()
)
lesLecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesLecIndex.setStatus("current")
_LesLecAtmAddr_Type = AtmLaneAddress
_LesLecAtmAddr_Object = MibTableColumn
lesLecAtmAddr = _LesLecAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 2),
    _LesLecAtmAddr_Type()
)
lesLecAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecAtmAddr.setStatus("current")


class _LesLecProxy_Type(TruthValue):
    """Custom type lesLecProxy based on TruthValue"""
    defaultValue = 2


_LesLecProxy_Type.__name__ = "TruthValue"
_LesLecProxy_Object = MibTableColumn
lesLecProxy = _LesLecProxy_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 3),
    _LesLecProxy_Type()
)
lesLecProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecProxy.setStatus("current")


class _LesLecId_Type(LecId):
    """Custom type lesLecId based on LecId"""
    defaultValue = 0


_LesLecId_Type.__name__ = "LecId"
_LesLecId_Object = MibTableColumn
lesLecId = _LesLecId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 4),
    _LesLecId_Type()
)
lesLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecId.setStatus("current")
_LesLecAtmIfIndex_Type = IfIndexOrZero
_LesLecAtmIfIndex_Object = MibTableColumn
lesLecAtmIfIndex = _LesLecAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 5),
    _LesLecAtmIfIndex_Type()
)
lesLecAtmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLecAtmIfIndex.setStatus("current")
_LesLecCtlDirectVpi_Type = VpiInteger
_LesLecCtlDirectVpi_Object = MibTableColumn
lesLecCtlDirectVpi = _LesLecCtlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 6),
    _LesLecCtlDirectVpi_Type()
)
lesLecCtlDirectVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLecCtlDirectVpi.setStatus("current")
_LesLecCtlDirectVci_Type = VciInteger
_LesLecCtlDirectVci_Object = MibTableColumn
lesLecCtlDirectVci = _LesLecCtlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 7),
    _LesLecCtlDirectVci_Type()
)
lesLecCtlDirectVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLecCtlDirectVci.setStatus("current")
_LesLecLastChange_Type = TimeStamp
_LesLecLastChange_Object = MibTableColumn
lesLecLastChange = _LesLecLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 8),
    _LesLecLastChange_Type()
)
lesLecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecLastChange.setStatus("current")


class _LesLecState_Type(Integer32):
    """Custom type lesLecState based on Integer32"""
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
          ("noLesConnect", 2),
          ("lesConnect", 3),
          ("joining", 4),
          ("addLec", 5),
          ("joinedLes", 6))
    )


_LesLecState_Type.__name__ = "Integer32"
_LesLecState_Object = MibTableColumn
lesLecState = _LesLecState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 9),
    _LesLecState_Type()
)
lesLecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecState.setStatus("current")
_LesLecRowStatus_Type = RowStatus
_LesLecRowStatus_Object = MibTableColumn
lesLecRowStatus = _LesLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 1, 8, 1, 10),
    _LesLecRowStatus_Type()
)
lesLecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lesLecRowStatus.setStatus("current")
_LesStatGroup_ObjectIdentity = ObjectIdentity
lesStatGroup = _LesStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2)
)
_LesStatTable_Object = MibTable
lesStatTable = _LesStatTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lesStatTable.setStatus("current")
_LesStatEntry_Object = MibTableRow
lesStatEntry = _LesStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lesStatEntry.setStatus("current")
_LesStatJoinOk_Type = Counter32
_LesStatJoinOk_Object = MibTableColumn
lesStatJoinOk = _LesStatJoinOk_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 1),
    _LesStatJoinOk_Type()
)
lesStatJoinOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatJoinOk.setStatus("current")
_LesStatVerNotSup_Type = Counter32
_LesStatVerNotSup_Object = MibTableColumn
lesStatVerNotSup = _LesStatVerNotSup_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 2),
    _LesStatVerNotSup_Type()
)
lesStatVerNotSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatVerNotSup.setStatus("current")
_LesStatInvalidReqParam_Type = Counter32
_LesStatInvalidReqParam_Object = MibTableColumn
lesStatInvalidReqParam = _LesStatInvalidReqParam_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 3),
    _LesStatInvalidReqParam_Type()
)
lesStatInvalidReqParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidReqParam.setStatus("current")
_LesStatDupLanDest_Type = Counter32
_LesStatDupLanDest_Object = MibTableColumn
lesStatDupLanDest = _LesStatDupLanDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 4),
    _LesStatDupLanDest_Type()
)
lesStatDupLanDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatDupLanDest.setStatus("current")
_LesStatDupAtmAddr_Type = Counter32
_LesStatDupAtmAddr_Object = MibTableColumn
lesStatDupAtmAddr = _LesStatDupAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 5),
    _LesStatDupAtmAddr_Type()
)
lesStatDupAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatDupAtmAddr.setStatus("current")
_LesStatInsRes_Type = Counter32
_LesStatInsRes_Object = MibTableColumn
lesStatInsRes = _LesStatInsRes_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 6),
    _LesStatInsRes_Type()
)
lesStatInsRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInsRes.setStatus("current")
_LesStatAccDenied_Type = Counter32
_LesStatAccDenied_Object = MibTableColumn
lesStatAccDenied = _LesStatAccDenied_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 7),
    _LesStatAccDenied_Type()
)
lesStatAccDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatAccDenied.setStatus("current")
_LesStatInvalidReqId_Type = Counter32
_LesStatInvalidReqId_Object = MibTableColumn
lesStatInvalidReqId = _LesStatInvalidReqId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 8),
    _LesStatInvalidReqId_Type()
)
lesStatInvalidReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidReqId.setStatus("current")
_LesStatInvalidLanDest_Type = Counter32
_LesStatInvalidLanDest_Object = MibTableColumn
lesStatInvalidLanDest = _LesStatInvalidLanDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 9),
    _LesStatInvalidLanDest_Type()
)
lesStatInvalidLanDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidLanDest.setStatus("current")
_LesStatInvalidAtmAddr_Type = Counter32
_LesStatInvalidAtmAddr_Object = MibTableColumn
lesStatInvalidAtmAddr = _LesStatInvalidAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 10),
    _LesStatInvalidAtmAddr_Type()
)
lesStatInvalidAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInvalidAtmAddr.setStatus("current")
_LesStatInBadPkts_Type = Counter32
_LesStatInBadPkts_Object = MibTableColumn
lesStatInBadPkts = _LesStatInBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 11),
    _LesStatInBadPkts_Type()
)
lesStatInBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatInBadPkts.setStatus("current")
_LesStatOutRegFails_Type = Counter32
_LesStatOutRegFails_Object = MibTableColumn
lesStatOutRegFails = _LesStatOutRegFails_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 12),
    _LesStatOutRegFails_Type()
)
lesStatOutRegFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatOutRegFails.setStatus("current")
_LesStatLeArpIn_Type = Counter32
_LesStatLeArpIn_Object = MibTableColumn
lesStatLeArpIn = _LesStatLeArpIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 13),
    _LesStatLeArpIn_Type()
)
lesStatLeArpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatLeArpIn.setStatus("current")
_LesStatLeArpFwd_Type = Counter32
_LesStatLeArpFwd_Object = MibTableColumn
lesStatLeArpFwd = _LesStatLeArpFwd_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 2, 1, 1, 14),
    _LesStatLeArpFwd_Type()
)
lesStatLeArpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesStatLeArpFwd.setStatus("current")
_LesLecStatGroup_ObjectIdentity = ObjectIdentity
lesLecStatGroup = _LesLecStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3)
)
_LesLecStatTable_Object = MibTable
lesLecStatTable = _LesLecStatTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lesLecStatTable.setStatus("current")
_LesLecStatEntry_Object = MibTableRow
lesLecStatEntry = _LesLecStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lesLecStatEntry.setStatus("current")
_LesLecRecvs_Type = Counter32
_LesLecRecvs_Object = MibTableColumn
lesLecRecvs = _LesLecRecvs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 1),
    _LesLecRecvs_Type()
)
lesLecRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecRecvs.setStatus("current")
_LesLecSends_Type = Counter32
_LesLecSends_Object = MibTableColumn
lesLecSends = _LesLecSends_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 3),
    _LesLecSends_Type()
)
lesLecSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecSends.setStatus("current")
_LesLecInRegReq_Type = Counter32
_LesLecInRegReq_Object = MibTableColumn
lesLecInRegReq = _LesLecInRegReq_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 4),
    _LesLecInRegReq_Type()
)
lesLecInRegReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInRegReq.setStatus("current")
_LesLecInUnReg_Type = Counter32
_LesLecInUnReg_Object = MibTableColumn
lesLecInUnReg = _LesLecInUnReg_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 5),
    _LesLecInUnReg_Type()
)
lesLecInUnReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInUnReg.setStatus("current")
_LesLecInLeArpUcast_Type = Counter32
_LesLecInLeArpUcast_Object = MibTableColumn
lesLecInLeArpUcast = _LesLecInLeArpUcast_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 6),
    _LesLecInLeArpUcast_Type()
)
lesLecInLeArpUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInLeArpUcast.setStatus("current")
_LesLecInLeArpBcast_Type = Counter32
_LesLecInLeArpBcast_Object = MibTableColumn
lesLecInLeArpBcast = _LesLecInLeArpBcast_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 7),
    _LesLecInLeArpBcast_Type()
)
lesLecInLeArpBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInLeArpBcast.setStatus("current")
_LesLecInLeArpResp_Type = Counter32
_LesLecInLeArpResp_Object = MibTableColumn
lesLecInLeArpResp = _LesLecInLeArpResp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 8),
    _LesLecInLeArpResp_Type()
)
lesLecInLeArpResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInLeArpResp.setStatus("current")
_LesLecInNArp_Type = Counter32
_LesLecInNArp_Object = MibTableColumn
lesLecInNArp = _LesLecInNArp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 3, 1, 1, 10),
    _LesLecInNArp_Type()
)
lesLecInNArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesLecInNArp.setStatus("current")
_LesFaultGroup_ObjectIdentity = ObjectIdentity
lesFaultGroup = _LesFaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4)
)
_LesErrCtlTable_Object = MibTable
lesErrCtlTable = _LesErrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lesErrCtlTable.setStatus("current")
_LesErrCtlEntry_Object = MibTableRow
lesErrCtlEntry = _LesErrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lesErrCtlEntry.setStatus("current")


class _LesErrCtlAdminStatus_Type(Integer32):
    """Custom type lesErrCtlAdminStatus based on Integer32"""
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


_LesErrCtlAdminStatus_Type.__name__ = "Integer32"
_LesErrCtlAdminStatus_Object = MibTableColumn
lesErrCtlAdminStatus = _LesErrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 1),
    _LesErrCtlAdminStatus_Type()
)
lesErrCtlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesErrCtlAdminStatus.setStatus("current")


class _LesErrCtlOperStatus_Type(Integer32):
    """Custom type lesErrCtlOperStatus based on Integer32"""
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


_LesErrCtlOperStatus_Type.__name__ = "Integer32"
_LesErrCtlOperStatus_Object = MibTableColumn
lesErrCtlOperStatus = _LesErrCtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 2),
    _LesErrCtlOperStatus_Type()
)
lesErrCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrCtlOperStatus.setStatus("current")


class _LesErrCtlClearLog_Type(Integer32):
    """Custom type lesErrCtlClearLog based on Integer32"""
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


_LesErrCtlClearLog_Type.__name__ = "Integer32"
_LesErrCtlClearLog_Object = MibTableColumn
lesErrCtlClearLog = _LesErrCtlClearLog_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 3),
    _LesErrCtlClearLog_Type()
)
lesErrCtlClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesErrCtlClearLog.setStatus("current")


class _LesErrCtlMaxEntries_Type(Integer32):
    """Custom type lesErrCtlMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LesErrCtlMaxEntries_Type.__name__ = "Integer32"
_LesErrCtlMaxEntries_Object = MibTableColumn
lesErrCtlMaxEntries = _LesErrCtlMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 4),
    _LesErrCtlMaxEntries_Type()
)
lesErrCtlMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrCtlMaxEntries.setStatus("current")
_LesErrCtlLastEntry_Type = LesErrLogIndexType
_LesErrCtlLastEntry_Object = MibTableColumn
lesErrCtlLastEntry = _LesErrCtlLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 1, 1, 5),
    _LesErrCtlLastEntry_Type()
)
lesErrCtlLastEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesErrCtlLastEntry.setStatus("current")
_LesErrLogTable_Object = MibTable
lesErrLogTable = _LesErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    lesErrLogTable.setStatus("current")
_LesErrLogEntry_Object = MibTableRow
lesErrLogEntry = _LesErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1)
)
lesErrLogEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "LAN-EMULATION-LES-MIB", "lesErrLogIndex"),
)
if mibBuilder.loadTexts:
    lesErrLogEntry.setStatus("current")
_LesErrLogIndex_Type = LesErrLogIndexType
_LesErrLogIndex_Object = MibTableColumn
lesErrLogIndex = _LesErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 1),
    _LesErrLogIndex_Type()
)
lesErrLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesErrLogIndex.setStatus("current")
_LesErrLogAtmAddr_Type = AtmLaneAddress
_LesErrLogAtmAddr_Object = MibTableColumn
lesErrLogAtmAddr = _LesErrLogAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 2),
    _LesErrLogAtmAddr_Type()
)
lesErrLogAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrLogAtmAddr.setStatus("current")


class _LesErrLogErrCode_Type(Integer32):
    """Custom type lesErrLogErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_LesErrLogErrCode_Type.__name__ = "Integer32"
_LesErrLogErrCode_Object = MibTableColumn
lesErrLogErrCode = _LesErrLogErrCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 3),
    _LesErrLogErrCode_Type()
)
lesErrLogErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrLogErrCode.setStatus("current")
_LesErrLogTime_Type = TimeStamp
_LesErrLogTime_Object = MibTableColumn
lesErrLogTime = _LesErrLogTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 4, 2, 1, 4),
    _LesErrLogTime_Type()
)
lesErrLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesErrLogTime.setStatus("current")
_LesMIBConformance_ObjectIdentity = ObjectIdentity
lesMIBConformance = _LesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5)
)
_LesMIBGroups_ObjectIdentity = ObjectIdentity
lesMIBGroups = _LesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 1)
)
_LesMIBCompliances_ObjectIdentity = ObjectIdentity
lesMIBCompliances = _LesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 2)
)
lesConfEntry.registerAugmentions(
    ("LAN-EMULATION-LES-MIB",
     "lesStatEntry")
)
lesStatEntry.setIndexNames(*lesConfEntry.getIndexNames())
lesLecEntry.registerAugmentions(
    ("LAN-EMULATION-LES-MIB",
     "lesLecStatEntry")
)
lesLecStatEntry.setIndexNames(*lesLecEntry.getIndexNames())
lesConfEntry.registerAugmentions(
    ("LAN-EMULATION-LES-MIB",
     "lesErrCtlEntry")
)
lesErrCtlEntry.setIndexNames(*lesConfEntry.getIndexNames())

# Managed Objects groups

lesCConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 1, 1)
)
lesCConfGroup.setObjects(
      *(("LAN-EMULATION-LES-MIB", "lesConfNextId"),
        ("LAN-EMULATION-LES-MIB", "lesAtmAddrSpec"),
        ("LAN-EMULATION-LES-MIB", "lesAtmAddrMask"),
        ("LAN-EMULATION-LES-MIB", "lesAtmAddrActual"),
        ("LAN-EMULATION-LES-MIB", "lesElanName"),
        ("LAN-EMULATION-LES-MIB", "lesLanType"),
        ("LAN-EMULATION-LES-MIB", "lesLastChange"),
        ("LAN-EMULATION-LES-MIB", "lesControlTimeOut"),
        ("LAN-EMULATION-LES-MIB", "lesMaxFrameSize"),
        ("LAN-EMULATION-LES-MIB", "lesVccRowStatus"),
        ("LAN-EMULATION-LES-MIB", "lesOperStatus"),
        ("LAN-EMULATION-LES-MIB", "lesAdminStatus"),
        ("LAN-EMULATION-LES-MIB", "lesRowStatus"),
        ("LAN-EMULATION-LES-MIB", "lesBusAddress"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpLecId"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpAtmAddr"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpEntryType"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpRowStatus"),
        ("LAN-EMULATION-LES-MIB", "lesLecTableLastChange"),
        ("LAN-EMULATION-LES-MIB", "lesLecAtmIfIndex"),
        ("LAN-EMULATION-LES-MIB", "lesLecProxy"),
        ("LAN-EMULATION-LES-MIB", "lesLecAtmAddr"),
        ("LAN-EMULATION-LES-MIB", "lesLecId"),
        ("LAN-EMULATION-LES-MIB", "lesLecCtlDirectVpi"),
        ("LAN-EMULATION-LES-MIB", "lesLecCtlDirectVci"),
        ("LAN-EMULATION-LES-MIB", "lesLecLastChange"),
        ("LAN-EMULATION-LES-MIB", "lesLecRowStatus"),
        ("LAN-EMULATION-LES-MIB", "lesLecState"))
)
if mibBuilder.loadTexts:
    lesCConfGroup.setStatus("current")

lesRdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 1, 2)
)
lesRdGroup.setObjects(
      *(("LAN-EMULATION-LES-MIB", "lesLeArpRdLecId"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpRdAtmAddr"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpRdEntryType"),
        ("LAN-EMULATION-LES-MIB", "lesLeArpRdRowStatus"))
)
if mibBuilder.loadTexts:
    lesRdGroup.setStatus("current")

lesCStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 1, 3)
)
lesCStatGroup.setObjects(
      *(("LAN-EMULATION-LES-MIB", "lesStatJoinOk"),
        ("LAN-EMULATION-LES-MIB", "lesStatInBadPkts"),
        ("LAN-EMULATION-LES-MIB", "lesStatOutRegFails"),
        ("LAN-EMULATION-LES-MIB", "lesStatVerNotSup"),
        ("LAN-EMULATION-LES-MIB", "lesStatInvalidReqParam"),
        ("LAN-EMULATION-LES-MIB", "lesStatDupLanDest"),
        ("LAN-EMULATION-LES-MIB", "lesStatDupAtmAddr"),
        ("LAN-EMULATION-LES-MIB", "lesStatInsRes"),
        ("LAN-EMULATION-LES-MIB", "lesStatAccDenied"),
        ("LAN-EMULATION-LES-MIB", "lesStatInvalidReqId"),
        ("LAN-EMULATION-LES-MIB", "lesStatInvalidLanDest"),
        ("LAN-EMULATION-LES-MIB", "lesStatInvalidAtmAddr"),
        ("LAN-EMULATION-LES-MIB", "lesStatLeArpIn"),
        ("LAN-EMULATION-LES-MIB", "lesStatLeArpFwd"))
)
if mibBuilder.loadTexts:
    lesCStatGroup.setStatus("current")

lesLecCStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 1, 4)
)
lesLecCStatGroup.setObjects(
      *(("LAN-EMULATION-LES-MIB", "lesLecRecvs"),
        ("LAN-EMULATION-LES-MIB", "lesLecSends"),
        ("LAN-EMULATION-LES-MIB", "lesLecInRegReq"),
        ("LAN-EMULATION-LES-MIB", "lesLecInUnReg"),
        ("LAN-EMULATION-LES-MIB", "lesLecInLeArpUcast"),
        ("LAN-EMULATION-LES-MIB", "lesLecInLeArpBcast"),
        ("LAN-EMULATION-LES-MIB", "lesLecInLeArpResp"),
        ("LAN-EMULATION-LES-MIB", "lesLecInNArp"))
)
if mibBuilder.loadTexts:
    lesLecCStatGroup.setStatus("current")

lesFaultCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 1, 5)
)
lesFaultCGroup.setObjects(
      *(("LAN-EMULATION-LES-MIB", "lesErrCtlAdminStatus"),
        ("LAN-EMULATION-LES-MIB", "lesErrCtlOperStatus"),
        ("LAN-EMULATION-LES-MIB", "lesErrCtlClearLog"),
        ("LAN-EMULATION-LES-MIB", "lesErrCtlMaxEntries"),
        ("LAN-EMULATION-LES-MIB", "lesErrCtlLastEntry"),
        ("LAN-EMULATION-LES-MIB", "lesErrLogAtmAddr"),
        ("LAN-EMULATION-LES-MIB", "lesErrLogErrCode"),
        ("LAN-EMULATION-LES-MIB", "lesErrLogTime"))
)
if mibBuilder.loadTexts:
    lesFaultCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 3, 5, 2, 1)
)
lesMIBCompliance.setObjects(
      *(("LAN-EMULATION-LES-MIB", "lesCConfGroup"),
        ("LAN-EMULATION-LES-MIB", "lesCStatGroup"),
        ("LAN-EMULATION-LES-MIB", "lesLecCStatGroup"),
        ("LAN-EMULATION-LES-MIB", "lesFaultCGroup"))
)
if mibBuilder.loadTexts:
    lesMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-EMULATION-LES-MIB",
    **{"LecId": LecId,
       "BusConfIndex": BusConfIndex,
       "LesLocalIndex": LesLocalIndex,
       "LesLecDataFrameFormat": LesLecDataFrameFormat,
       "LesLecDataFrameSize": LesLecDataFrameSize,
       "LesErrLogIndexType": LesErrLogIndexType,
       "lesMIB": lesMIB,
       "lesConfGroup": lesConfGroup,
       "lesConfNextId": lesConfNextId,
       "lesConfTable": lesConfTable,
       "lesConfEntry": lesConfEntry,
       "lesConfIndex": lesConfIndex,
       "lesAtmAddrSpec": lesAtmAddrSpec,
       "lesAtmAddrMask": lesAtmAddrMask,
       "lesAtmAddrActual": lesAtmAddrActual,
       "lesElanName": lesElanName,
       "lesLanType": lesLanType,
       "lesLastChange": lesLastChange,
       "lesMaxFrameSize": lesMaxFrameSize,
       "lesControlTimeOut": lesControlTimeOut,
       "lesOperStatus": lesOperStatus,
       "lesAdminStatus": lesAdminStatus,
       "lesRowStatus": lesRowStatus,
       "lesVccTable": lesVccTable,
       "lesVccEntry": lesVccEntry,
       "lesVccAtmIfIndex": lesVccAtmIfIndex,
       "lesVccCtlDistVpi": lesVccCtlDistVpi,
       "lesVccCtlDistVci": lesVccCtlDistVci,
       "lesVccRowStatus": lesVccRowStatus,
       "lesBusTable": lesBusTable,
       "lesBusEntry": lesBusEntry,
       "lesBusConfIndex": lesBusConfIndex,
       "lesBusAddress": lesBusAddress,
       "lesLeArpMacTable": lesLeArpMacTable,
       "lesLeArpMacEntry": lesLeArpMacEntry,
       "lesLeArpMacAddr": lesLeArpMacAddr,
       "lesLeArpLecId": lesLeArpLecId,
       "lesLeArpAtmAddr": lesLeArpAtmAddr,
       "lesLeArpEntryType": lesLeArpEntryType,
       "lesLeArpRowStatus": lesLeArpRowStatus,
       "lesLeArpRdTable": lesLeArpRdTable,
       "lesLeArpRdEntry": lesLeArpRdEntry,
       "lesLeArpRdSegId": lesLeArpRdSegId,
       "lesLeArpRdBridgeNum": lesLeArpRdBridgeNum,
       "lesLeArpRdLecId": lesLeArpRdLecId,
       "lesLeArpRdAtmAddr": lesLeArpRdAtmAddr,
       "lesLeArpRdEntryType": lesLeArpRdEntryType,
       "lesLeArpRdRowStatus": lesLeArpRdRowStatus,
       "lesLecTableLastChange": lesLecTableLastChange,
       "lesLecTable": lesLecTable,
       "lesLecEntry": lesLecEntry,
       "lesLecIndex": lesLecIndex,
       "lesLecAtmAddr": lesLecAtmAddr,
       "lesLecProxy": lesLecProxy,
       "lesLecId": lesLecId,
       "lesLecAtmIfIndex": lesLecAtmIfIndex,
       "lesLecCtlDirectVpi": lesLecCtlDirectVpi,
       "lesLecCtlDirectVci": lesLecCtlDirectVci,
       "lesLecLastChange": lesLecLastChange,
       "lesLecState": lesLecState,
       "lesLecRowStatus": lesLecRowStatus,
       "lesStatGroup": lesStatGroup,
       "lesStatTable": lesStatTable,
       "lesStatEntry": lesStatEntry,
       "lesStatJoinOk": lesStatJoinOk,
       "lesStatVerNotSup": lesStatVerNotSup,
       "lesStatInvalidReqParam": lesStatInvalidReqParam,
       "lesStatDupLanDest": lesStatDupLanDest,
       "lesStatDupAtmAddr": lesStatDupAtmAddr,
       "lesStatInsRes": lesStatInsRes,
       "lesStatAccDenied": lesStatAccDenied,
       "lesStatInvalidReqId": lesStatInvalidReqId,
       "lesStatInvalidLanDest": lesStatInvalidLanDest,
       "lesStatInvalidAtmAddr": lesStatInvalidAtmAddr,
       "lesStatInBadPkts": lesStatInBadPkts,
       "lesStatOutRegFails": lesStatOutRegFails,
       "lesStatLeArpIn": lesStatLeArpIn,
       "lesStatLeArpFwd": lesStatLeArpFwd,
       "lesLecStatGroup": lesLecStatGroup,
       "lesLecStatTable": lesLecStatTable,
       "lesLecStatEntry": lesLecStatEntry,
       "lesLecRecvs": lesLecRecvs,
       "lesLecSends": lesLecSends,
       "lesLecInRegReq": lesLecInRegReq,
       "lesLecInUnReg": lesLecInUnReg,
       "lesLecInLeArpUcast": lesLecInLeArpUcast,
       "lesLecInLeArpBcast": lesLecInLeArpBcast,
       "lesLecInLeArpResp": lesLecInLeArpResp,
       "lesLecInNArp": lesLecInNArp,
       "lesFaultGroup": lesFaultGroup,
       "lesErrCtlTable": lesErrCtlTable,
       "lesErrCtlEntry": lesErrCtlEntry,
       "lesErrCtlAdminStatus": lesErrCtlAdminStatus,
       "lesErrCtlOperStatus": lesErrCtlOperStatus,
       "lesErrCtlClearLog": lesErrCtlClearLog,
       "lesErrCtlMaxEntries": lesErrCtlMaxEntries,
       "lesErrCtlLastEntry": lesErrCtlLastEntry,
       "lesErrLogTable": lesErrLogTable,
       "lesErrLogEntry": lesErrLogEntry,
       "lesErrLogIndex": lesErrLogIndex,
       "lesErrLogAtmAddr": lesErrLogAtmAddr,
       "lesErrLogErrCode": lesErrLogErrCode,
       "lesErrLogTime": lesErrLogTime,
       "lesMIBConformance": lesMIBConformance,
       "lesMIBGroups": lesMIBGroups,
       "lesCConfGroup": lesCConfGroup,
       "lesRdGroup": lesRdGroup,
       "lesCStatGroup": lesCStatGroup,
       "lesLecCStatGroup": lesLecCStatGroup,
       "lesFaultCGroup": lesFaultCGroup,
       "lesMIBCompliances": lesMIBCompliances,
       "lesMIBCompliance": lesMIBCompliance}
)
