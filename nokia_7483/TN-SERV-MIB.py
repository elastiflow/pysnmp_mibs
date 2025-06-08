# SNMP MIB module (TN-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-SERV-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:37 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(ServObjDesc,
 ServiceAdminStatus,
 ServiceOperStatus,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "ServObjDesc",
    "ServiceAdminStatus",
    "ServiceOperStatus",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrIDOrZero")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnServicesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tnServicesMIBModule.setRevisions(
        ("1912-12-13 00:00",
         "1912-12-05 00:00",
         "1912-09-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-02-28 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServObjName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ServObjLongDesc(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )



class ServType(TextualConvention, Integer32):
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("epipe", 1),
          ("p3pipe", 2),
          ("tls", 3),
          ("vprn", 4),
          ("ies", 5),
          ("mirror", 6),
          ("apipe", 7),
          ("fpipe", 8),
          ("ipipe", 9),
          ("cpipe", 10))
    )



class VpnId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class SdpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 17407),
    )



class SdpTemplateId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class PWTemplateId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class TlsBpduTranslation(TextualConvention, Integer32):
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
        *(("auto", 1),
          ("disabled", 2),
          ("pvst", 3),
          ("stp", 4),
          ("pvst-rw", 5),
          ("auto-rw", 6))
    )



class TlsLimitMacMoveLevel(TextualConvention, Integer32):
    status = "current"
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
          ("tertiary", 3))
    )



class TlsLimitMacMove(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockable", 1),
          ("nonBlockable", 2))
    )



class SdpBindVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("undef", 1),
          ("ether", 2),
          ("vlan", 4),
          ("mirror", 5),
          ("atmSdu", 6),
          ("atmCell", 7),
          ("atmVcc", 8),
          ("atmVpc", 9),
          ("frDlci", 10),
          ("ipipe", 11),
          ("satopE1", 12),
          ("satopT1", 13),
          ("satopE3", 14),
          ("satopT3", 15),
          ("cesopsn", 16),
          ("cesopsnCas", 17))
    )



class StpExceptionCondition(TextualConvention, Integer32):
    status = "current"
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
          ("oneWayCommuniation", 2),
          ("downstreamLoopDetected", 3))
    )



class LspIdList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )



class BridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TSapIngQueueId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class TSapEgrQueueId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TStpPortState(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("discarding", 7))
    )



class StpPortRole(TextualConvention, Integer32):
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
        *(("master", 0),
          ("root", 1),
          ("designated", 2),
          ("alternate", 3),
          ("backup", 4),
          ("disabled", 5))
    )



class StpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("stp", 1),
          ("rstp", 2),
          ("mstp", 3))
    )



class MfibLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )



class MfibGrpSrcFwdOrBlk(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )



class MvplsPruneState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("notPruned", 2),
          ("pruned", 3))
    )



class TQosQueueAttribute(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cbs", 0),
          ("cir", 1),
          ("cirAdaptRule", 2),
          ("mbs", 3),
          ("pir", 4),
          ("pirAdaptRule", 5),
          ("hiPrioOnly", 6),
          ("avgOverhead", 7))
    )


class TVirtSchedAttribute(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cir", 0),
          ("pir", 1),
          ("summedCir", 2))
    )


class MstiInstanceId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class MstiInstanceIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class DhcpLseStateInfoOrigin(TextualConvention, Integer32):
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
        *(("none", 0),
          ("dhcp", 1),
          ("radius", 2),
          ("retailerRadius", 3),
          ("retailerDhcp", 4),
          ("default", 5))
    )



class IAIDType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("temporary", 1),
          ("non-temporary", 2),
          ("prefix", 3))
    )



class TdmOptionsSigPkts(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSigPkts", 0),
          ("dataPkts", 1),
          ("sigPkts", 2),
          ("dataAndSigPkts", 3))
    )



class TdmOptionsCasTrunkFraming(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCas", 0),
          ("e1Trunk", 1),
          ("t1EsfTrunk", 2),
          ("t1SfTrunk", 3))
    )



class CemSapReportAlarm(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("strayPkts", 1),
          ("malformedPkts", 2),
          ("pktLoss", 3),
          ("bfrOverrun", 4),
          ("bfrUnderrun", 5),
          ("rmtPktLoss", 6),
          ("rmtFault", 7),
          ("rmtRdi", 8))
    )


class CemSapEcid(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class SdpBFHundredthsOfPercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )



class SdpBindBandwidth(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class L2ptProtocols(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("stp", 0),
          ("cdp", 1),
          ("vtp", 2),
          ("dtp", 3),
          ("pagp", 4),
          ("udld", 5))
    )


class SvcISID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777215),
    )



class L2RouteOrigin(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("bgp-l2vpn", 2),
          ("radius", 3))
    )



class ConfigStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("modified", 2),
          ("deleted", 3))
    )



class ServAccessLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("spoke", 2))
    )



class ServShcvOperState(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 1),
          ("undefined", 2),
          ("down", 3),
          ("up", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnServObjs_ObjectIdentity = ObjectIdentity
tnServObjs = _TnServObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4)
)
_TnCustObjs_ObjectIdentity = ObjectIdentity
tnCustObjs = _TnCustObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1)
)
_TnCustNumEntries_Type = Integer32
_TnCustNumEntries_Object = MibScalar
tnCustNumEntries = _TnCustNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 1),
    _TnCustNumEntries_Type()
)
tnCustNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCustNumEntries.setStatus("current")
_TnCustNextFreeId_Type = TmnxCustId
_TnCustNextFreeId_Object = MibScalar
tnCustNextFreeId = _TnCustNextFreeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 2),
    _TnCustNextFreeId_Type()
)
tnCustNextFreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCustNextFreeId.setStatus("current")
_TnCustInfoTable_Object = MibTable
tnCustInfoTable = _TnCustInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tnCustInfoTable.setStatus("current")
_TnCustInfoEntry_Object = MibTableRow
tnCustInfoEntry = _TnCustInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1)
)
tnCustInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnCustId"),
)
if mibBuilder.loadTexts:
    tnCustInfoEntry.setStatus("current")
_TnCustId_Type = TmnxCustId
_TnCustId_Object = MibTableColumn
tnCustId = _TnCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1, 1),
    _TnCustId_Type()
)
tnCustId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCustId.setStatus("current")
_TnCustRowStatus_Type = RowStatus
_TnCustRowStatus_Object = MibTableColumn
tnCustRowStatus = _TnCustRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1, 2),
    _TnCustRowStatus_Type()
)
tnCustRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCustRowStatus.setStatus("current")


class _TnCustDescription_Type(ServObjDesc):
    """Custom type tnCustDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_TnCustDescription_Type.__name__ = "ServObjDesc"
_TnCustDescription_Object = MibTableColumn
tnCustDescription = _TnCustDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1, 3),
    _TnCustDescription_Type()
)
tnCustDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCustDescription.setStatus("current")


class _TnCustContact_Type(ServObjDesc):
    """Custom type tnCustContact based on ServObjDesc"""
    defaultValue = OctetString("")


_TnCustContact_Type.__name__ = "ServObjDesc"
_TnCustContact_Object = MibTableColumn
tnCustContact = _TnCustContact_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1, 4),
    _TnCustContact_Type()
)
tnCustContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCustContact.setStatus("current")


class _TnCustPhone_Type(ServObjDesc):
    """Custom type tnCustPhone based on ServObjDesc"""
    defaultValue = OctetString("")


_TnCustPhone_Type.__name__ = "ServObjDesc"
_TnCustPhone_Object = MibTableColumn
tnCustPhone = _TnCustPhone_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1, 5),
    _TnCustPhone_Type()
)
tnCustPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCustPhone.setStatus("current")
_TnCustLastMgmtChange_Type = TimeStamp
_TnCustLastMgmtChange_Object = MibTableColumn
tnCustLastMgmtChange = _TnCustLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 1, 3, 1, 6),
    _TnCustLastMgmtChange_Type()
)
tnCustLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCustLastMgmtChange.setStatus("current")
_TnSvcObjs_ObjectIdentity = ObjectIdentity
tnSvcObjs = _TnSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2)
)
_TnSvcNumEntries_Type = Integer32
_TnSvcNumEntries_Object = MibScalar
tnSvcNumEntries = _TnSvcNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 1),
    _TnSvcNumEntries_Type()
)
tnSvcNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcNumEntries.setStatus("current")
_TnSvcBaseInfoTable_Object = MibTable
tnSvcBaseInfoTable = _TnSvcBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    tnSvcBaseInfoTable.setStatus("current")
_TnSvcBaseInfoEntry_Object = MibTableRow
tnSvcBaseInfoEntry = _TnSvcBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1)
)
tnSvcBaseInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnSvcBaseInfoEntry.setStatus("current")
_TnSvcId_Type = TmnxServId
_TnSvcId_Object = MibTableColumn
tnSvcId = _TnSvcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 1),
    _TnSvcId_Type()
)
tnSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSvcId.setStatus("current")
_TnSvcRowStatus_Type = RowStatus
_TnSvcRowStatus_Object = MibTableColumn
tnSvcRowStatus = _TnSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 2),
    _TnSvcRowStatus_Type()
)
tnSvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcRowStatus.setStatus("current")
_TnSvcType_Type = ServType
_TnSvcType_Object = MibTableColumn
tnSvcType = _TnSvcType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 3),
    _TnSvcType_Type()
)
tnSvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcType.setStatus("current")
_TnSvcCustId_Type = TmnxCustId
_TnSvcCustId_Object = MibTableColumn
tnSvcCustId = _TnSvcCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 4),
    _TnSvcCustId_Type()
)
tnSvcCustId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcCustId.setStatus("current")
_TnSvcIpRouting_Type = TmnxEnabledDisabled
_TnSvcIpRouting_Object = MibTableColumn
tnSvcIpRouting = _TnSvcIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 5),
    _TnSvcIpRouting_Type()
)
tnSvcIpRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcIpRouting.setStatus("current")


class _TnSvcDescription_Type(ServObjDesc):
    """Custom type tnSvcDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_TnSvcDescription_Type.__name__ = "ServObjDesc"
_TnSvcDescription_Object = MibTableColumn
tnSvcDescription = _TnSvcDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 6),
    _TnSvcDescription_Type()
)
tnSvcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcDescription.setStatus("current")


class _TnSvcMtu_Type(Integer32):
    """Custom type tnSvcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9194),
    )


_TnSvcMtu_Type.__name__ = "Integer32"
_TnSvcMtu_Object = MibTableColumn
tnSvcMtu = _TnSvcMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 7),
    _TnSvcMtu_Type()
)
tnSvcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcMtu.setStatus("current")


class _TnSvcAdminStatus_Type(ServiceAdminStatus):
    """Custom type tnSvcAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_TnSvcAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TnSvcAdminStatus_Object = MibTableColumn
tnSvcAdminStatus = _TnSvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 8),
    _TnSvcAdminStatus_Type()
)
tnSvcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcAdminStatus.setStatus("current")
_TnSvcOperStatus_Type = ServiceOperStatus
_TnSvcOperStatus_Object = MibTableColumn
tnSvcOperStatus = _TnSvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 9),
    _TnSvcOperStatus_Type()
)
tnSvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcOperStatus.setStatus("current")
_TnSvcNumSaps_Type = Integer32
_TnSvcNumSaps_Object = MibTableColumn
tnSvcNumSaps = _TnSvcNumSaps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 10),
    _TnSvcNumSaps_Type()
)
tnSvcNumSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcNumSaps.setStatus("current")
_TnSvcNumSdps_Type = Integer32
_TnSvcNumSdps_Object = MibTableColumn
tnSvcNumSdps = _TnSvcNumSdps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 11),
    _TnSvcNumSdps_Type()
)
tnSvcNumSdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcNumSdps.setStatus("current")
_TnSvcLastMgmtChange_Type = TimeStamp
_TnSvcLastMgmtChange_Object = MibTableColumn
tnSvcLastMgmtChange = _TnSvcLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 12),
    _TnSvcLastMgmtChange_Type()
)
tnSvcLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcLastMgmtChange.setStatus("current")
_TnSvcDefMeshVcId_Type = Unsigned32
_TnSvcDefMeshVcId_Object = MibTableColumn
tnSvcDefMeshVcId = _TnSvcDefMeshVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 13),
    _TnSvcDefMeshVcId_Type()
)
tnSvcDefMeshVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcDefMeshVcId.setStatus("current")


class _TnSvcVpnId_Type(VpnId):
    """Custom type tnSvcVpnId based on VpnId"""
    defaultValue = 0


_TnSvcVpnId_Type.__name__ = "VpnId"
_TnSvcVpnId_Object = MibTableColumn
tnSvcVpnId = _TnSvcVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 14),
    _TnSvcVpnId_Type()
)
tnSvcVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcVpnId.setStatus("current")


class _TnSvcVRouterId_Type(TmnxVRtrIDOrZero):
    """Custom type tnSvcVRouterId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TnSvcVRouterId_Type.__name__ = "TmnxVRtrIDOrZero"
_TnSvcVRouterId_Object = MibTableColumn
tnSvcVRouterId = _TnSvcVRouterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 15),
    _TnSvcVRouterId_Type()
)
tnSvcVRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcVRouterId.setStatus("current")


class _TnSvcAutoBind_Type(Integer32):
    """Custom type tnSvcAutoBind based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("gre", 2),
          ("ldp", 3),
          ("rsvp-te", 4),
          ("mpls", 5))
    )


_TnSvcAutoBind_Type.__name__ = "Integer32"
_TnSvcAutoBind_Object = MibTableColumn
tnSvcAutoBind = _TnSvcAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 16),
    _TnSvcAutoBind_Type()
)
tnSvcAutoBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcAutoBind.setStatus("current")
_TnSvcLastStatusChange_Type = TimeStamp
_TnSvcLastStatusChange_Object = MibTableColumn
tnSvcLastStatusChange = _TnSvcLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 17),
    _TnSvcLastStatusChange_Type()
)
tnSvcLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcLastStatusChange.setStatus("current")


class _TnSvcVllType_Type(Integer32):
    """Custom type tnSvcVllType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              9,
              10,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("undef", 1),
          ("atmSdu", 6),
          ("atmCell", 7),
          ("atmVcc", 8),
          ("atmVpc", 9),
          ("frDlci", 10),
          ("satopE1", 12),
          ("satopT1", 13),
          ("satopE3", 14),
          ("satopT3", 15),
          ("cesopsn", 16),
          ("cesopsnCas", 17))
    )


_TnSvcVllType_Type.__name__ = "Integer32"
_TnSvcVllType_Object = MibTableColumn
tnSvcVllType = _TnSvcVllType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 18),
    _TnSvcVllType_Type()
)
tnSvcVllType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcVllType.setStatus("current")


class _TnSvcMgmtVpls_Type(TruthValue):
    """Custom type tnSvcMgmtVpls based on TruthValue"""
    defaultValue = 2


_TnSvcMgmtVpls_Type.__name__ = "TruthValue"
_TnSvcMgmtVpls_Object = MibTableColumn
tnSvcMgmtVpls = _TnSvcMgmtVpls_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 19),
    _TnSvcMgmtVpls_Type()
)
tnSvcMgmtVpls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcMgmtVpls.setStatus("current")


class _TnSvcRadiusDiscovery_Type(TruthValue):
    """Custom type tnSvcRadiusDiscovery based on TruthValue"""
    defaultValue = 2


_TnSvcRadiusDiscovery_Type.__name__ = "TruthValue"
_TnSvcRadiusDiscovery_Object = MibTableColumn
tnSvcRadiusDiscovery = _TnSvcRadiusDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 20),
    _TnSvcRadiusDiscovery_Type()
)
tnSvcRadiusDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcRadiusDiscovery.setStatus("current")


class _TnSvcRadiusUserNameType_Type(Integer32):
    """Custom type tnSvcRadiusUserNameType based on Integer32"""
    defaultValue = 0

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
          ("vpn-id", 1),
          ("router-distinguisher", 2))
    )


_TnSvcRadiusUserNameType_Type.__name__ = "Integer32"
_TnSvcRadiusUserNameType_Object = MibTableColumn
tnSvcRadiusUserNameType = _TnSvcRadiusUserNameType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 21),
    _TnSvcRadiusUserNameType_Type()
)
tnSvcRadiusUserNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcRadiusUserNameType.setStatus("current")


class _TnSvcRadiusUserName_Type(DisplayString):
    """Custom type tnSvcRadiusUserName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSvcRadiusUserName_Type.__name__ = "DisplayString"
_TnSvcRadiusUserName_Object = MibTableColumn
tnSvcRadiusUserName = _TnSvcRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 22),
    _TnSvcRadiusUserName_Type()
)
tnSvcRadiusUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcRadiusUserName.setStatus("current")


class _TnSvcVcSwitching_Type(TruthValue):
    """Custom type tnSvcVcSwitching based on TruthValue"""
    defaultValue = 2


_TnSvcVcSwitching_Type.__name__ = "TruthValue"
_TnSvcVcSwitching_Object = MibTableColumn
tnSvcVcSwitching = _TnSvcVcSwitching_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 23),
    _TnSvcVcSwitching_Type()
)
tnSvcVcSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcVcSwitching.setStatus("current")


class _TnSvcRadiusPEDiscPolicy_Type(TNamedItemOrEmpty):
    """Custom type tnSvcRadiusPEDiscPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnSvcRadiusPEDiscPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TnSvcRadiusPEDiscPolicy_Object = MibTableColumn
tnSvcRadiusPEDiscPolicy = _TnSvcRadiusPEDiscPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 24),
    _TnSvcRadiusPEDiscPolicy_Type()
)
tnSvcRadiusPEDiscPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcRadiusPEDiscPolicy.setStatus("current")


class _TnSvcRadiusDiscoveryShutdown_Type(ServiceAdminStatus):
    """Custom type tnSvcRadiusDiscoveryShutdown based on ServiceAdminStatus"""
    defaultValue = 2


_TnSvcRadiusDiscoveryShutdown_Type.__name__ = "ServiceAdminStatus"
_TnSvcRadiusDiscoveryShutdown_Object = MibTableColumn
tnSvcRadiusDiscoveryShutdown = _TnSvcRadiusDiscoveryShutdown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 25),
    _TnSvcRadiusDiscoveryShutdown_Type()
)
tnSvcRadiusDiscoveryShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcRadiusDiscoveryShutdown.setStatus("current")


class _TnSvcVplsType_Type(Integer32):
    """Custom type tnSvcVplsType based on Integer32"""
    defaultValue = 1

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
          ("bVpls", 2),
          ("iVpls", 3))
    )


_TnSvcVplsType_Type.__name__ = "Integer32"
_TnSvcVplsType_Object = MibTableColumn
tnSvcVplsType = _TnSvcVplsType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 26),
    _TnSvcVplsType_Type()
)
tnSvcVplsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcVplsType.setStatus("current")
_TnSvcNumMcStandbySaps_Type = Integer32
_TnSvcNumMcStandbySaps_Object = MibTableColumn
tnSvcNumMcStandbySaps = _TnSvcNumMcStandbySaps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 27),
    _TnSvcNumMcStandbySaps_Type()
)
tnSvcNumMcStandbySaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcNumMcStandbySaps.setStatus("current")


class _TnSvcName_Type(TNamedItemOrEmpty):
    """Custom type tnSvcName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSvcName_Type.__name__ = "TNamedItemOrEmpty"
_TnSvcName_Object = MibTableColumn
tnSvcName = _TnSvcName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 2, 1, 28),
    _TnSvcName_Type()
)
tnSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcName.setStatus("current")
_TnSvcTlsInfoTable_Object = MibTable
tnSvcTlsInfoTable = _TnSvcTlsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    tnSvcTlsInfoTable.setStatus("current")
_TnSvcTlsInfoEntry_Object = MibTableRow
tnSvcTlsInfoEntry = _TnSvcTlsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1)
)
tnSvcTlsInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnSvcTlsInfoEntry.setStatus("current")


class _TnSvcTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsMacLearning based on TmnxEnabledDisabled"""
    defaultValue = 1


_TnSvcTlsMacLearning_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsMacLearning_Object = MibTableColumn
tnSvcTlsMacLearning = _TnSvcTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 1),
    _TnSvcTlsMacLearning_Type()
)
tnSvcTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacLearning.setStatus("current")


class _TnSvcTlsDiscardUnknownDest_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsDiscardUnknownDest based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsDiscardUnknownDest_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsDiscardUnknownDest_Object = MibTableColumn
tnSvcTlsDiscardUnknownDest = _TnSvcTlsDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 2),
    _TnSvcTlsDiscardUnknownDest_Type()
)
tnSvcTlsDiscardUnknownDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsDiscardUnknownDest.setStatus("current")


class _TnSvcTlsFdbTableSize_Type(Integer32):
    """Custom type tnSvcTlsFdbTableSize based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511999),
    )


_TnSvcTlsFdbTableSize_Type.__name__ = "Integer32"
_TnSvcTlsFdbTableSize_Object = MibTableColumn
tnSvcTlsFdbTableSize = _TnSvcTlsFdbTableSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 3),
    _TnSvcTlsFdbTableSize_Type()
)
tnSvcTlsFdbTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsFdbTableSize.setStatus("current")
_TnSvcTlsFdbNumEntries_Type = Integer32
_TnSvcTlsFdbNumEntries_Object = MibTableColumn
tnSvcTlsFdbNumEntries = _TnSvcTlsFdbNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 4),
    _TnSvcTlsFdbNumEntries_Type()
)
tnSvcTlsFdbNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsFdbNumEntries.setStatus("current")
_TnSvcTlsFdbNumStaticEntries_Type = Integer32
_TnSvcTlsFdbNumStaticEntries_Object = MibTableColumn
tnSvcTlsFdbNumStaticEntries = _TnSvcTlsFdbNumStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 5),
    _TnSvcTlsFdbNumStaticEntries_Type()
)
tnSvcTlsFdbNumStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsFdbNumStaticEntries.setStatus("current")


class _TnSvcTlsFdbLocalAgeTime_Type(Integer32):
    """Custom type tnSvcTlsFdbLocalAgeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TnSvcTlsFdbLocalAgeTime_Type.__name__ = "Integer32"
_TnSvcTlsFdbLocalAgeTime_Object = MibTableColumn
tnSvcTlsFdbLocalAgeTime = _TnSvcTlsFdbLocalAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 6),
    _TnSvcTlsFdbLocalAgeTime_Type()
)
tnSvcTlsFdbLocalAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsFdbLocalAgeTime.setStatus("current")


class _TnSvcTlsFdbRemoteAgeTime_Type(Integer32):
    """Custom type tnSvcTlsFdbRemoteAgeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TnSvcTlsFdbRemoteAgeTime_Type.__name__ = "Integer32"
_TnSvcTlsFdbRemoteAgeTime_Object = MibTableColumn
tnSvcTlsFdbRemoteAgeTime = _TnSvcTlsFdbRemoteAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 7),
    _TnSvcTlsFdbRemoteAgeTime_Type()
)
tnSvcTlsFdbRemoteAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsFdbRemoteAgeTime.setStatus("current")


class _TnSvcTlsStpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsStpAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsStpAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsStpAdminStatus_Object = MibTableColumn
tnSvcTlsStpAdminStatus = _TnSvcTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 8),
    _TnSvcTlsStpAdminStatus_Type()
)
tnSvcTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpAdminStatus.setStatus("current")


class _TnSvcTlsStpPriority_Type(Integer32):
    """Custom type tnSvcTlsStpPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSvcTlsStpPriority_Type.__name__ = "Integer32"
_TnSvcTlsStpPriority_Object = MibTableColumn
tnSvcTlsStpPriority = _TnSvcTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 9),
    _TnSvcTlsStpPriority_Type()
)
tnSvcTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpPriority.setStatus("current")
_TnSvcTlsStpBridgeAddress_Type = MacAddress
_TnSvcTlsStpBridgeAddress_Object = MibTableColumn
tnSvcTlsStpBridgeAddress = _TnSvcTlsStpBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 10),
    _TnSvcTlsStpBridgeAddress_Type()
)
tnSvcTlsStpBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpBridgeAddress.setStatus("current")
_TnSvcTlsStpTimeSinceTopologyChange_Type = TimeTicks
_TnSvcTlsStpTimeSinceTopologyChange_Object = MibTableColumn
tnSvcTlsStpTimeSinceTopologyChange = _TnSvcTlsStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 11),
    _TnSvcTlsStpTimeSinceTopologyChange_Type()
)
tnSvcTlsStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpTimeSinceTopologyChange.setStatus("current")
_TnSvcTlsStpTopologyChanges_Type = Integer32
_TnSvcTlsStpTopologyChanges_Object = MibTableColumn
tnSvcTlsStpTopologyChanges = _TnSvcTlsStpTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 12),
    _TnSvcTlsStpTopologyChanges_Type()
)
tnSvcTlsStpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpTopologyChanges.setStatus("current")
_TnSvcTlsStpDesignatedRoot_Type = BridgeId
_TnSvcTlsStpDesignatedRoot_Object = MibTableColumn
tnSvcTlsStpDesignatedRoot = _TnSvcTlsStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 13),
    _TnSvcTlsStpDesignatedRoot_Type()
)
tnSvcTlsStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpDesignatedRoot.setStatus("current")
_TnSvcTlsStpRootCost_Type = Integer32
_TnSvcTlsStpRootCost_Object = MibTableColumn
tnSvcTlsStpRootCost = _TnSvcTlsStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 14),
    _TnSvcTlsStpRootCost_Type()
)
tnSvcTlsStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpRootCost.setStatus("current")
_TnSvcTlsStpRootPort_Type = Integer32
_TnSvcTlsStpRootPort_Object = MibTableColumn
tnSvcTlsStpRootPort = _TnSvcTlsStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 15),
    _TnSvcTlsStpRootPort_Type()
)
tnSvcTlsStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpRootPort.setStatus("current")
_TnSvcTlsStpMaxAge_Type = Integer32
_TnSvcTlsStpMaxAge_Object = MibTableColumn
tnSvcTlsStpMaxAge = _TnSvcTlsStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 16),
    _TnSvcTlsStpMaxAge_Type()
)
tnSvcTlsStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpMaxAge.setStatus("current")
_TnSvcTlsStpHelloTime_Type = Integer32
_TnSvcTlsStpHelloTime_Object = MibTableColumn
tnSvcTlsStpHelloTime = _TnSvcTlsStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 17),
    _TnSvcTlsStpHelloTime_Type()
)
tnSvcTlsStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpHelloTime.setStatus("current")
_TnSvcTlsStpForwardDelay_Type = Integer32
_TnSvcTlsStpForwardDelay_Object = MibTableColumn
tnSvcTlsStpForwardDelay = _TnSvcTlsStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 19),
    _TnSvcTlsStpForwardDelay_Type()
)
tnSvcTlsStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpForwardDelay.setStatus("current")


class _TnSvcTlsStpBridgeMaxAge_Type(Integer32):
    """Custom type tnSvcTlsStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_TnSvcTlsStpBridgeMaxAge_Type.__name__ = "Integer32"
_TnSvcTlsStpBridgeMaxAge_Object = MibTableColumn
tnSvcTlsStpBridgeMaxAge = _TnSvcTlsStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 20),
    _TnSvcTlsStpBridgeMaxAge_Type()
)
tnSvcTlsStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpBridgeMaxAge.setStatus("current")


class _TnSvcTlsStpBridgeHelloTime_Type(Integer32):
    """Custom type tnSvcTlsStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnSvcTlsStpBridgeHelloTime_Type.__name__ = "Integer32"
_TnSvcTlsStpBridgeHelloTime_Object = MibTableColumn
tnSvcTlsStpBridgeHelloTime = _TnSvcTlsStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 21),
    _TnSvcTlsStpBridgeHelloTime_Type()
)
tnSvcTlsStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpBridgeHelloTime.setStatus("current")


class _TnSvcTlsStpBridgeForwardDelay_Type(Integer32):
    """Custom type tnSvcTlsStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_TnSvcTlsStpBridgeForwardDelay_Type.__name__ = "Integer32"
_TnSvcTlsStpBridgeForwardDelay_Object = MibTableColumn
tnSvcTlsStpBridgeForwardDelay = _TnSvcTlsStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 22),
    _TnSvcTlsStpBridgeForwardDelay_Type()
)
tnSvcTlsStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpBridgeForwardDelay.setStatus("current")


class _TnSvcTlsStpOperStatus_Type(Integer32):
    """Custom type tnSvcTlsStpOperStatus based on Integer32"""
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


_TnSvcTlsStpOperStatus_Type.__name__ = "Integer32"
_TnSvcTlsStpOperStatus_Object = MibTableColumn
tnSvcTlsStpOperStatus = _TnSvcTlsStpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 30),
    _TnSvcTlsStpOperStatus_Type()
)
tnSvcTlsStpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpOperStatus.setStatus("current")


class _TnSvcTlsStpVirtualRootBridgeStatus_Type(Integer32):
    """Custom type tnSvcTlsStpVirtualRootBridgeStatus based on Integer32"""
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


_TnSvcTlsStpVirtualRootBridgeStatus_Type.__name__ = "Integer32"
_TnSvcTlsStpVirtualRootBridgeStatus_Object = MibTableColumn
tnSvcTlsStpVirtualRootBridgeStatus = _TnSvcTlsStpVirtualRootBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 31),
    _TnSvcTlsStpVirtualRootBridgeStatus_Type()
)
tnSvcTlsStpVirtualRootBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpVirtualRootBridgeStatus.setStatus("current")


class _TnSvcTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsMacAgeing based on TmnxEnabledDisabled"""
    defaultValue = 1


_TnSvcTlsMacAgeing_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsMacAgeing_Object = MibTableColumn
tnSvcTlsMacAgeing = _TnSvcTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 32),
    _TnSvcTlsMacAgeing_Type()
)
tnSvcTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacAgeing.setStatus("current")
_TnSvcTlsStpTopologyChangeActive_Type = TruthValue
_TnSvcTlsStpTopologyChangeActive_Object = MibTableColumn
tnSvcTlsStpTopologyChangeActive = _TnSvcTlsStpTopologyChangeActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 33),
    _TnSvcTlsStpTopologyChangeActive_Type()
)
tnSvcTlsStpTopologyChangeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpTopologyChangeActive.setStatus("current")


class _TnSvcTlsFdbTableFullHighWatermark_Type(Integer32):
    """Custom type tnSvcTlsFdbTableFullHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsFdbTableFullHighWatermark_Type.__name__ = "Integer32"
_TnSvcTlsFdbTableFullHighWatermark_Object = MibTableColumn
tnSvcTlsFdbTableFullHighWatermark = _TnSvcTlsFdbTableFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 34),
    _TnSvcTlsFdbTableFullHighWatermark_Type()
)
tnSvcTlsFdbTableFullHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsFdbTableFullHighWatermark.setStatus("current")


class _TnSvcTlsFdbTableFullLowWatermark_Type(Integer32):
    """Custom type tnSvcTlsFdbTableFullLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsFdbTableFullLowWatermark_Type.__name__ = "Integer32"
_TnSvcTlsFdbTableFullLowWatermark_Object = MibTableColumn
tnSvcTlsFdbTableFullLowWatermark = _TnSvcTlsFdbTableFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 35),
    _TnSvcTlsFdbTableFullLowWatermark_Type()
)
tnSvcTlsFdbTableFullLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsFdbTableFullLowWatermark.setStatus("current")
_TnSvcTlsVpnId_Type = VpnId
_TnSvcTlsVpnId_Object = MibTableColumn
tnSvcTlsVpnId = _TnSvcTlsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 36),
    _TnSvcTlsVpnId_Type()
)
tnSvcTlsVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsVpnId.setStatus("current")
_TnSvcTlsCustId_Type = TmnxCustId
_TnSvcTlsCustId_Object = MibTableColumn
tnSvcTlsCustId = _TnSvcTlsCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 37),
    _TnSvcTlsCustId_Type()
)
tnSvcTlsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsCustId.setStatus("current")


class _TnSvcTlsStpVersion_Type(Integer32):
    """Custom type tnSvcTlsStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("compDot1w", 3),
          ("dot1w", 4),
          ("mstp", 5),
          ("pmstp", 6))
    )


_TnSvcTlsStpVersion_Type.__name__ = "Integer32"
_TnSvcTlsStpVersion_Object = MibTableColumn
tnSvcTlsStpVersion = _TnSvcTlsStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 38),
    _TnSvcTlsStpVersion_Type()
)
tnSvcTlsStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpVersion.setStatus("current")


class _TnSvcTlsStpHoldCount_Type(Integer32):
    """Custom type tnSvcTlsStpHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnSvcTlsStpHoldCount_Type.__name__ = "Integer32"
_TnSvcTlsStpHoldCount_Object = MibTableColumn
tnSvcTlsStpHoldCount = _TnSvcTlsStpHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 39),
    _TnSvcTlsStpHoldCount_Type()
)
tnSvcTlsStpHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpHoldCount.setStatus("current")
_TnSvcTlsStpPrimaryBridge_Type = BridgeId
_TnSvcTlsStpPrimaryBridge_Object = MibTableColumn
tnSvcTlsStpPrimaryBridge = _TnSvcTlsStpPrimaryBridge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 40),
    _TnSvcTlsStpPrimaryBridge_Type()
)
tnSvcTlsStpPrimaryBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpPrimaryBridge.setStatus("current")


class _TnSvcTlsStpBridgeInstanceId_Type(Integer32):
    """Custom type tnSvcTlsStpBridgeInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TnSvcTlsStpBridgeInstanceId_Type.__name__ = "Integer32"
_TnSvcTlsStpBridgeInstanceId_Object = MibTableColumn
tnSvcTlsStpBridgeInstanceId = _TnSvcTlsStpBridgeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 41),
    _TnSvcTlsStpBridgeInstanceId_Type()
)
tnSvcTlsStpBridgeInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpBridgeInstanceId.setStatus("current")
_TnSvcTlsStpVcpOperProtocol_Type = StpProtocol
_TnSvcTlsStpVcpOperProtocol_Object = MibTableColumn
tnSvcTlsStpVcpOperProtocol = _TnSvcTlsStpVcpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 42),
    _TnSvcTlsStpVcpOperProtocol_Type()
)
tnSvcTlsStpVcpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpVcpOperProtocol.setStatus("current")


class _TnSvcTlsMacMoveMaxRate_Type(Unsigned32):
    """Custom type tnSvcTlsMacMoveMaxRate based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnSvcTlsMacMoveMaxRate_Type.__name__ = "Unsigned32"
_TnSvcTlsMacMoveMaxRate_Object = MibTableColumn
tnSvcTlsMacMoveMaxRate = _TnSvcTlsMacMoveMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 43),
    _TnSvcTlsMacMoveMaxRate_Type()
)
tnSvcTlsMacMoveMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacMoveMaxRate.setStatus("current")


class _TnSvcTlsMacMoveRetryTimeout_Type(Unsigned32):
    """Custom type tnSvcTlsMacMoveRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TnSvcTlsMacMoveRetryTimeout_Type.__name__ = "Unsigned32"
_TnSvcTlsMacMoveRetryTimeout_Object = MibTableColumn
tnSvcTlsMacMoveRetryTimeout = _TnSvcTlsMacMoveRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 44),
    _TnSvcTlsMacMoveRetryTimeout_Type()
)
tnSvcTlsMacMoveRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacMoveRetryTimeout.setStatus("current")


class _TnSvcTlsMacMoveAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsMacMoveAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsMacMoveAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsMacMoveAdminStatus_Object = MibTableColumn
tnSvcTlsMacMoveAdminStatus = _TnSvcTlsMacMoveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 45),
    _TnSvcTlsMacMoveAdminStatus_Type()
)
tnSvcTlsMacMoveAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacMoveAdminStatus.setStatus("current")
_TnSvcTlsMacRelearnOnly_Type = TruthValue
_TnSvcTlsMacRelearnOnly_Object = MibTableColumn
tnSvcTlsMacRelearnOnly = _TnSvcTlsMacRelearnOnly_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 46),
    _TnSvcTlsMacRelearnOnly_Type()
)
tnSvcTlsMacRelearnOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsMacRelearnOnly.setStatus("current")


class _TnSvcTlsMfibTableSize_Type(Integer32):
    """Custom type tnSvcTlsMfibTableSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_TnSvcTlsMfibTableSize_Type.__name__ = "Integer32"
_TnSvcTlsMfibTableSize_Object = MibTableColumn
tnSvcTlsMfibTableSize = _TnSvcTlsMfibTableSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 47),
    _TnSvcTlsMfibTableSize_Type()
)
tnSvcTlsMfibTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMfibTableSize.setStatus("current")


class _TnSvcTlsMfibTableFullHighWatermark_Type(Integer32):
    """Custom type tnSvcTlsMfibTableFullHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsMfibTableFullHighWatermark_Type.__name__ = "Integer32"
_TnSvcTlsMfibTableFullHighWatermark_Object = MibTableColumn
tnSvcTlsMfibTableFullHighWatermark = _TnSvcTlsMfibTableFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 48),
    _TnSvcTlsMfibTableFullHighWatermark_Type()
)
tnSvcTlsMfibTableFullHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMfibTableFullHighWatermark.setStatus("current")


class _TnSvcTlsMfibTableFullLowWatermark_Type(Integer32):
    """Custom type tnSvcTlsMfibTableFullLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsMfibTableFullLowWatermark_Type.__name__ = "Integer32"
_TnSvcTlsMfibTableFullLowWatermark_Object = MibTableColumn
tnSvcTlsMfibTableFullLowWatermark = _TnSvcTlsMfibTableFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 49),
    _TnSvcTlsMfibTableFullLowWatermark_Type()
)
tnSvcTlsMfibTableFullLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMfibTableFullLowWatermark.setStatus("current")


class _TnSvcTlsMacFlushOnFail_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsMacFlushOnFail based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsMacFlushOnFail_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsMacFlushOnFail_Object = MibTableColumn
tnSvcTlsMacFlushOnFail = _TnSvcTlsMacFlushOnFail_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 50),
    _TnSvcTlsMacFlushOnFail_Type()
)
tnSvcTlsMacFlushOnFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacFlushOnFail.setStatus("current")


class _TnSvcTlsStpRegionName_Type(DisplayString):
    """Custom type tnSvcTlsStpRegionName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSvcTlsStpRegionName_Type.__name__ = "DisplayString"
_TnSvcTlsStpRegionName_Object = MibTableColumn
tnSvcTlsStpRegionName = _TnSvcTlsStpRegionName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 51),
    _TnSvcTlsStpRegionName_Type()
)
tnSvcTlsStpRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpRegionName.setStatus("current")


class _TnSvcTlsStpRegionRevision_Type(Integer32):
    """Custom type tnSvcTlsStpRegionRevision based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSvcTlsStpRegionRevision_Type.__name__ = "Integer32"
_TnSvcTlsStpRegionRevision_Object = MibTableColumn
tnSvcTlsStpRegionRevision = _TnSvcTlsStpRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 52),
    _TnSvcTlsStpRegionRevision_Type()
)
tnSvcTlsStpRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpRegionRevision.setStatus("current")


class _TnSvcTlsStpBridgeMaxHops_Type(Integer32):
    """Custom type tnSvcTlsStpBridgeMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_TnSvcTlsStpBridgeMaxHops_Type.__name__ = "Integer32"
_TnSvcTlsStpBridgeMaxHops_Object = MibTableColumn
tnSvcTlsStpBridgeMaxHops = _TnSvcTlsStpBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 53),
    _TnSvcTlsStpBridgeMaxHops_Type()
)
tnSvcTlsStpBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsStpBridgeMaxHops.setStatus("current")
_TnSvcTlsStpCistRegionalRoot_Type = BridgeId
_TnSvcTlsStpCistRegionalRoot_Object = MibTableColumn
tnSvcTlsStpCistRegionalRoot = _TnSvcTlsStpCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 54),
    _TnSvcTlsStpCistRegionalRoot_Type()
)
tnSvcTlsStpCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpCistRegionalRoot.setStatus("current")
_TnSvcTlsStpCistIntRootCost_Type = Integer32
_TnSvcTlsStpCistIntRootCost_Object = MibTableColumn
tnSvcTlsStpCistIntRootCost = _TnSvcTlsStpCistIntRootCost_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 55),
    _TnSvcTlsStpCistIntRootCost_Type()
)
tnSvcTlsStpCistIntRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpCistIntRootCost.setStatus("current")
_TnSvcTlsStpCistRemainingHopCount_Type = Integer32
_TnSvcTlsStpCistRemainingHopCount_Object = MibTableColumn
tnSvcTlsStpCistRemainingHopCount = _TnSvcTlsStpCistRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 56),
    _TnSvcTlsStpCistRemainingHopCount_Type()
)
tnSvcTlsStpCistRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpCistRemainingHopCount.setStatus("current")
_TnSvcTlsStpCistRegionalRootPort_Type = Integer32
_TnSvcTlsStpCistRegionalRootPort_Object = MibTableColumn
tnSvcTlsStpCistRegionalRootPort = _TnSvcTlsStpCistRegionalRootPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 57),
    _TnSvcTlsStpCistRegionalRootPort_Type()
)
tnSvcTlsStpCistRegionalRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsStpCistRegionalRootPort.setStatus("current")
_TnSvcTlsFdbNumLearnedEntries_Type = Integer32
_TnSvcTlsFdbNumLearnedEntries_Object = MibTableColumn
tnSvcTlsFdbNumLearnedEntries = _TnSvcTlsFdbNumLearnedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 58),
    _TnSvcTlsFdbNumLearnedEntries_Type()
)
tnSvcTlsFdbNumLearnedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsFdbNumLearnedEntries.setStatus("current")
_TnSvcTlsFdbNumOamEntries_Type = Integer32
_TnSvcTlsFdbNumOamEntries_Object = MibTableColumn
tnSvcTlsFdbNumOamEntries = _TnSvcTlsFdbNumOamEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 59),
    _TnSvcTlsFdbNumOamEntries_Type()
)
tnSvcTlsFdbNumOamEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsFdbNumOamEntries.setStatus("current")
_TnSvcTlsFdbNumDhcpEntries_Type = Integer32
_TnSvcTlsFdbNumDhcpEntries_Object = MibTableColumn
tnSvcTlsFdbNumDhcpEntries = _TnSvcTlsFdbNumDhcpEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 60),
    _TnSvcTlsFdbNumDhcpEntries_Type()
)
tnSvcTlsFdbNumDhcpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsFdbNumDhcpEntries.setStatus("current")
_TnSvcTlsFdbNumHostEntries_Type = Integer32
_TnSvcTlsFdbNumHostEntries_Object = MibTableColumn
tnSvcTlsFdbNumHostEntries = _TnSvcTlsFdbNumHostEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 61),
    _TnSvcTlsFdbNumHostEntries_Type()
)
tnSvcTlsFdbNumHostEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsFdbNumHostEntries.setStatus("current")


class _TnSvcTlsShcvAction_Type(Integer32):
    """Custom type tnSvcTlsShcvAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("remove", 2))
    )


_TnSvcTlsShcvAction_Type.__name__ = "Integer32"
_TnSvcTlsShcvAction_Object = MibTableColumn
tnSvcTlsShcvAction = _TnSvcTlsShcvAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 62),
    _TnSvcTlsShcvAction_Type()
)
tnSvcTlsShcvAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsShcvAction.setStatus("current")
_TnSvcTlsShcvSrcIp_Type = IpAddress
_TnSvcTlsShcvSrcIp_Object = MibTableColumn
tnSvcTlsShcvSrcIp = _TnSvcTlsShcvSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 63),
    _TnSvcTlsShcvSrcIp_Type()
)
tnSvcTlsShcvSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsShcvSrcIp.setStatus("current")
_TnSvcTlsShcvSrcMac_Type = MacAddress
_TnSvcTlsShcvSrcMac_Object = MibTableColumn
tnSvcTlsShcvSrcMac = _TnSvcTlsShcvSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 64),
    _TnSvcTlsShcvSrcMac_Type()
)
tnSvcTlsShcvSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsShcvSrcMac.setStatus("current")


class _TnSvcTlsShcvInterval_Type(Unsigned32):
    """Custom type tnSvcTlsShcvInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_TnSvcTlsShcvInterval_Type.__name__ = "Unsigned32"
_TnSvcTlsShcvInterval_Object = MibTableColumn
tnSvcTlsShcvInterval = _TnSvcTlsShcvInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 65),
    _TnSvcTlsShcvInterval_Type()
)
tnSvcTlsShcvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsShcvInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnSvcTlsShcvInterval.setUnits("minutes")


class _TnSvcTlsPriPortsCumulativeFactor_Type(Unsigned32):
    """Custom type tnSvcTlsPriPortsCumulativeFactor based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_TnSvcTlsPriPortsCumulativeFactor_Type.__name__ = "Unsigned32"
_TnSvcTlsPriPortsCumulativeFactor_Object = MibTableColumn
tnSvcTlsPriPortsCumulativeFactor = _TnSvcTlsPriPortsCumulativeFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 66),
    _TnSvcTlsPriPortsCumulativeFactor_Type()
)
tnSvcTlsPriPortsCumulativeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsPriPortsCumulativeFactor.setStatus("current")


class _TnSvcTlsSecPortsCumulativeFactor_Type(Unsigned32):
    """Custom type tnSvcTlsSecPortsCumulativeFactor based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9),
    )


_TnSvcTlsSecPortsCumulativeFactor_Type.__name__ = "Unsigned32"
_TnSvcTlsSecPortsCumulativeFactor_Object = MibTableColumn
tnSvcTlsSecPortsCumulativeFactor = _TnSvcTlsSecPortsCumulativeFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 67),
    _TnSvcTlsSecPortsCumulativeFactor_Type()
)
tnSvcTlsSecPortsCumulativeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsSecPortsCumulativeFactor.setStatus("current")
_TnSvcTlsL2ptTermEnabled_Type = TruthValue
_TnSvcTlsL2ptTermEnabled_Object = MibTableColumn
tnSvcTlsL2ptTermEnabled = _TnSvcTlsL2ptTermEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 68),
    _TnSvcTlsL2ptTermEnabled_Type()
)
tnSvcTlsL2ptTermEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsL2ptTermEnabled.setStatus("current")


class _TnSvcTlsPropagateMacFlush_Type(TruthValue):
    """Custom type tnSvcTlsPropagateMacFlush based on TruthValue"""
    defaultValue = 2


_TnSvcTlsPropagateMacFlush_Type.__name__ = "TruthValue"
_TnSvcTlsPropagateMacFlush_Object = MibTableColumn
tnSvcTlsPropagateMacFlush = _TnSvcTlsPropagateMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 69),
    _TnSvcTlsPropagateMacFlush_Type()
)
tnSvcTlsPropagateMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsPropagateMacFlush.setStatus("current")


class _TnSvcTlsMrpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsMrpAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsMrpAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsMrpAdminStatus_Object = MibTableColumn
tnSvcTlsMrpAdminStatus = _TnSvcTlsMrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 70),
    _TnSvcTlsMrpAdminStatus_Type()
)
tnSvcTlsMrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMrpAdminStatus.setStatus("current")


class _TnSvcTlsMrpMaxAttributes_Type(Unsigned32):
    """Custom type tnSvcTlsMrpMaxAttributes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TnSvcTlsMrpMaxAttributes_Type.__name__ = "Unsigned32"
_TnSvcTlsMrpMaxAttributes_Object = MibTableColumn
tnSvcTlsMrpMaxAttributes = _TnSvcTlsMrpMaxAttributes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 71),
    _TnSvcTlsMrpMaxAttributes_Type()
)
tnSvcTlsMrpMaxAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMrpMaxAttributes.setStatus("current")
_TnSvcTlsMrpAttributeCount_Type = Unsigned32
_TnSvcTlsMrpAttributeCount_Object = MibTableColumn
tnSvcTlsMrpAttributeCount = _TnSvcTlsMrpAttributeCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 72),
    _TnSvcTlsMrpAttributeCount_Type()
)
tnSvcTlsMrpAttributeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsMrpAttributeCount.setStatus("current")
_TnSvcTlsMrpFailedRegisterCount_Type = Unsigned32
_TnSvcTlsMrpFailedRegisterCount_Object = MibTableColumn
tnSvcTlsMrpFailedRegisterCount = _TnSvcTlsMrpFailedRegisterCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 73),
    _TnSvcTlsMrpFailedRegisterCount_Type()
)
tnSvcTlsMrpFailedRegisterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsMrpFailedRegisterCount.setStatus("current")


class _TnSvcTlsMcPathMgmtPlcyName_Type(TNamedItem):
    """Custom type tnSvcTlsMcPathMgmtPlcyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TnSvcTlsMcPathMgmtPlcyName_Type.__name__ = "TNamedItem"
_TnSvcTlsMcPathMgmtPlcyName_Object = MibTableColumn
tnSvcTlsMcPathMgmtPlcyName = _TnSvcTlsMcPathMgmtPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 74),
    _TnSvcTlsMcPathMgmtPlcyName_Type()
)
tnSvcTlsMcPathMgmtPlcyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMcPathMgmtPlcyName.setStatus("current")


class _TnSvcTlsMrpFloodTime_Type(Unsigned32):
    """Custom type tnSvcTlsMrpFloodTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 600),
    )


_TnSvcTlsMrpFloodTime_Type.__name__ = "Unsigned32"
_TnSvcTlsMrpFloodTime_Object = MibTableColumn
tnSvcTlsMrpFloodTime = _TnSvcTlsMrpFloodTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 75),
    _TnSvcTlsMrpFloodTime_Type()
)
tnSvcTlsMrpFloodTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMrpFloodTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSvcTlsMrpFloodTime.setUnits("seconds")


class _TnSvcTlsMrpAttrTblHighWatermark_Type(Integer32):
    """Custom type tnSvcTlsMrpAttrTblHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsMrpAttrTblHighWatermark_Type.__name__ = "Integer32"
_TnSvcTlsMrpAttrTblHighWatermark_Object = MibTableColumn
tnSvcTlsMrpAttrTblHighWatermark = _TnSvcTlsMrpAttrTblHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 76),
    _TnSvcTlsMrpAttrTblHighWatermark_Type()
)
tnSvcTlsMrpAttrTblHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMrpAttrTblHighWatermark.setStatus("current")


class _TnSvcTlsMrpAttrTblLowWatermark_Type(Integer32):
    """Custom type tnSvcTlsMrpAttrTblLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsMrpAttrTblLowWatermark_Type.__name__ = "Integer32"
_TnSvcTlsMrpAttrTblLowWatermark_Object = MibTableColumn
tnSvcTlsMrpAttrTblLowWatermark = _TnSvcTlsMrpAttrTblLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 77),
    _TnSvcTlsMrpAttrTblLowWatermark_Type()
)
tnSvcTlsMrpAttrTblLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMrpAttrTblLowWatermark.setStatus("current")


class _TnSvcTlsMacMoveNumRetries_Type(Unsigned32):
    """Custom type tnSvcTlsMacMoveNumRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSvcTlsMacMoveNumRetries_Type.__name__ = "Unsigned32"
_TnSvcTlsMacMoveNumRetries_Object = MibTableColumn
tnSvcTlsMacMoveNumRetries = _TnSvcTlsMacMoveNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 78),
    _TnSvcTlsMacMoveNumRetries_Type()
)
tnSvcTlsMacMoveNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacMoveNumRetries.setStatus("current")


class _TnSvcTlsMacSubNetLen_Type(Integer32):
    """Custom type tnSvcTlsMacSubNetLen based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 48),
    )


_TnSvcTlsMacSubNetLen_Type.__name__ = "Integer32"
_TnSvcTlsMacSubNetLen_Object = MibTableColumn
tnSvcTlsMacSubNetLen = _TnSvcTlsMacSubNetLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 79),
    _TnSvcTlsMacSubNetLen_Type()
)
tnSvcTlsMacSubNetLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacSubNetLen.setStatus("current")


class _TnSvcTlsSendFlushOnBVplsFail_Type(TruthValue):
    """Custom type tnSvcTlsSendFlushOnBVplsFail based on TruthValue"""
    defaultValue = 2


_TnSvcTlsSendFlushOnBVplsFail_Type.__name__ = "TruthValue"
_TnSvcTlsSendFlushOnBVplsFail_Object = MibTableColumn
tnSvcTlsSendFlushOnBVplsFail = _TnSvcTlsSendFlushOnBVplsFail_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 80),
    _TnSvcTlsSendFlushOnBVplsFail_Type()
)
tnSvcTlsSendFlushOnBVplsFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsSendFlushOnBVplsFail.setStatus("current")


class _TnSvcTlsPropMacFlushFromBVpls_Type(TruthValue):
    """Custom type tnSvcTlsPropMacFlushFromBVpls based on TruthValue"""
    defaultValue = 2


_TnSvcTlsPropMacFlushFromBVpls_Type.__name__ = "TruthValue"
_TnSvcTlsPropMacFlushFromBVpls_Object = MibTableColumn
tnSvcTlsPropMacFlushFromBVpls = _TnSvcTlsPropMacFlushFromBVpls_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 81),
    _TnSvcTlsPropMacFlushFromBVpls_Type()
)
tnSvcTlsPropMacFlushFromBVpls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsPropMacFlushFromBVpls.setStatus("current")


class _TnSvcTlsMacNotifInterval_Type(Unsigned32):
    """Custom type tnSvcTlsMacNotifInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSvcTlsMacNotifInterval_Type.__name__ = "Unsigned32"
_TnSvcTlsMacNotifInterval_Object = MibTableColumn
tnSvcTlsMacNotifInterval = _TnSvcTlsMacNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 82),
    _TnSvcTlsMacNotifInterval_Type()
)
tnSvcTlsMacNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnSvcTlsMacNotifInterval.setUnits("deci-seconds")


class _TnSvcTlsMacNotifCount_Type(Unsigned32):
    """Custom type tnSvcTlsMacNotifCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TnSvcTlsMacNotifCount_Type.__name__ = "Unsigned32"
_TnSvcTlsMacNotifCount_Object = MibTableColumn
tnSvcTlsMacNotifCount = _TnSvcTlsMacNotifCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 83),
    _TnSvcTlsMacNotifCount_Type()
)
tnSvcTlsMacNotifCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacNotifCount.setStatus("current")


class _TnSvcTlsMacNotifAdminState_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsMacNotifAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsMacNotifAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsMacNotifAdminState_Object = MibTableColumn
tnSvcTlsMacNotifAdminState = _TnSvcTlsMacNotifAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 84),
    _TnSvcTlsMacNotifAdminState_Type()
)
tnSvcTlsMacNotifAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsMacNotifAdminState.setStatus("current")


class _TnSvcTlsShcvRetryTimeout_Type(Unsigned32):
    """Custom type tnSvcTlsShcvRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_TnSvcTlsShcvRetryTimeout_Type.__name__ = "Unsigned32"
_TnSvcTlsShcvRetryTimeout_Object = MibTableColumn
tnSvcTlsShcvRetryTimeout = _TnSvcTlsShcvRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 87),
    _TnSvcTlsShcvRetryTimeout_Type()
)
tnSvcTlsShcvRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsShcvRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnSvcTlsShcvRetryTimeout.setUnits("seconds")


class _TnSvcTlsShcvRetryCount_Type(Unsigned32):
    """Custom type tnSvcTlsShcvRetryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 29),
    )


_TnSvcTlsShcvRetryCount_Type.__name__ = "Unsigned32"
_TnSvcTlsShcvRetryCount_Object = MibTableColumn
tnSvcTlsShcvRetryCount = _TnSvcTlsShcvRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 88),
    _TnSvcTlsShcvRetryCount_Type()
)
tnSvcTlsShcvRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsShcvRetryCount.setStatus("current")


class _TnsvcTlsAllowIpIfBinding_Type(TruthValue):
    """Custom type tnsvcTlsAllowIpIfBinding based on TruthValue"""
    defaultValue = 2


_TnsvcTlsAllowIpIfBinding_Type.__name__ = "TruthValue"
_TnsvcTlsAllowIpIfBinding_Object = MibTableColumn
tnsvcTlsAllowIpIfBinding = _TnsvcTlsAllowIpIfBinding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 3, 1, 89),
    _TnsvcTlsAllowIpIfBinding_Type()
)
tnsvcTlsAllowIpIfBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnsvcTlsAllowIpIfBinding.setStatus("current")
_TnTlsFdbInfoTable_Object = MibTable
tnTlsFdbInfoTable = _TnTlsFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    tnTlsFdbInfoTable.setStatus("current")
_TnTlsFdbInfoEntry_Object = MibTableRow
tnTlsFdbInfoEntry = _TnTlsFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1)
)
tnTlsFdbInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SERV-MIB", "tnTlsFdbMacAddr"),
)
if mibBuilder.loadTexts:
    tnTlsFdbInfoEntry.setStatus("current")
_TnTlsFdbMacAddr_Type = MacAddress
_TnTlsFdbMacAddr_Object = MibTableColumn
tnTlsFdbMacAddr = _TnTlsFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 1),
    _TnTlsFdbMacAddr_Type()
)
tnTlsFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsFdbMacAddr.setStatus("current")
_TnTlsFdbRowStatus_Type = RowStatus
_TnTlsFdbRowStatus_Object = MibTableColumn
tnTlsFdbRowStatus = _TnTlsFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 2),
    _TnTlsFdbRowStatus_Type()
)
tnTlsFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbRowStatus.setStatus("current")


class _TnTlsFdbType_Type(Integer32):
    """Custom type tnTlsFdbType based on Integer32"""
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
        *(("static", 1),
          ("learned", 2),
          ("oam", 3),
          ("dhcp", 4),
          ("host", 5))
    )


_TnTlsFdbType_Type.__name__ = "Integer32"
_TnTlsFdbType_Object = MibTableColumn
tnTlsFdbType = _TnTlsFdbType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 3),
    _TnTlsFdbType_Type()
)
tnTlsFdbType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbType.setStatus("current")


class _TnTlsFdbLocale_Type(Integer32):
    """Custom type tnTlsFdbLocale based on Integer32"""
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
        *(("sap", 1),
          ("sdp", 2),
          ("cpm", 3),
          ("endpoint", 4))
    )


_TnTlsFdbLocale_Type.__name__ = "Integer32"
_TnTlsFdbLocale_Object = MibTableColumn
tnTlsFdbLocale = _TnTlsFdbLocale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 4),
    _TnTlsFdbLocale_Type()
)
tnTlsFdbLocale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbLocale.setStatus("current")
_TnTlsFdbPortId_Type = TmnxPortID
_TnTlsFdbPortId_Object = MibTableColumn
tnTlsFdbPortId = _TnTlsFdbPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 5),
    _TnTlsFdbPortId_Type()
)
tnTlsFdbPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbPortId.setStatus("current")
_TnTlsFdbEncapValue_Type = TmnxEncapVal
_TnTlsFdbEncapValue_Object = MibTableColumn
tnTlsFdbEncapValue = _TnTlsFdbEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 6),
    _TnTlsFdbEncapValue_Type()
)
tnTlsFdbEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbEncapValue.setStatus("current")
_TnTlsFdbSdpId_Type = SdpId
_TnTlsFdbSdpId_Object = MibTableColumn
tnTlsFdbSdpId = _TnTlsFdbSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 7),
    _TnTlsFdbSdpId_Type()
)
tnTlsFdbSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbSdpId.setStatus("current")
_TnTlsFdbVcId_Type = Unsigned32
_TnTlsFdbVcId_Object = MibTableColumn
tnTlsFdbVcId = _TnTlsFdbVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 8),
    _TnTlsFdbVcId_Type()
)
tnTlsFdbVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbVcId.setStatus("current")
_TnTlsFdbVpnId_Type = VpnId
_TnTlsFdbVpnId_Object = MibTableColumn
tnTlsFdbVpnId = _TnTlsFdbVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 9),
    _TnTlsFdbVpnId_Type()
)
tnTlsFdbVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbVpnId.setStatus("current")
_TnTlsFdbCustId_Type = TmnxCustId
_TnTlsFdbCustId_Object = MibTableColumn
tnTlsFdbCustId = _TnTlsFdbCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 10),
    _TnTlsFdbCustId_Type()
)
tnTlsFdbCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbCustId.setStatus("current")
_TnTlsFdbLastStateChange_Type = TimeStamp
_TnTlsFdbLastStateChange_Object = MibTableColumn
tnTlsFdbLastStateChange = _TnTlsFdbLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 11),
    _TnTlsFdbLastStateChange_Type()
)
tnTlsFdbLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbLastStateChange.setStatus("current")
_TnTlsFdbProtected_Type = TruthValue
_TnTlsFdbProtected_Object = MibTableColumn
tnTlsFdbProtected = _TnTlsFdbProtected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 12),
    _TnTlsFdbProtected_Type()
)
tnTlsFdbProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbProtected.setStatus("current")
_TnTlsFdbBackboneDstMac_Type = MacAddress
_TnTlsFdbBackboneDstMac_Object = MibTableColumn
tnTlsFdbBackboneDstMac = _TnTlsFdbBackboneDstMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 13),
    _TnTlsFdbBackboneDstMac_Type()
)
tnTlsFdbBackboneDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbBackboneDstMac.setStatus("current")
_TnTlsFdbNumIVplsMac_Type = Unsigned32
_TnTlsFdbNumIVplsMac_Object = MibTableColumn
tnTlsFdbNumIVplsMac = _TnTlsFdbNumIVplsMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 14),
    _TnTlsFdbNumIVplsMac_Type()
)
tnTlsFdbNumIVplsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbNumIVplsMac.setStatus("current")


class _TnTlsFdbEndPointName_Type(TNamedItemOrEmpty):
    """Custom type tnTlsFdbEndPointName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnTlsFdbEndPointName_Type.__name__ = "TNamedItemOrEmpty"
_TnTlsFdbEndPointName_Object = MibTableColumn
tnTlsFdbEndPointName = _TnTlsFdbEndPointName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 15),
    _TnTlsFdbEndPointName_Type()
)
tnTlsFdbEndPointName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsFdbEndPointName.setStatus("current")
_TnTlsFdbEPMacOperSdpId_Type = SdpId
_TnTlsFdbEPMacOperSdpId_Object = MibTableColumn
tnTlsFdbEPMacOperSdpId = _TnTlsFdbEPMacOperSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 16),
    _TnTlsFdbEPMacOperSdpId_Type()
)
tnTlsFdbEPMacOperSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbEPMacOperSdpId.setStatus("current")
_TnTlsFdbEPMacOperVcId_Type = Unsigned32
_TnTlsFdbEPMacOperVcId_Object = MibTableColumn
tnTlsFdbEPMacOperVcId = _TnTlsFdbEPMacOperVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 17),
    _TnTlsFdbEPMacOperVcId_Type()
)
tnTlsFdbEPMacOperVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbEPMacOperVcId.setStatus("current")
_TnTlsFdbPbbNumEpipes_Type = Unsigned32
_TnTlsFdbPbbNumEpipes_Object = MibTableColumn
tnTlsFdbPbbNumEpipes = _TnTlsFdbPbbNumEpipes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 4, 1, 18),
    _TnTlsFdbPbbNumEpipes_Type()
)
tnTlsFdbPbbNumEpipes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsFdbPbbNumEpipes.setStatus("current")
_TnTlsShgInfoTable_Object = MibTable
tnTlsShgInfoTable = _TnTlsShgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    tnTlsShgInfoTable.setStatus("current")
_TnTlsShgInfoEntry_Object = MibTableRow
tnTlsShgInfoEntry = _TnTlsShgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1)
)
tnTlsShgInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (1, "TN-SERV-MIB", "tnTlsShgName"),
)
if mibBuilder.loadTexts:
    tnTlsShgInfoEntry.setStatus("current")
_TnTlsShgName_Type = TNamedItem
_TnTlsShgName_Object = MibTableColumn
tnTlsShgName = _TnTlsShgName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 1),
    _TnTlsShgName_Type()
)
tnTlsShgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsShgName.setStatus("current")
_TnTlsShgRowStatus_Type = RowStatus
_TnTlsShgRowStatus_Object = MibTableColumn
tnTlsShgRowStatus = _TnTlsShgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 2),
    _TnTlsShgRowStatus_Type()
)
tnTlsShgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsShgRowStatus.setStatus("current")
_TnTlsShgCustId_Type = TmnxCustId
_TnTlsShgCustId_Object = MibTableColumn
tnTlsShgCustId = _TnTlsShgCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 3),
    _TnTlsShgCustId_Type()
)
tnTlsShgCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsShgCustId.setStatus("current")
_TnTlsShgInstanceId_Type = Unsigned32
_TnTlsShgInstanceId_Object = MibTableColumn
tnTlsShgInstanceId = _TnTlsShgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 4),
    _TnTlsShgInstanceId_Type()
)
tnTlsShgInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsShgInstanceId.setStatus("current")


class _TnTlsShgDescription_Type(ServObjDesc):
    """Custom type tnTlsShgDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_TnTlsShgDescription_Type.__name__ = "ServObjDesc"
_TnTlsShgDescription_Object = MibTableColumn
tnTlsShgDescription = _TnTlsShgDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 5),
    _TnTlsShgDescription_Type()
)
tnTlsShgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsShgDescription.setStatus("current")
_TnTlsShgLastMgmtChange_Type = TimeStamp
_TnTlsShgLastMgmtChange_Object = MibTableColumn
tnTlsShgLastMgmtChange = _TnTlsShgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 6),
    _TnTlsShgLastMgmtChange_Type()
)
tnTlsShgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsShgLastMgmtChange.setStatus("current")


class _TnTlsShgResidential_Type(TruthValue):
    """Custom type tnTlsShgResidential based on TruthValue"""
    defaultValue = 2


_TnTlsShgResidential_Type.__name__ = "TruthValue"
_TnTlsShgResidential_Object = MibTableColumn
tnTlsShgResidential = _TnTlsShgResidential_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 7),
    _TnTlsShgResidential_Type()
)
tnTlsShgResidential.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsShgResidential.setStatus("current")


class _TnTlsShgRestProtSrcMac_Type(TruthValue):
    """Custom type tnTlsShgRestProtSrcMac based on TruthValue"""
    defaultValue = 2


_TnTlsShgRestProtSrcMac_Type.__name__ = "TruthValue"
_TnTlsShgRestProtSrcMac_Object = MibTableColumn
tnTlsShgRestProtSrcMac = _TnTlsShgRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 8),
    _TnTlsShgRestProtSrcMac_Type()
)
tnTlsShgRestProtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsShgRestProtSrcMac.setStatus("current")


class _TnTlsShgRestUnprotDstMac_Type(TruthValue):
    """Custom type tnTlsShgRestUnprotDstMac based on TruthValue"""
    defaultValue = 2


_TnTlsShgRestUnprotDstMac_Type.__name__ = "TruthValue"
_TnTlsShgRestUnprotDstMac_Object = MibTableColumn
tnTlsShgRestUnprotDstMac = _TnTlsShgRestUnprotDstMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 9),
    _TnTlsShgRestUnprotDstMac_Type()
)
tnTlsShgRestUnprotDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsShgRestUnprotDstMac.setStatus("current")


class _TnTlsShgRestProtSrcMacAction_Type(Integer32):
    """Custom type tnTlsShgRestProtSrcMacAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarm-only", 2))
    )


_TnTlsShgRestProtSrcMacAction_Type.__name__ = "Integer32"
_TnTlsShgRestProtSrcMacAction_Object = MibTableColumn
tnTlsShgRestProtSrcMacAction = _TnTlsShgRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 10),
    _TnTlsShgRestProtSrcMacAction_Type()
)
tnTlsShgRestProtSrcMacAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsShgRestProtSrcMacAction.setStatus("current")
_TnTlsShgCreationOrigin_Type = L2RouteOrigin
_TnTlsShgCreationOrigin_Object = MibTableColumn
tnTlsShgCreationOrigin = _TnTlsShgCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 6, 1, 11),
    _TnTlsShgCreationOrigin_Type()
)
tnTlsShgCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsShgCreationOrigin.setStatus("current")
_TnSvcTlsBackboneInfoTable_Object = MibTable
tnSvcTlsBackboneInfoTable = _TnSvcTlsBackboneInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27)
)
if mibBuilder.loadTexts:
    tnSvcTlsBackboneInfoTable.setStatus("current")
_TnSvcTlsBackboneInfoEntry_Object = MibTableRow
tnSvcTlsBackboneInfoEntry = _TnSvcTlsBackboneInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1)
)
if mibBuilder.loadTexts:
    tnSvcTlsBackboneInfoEntry.setStatus("current")


class _TnSvcTlsBackboneSrcMac_Type(MacAddress):
    """Custom type tnSvcTlsBackboneSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TnSvcTlsBackboneSrcMac_Type.__name__ = "MacAddress"
_TnSvcTlsBackboneSrcMac_Object = MibTableColumn
tnSvcTlsBackboneSrcMac = _TnSvcTlsBackboneSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 1),
    _TnSvcTlsBackboneSrcMac_Type()
)
tnSvcTlsBackboneSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneSrcMac.setStatus("current")


class _TnSvcTlsBackboneVplsSvcId_Type(TmnxServId):
    """Custom type tnSvcTlsBackboneVplsSvcId based on TmnxServId"""
    defaultValue = 0


_TnSvcTlsBackboneVplsSvcId_Type.__name__ = "TmnxServId"
_TnSvcTlsBackboneVplsSvcId_Object = MibTableColumn
tnSvcTlsBackboneVplsSvcId = _TnSvcTlsBackboneVplsSvcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 2),
    _TnSvcTlsBackboneVplsSvcId_Type()
)
tnSvcTlsBackboneVplsSvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneVplsSvcId.setStatus("current")


class _TnSvcTlsBackboneVplsSvcISID_Type(SvcISID):
    """Custom type tnSvcTlsBackboneVplsSvcISID based on SvcISID"""
    defaultValue = -1


_TnSvcTlsBackboneVplsSvcISID_Type.__name__ = "SvcISID"
_TnSvcTlsBackboneVplsSvcISID_Object = MibTableColumn
tnSvcTlsBackboneVplsSvcISID = _TnSvcTlsBackboneVplsSvcISID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 3),
    _TnSvcTlsBackboneVplsSvcISID_Type()
)
tnSvcTlsBackboneVplsSvcISID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneVplsSvcISID.setStatus("current")
_TnSvcTlsBackboneOperSrcMac_Type = MacAddress
_TnSvcTlsBackboneOperSrcMac_Object = MibTableColumn
tnSvcTlsBackboneOperSrcMac = _TnSvcTlsBackboneOperSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 4),
    _TnSvcTlsBackboneOperSrcMac_Type()
)
tnSvcTlsBackboneOperSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneOperSrcMac.setStatus("current")
_TnSvcTlsBackboneOperVplsSvcISID_Type = SvcISID
_TnSvcTlsBackboneOperVplsSvcISID_Object = MibTableColumn
tnSvcTlsBackboneOperVplsSvcISID = _TnSvcTlsBackboneOperVplsSvcISID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 5),
    _TnSvcTlsBackboneOperVplsSvcISID_Type()
)
tnSvcTlsBackboneOperVplsSvcISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneOperVplsSvcISID.setStatus("current")


class _TnSvcTlsBackboneLDPMacFlush_Type(TruthValue):
    """Custom type tnSvcTlsBackboneLDPMacFlush based on TruthValue"""
    defaultValue = 2


_TnSvcTlsBackboneLDPMacFlush_Type.__name__ = "TruthValue"
_TnSvcTlsBackboneLDPMacFlush_Object = MibTableColumn
tnSvcTlsBackboneLDPMacFlush = _TnSvcTlsBackboneLDPMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 6),
    _TnSvcTlsBackboneLDPMacFlush_Type()
)
tnSvcTlsBackboneLDPMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneLDPMacFlush.setStatus("current")


class _TnSvcTlsBackboneVplsStp_Type(TmnxEnabledDisabled):
    """Custom type tnSvcTlsBackboneVplsStp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSvcTlsBackboneVplsStp_Type.__name__ = "TmnxEnabledDisabled"
_TnSvcTlsBackboneVplsStp_Object = MibTableColumn
tnSvcTlsBackboneVplsStp = _TnSvcTlsBackboneVplsStp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 7),
    _TnSvcTlsBackboneVplsStp_Type()
)
tnSvcTlsBackboneVplsStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneVplsStp.setStatus("current")


class _TnSvcTlsBackboneLDPMacFlushNotMine_Type(TruthValue):
    """Custom type tnSvcTlsBackboneLDPMacFlushNotMine based on TruthValue"""
    defaultValue = 2


_TnSvcTlsBackboneLDPMacFlushNotMine_Type.__name__ = "TruthValue"
_TnSvcTlsBackboneLDPMacFlushNotMine_Object = MibTableColumn
tnSvcTlsBackboneLDPMacFlushNotMine = _TnSvcTlsBackboneLDPMacFlushNotMine_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 8),
    _TnSvcTlsBackboneLDPMacFlushNotMine_Type()
)
tnSvcTlsBackboneLDPMacFlushNotMine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneLDPMacFlushNotMine.setStatus("current")


class _TnSvcTlsBackboneUseSapBMac_Type(TruthValue):
    """Custom type tnSvcTlsBackboneUseSapBMac based on TruthValue"""
    defaultValue = 2


_TnSvcTlsBackboneUseSapBMac_Type.__name__ = "TruthValue"
_TnSvcTlsBackboneUseSapBMac_Object = MibTableColumn
tnSvcTlsBackboneUseSapBMac = _TnSvcTlsBackboneUseSapBMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 27, 1, 9),
    _TnSvcTlsBackboneUseSapBMac_Type()
)
tnSvcTlsBackboneUseSapBMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSvcTlsBackboneUseSapBMac.setStatus("current")
_TnTlsMFibTable_Object = MibTable
tnTlsMFibTable = _TnTlsMFibTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28)
)
if mibBuilder.loadTexts:
    tnTlsMFibTable.setStatus("current")
_TnTlsMFibEntry_Object = MibTableRow
tnTlsMFibEntry = _TnTlsMFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1)
)
tnTlsMFibEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SERV-MIB", "tnTlsMFibEntryType"),
    (0, "TN-SERV-MIB", "tnTlsMFibGrpMacAddr"),
    (0, "TN-SERV-MIB", "tnTlsMFibGrpInetAddrType"),
    (0, "TN-SERV-MIB", "tnTlsMFibGrpInetAddr"),
    (0, "TN-SERV-MIB", "tnTlsMFibSrcInetAddrType"),
    (0, "TN-SERV-MIB", "tnTlsMFibSrcInetAddr"),
    (0, "TN-SERV-MIB", "tnTlsMFibLocale"),
    (0, "TN-SERV-MIB", "tnTlsMFibPortId"),
    (0, "TN-SERV-MIB", "tnTlsMFibEncapValue"),
    (0, "TN-SERV-MIB", "tnTlsMFibSdpId"),
    (0, "TN-SERV-MIB", "tnTlsMFibVcId"),
)
if mibBuilder.loadTexts:
    tnTlsMFibEntry.setStatus("current")


class _TnTlsMFibEntryType_Type(Integer32):
    """Custom type tnTlsMFibEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipBased", 1),
          ("macBased", 2))
    )


_TnTlsMFibEntryType_Type.__name__ = "Integer32"
_TnTlsMFibEntryType_Object = MibTableColumn
tnTlsMFibEntryType = _TnTlsMFibEntryType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 1),
    _TnTlsMFibEntryType_Type()
)
tnTlsMFibEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibEntryType.setStatus("current")
_TnTlsMFibGrpMacAddr_Type = MacAddress
_TnTlsMFibGrpMacAddr_Object = MibTableColumn
tnTlsMFibGrpMacAddr = _TnTlsMFibGrpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 2),
    _TnTlsMFibGrpMacAddr_Type()
)
tnTlsMFibGrpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibGrpMacAddr.setStatus("current")
_TnTlsMFibGrpInetAddrType_Type = InetAddressType
_TnTlsMFibGrpInetAddrType_Object = MibTableColumn
tnTlsMFibGrpInetAddrType = _TnTlsMFibGrpInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 3),
    _TnTlsMFibGrpInetAddrType_Type()
)
tnTlsMFibGrpInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibGrpInetAddrType.setStatus("current")


class _TnTlsMFibGrpInetAddr_Type(InetAddress):
    """Custom type tnTlsMFibGrpInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnTlsMFibGrpInetAddr_Type.__name__ = "InetAddress"
_TnTlsMFibGrpInetAddr_Object = MibTableColumn
tnTlsMFibGrpInetAddr = _TnTlsMFibGrpInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 4),
    _TnTlsMFibGrpInetAddr_Type()
)
tnTlsMFibGrpInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibGrpInetAddr.setStatus("current")
_TnTlsMFibSrcInetAddrType_Type = InetAddressType
_TnTlsMFibSrcInetAddrType_Object = MibTableColumn
tnTlsMFibSrcInetAddrType = _TnTlsMFibSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 5),
    _TnTlsMFibSrcInetAddrType_Type()
)
tnTlsMFibSrcInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibSrcInetAddrType.setStatus("current")


class _TnTlsMFibSrcInetAddr_Type(InetAddress):
    """Custom type tnTlsMFibSrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnTlsMFibSrcInetAddr_Type.__name__ = "InetAddress"
_TnTlsMFibSrcInetAddr_Object = MibTableColumn
tnTlsMFibSrcInetAddr = _TnTlsMFibSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 6),
    _TnTlsMFibSrcInetAddr_Type()
)
tnTlsMFibSrcInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibSrcInetAddr.setStatus("current")
_TnTlsMFibLocale_Type = MfibLocation
_TnTlsMFibLocale_Object = MibTableColumn
tnTlsMFibLocale = _TnTlsMFibLocale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 7),
    _TnTlsMFibLocale_Type()
)
tnTlsMFibLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibLocale.setStatus("current")
_TnTlsMFibPortId_Type = TmnxPortID
_TnTlsMFibPortId_Object = MibTableColumn
tnTlsMFibPortId = _TnTlsMFibPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 8),
    _TnTlsMFibPortId_Type()
)
tnTlsMFibPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibPortId.setStatus("current")
_TnTlsMFibEncapValue_Type = TmnxEncapVal
_TnTlsMFibEncapValue_Object = MibTableColumn
tnTlsMFibEncapValue = _TnTlsMFibEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 9),
    _TnTlsMFibEncapValue_Type()
)
tnTlsMFibEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibEncapValue.setStatus("current")
_TnTlsMFibSdpId_Type = SdpId
_TnTlsMFibSdpId_Object = MibTableColumn
tnTlsMFibSdpId = _TnTlsMFibSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 10),
    _TnTlsMFibSdpId_Type()
)
tnTlsMFibSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibSdpId.setStatus("current")
_TnTlsMFibVcId_Type = Unsigned32
_TnTlsMFibVcId_Object = MibTableColumn
tnTlsMFibVcId = _TnTlsMFibVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 11),
    _TnTlsMFibVcId_Type()
)
tnTlsMFibVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsMFibVcId.setStatus("current")
_TnTlsMFibFwdOrBlk_Type = MfibGrpSrcFwdOrBlk
_TnTlsMFibFwdOrBlk_Object = MibTableColumn
tnTlsMFibFwdOrBlk = _TnTlsMFibFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 12),
    _TnTlsMFibFwdOrBlk_Type()
)
tnTlsMFibFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsMFibFwdOrBlk.setStatus("current")
_TnTlsMFibSvcId_Type = TmnxServId
_TnTlsMFibSvcId_Object = MibTableColumn
tnTlsMFibSvcId = _TnTlsMFibSvcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 28, 1, 13),
    _TnTlsMFibSvcId_Type()
)
tnTlsMFibSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsMFibSvcId.setStatus("current")
_TnSvcTlsBgpADTableLastChanged_Type = TimeStamp
_TnSvcTlsBgpADTableLastChanged_Object = MibScalar
tnSvcTlsBgpADTableLastChanged = _TnSvcTlsBgpADTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 30),
    _TnSvcTlsBgpADTableLastChanged_Type()
)
tnSvcTlsBgpADTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTlsBgpADTableLastChanged.setStatus("current")
_TnSvcEpipePbbTableLastChanged_Type = TimeStamp
_TnSvcEpipePbbTableLastChanged_Object = MibScalar
tnSvcEpipePbbTableLastChanged = _TnSvcEpipePbbTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 36),
    _TnSvcEpipePbbTableLastChanged_Type()
)
tnSvcEpipePbbTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcEpipePbbTableLastChanged.setStatus("current")
_TnSvcTotalFdbMimDestIdxEntries_Type = Unsigned32
_TnSvcTotalFdbMimDestIdxEntries_Object = MibScalar
tnSvcTotalFdbMimDestIdxEntries = _TnSvcTotalFdbMimDestIdxEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 42),
    _TnSvcTotalFdbMimDestIdxEntries_Type()
)
tnSvcTotalFdbMimDestIdxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcTotalFdbMimDestIdxEntries.setStatus("current")
_TnSvcArpHostTableLastChanged_Type = TimeStamp
_TnSvcArpHostTableLastChanged_Object = MibScalar
tnSvcArpHostTableLastChanged = _TnSvcArpHostTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 44),
    _TnSvcArpHostTableLastChanged_Type()
)
tnSvcArpHostTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcArpHostTableLastChanged.setStatus("current")
_TnSvcArpHostIfTableLastMgmtChange_Type = TimeStamp
_TnSvcArpHostIfTableLastMgmtChange_Object = MibScalar
tnSvcArpHostIfTableLastMgmtChange = _TnSvcArpHostIfTableLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 46),
    _TnSvcArpHostIfTableLastMgmtChange_Type()
)
tnSvcArpHostIfTableLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcArpHostIfTableLastMgmtChange.setStatus("current")
_TnSvcArpHostDefaultSessionTimeout_Type = Unsigned32
_TnSvcArpHostDefaultSessionTimeout_Object = MibScalar
tnSvcArpHostDefaultSessionTimeout = _TnSvcArpHostDefaultSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 48),
    _TnSvcArpHostDefaultSessionTimeout_Type()
)
tnSvcArpHostDefaultSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcArpHostDefaultSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnSvcArpHostDefaultSessionTimeout.setUnits("seconds")
_TnSvcIgmpTrkTableLastMgmtChange_Type = TimeStamp
_TnSvcIgmpTrkTableLastMgmtChange_Object = MibScalar
tnSvcIgmpTrkTableLastMgmtChange = _TnSvcIgmpTrkTableLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 49),
    _TnSvcIgmpTrkTableLastMgmtChange_Type()
)
tnSvcIgmpTrkTableLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpTrkTableLastMgmtChange.setStatus("current")
_TnSvcIpipeInfoTableLastMgmtChange_Type = TimeStamp
_TnSvcIpipeInfoTableLastMgmtChange_Object = MibScalar
tnSvcIpipeInfoTableLastMgmtChange = _TnSvcIpipeInfoTableLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 51),
    _TnSvcIpipeInfoTableLastMgmtChange_Type()
)
tnSvcIpipeInfoTableLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIpipeInfoTableLastMgmtChange.setStatus("current")
_TnSvcMacNameTableLastChanged_Type = TimeStamp
_TnSvcMacNameTableLastChanged_Object = MibScalar
tnSvcMacNameTableLastChanged = _TnSvcMacNameTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 58),
    _TnSvcMacNameTableLastChanged_Type()
)
tnSvcMacNameTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcMacNameTableLastChanged.setStatus("current")
_TnSvcScalar1_Type = Unsigned32
_TnSvcScalar1_Object = MibScalar
tnSvcScalar1 = _TnSvcScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 101),
    _TnSvcScalar1_Type()
)
tnSvcScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcScalar1.setStatus("current")
_TnSvcScalar2_Type = Unsigned32
_TnSvcScalar2_Object = MibScalar
tnSvcScalar2 = _TnSvcScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 102),
    _TnSvcScalar2_Type()
)
tnSvcScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcScalar2.setStatus("current")
_TnSvcScalar3_Type = Unsigned32
_TnSvcScalar3_Object = MibScalar
tnSvcScalar3 = _TnSvcScalar3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 103),
    _TnSvcScalar3_Type()
)
tnSvcScalar3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcScalar3.setStatus("current")
_TnSvcScalar4_Type = Unsigned32
_TnSvcScalar4_Object = MibScalar
tnSvcScalar4 = _TnSvcScalar4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 104),
    _TnSvcScalar4_Type()
)
tnSvcScalar4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcScalar4.setStatus("current")
_TnSvcScalar5_Type = Unsigned32
_TnSvcScalar5_Object = MibScalar
tnSvcScalar5 = _TnSvcScalar5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 2, 105),
    _TnSvcScalar5_Type()
)
tnSvcScalar5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcScalar5.setStatus("current")
_TnServNotifications_ObjectIdentity = ObjectIdentity
tnServNotifications = _TnServNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4)
)
_TnCustTrapsPrefix_ObjectIdentity = ObjectIdentity
tnCustTrapsPrefix = _TnCustTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 1)
)
_TnCustTraps_ObjectIdentity = ObjectIdentity
tnCustTraps = _TnCustTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 1, 0)
)
_TnSvcTrapsPrefix_ObjectIdentity = ObjectIdentity
tnSvcTrapsPrefix = _TnSvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 2)
)
_TnSvcTraps_ObjectIdentity = ObjectIdentity
tnSvcTraps = _TnSvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 2, 0)
)
_TnTstpTrapsPrefix_ObjectIdentity = ObjectIdentity
tnTstpTrapsPrefix = _TnTstpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5)
)
_TnTstpTraps_ObjectIdentity = ObjectIdentity
tnTstpTraps = _TnTstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0)
)
tnSvcTlsInfoEntry.registerAugmentions(
    ("TN-SERV-MIB",
     "tnSvcTlsBackboneInfoEntry")
)
tnSvcTlsBackboneInfoEntry.setIndexNames(*tnSvcTlsInfoEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SERV-MIB",
    **{"ServObjName": ServObjName,
       "ServObjLongDesc": ServObjLongDesc,
       "ServType": ServType,
       "VpnId": VpnId,
       "SdpId": SdpId,
       "SdpTemplateId": SdpTemplateId,
       "PWTemplateId": PWTemplateId,
       "TlsBpduTranslation": TlsBpduTranslation,
       "TlsLimitMacMoveLevel": TlsLimitMacMoveLevel,
       "TlsLimitMacMove": TlsLimitMacMove,
       "SdpBindVcType": SdpBindVcType,
       "StpExceptionCondition": StpExceptionCondition,
       "LspIdList": LspIdList,
       "BridgeId": BridgeId,
       "TSapIngQueueId": TSapIngQueueId,
       "TSapEgrQueueId": TSapEgrQueueId,
       "TStpPortState": TStpPortState,
       "StpPortRole": StpPortRole,
       "StpProtocol": StpProtocol,
       "MfibLocation": MfibLocation,
       "MfibGrpSrcFwdOrBlk": MfibGrpSrcFwdOrBlk,
       "MvplsPruneState": MvplsPruneState,
       "TQosQueueAttribute": TQosQueueAttribute,
       "TVirtSchedAttribute": TVirtSchedAttribute,
       "MstiInstanceId": MstiInstanceId,
       "MstiInstanceIdOrZero": MstiInstanceIdOrZero,
       "DhcpLseStateInfoOrigin": DhcpLseStateInfoOrigin,
       "IAIDType": IAIDType,
       "TdmOptionsSigPkts": TdmOptionsSigPkts,
       "TdmOptionsCasTrunkFraming": TdmOptionsCasTrunkFraming,
       "CemSapReportAlarm": CemSapReportAlarm,
       "CemSapEcid": CemSapEcid,
       "SdpBFHundredthsOfPercent": SdpBFHundredthsOfPercent,
       "SdpBindBandwidth": SdpBindBandwidth,
       "L2ptProtocols": L2ptProtocols,
       "SvcISID": SvcISID,
       "L2RouteOrigin": L2RouteOrigin,
       "ConfigStatus": ConfigStatus,
       "ServAccessLocation": ServAccessLocation,
       "ServShcvOperState": ServShcvOperState,
       "tnServicesMIBModule": tnServicesMIBModule,
       "tnServObjs": tnServObjs,
       "tnCustObjs": tnCustObjs,
       "tnCustNumEntries": tnCustNumEntries,
       "tnCustNextFreeId": tnCustNextFreeId,
       "tnCustInfoTable": tnCustInfoTable,
       "tnCustInfoEntry": tnCustInfoEntry,
       "tnCustId": tnCustId,
       "tnCustRowStatus": tnCustRowStatus,
       "tnCustDescription": tnCustDescription,
       "tnCustContact": tnCustContact,
       "tnCustPhone": tnCustPhone,
       "tnCustLastMgmtChange": tnCustLastMgmtChange,
       "tnSvcObjs": tnSvcObjs,
       "tnSvcNumEntries": tnSvcNumEntries,
       "tnSvcBaseInfoTable": tnSvcBaseInfoTable,
       "tnSvcBaseInfoEntry": tnSvcBaseInfoEntry,
       "tnSvcId": tnSvcId,
       "tnSvcRowStatus": tnSvcRowStatus,
       "tnSvcType": tnSvcType,
       "tnSvcCustId": tnSvcCustId,
       "tnSvcIpRouting": tnSvcIpRouting,
       "tnSvcDescription": tnSvcDescription,
       "tnSvcMtu": tnSvcMtu,
       "tnSvcAdminStatus": tnSvcAdminStatus,
       "tnSvcOperStatus": tnSvcOperStatus,
       "tnSvcNumSaps": tnSvcNumSaps,
       "tnSvcNumSdps": tnSvcNumSdps,
       "tnSvcLastMgmtChange": tnSvcLastMgmtChange,
       "tnSvcDefMeshVcId": tnSvcDefMeshVcId,
       "tnSvcVpnId": tnSvcVpnId,
       "tnSvcVRouterId": tnSvcVRouterId,
       "tnSvcAutoBind": tnSvcAutoBind,
       "tnSvcLastStatusChange": tnSvcLastStatusChange,
       "tnSvcVllType": tnSvcVllType,
       "tnSvcMgmtVpls": tnSvcMgmtVpls,
       "tnSvcRadiusDiscovery": tnSvcRadiusDiscovery,
       "tnSvcRadiusUserNameType": tnSvcRadiusUserNameType,
       "tnSvcRadiusUserName": tnSvcRadiusUserName,
       "tnSvcVcSwitching": tnSvcVcSwitching,
       "tnSvcRadiusPEDiscPolicy": tnSvcRadiusPEDiscPolicy,
       "tnSvcRadiusDiscoveryShutdown": tnSvcRadiusDiscoveryShutdown,
       "tnSvcVplsType": tnSvcVplsType,
       "tnSvcNumMcStandbySaps": tnSvcNumMcStandbySaps,
       "tnSvcName": tnSvcName,
       "tnSvcTlsInfoTable": tnSvcTlsInfoTable,
       "tnSvcTlsInfoEntry": tnSvcTlsInfoEntry,
       "tnSvcTlsMacLearning": tnSvcTlsMacLearning,
       "tnSvcTlsDiscardUnknownDest": tnSvcTlsDiscardUnknownDest,
       "tnSvcTlsFdbTableSize": tnSvcTlsFdbTableSize,
       "tnSvcTlsFdbNumEntries": tnSvcTlsFdbNumEntries,
       "tnSvcTlsFdbNumStaticEntries": tnSvcTlsFdbNumStaticEntries,
       "tnSvcTlsFdbLocalAgeTime": tnSvcTlsFdbLocalAgeTime,
       "tnSvcTlsFdbRemoteAgeTime": tnSvcTlsFdbRemoteAgeTime,
       "tnSvcTlsStpAdminStatus": tnSvcTlsStpAdminStatus,
       "tnSvcTlsStpPriority": tnSvcTlsStpPriority,
       "tnSvcTlsStpBridgeAddress": tnSvcTlsStpBridgeAddress,
       "tnSvcTlsStpTimeSinceTopologyChange": tnSvcTlsStpTimeSinceTopologyChange,
       "tnSvcTlsStpTopologyChanges": tnSvcTlsStpTopologyChanges,
       "tnSvcTlsStpDesignatedRoot": tnSvcTlsStpDesignatedRoot,
       "tnSvcTlsStpRootCost": tnSvcTlsStpRootCost,
       "tnSvcTlsStpRootPort": tnSvcTlsStpRootPort,
       "tnSvcTlsStpMaxAge": tnSvcTlsStpMaxAge,
       "tnSvcTlsStpHelloTime": tnSvcTlsStpHelloTime,
       "tnSvcTlsStpForwardDelay": tnSvcTlsStpForwardDelay,
       "tnSvcTlsStpBridgeMaxAge": tnSvcTlsStpBridgeMaxAge,
       "tnSvcTlsStpBridgeHelloTime": tnSvcTlsStpBridgeHelloTime,
       "tnSvcTlsStpBridgeForwardDelay": tnSvcTlsStpBridgeForwardDelay,
       "tnSvcTlsStpOperStatus": tnSvcTlsStpOperStatus,
       "tnSvcTlsStpVirtualRootBridgeStatus": tnSvcTlsStpVirtualRootBridgeStatus,
       "tnSvcTlsMacAgeing": tnSvcTlsMacAgeing,
       "tnSvcTlsStpTopologyChangeActive": tnSvcTlsStpTopologyChangeActive,
       "tnSvcTlsFdbTableFullHighWatermark": tnSvcTlsFdbTableFullHighWatermark,
       "tnSvcTlsFdbTableFullLowWatermark": tnSvcTlsFdbTableFullLowWatermark,
       "tnSvcTlsVpnId": tnSvcTlsVpnId,
       "tnSvcTlsCustId": tnSvcTlsCustId,
       "tnSvcTlsStpVersion": tnSvcTlsStpVersion,
       "tnSvcTlsStpHoldCount": tnSvcTlsStpHoldCount,
       "tnSvcTlsStpPrimaryBridge": tnSvcTlsStpPrimaryBridge,
       "tnSvcTlsStpBridgeInstanceId": tnSvcTlsStpBridgeInstanceId,
       "tnSvcTlsStpVcpOperProtocol": tnSvcTlsStpVcpOperProtocol,
       "tnSvcTlsMacMoveMaxRate": tnSvcTlsMacMoveMaxRate,
       "tnSvcTlsMacMoveRetryTimeout": tnSvcTlsMacMoveRetryTimeout,
       "tnSvcTlsMacMoveAdminStatus": tnSvcTlsMacMoveAdminStatus,
       "tnSvcTlsMacRelearnOnly": tnSvcTlsMacRelearnOnly,
       "tnSvcTlsMfibTableSize": tnSvcTlsMfibTableSize,
       "tnSvcTlsMfibTableFullHighWatermark": tnSvcTlsMfibTableFullHighWatermark,
       "tnSvcTlsMfibTableFullLowWatermark": tnSvcTlsMfibTableFullLowWatermark,
       "tnSvcTlsMacFlushOnFail": tnSvcTlsMacFlushOnFail,
       "tnSvcTlsStpRegionName": tnSvcTlsStpRegionName,
       "tnSvcTlsStpRegionRevision": tnSvcTlsStpRegionRevision,
       "tnSvcTlsStpBridgeMaxHops": tnSvcTlsStpBridgeMaxHops,
       "tnSvcTlsStpCistRegionalRoot": tnSvcTlsStpCistRegionalRoot,
       "tnSvcTlsStpCistIntRootCost": tnSvcTlsStpCistIntRootCost,
       "tnSvcTlsStpCistRemainingHopCount": tnSvcTlsStpCistRemainingHopCount,
       "tnSvcTlsStpCistRegionalRootPort": tnSvcTlsStpCistRegionalRootPort,
       "tnSvcTlsFdbNumLearnedEntries": tnSvcTlsFdbNumLearnedEntries,
       "tnSvcTlsFdbNumOamEntries": tnSvcTlsFdbNumOamEntries,
       "tnSvcTlsFdbNumDhcpEntries": tnSvcTlsFdbNumDhcpEntries,
       "tnSvcTlsFdbNumHostEntries": tnSvcTlsFdbNumHostEntries,
       "tnSvcTlsShcvAction": tnSvcTlsShcvAction,
       "tnSvcTlsShcvSrcIp": tnSvcTlsShcvSrcIp,
       "tnSvcTlsShcvSrcMac": tnSvcTlsShcvSrcMac,
       "tnSvcTlsShcvInterval": tnSvcTlsShcvInterval,
       "tnSvcTlsPriPortsCumulativeFactor": tnSvcTlsPriPortsCumulativeFactor,
       "tnSvcTlsSecPortsCumulativeFactor": tnSvcTlsSecPortsCumulativeFactor,
       "tnSvcTlsL2ptTermEnabled": tnSvcTlsL2ptTermEnabled,
       "tnSvcTlsPropagateMacFlush": tnSvcTlsPropagateMacFlush,
       "tnSvcTlsMrpAdminStatus": tnSvcTlsMrpAdminStatus,
       "tnSvcTlsMrpMaxAttributes": tnSvcTlsMrpMaxAttributes,
       "tnSvcTlsMrpAttributeCount": tnSvcTlsMrpAttributeCount,
       "tnSvcTlsMrpFailedRegisterCount": tnSvcTlsMrpFailedRegisterCount,
       "tnSvcTlsMcPathMgmtPlcyName": tnSvcTlsMcPathMgmtPlcyName,
       "tnSvcTlsMrpFloodTime": tnSvcTlsMrpFloodTime,
       "tnSvcTlsMrpAttrTblHighWatermark": tnSvcTlsMrpAttrTblHighWatermark,
       "tnSvcTlsMrpAttrTblLowWatermark": tnSvcTlsMrpAttrTblLowWatermark,
       "tnSvcTlsMacMoveNumRetries": tnSvcTlsMacMoveNumRetries,
       "tnSvcTlsMacSubNetLen": tnSvcTlsMacSubNetLen,
       "tnSvcTlsSendFlushOnBVplsFail": tnSvcTlsSendFlushOnBVplsFail,
       "tnSvcTlsPropMacFlushFromBVpls": tnSvcTlsPropMacFlushFromBVpls,
       "tnSvcTlsMacNotifInterval": tnSvcTlsMacNotifInterval,
       "tnSvcTlsMacNotifCount": tnSvcTlsMacNotifCount,
       "tnSvcTlsMacNotifAdminState": tnSvcTlsMacNotifAdminState,
       "tnSvcTlsShcvRetryTimeout": tnSvcTlsShcvRetryTimeout,
       "tnSvcTlsShcvRetryCount": tnSvcTlsShcvRetryCount,
       "tnsvcTlsAllowIpIfBinding": tnsvcTlsAllowIpIfBinding,
       "tnTlsFdbInfoTable": tnTlsFdbInfoTable,
       "tnTlsFdbInfoEntry": tnTlsFdbInfoEntry,
       "tnTlsFdbMacAddr": tnTlsFdbMacAddr,
       "tnTlsFdbRowStatus": tnTlsFdbRowStatus,
       "tnTlsFdbType": tnTlsFdbType,
       "tnTlsFdbLocale": tnTlsFdbLocale,
       "tnTlsFdbPortId": tnTlsFdbPortId,
       "tnTlsFdbEncapValue": tnTlsFdbEncapValue,
       "tnTlsFdbSdpId": tnTlsFdbSdpId,
       "tnTlsFdbVcId": tnTlsFdbVcId,
       "tnTlsFdbVpnId": tnTlsFdbVpnId,
       "tnTlsFdbCustId": tnTlsFdbCustId,
       "tnTlsFdbLastStateChange": tnTlsFdbLastStateChange,
       "tnTlsFdbProtected": tnTlsFdbProtected,
       "tnTlsFdbBackboneDstMac": tnTlsFdbBackboneDstMac,
       "tnTlsFdbNumIVplsMac": tnTlsFdbNumIVplsMac,
       "tnTlsFdbEndPointName": tnTlsFdbEndPointName,
       "tnTlsFdbEPMacOperSdpId": tnTlsFdbEPMacOperSdpId,
       "tnTlsFdbEPMacOperVcId": tnTlsFdbEPMacOperVcId,
       "tnTlsFdbPbbNumEpipes": tnTlsFdbPbbNumEpipes,
       "tnTlsShgInfoTable": tnTlsShgInfoTable,
       "tnTlsShgInfoEntry": tnTlsShgInfoEntry,
       "tnTlsShgName": tnTlsShgName,
       "tnTlsShgRowStatus": tnTlsShgRowStatus,
       "tnTlsShgCustId": tnTlsShgCustId,
       "tnTlsShgInstanceId": tnTlsShgInstanceId,
       "tnTlsShgDescription": tnTlsShgDescription,
       "tnTlsShgLastMgmtChange": tnTlsShgLastMgmtChange,
       "tnTlsShgResidential": tnTlsShgResidential,
       "tnTlsShgRestProtSrcMac": tnTlsShgRestProtSrcMac,
       "tnTlsShgRestUnprotDstMac": tnTlsShgRestUnprotDstMac,
       "tnTlsShgRestProtSrcMacAction": tnTlsShgRestProtSrcMacAction,
       "tnTlsShgCreationOrigin": tnTlsShgCreationOrigin,
       "tnSvcTlsBackboneInfoTable": tnSvcTlsBackboneInfoTable,
       "tnSvcTlsBackboneInfoEntry": tnSvcTlsBackboneInfoEntry,
       "tnSvcTlsBackboneSrcMac": tnSvcTlsBackboneSrcMac,
       "tnSvcTlsBackboneVplsSvcId": tnSvcTlsBackboneVplsSvcId,
       "tnSvcTlsBackboneVplsSvcISID": tnSvcTlsBackboneVplsSvcISID,
       "tnSvcTlsBackboneOperSrcMac": tnSvcTlsBackboneOperSrcMac,
       "tnSvcTlsBackboneOperVplsSvcISID": tnSvcTlsBackboneOperVplsSvcISID,
       "tnSvcTlsBackboneLDPMacFlush": tnSvcTlsBackboneLDPMacFlush,
       "tnSvcTlsBackboneVplsStp": tnSvcTlsBackboneVplsStp,
       "tnSvcTlsBackboneLDPMacFlushNotMine": tnSvcTlsBackboneLDPMacFlushNotMine,
       "tnSvcTlsBackboneUseSapBMac": tnSvcTlsBackboneUseSapBMac,
       "tnTlsMFibTable": tnTlsMFibTable,
       "tnTlsMFibEntry": tnTlsMFibEntry,
       "tnTlsMFibEntryType": tnTlsMFibEntryType,
       "tnTlsMFibGrpMacAddr": tnTlsMFibGrpMacAddr,
       "tnTlsMFibGrpInetAddrType": tnTlsMFibGrpInetAddrType,
       "tnTlsMFibGrpInetAddr": tnTlsMFibGrpInetAddr,
       "tnTlsMFibSrcInetAddrType": tnTlsMFibSrcInetAddrType,
       "tnTlsMFibSrcInetAddr": tnTlsMFibSrcInetAddr,
       "tnTlsMFibLocale": tnTlsMFibLocale,
       "tnTlsMFibPortId": tnTlsMFibPortId,
       "tnTlsMFibEncapValue": tnTlsMFibEncapValue,
       "tnTlsMFibSdpId": tnTlsMFibSdpId,
       "tnTlsMFibVcId": tnTlsMFibVcId,
       "tnTlsMFibFwdOrBlk": tnTlsMFibFwdOrBlk,
       "tnTlsMFibSvcId": tnTlsMFibSvcId,
       "tnSvcTlsBgpADTableLastChanged": tnSvcTlsBgpADTableLastChanged,
       "tnSvcEpipePbbTableLastChanged": tnSvcEpipePbbTableLastChanged,
       "tnSvcTotalFdbMimDestIdxEntries": tnSvcTotalFdbMimDestIdxEntries,
       "tnSvcArpHostTableLastChanged": tnSvcArpHostTableLastChanged,
       "tnSvcArpHostIfTableLastMgmtChange": tnSvcArpHostIfTableLastMgmtChange,
       "tnSvcArpHostDefaultSessionTimeout": tnSvcArpHostDefaultSessionTimeout,
       "tnSvcIgmpTrkTableLastMgmtChange": tnSvcIgmpTrkTableLastMgmtChange,
       "tnSvcIpipeInfoTableLastMgmtChange": tnSvcIpipeInfoTableLastMgmtChange,
       "tnSvcMacNameTableLastChanged": tnSvcMacNameTableLastChanged,
       "tnSvcScalar1": tnSvcScalar1,
       "tnSvcScalar2": tnSvcScalar2,
       "tnSvcScalar3": tnSvcScalar3,
       "tnSvcScalar4": tnSvcScalar4,
       "tnSvcScalar5": tnSvcScalar5,
       "tnServNotifications": tnServNotifications,
       "tnCustTrapsPrefix": tnCustTrapsPrefix,
       "tnCustTraps": tnCustTraps,
       "tnSvcTrapsPrefix": tnSvcTrapsPrefix,
       "tnSvcTraps": tnSvcTraps,
       "tnTstpTrapsPrefix": tnTstpTrapsPrefix,
       "tnTstpTraps": tnTstpTraps}
)
