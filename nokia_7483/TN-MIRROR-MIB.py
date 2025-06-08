# SNMP MIB module (TN-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-MIRROR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(SdpId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "SdpId")

(ServiceAdminStatus,
 ServiceOperStatus,
 TFCName,
 TItemDescription,
 TPolicyID,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "ServiceAdminStatus",
    "ServiceOperStatus",
    "TFCName",
    "TItemDescription",
    "TPolicyID",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnMirrorMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 18)
)
if mibBuilder.loadTexts:
    tnMirrorMIBModule.setRevisions(
        ("1912-12-05 00:00",
         "1912-09-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1902-03-14 00:00",
         "1902-03-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TMplsLabel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class TEtherType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )



class TSessionId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxMirrorEncapType(TextualConvention, Integer32):
    status = "current"
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
        *(("ether", 1),
          ("frameRelay", 2),
          ("ppp", 3),
          ("atmSdu", 4),
          ("satopE1", 5),
          ("satopT1", 6),
          ("satopE3", 7),
          ("satopT3", 8),
          ("cesopsn", 9),
          ("cesopsnCas", 10),
          ("ipOnly", 11))
    )



# MIB Managed Objects in the order of their OIDs

_TnMirrorObjects_ObjectIdentity = ObjectIdentity
tnMirrorObjects = _TnMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18)
)
_TnMirrorDestinationObjects_ObjectIdentity = ObjectIdentity
tnMirrorDestinationObjects = _TnMirrorDestinationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1)
)
_TnMirrorDestinationTable_Object = MibTable
tnMirrorDestinationTable = _TnMirrorDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1)
)
if mibBuilder.loadTexts:
    tnMirrorDestinationTable.setStatus("current")
_TnMirrorDestinationEntry_Object = MibTableRow
tnMirrorDestinationEntry = _TnMirrorDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1)
)
tnMirrorDestinationEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MIRROR-MIB", "tnMirrorDestinationIndex"),
)
if mibBuilder.loadTexts:
    tnMirrorDestinationEntry.setStatus("current")
_TnMirrorDestinationIndex_Type = TmnxServId
_TnMirrorDestinationIndex_Object = MibTableColumn
tnMirrorDestinationIndex = _TnMirrorDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 1),
    _TnMirrorDestinationIndex_Type()
)
tnMirrorDestinationIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnMirrorDestinationIndex.setStatus("current")
_TnMirrorDestinationRowStatus_Type = RowStatus
_TnMirrorDestinationRowStatus_Object = MibTableColumn
tnMirrorDestinationRowStatus = _TnMirrorDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 2),
    _TnMirrorDestinationRowStatus_Type()
)
tnMirrorDestinationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationRowStatus.setStatus("current")


class _TnMirrorDestinationDescription_Type(TItemDescription):
    """Custom type tnMirrorDestinationDescription based on TItemDescription"""
    defaultHexValue = ""


_TnMirrorDestinationDescription_Type.__name__ = "TItemDescription"
_TnMirrorDestinationDescription_Object = MibTableColumn
tnMirrorDestinationDescription = _TnMirrorDestinationDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 3),
    _TnMirrorDestinationDescription_Type()
)
tnMirrorDestinationDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationDescription.setStatus("current")


class _TnMirrorDestinationFC_Type(TFCName):
    """Custom type tnMirrorDestinationFC based on TFCName"""
    defaultHexValue = "be"


_TnMirrorDestinationFC_Type.__name__ = "TFCName"
_TnMirrorDestinationFC_Object = MibTableColumn
tnMirrorDestinationFC = _TnMirrorDestinationFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 4),
    _TnMirrorDestinationFC_Type()
)
tnMirrorDestinationFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationFC.setStatus("current")


class _TnMirrorDestinationRemoteSource_Type(TruthValue):
    """Custom type tnMirrorDestinationRemoteSource based on TruthValue"""
    defaultValue = 2


_TnMirrorDestinationRemoteSource_Type.__name__ = "TruthValue"
_TnMirrorDestinationRemoteSource_Object = MibTableColumn
tnMirrorDestinationRemoteSource = _TnMirrorDestinationRemoteSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 5),
    _TnMirrorDestinationRemoteSource_Type()
)
tnMirrorDestinationRemoteSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationRemoteSource.setStatus("current")


class _TnMirrorDestinationSapPortId_Type(TmnxPortID):
    """Custom type tnMirrorDestinationSapPortId based on TmnxPortID"""
    defaultValue = 503316480


_TnMirrorDestinationSapPortId_Type.__name__ = "TmnxPortID"
_TnMirrorDestinationSapPortId_Object = MibTableColumn
tnMirrorDestinationSapPortId = _TnMirrorDestinationSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 6),
    _TnMirrorDestinationSapPortId_Type()
)
tnMirrorDestinationSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationSapPortId.setStatus("current")


class _TnMirrorDestinationSapEncapValue_Type(TmnxEncapVal):
    """Custom type tnMirrorDestinationSapEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TnMirrorDestinationSapEncapValue_Type.__name__ = "TmnxEncapVal"
_TnMirrorDestinationSapEncapValue_Object = MibTableColumn
tnMirrorDestinationSapEncapValue = _TnMirrorDestinationSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 7),
    _TnMirrorDestinationSapEncapValue_Type()
)
tnMirrorDestinationSapEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationSapEncapValue.setStatus("current")


class _TnMirrorDestinationSdpNumber_Type(SdpId):
    """Custom type tnMirrorDestinationSdpNumber based on SdpId"""
    defaultValue = 0


_TnMirrorDestinationSdpNumber_Type.__name__ = "SdpId"
_TnMirrorDestinationSdpNumber_Object = MibTableColumn
tnMirrorDestinationSdpNumber = _TnMirrorDestinationSdpNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 8),
    _TnMirrorDestinationSdpNumber_Type()
)
tnMirrorDestinationSdpNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationSdpNumber.setStatus("current")


class _TnMirrorDestinationAdminStatus_Type(ServiceAdminStatus):
    """Custom type tnMirrorDestinationAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_TnMirrorDestinationAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TnMirrorDestinationAdminStatus_Object = MibTableColumn
tnMirrorDestinationAdminStatus = _TnMirrorDestinationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 10),
    _TnMirrorDestinationAdminStatus_Type()
)
tnMirrorDestinationAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationAdminStatus.setStatus("current")
_TnMirrorDestinationOperStatus_Type = ServiceOperStatus
_TnMirrorDestinationOperStatus_Object = MibTableColumn
tnMirrorDestinationOperStatus = _TnMirrorDestinationOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 11),
    _TnMirrorDestinationOperStatus_Type()
)
tnMirrorDestinationOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorDestinationOperStatus.setStatus("current")


class _TnMirrorDestinationSliceSize_Type(Unsigned32):
    """Custom type tnMirrorDestinationSliceSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 9216),
    )


_TnMirrorDestinationSliceSize_Type.__name__ = "Unsigned32"
_TnMirrorDestinationSliceSize_Object = MibTableColumn
tnMirrorDestinationSliceSize = _TnMirrorDestinationSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 13),
    _TnMirrorDestinationSliceSize_Type()
)
tnMirrorDestinationSliceSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationSliceSize.setStatus("current")


class _TnMirrorDestinationSdpEgrSvcLabel_Type(TMplsLabel):
    """Custom type tnMirrorDestinationSdpEgrSvcLabel based on TMplsLabel"""
    defaultValue = 0

    subtypeSpec = TMplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_TnMirrorDestinationSdpEgrSvcLabel_Type.__name__ = "TMplsLabel"
_TnMirrorDestinationSdpEgrSvcLabel_Object = MibTableColumn
tnMirrorDestinationSdpEgrSvcLabel = _TnMirrorDestinationSdpEgrSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 18),
    _TnMirrorDestinationSdpEgrSvcLabel_Type()
)
tnMirrorDestinationSdpEgrSvcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationSdpEgrSvcLabel.setStatus("current")


class _TnMirrorDestinationSapEgressQosPolicyId_Type(TPolicyID):
    """Custom type tnMirrorDestinationSapEgressQosPolicyId based on TPolicyID"""
    defaultValue = 1


_TnMirrorDestinationSapEgressQosPolicyId_Type.__name__ = "TPolicyID"
_TnMirrorDestinationSapEgressQosPolicyId_Object = MibTableColumn
tnMirrorDestinationSapEgressQosPolicyId = _TnMirrorDestinationSapEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 19),
    _TnMirrorDestinationSapEgressQosPolicyId_Type()
)
tnMirrorDestinationSapEgressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationSapEgressQosPolicyId.setStatus("current")


class _TnMirrorDestinationEncapsulation_Type(TmnxMirrorEncapType):
    """Custom type tnMirrorDestinationEncapsulation based on TmnxMirrorEncapType"""
    defaultValue = 1


_TnMirrorDestinationEncapsulation_Type.__name__ = "TmnxMirrorEncapType"
_TnMirrorDestinationEncapsulation_Object = MibTableColumn
tnMirrorDestinationEncapsulation = _TnMirrorDestinationEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 20),
    _TnMirrorDestinationEncapsulation_Type()
)
tnMirrorDestinationEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationEncapsulation.setStatus("current")
_TnMirrorDestinationSdpOperEgrSvcLabel_Type = TMplsLabel
_TnMirrorDestinationSdpOperEgrSvcLabel_Object = MibTableColumn
tnMirrorDestinationSdpOperEgrSvcLabel = _TnMirrorDestinationSdpOperEgrSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 21),
    _TnMirrorDestinationSdpOperEgrSvcLabel_Type()
)
tnMirrorDestinationSdpOperEgrSvcLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorDestinationSdpOperEgrSvcLabel.setStatus("current")


class _TnMirrorDestinationEnablePortId_Type(TruthValue):
    """Custom type tnMirrorDestinationEnablePortId based on TruthValue"""
    defaultValue = 2


_TnMirrorDestinationEnablePortId_Type.__name__ = "TruthValue"
_TnMirrorDestinationEnablePortId_Object = MibTableColumn
tnMirrorDestinationEnablePortId = _TnMirrorDestinationEnablePortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 22),
    _TnMirrorDestinationEnablePortId_Type()
)
tnMirrorDestinationEnablePortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationEnablePortId.setStatus("current")


class _TnMirrorDestSapEgrIpMirrorSA_Type(MacAddress):
    """Custom type tnMirrorDestSapEgrIpMirrorSA based on MacAddress"""
    defaultHexValue = "000000000000"


_TnMirrorDestSapEgrIpMirrorSA_Type.__name__ = "MacAddress"
_TnMirrorDestSapEgrIpMirrorSA_Object = MibTableColumn
tnMirrorDestSapEgrIpMirrorSA = _TnMirrorDestSapEgrIpMirrorSA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 23),
    _TnMirrorDestSapEgrIpMirrorSA_Type()
)
tnMirrorDestSapEgrIpMirrorSA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestSapEgrIpMirrorSA.setStatus("current")


class _TnMirrorDestSapEgrIpMirrorDA_Type(MacAddress):
    """Custom type tnMirrorDestSapEgrIpMirrorDA based on MacAddress"""
    defaultHexValue = "000000000000"


_TnMirrorDestSapEgrIpMirrorDA_Type.__name__ = "MacAddress"
_TnMirrorDestSapEgrIpMirrorDA_Object = MibTableColumn
tnMirrorDestSapEgrIpMirrorDA = _TnMirrorDestSapEgrIpMirrorDA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 24),
    _TnMirrorDestSapEgrIpMirrorDA_Type()
)
tnMirrorDestSapEgrIpMirrorDA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestSapEgrIpMirrorDA.setStatus("current")
_TnMirrorDestLastChanged_Type = TimeStamp
_TnMirrorDestLastChanged_Object = MibTableColumn
tnMirrorDestLastChanged = _TnMirrorDestLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 1, 1, 25),
    _TnMirrorDestLastChanged_Type()
)
tnMirrorDestLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorDestLastChanged.setStatus("current")
_TnMirrorDestinationScalar1_Type = Unsigned32
_TnMirrorDestinationScalar1_Object = MibScalar
tnMirrorDestinationScalar1 = _TnMirrorDestinationScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 101),
    _TnMirrorDestinationScalar1_Type()
)
tnMirrorDestinationScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorDestinationScalar1.setStatus("current")
_TnMirrorDestinationScalar2_Type = Unsigned32
_TnMirrorDestinationScalar2_Object = MibScalar
tnMirrorDestinationScalar2 = _TnMirrorDestinationScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 1, 102),
    _TnMirrorDestinationScalar2_Type()
)
tnMirrorDestinationScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorDestinationScalar2.setStatus("current")
_TnMirrorSourceObjects_ObjectIdentity = ObjectIdentity
tnMirrorSourceObjects = _TnMirrorSourceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2)
)
_TnMirrorSourceTable_Object = MibTable
tnMirrorSourceTable = _TnMirrorSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    tnMirrorSourceTable.setStatus("current")
_TnMirrorSourceEntry_Object = MibTableRow
tnMirrorSourceEntry = _TnMirrorSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 1, 1)
)
tnMirrorSourceEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MIRROR-MIB", "tnMirrorSourceIndex"),
)
if mibBuilder.loadTexts:
    tnMirrorSourceEntry.setStatus("current")
_TnMirrorSourceIndex_Type = TmnxServId
_TnMirrorSourceIndex_Object = MibTableColumn
tnMirrorSourceIndex = _TnMirrorSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 1, 1, 1),
    _TnMirrorSourceIndex_Type()
)
tnMirrorSourceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tnMirrorSourceIndex.setStatus("current")


class _TnMirrorSourceAdminStatus_Type(ServiceAdminStatus):
    """Custom type tnMirrorSourceAdminStatus based on ServiceAdminStatus"""
    defaultValue = 1


_TnMirrorSourceAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TnMirrorSourceAdminStatus_Object = MibTableColumn
tnMirrorSourceAdminStatus = _TnMirrorSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 1, 1, 2),
    _TnMirrorSourceAdminStatus_Type()
)
tnMirrorSourceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorSourceAdminStatus.setStatus("current")
_TnMirrorSourceRowStatus_Type = RowStatus
_TnMirrorSourceRowStatus_Object = MibTableColumn
tnMirrorSourceRowStatus = _TnMirrorSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 1, 1, 3),
    _TnMirrorSourceRowStatus_Type()
)
tnMirrorSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorSourceRowStatus.setStatus("current")
_TnMirrorSourceLastChgd_Type = TimeStamp
_TnMirrorSourceLastChgd_Object = MibTableColumn
tnMirrorSourceLastChgd = _TnMirrorSourceLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 1, 1, 4),
    _TnMirrorSourceLastChgd_Type()
)
tnMirrorSourceLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorSourceLastChgd.setStatus("current")
_TnMirrorSourcePortTable_Object = MibTable
tnMirrorSourcePortTable = _TnMirrorSourcePortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    tnMirrorSourcePortTable.setStatus("current")
_TnMirrorSourcePortEntry_Object = MibTableRow
tnMirrorSourcePortEntry = _TnMirrorSourcePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5, 1)
)
tnMirrorSourcePortEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MIRROR-MIB", "tnMirrorSourceIndex"),
    (0, "TN-MIRROR-MIB", "tnMirrorSourcePortIndex"),
)
if mibBuilder.loadTexts:
    tnMirrorSourcePortEntry.setStatus("current")
_TnMirrorSourcePortIndex_Type = TmnxPortID
_TnMirrorSourcePortIndex_Object = MibTableColumn
tnMirrorSourcePortIndex = _TnMirrorSourcePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5, 1, 1),
    _TnMirrorSourcePortIndex_Type()
)
tnMirrorSourcePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMirrorSourcePortIndex.setStatus("current")
_TnMirrorSourcePortRowStatus_Type = RowStatus
_TnMirrorSourcePortRowStatus_Object = MibTableColumn
tnMirrorSourcePortRowStatus = _TnMirrorSourcePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5, 1, 2),
    _TnMirrorSourcePortRowStatus_Type()
)
tnMirrorSourcePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorSourcePortRowStatus.setStatus("current")


class _TnMirrorSourcePortEgressEnabled_Type(TruthValue):
    """Custom type tnMirrorSourcePortEgressEnabled based on TruthValue"""
    defaultValue = 2


_TnMirrorSourcePortEgressEnabled_Type.__name__ = "TruthValue"
_TnMirrorSourcePortEgressEnabled_Object = MibTableColumn
tnMirrorSourcePortEgressEnabled = _TnMirrorSourcePortEgressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5, 1, 3),
    _TnMirrorSourcePortEgressEnabled_Type()
)
tnMirrorSourcePortEgressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorSourcePortEgressEnabled.setStatus("current")


class _TnMirrorSourcePortIngressEnabled_Type(TruthValue):
    """Custom type tnMirrorSourcePortIngressEnabled based on TruthValue"""
    defaultValue = 2


_TnMirrorSourcePortIngressEnabled_Type.__name__ = "TruthValue"
_TnMirrorSourcePortIngressEnabled_Object = MibTableColumn
tnMirrorSourcePortIngressEnabled = _TnMirrorSourcePortIngressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5, 1, 4),
    _TnMirrorSourcePortIngressEnabled_Type()
)
tnMirrorSourcePortIngressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorSourcePortIngressEnabled.setStatus("current")
_TnMirrorSourcePortLastChgd_Type = TimeStamp
_TnMirrorSourcePortLastChgd_Object = MibTableColumn
tnMirrorSourcePortLastChgd = _TnMirrorSourcePortLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 18, 2, 5, 1, 5),
    _TnMirrorSourcePortLastChgd_Type()
)
tnMirrorSourcePortLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirrorSourcePortLastChgd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MIRROR-MIB",
    **{"TMplsLabel": TMplsLabel,
       "TEtherType": TEtherType,
       "TSessionId": TSessionId,
       "TmnxMirrorEncapType": TmnxMirrorEncapType,
       "tnMirrorMIBModule": tnMirrorMIBModule,
       "tnMirrorObjects": tnMirrorObjects,
       "tnMirrorDestinationObjects": tnMirrorDestinationObjects,
       "tnMirrorDestinationTable": tnMirrorDestinationTable,
       "tnMirrorDestinationEntry": tnMirrorDestinationEntry,
       "tnMirrorDestinationIndex": tnMirrorDestinationIndex,
       "tnMirrorDestinationRowStatus": tnMirrorDestinationRowStatus,
       "tnMirrorDestinationDescription": tnMirrorDestinationDescription,
       "tnMirrorDestinationFC": tnMirrorDestinationFC,
       "tnMirrorDestinationRemoteSource": tnMirrorDestinationRemoteSource,
       "tnMirrorDestinationSapPortId": tnMirrorDestinationSapPortId,
       "tnMirrorDestinationSapEncapValue": tnMirrorDestinationSapEncapValue,
       "tnMirrorDestinationSdpNumber": tnMirrorDestinationSdpNumber,
       "tnMirrorDestinationAdminStatus": tnMirrorDestinationAdminStatus,
       "tnMirrorDestinationOperStatus": tnMirrorDestinationOperStatus,
       "tnMirrorDestinationSliceSize": tnMirrorDestinationSliceSize,
       "tnMirrorDestinationSdpEgrSvcLabel": tnMirrorDestinationSdpEgrSvcLabel,
       "tnMirrorDestinationSapEgressQosPolicyId": tnMirrorDestinationSapEgressQosPolicyId,
       "tnMirrorDestinationEncapsulation": tnMirrorDestinationEncapsulation,
       "tnMirrorDestinationSdpOperEgrSvcLabel": tnMirrorDestinationSdpOperEgrSvcLabel,
       "tnMirrorDestinationEnablePortId": tnMirrorDestinationEnablePortId,
       "tnMirrorDestSapEgrIpMirrorSA": tnMirrorDestSapEgrIpMirrorSA,
       "tnMirrorDestSapEgrIpMirrorDA": tnMirrorDestSapEgrIpMirrorDA,
       "tnMirrorDestLastChanged": tnMirrorDestLastChanged,
       "tnMirrorDestinationScalar1": tnMirrorDestinationScalar1,
       "tnMirrorDestinationScalar2": tnMirrorDestinationScalar2,
       "tnMirrorSourceObjects": tnMirrorSourceObjects,
       "tnMirrorSourceTable": tnMirrorSourceTable,
       "tnMirrorSourceEntry": tnMirrorSourceEntry,
       "tnMirrorSourceIndex": tnMirrorSourceIndex,
       "tnMirrorSourceAdminStatus": tnMirrorSourceAdminStatus,
       "tnMirrorSourceRowStatus": tnMirrorSourceRowStatus,
       "tnMirrorSourceLastChgd": tnMirrorSourceLastChgd,
       "tnMirrorSourcePortTable": tnMirrorSourcePortTable,
       "tnMirrorSourcePortEntry": tnMirrorSourcePortEntry,
       "tnMirrorSourcePortIndex": tnMirrorSourcePortIndex,
       "tnMirrorSourcePortRowStatus": tnMirrorSourcePortRowStatus,
       "tnMirrorSourcePortEgressEnabled": tnMirrorSourcePortEgressEnabled,
       "tnMirrorSourcePortIngressEnabled": tnMirrorSourcePortIngressEnabled,
       "tnMirrorSourcePortLastChgd": tnMirrorSourcePortLastChgd}
)
