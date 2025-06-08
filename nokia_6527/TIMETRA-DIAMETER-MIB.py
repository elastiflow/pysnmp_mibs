# SNMP MIB module (TIMETRA-DIAMETER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-DIAMETER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:31 2025
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxBinarySpecification,
 TmnxEnabledDisabled,
 TmnxMacSpecification,
 TmnxSubCallingStationIdType,
 TmnxSubNasPortPrefixType,
 TmnxSubNasPortSuffixType,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxBinarySpecification",
    "TmnxEnabledDisabled",
    "TmnxMacSpecification",
    "TmnxSubCallingStationIdType",
    "TmnxSubNasPortPrefixType",
    "TmnxSubNasPortSuffixType",
    "TmnxVRtrID")


# MODULE-IDENTITY

timetraDiameterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 58)
)
if mibBuilder.loadTexts:
    timetraDiameterMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-02-28 12:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxDiamPeerTransportProt(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tcp", 1)
    )



class TmnxDiamCcFailureHndlng(TextualConvention, Integer32):
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
        *(("terminate", 1),
          ("continue", 2),
          ("retryAndTerminate", 3))
    )



class TmnxDiamDccaApplicationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vfDccaV2", 1),
          ("gx", 2))
    )



class TmnxDiamPlcyVendorSupportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vodafone", 1),
          ("threeGpp", 2))
    )



class TmnxDiamPlcyDccaAvpOriginType(TextualConvention, Integer32):
    status = "current"
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
        *(("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3),
          ("msisdn", 4),
          ("imei", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDiameterConformance_ObjectIdentity = ObjectIdentity
tmnxDiameterConformance = _TmnxDiameterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58)
)
_TmnxDiameterCompliances_ObjectIdentity = ObjectIdentity
tmnxDiameterCompliances = _TmnxDiameterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1)
)
_TmnxDiameterGroups_ObjectIdentity = ObjectIdentity
tmnxDiameterGroups = _TmnxDiameterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2)
)
_TmnxDiameter_ObjectIdentity = ObjectIdentity
tmnxDiameter = _TmnxDiameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58)
)
_TmnxDiameterBaseObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterBaseObjects = _TmnxDiameterBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1)
)
_TmnxDiameterPlcyTableLastChngd_Type = TimeStamp
_TmnxDiameterPlcyTableLastChngd_Object = MibScalar
tmnxDiameterPlcyTableLastChngd = _TmnxDiameterPlcyTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 1),
    _TmnxDiameterPlcyTableLastChngd_Type()
)
tmnxDiameterPlcyTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiameterPlcyTableLastChngd.setStatus("current")
_TmnxDiameterPlcyTable_Object = MibTable
tmnxDiameterPlcyTable = _TmnxDiameterPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyTable.setStatus("current")
_TmnxDiameterPlcyEntry_Object = MibTableRow
tmnxDiameterPlcyEntry = _TmnxDiameterPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1)
)
tmnxDiameterPlcyEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyEntry.setStatus("current")
_TmnxDiamPlcyName_Type = TNamedItem
_TmnxDiamPlcyName_Object = MibTableColumn
tmnxDiamPlcyName = _TmnxDiamPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 1),
    _TmnxDiamPlcyName_Type()
)
tmnxDiamPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPlcyName.setStatus("current")
_TmnxDiamPlcyRowStatus_Type = RowStatus
_TmnxDiamPlcyRowStatus_Object = MibTableColumn
tmnxDiamPlcyRowStatus = _TmnxDiamPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 2),
    _TmnxDiamPlcyRowStatus_Type()
)
tmnxDiamPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyRowStatus.setStatus("current")
_TmnxDiamPlcyLastMgmtChange_Type = TimeStamp
_TmnxDiamPlcyLastMgmtChange_Object = MibTableColumn
tmnxDiamPlcyLastMgmtChange = _TmnxDiamPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 3),
    _TmnxDiamPlcyLastMgmtChange_Type()
)
tmnxDiamPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyLastMgmtChange.setStatus("current")


class _TmnxDiamPlcyDescription_Type(TItemDescription):
    """Custom type tmnxDiamPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDiamPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxDiamPlcyDescription_Object = MibTableColumn
tmnxDiamPlcyDescription = _TmnxDiamPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 4),
    _TmnxDiamPlcyDescription_Type()
)
tmnxDiamPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDescription.setStatus("current")


class _TmnxDiamPlcyOriginHost_Type(DisplayString):
    """Custom type tmnxDiamPlcyOriginHost based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyOriginHost_Type.__name__ = "DisplayString"
_TmnxDiamPlcyOriginHost_Object = MibTableColumn
tmnxDiamPlcyOriginHost = _TmnxDiamPlcyOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 5),
    _TmnxDiamPlcyOriginHost_Type()
)
tmnxDiamPlcyOriginHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyOriginHost.setStatus("current")


class _TmnxDiamPlcyOriginRealm_Type(DisplayString):
    """Custom type tmnxDiamPlcyOriginRealm based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyOriginRealm_Type.__name__ = "DisplayString"
_TmnxDiamPlcyOriginRealm_Object = MibTableColumn
tmnxDiamPlcyOriginRealm = _TmnxDiamPlcyOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 6),
    _TmnxDiamPlcyOriginRealm_Type()
)
tmnxDiamPlcyOriginRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyOriginRealm.setStatus("current")


class _TmnxDiamPlcyRouter_Type(TmnxVRtrID):
    """Custom type tmnxDiamPlcyRouter based on TmnxVRtrID"""
    defaultValue = 1


_TmnxDiamPlcyRouter_Type.__name__ = "TmnxVRtrID"
_TmnxDiamPlcyRouter_Object = MibTableColumn
tmnxDiamPlcyRouter = _TmnxDiamPlcyRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 7),
    _TmnxDiamPlcyRouter_Type()
)
tmnxDiamPlcyRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyRouter.setStatus("current")


class _TmnxDiamPlcySourceAddrType_Type(InetAddressType):
    """Custom type tmnxDiamPlcySourceAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamPlcySourceAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamPlcySourceAddrType_Object = MibTableColumn
tmnxDiamPlcySourceAddrType = _TmnxDiamPlcySourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 8),
    _TmnxDiamPlcySourceAddrType_Type()
)
tmnxDiamPlcySourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcySourceAddrType.setStatus("current")


class _TmnxDiamPlcySourceAddr_Type(InetAddress):
    """Custom type tmnxDiamPlcySourceAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxDiamPlcySourceAddr_Type.__name__ = "InetAddress"
_TmnxDiamPlcySourceAddr_Object = MibTableColumn
tmnxDiamPlcySourceAddr = _TmnxDiamPlcySourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 9),
    _TmnxDiamPlcySourceAddr_Type()
)
tmnxDiamPlcySourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcySourceAddr.setStatus("current")


class _TmnxDiamPlcyWatchdogTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyWatchdogTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyWatchdogTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyWatchdogTimer_Object = MibTableColumn
tmnxDiamPlcyWatchdogTimer = _TmnxDiamPlcyWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 10),
    _TmnxDiamPlcyWatchdogTimer_Type()
)
tmnxDiamPlcyWatchdogTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyWatchdogTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyWatchdogTimer.setUnits("seconds")


class _TmnxDiamPlcyConnectionTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyConnectionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyConnectionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyConnectionTimer_Object = MibTableColumn
tmnxDiamPlcyConnectionTimer = _TmnxDiamPlcyConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 11),
    _TmnxDiamPlcyConnectionTimer_Type()
)
tmnxDiamPlcyConnectionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyConnectionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyConnectionTimer.setUnits("seconds")


class _TmnxDiamPlcyTransactionTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyTransactionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyTransactionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyTransactionTimer_Object = MibTableColumn
tmnxDiamPlcyTransactionTimer = _TmnxDiamPlcyTransactionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 12),
    _TmnxDiamPlcyTransactionTimer_Type()
)
tmnxDiamPlcyTransactionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyTransactionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyTransactionTimer.setUnits("seconds")


class _TmnxDiamPlcyVendorSupport_Type(TmnxDiamPlcyVendorSupportType):
    """Custom type tmnxDiamPlcyVendorSupport based on TmnxDiamPlcyVendorSupportType"""
    defaultValue = 2


_TmnxDiamPlcyVendorSupport_Type.__name__ = "TmnxDiamPlcyVendorSupportType"
_TmnxDiamPlcyVendorSupport_Object = MibTableColumn
tmnxDiamPlcyVendorSupport = _TmnxDiamPlcyVendorSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 13),
    _TmnxDiamPlcyVendorSupport_Type()
)
tmnxDiamPlcyVendorSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyVendorSupport.setStatus("current")


class _TmnxDiamPlcyApplications_Type(Bits):
    """Custom type tmnxDiamPlcyApplications based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("gx", 0),
          ("gy", 1))
    )

_TmnxDiamPlcyApplications_Type.__name__ = "Bits"
_TmnxDiamPlcyApplications_Object = MibTableColumn
tmnxDiamPlcyApplications = _TmnxDiamPlcyApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 15),
    _TmnxDiamPlcyApplications_Type()
)
tmnxDiamPlcyApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyApplications.setStatus("current")


class _TmnxDiamPlcyPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamPlcyPythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamPlcyPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamPlcyPythonPolicy_Object = MibTableColumn
tmnxDiamPlcyPythonPolicy = _TmnxDiamPlcyPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 16),
    _TmnxDiamPlcyPythonPolicy_Type()
)
tmnxDiamPlcyPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPythonPolicy.setStatus("current")
_TmnxDiamPlcyPeerTableLastChngd_Type = TimeStamp
_TmnxDiamPlcyPeerTableLastChngd_Object = MibScalar
tmnxDiamPlcyPeerTableLastChngd = _TmnxDiamPlcyPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 3),
    _TmnxDiamPlcyPeerTableLastChngd_Type()
)
tmnxDiamPlcyPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTableLastChngd.setStatus("current")
_TmnxDiameterPlcyPeerTable_Object = MibTable
tmnxDiameterPlcyPeerTable = _TmnxDiameterPlcyPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyPeerTable.setStatus("current")
_TmnxDiameterPlcyPeerEntry_Object = MibTableRow
tmnxDiameterPlcyPeerEntry = _TmnxDiameterPlcyPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1)
)
tmnxDiameterPlcyPeerEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerName"),
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyPeerEntry.setStatus("current")
_TmnxDiamPlcyPeerName_Type = TNamedItem
_TmnxDiamPlcyPeerName_Object = MibTableColumn
tmnxDiamPlcyPeerName = _TmnxDiamPlcyPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 1),
    _TmnxDiamPlcyPeerName_Type()
)
tmnxDiamPlcyPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerName.setStatus("current")
_TmnxDiamPlcyPeerRowStatus_Type = RowStatus
_TmnxDiamPlcyPeerRowStatus_Object = MibTableColumn
tmnxDiamPlcyPeerRowStatus = _TmnxDiamPlcyPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 2),
    _TmnxDiamPlcyPeerRowStatus_Type()
)
tmnxDiamPlcyPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerRowStatus.setStatus("current")
_TmnxDiamPlcyPeerLastMgmtChange_Type = TimeStamp
_TmnxDiamPlcyPeerLastMgmtChange_Object = MibTableColumn
tmnxDiamPlcyPeerLastMgmtChange = _TmnxDiamPlcyPeerLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 3),
    _TmnxDiamPlcyPeerLastMgmtChange_Type()
)
tmnxDiamPlcyPeerLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerLastMgmtChange.setStatus("current")


class _TmnxDiamPlcyPeerAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxDiamPlcyPeerAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDiamPlcyPeerAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDiamPlcyPeerAdminState_Object = MibTableColumn
tmnxDiamPlcyPeerAdminState = _TmnxDiamPlcyPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 4),
    _TmnxDiamPlcyPeerAdminState_Type()
)
tmnxDiamPlcyPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerAdminState.setStatus("current")


class _TmnxDiamPlcyPeerAddrType_Type(InetAddressType):
    """Custom type tmnxDiamPlcyPeerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamPlcyPeerAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamPlcyPeerAddrType_Object = MibTableColumn
tmnxDiamPlcyPeerAddrType = _TmnxDiamPlcyPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 5),
    _TmnxDiamPlcyPeerAddrType_Type()
)
tmnxDiamPlcyPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerAddrType.setStatus("current")


class _TmnxDiamPlcyPeerAddr_Type(InetAddress):
    """Custom type tmnxDiamPlcyPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxDiamPlcyPeerAddr_Type.__name__ = "InetAddress"
_TmnxDiamPlcyPeerAddr_Object = MibTableColumn
tmnxDiamPlcyPeerAddr = _TmnxDiamPlcyPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 6),
    _TmnxDiamPlcyPeerAddr_Type()
)
tmnxDiamPlcyPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerAddr.setStatus("current")


class _TmnxDiamPlcyPeerTransportProt_Type(TmnxDiamPeerTransportProt):
    """Custom type tmnxDiamPlcyPeerTransportProt based on TmnxDiamPeerTransportProt"""
    defaultValue = 1


_TmnxDiamPlcyPeerTransportProt_Type.__name__ = "TmnxDiamPeerTransportProt"
_TmnxDiamPlcyPeerTransportProt_Object = MibTableColumn
tmnxDiamPlcyPeerTransportProt = _TmnxDiamPlcyPeerTransportProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 7),
    _TmnxDiamPlcyPeerTransportProt_Type()
)
tmnxDiamPlcyPeerTransportProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransportProt.setStatus("current")


class _TmnxDiamPlcyPeerTransportPort_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerTransportPort based on Unsigned32"""
    defaultValue = 3868

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxDiamPlcyPeerTransportPort_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerTransportPort_Object = MibTableColumn
tmnxDiamPlcyPeerTransportPort = _TmnxDiamPlcyPeerTransportPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 8),
    _TmnxDiamPlcyPeerTransportPort_Type()
)
tmnxDiamPlcyPeerTransportPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransportPort.setStatus("current")


class _TmnxDiamPlcyPeerDestHost_Type(DisplayString):
    """Custom type tmnxDiamPlcyPeerDestHost based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyPeerDestHost_Type.__name__ = "DisplayString"
_TmnxDiamPlcyPeerDestHost_Object = MibTableColumn
tmnxDiamPlcyPeerDestHost = _TmnxDiamPlcyPeerDestHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 9),
    _TmnxDiamPlcyPeerDestHost_Type()
)
tmnxDiamPlcyPeerDestHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerDestHost.setStatus("current")


class _TmnxDiamPlcyPeerDestRealm_Type(DisplayString):
    """Custom type tmnxDiamPlcyPeerDestRealm based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyPeerDestRealm_Type.__name__ = "DisplayString"
_TmnxDiamPlcyPeerDestRealm_Object = MibTableColumn
tmnxDiamPlcyPeerDestRealm = _TmnxDiamPlcyPeerDestRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 10),
    _TmnxDiamPlcyPeerDestRealm_Type()
)
tmnxDiamPlcyPeerDestRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerDestRealm.setStatus("current")


class _TmnxDiamPlcyPeerWatchdogTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerWatchdogTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyPeerWatchdogTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerWatchdogTimer_Object = MibTableColumn
tmnxDiamPlcyPeerWatchdogTimer = _TmnxDiamPlcyPeerWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 11),
    _TmnxDiamPlcyPeerWatchdogTimer_Type()
)
tmnxDiamPlcyPeerWatchdogTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerWatchdogTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerWatchdogTimer.setUnits("seconds")


class _TmnxDiamPlcyPeerConnectionTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerConnectionTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyPeerConnectionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerConnectionTimer_Object = MibTableColumn
tmnxDiamPlcyPeerConnectionTimer = _TmnxDiamPlcyPeerConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 12),
    _TmnxDiamPlcyPeerConnectionTimer_Type()
)
tmnxDiamPlcyPeerConnectionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerConnectionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerConnectionTimer.setUnits("seconds")


class _TmnxDiamPlcyPeerTransactTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerTransactTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyPeerTransactTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerTransactTimer_Object = MibTableColumn
tmnxDiamPlcyPeerTransactTimer = _TmnxDiamPlcyPeerTransactTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 13),
    _TmnxDiamPlcyPeerTransactTimer_Type()
)
tmnxDiamPlcyPeerTransactTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransactTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransactTimer.setUnits("seconds")


class _TmnxDiamPlcyPeerPreference_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerPreference based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxDiamPlcyPeerPreference_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerPreference_Object = MibTableColumn
tmnxDiamPlcyPeerPreference = _TmnxDiamPlcyPeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 14),
    _TmnxDiamPlcyPeerPreference_Type()
)
tmnxDiamPlcyPeerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerPreference.setStatus("current")
_TmnxDiamPlcyPeerInfoTable_Object = MibTable
tmnxDiamPlcyPeerInfoTable = _TmnxDiamPlcyPeerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerInfoTable.setStatus("current")
_TmnxDiamPlcyPeerInfoEntry_Object = MibTableRow
tmnxDiamPlcyPeerInfoEntry = _TmnxDiamPlcyPeerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerInfoEntry.setStatus("current")


class _TmnxDiamPeerPsmState_Type(Integer32):
    """Custom type tmnxDiamPeerPsmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("wait-conn-ack", 1),
          ("wait-i-cea", 2),
          ("i-open", 3),
          ("closing", 4))
    )


_TmnxDiamPeerPsmState_Type.__name__ = "Integer32"
_TmnxDiamPeerPsmState_Object = MibTableColumn
tmnxDiamPeerPsmState = _TmnxDiamPeerPsmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 1),
    _TmnxDiamPeerPsmState_Type()
)
tmnxDiamPeerPsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPsmState.setStatus("current")
_TmnxDiamPeerConnectionSuspended_Type = TruthValue
_TmnxDiamPeerConnectionSuspended_Object = MibTableColumn
tmnxDiamPeerConnectionSuspended = _TmnxDiamPeerConnectionSuspended_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 2),
    _TmnxDiamPeerConnectionSuspended_Type()
)
tmnxDiamPeerConnectionSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerConnectionSuspended.setStatus("current")


class _TmnxDiamPeerCooldownSeqStage_Type(Integer32):
    """Custom type tmnxDiamPeerCooldownSeqStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stage1", 0),
          ("stage2", 1),
          ("stage3", 2))
    )


_TmnxDiamPeerCooldownSeqStage_Type.__name__ = "Integer32"
_TmnxDiamPeerCooldownSeqStage_Object = MibTableColumn
tmnxDiamPeerCooldownSeqStage = _TmnxDiamPeerCooldownSeqStage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 3),
    _TmnxDiamPeerCooldownSeqStage_Type()
)
tmnxDiamPeerCooldownSeqStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerCooldownSeqStage.setStatus("current")
_TmnxDiamPeerOrder_Type = Unsigned32
_TmnxDiamPeerOrder_Object = MibTableColumn
tmnxDiamPeerOrder = _TmnxDiamPeerOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 4),
    _TmnxDiamPeerOrder_Type()
)
tmnxDiamPeerOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerOrder.setStatus("current")


class _TmnxDiamPeerPrimarySecondary_Type(Integer32):
    """Custom type tmnxDiamPeerPrimarySecondary based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2))
    )


_TmnxDiamPeerPrimarySecondary_Type.__name__ = "Integer32"
_TmnxDiamPeerPrimarySecondary_Object = MibTableColumn
tmnxDiamPeerPrimarySecondary = _TmnxDiamPeerPrimarySecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 5),
    _TmnxDiamPeerPrimarySecondary_Type()
)
tmnxDiamPeerPrimarySecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPrimarySecondary.setStatus("current")
_TmnxDiamPeerTcTimerTimeLeft_Type = Unsigned32
_TmnxDiamPeerTcTimerTimeLeft_Object = MibTableColumn
tmnxDiamPeerTcTimerTimeLeft = _TmnxDiamPeerTcTimerTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 6),
    _TmnxDiamPeerTcTimerTimeLeft_Type()
)
tmnxDiamPeerTcTimerTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerTcTimerTimeLeft.setStatus("current")
_TmnxDiamPeerTtTimerTimeLeft_Type = Unsigned32
_TmnxDiamPeerTtTimerTimeLeft_Object = MibTableColumn
tmnxDiamPeerTtTimerTimeLeft = _TmnxDiamPeerTtTimerTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 7),
    _TmnxDiamPeerTtTimerTimeLeft_Type()
)
tmnxDiamPeerTtTimerTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerTtTimerTimeLeft.setStatus("current")
_TmnxDiamPeerTwTimerTimeLeft_Type = Unsigned32
_TmnxDiamPeerTwTimerTimeLeft_Object = MibTableColumn
tmnxDiamPeerTwTimerTimeLeft = _TmnxDiamPeerTwTimerTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 8),
    _TmnxDiamPeerTwTimerTimeLeft_Type()
)
tmnxDiamPeerTwTimerTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerTwTimerTimeLeft.setStatus("current")
_TmnxDiamPeerWatchdogAlgActive_Type = TruthValue
_TmnxDiamPeerWatchdogAlgActive_Object = MibTableColumn
tmnxDiamPeerWatchdogAlgActive = _TmnxDiamPeerWatchdogAlgActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 9),
    _TmnxDiamPeerWatchdogAlgActive_Type()
)
tmnxDiamPeerWatchdogAlgActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerWatchdogAlgActive.setStatus("current")
_TmnxDiamPeerWatchdogAnswPending_Type = TruthValue
_TmnxDiamPeerWatchdogAnswPending_Object = MibTableColumn
tmnxDiamPeerWatchdogAnswPending = _TmnxDiamPeerWatchdogAnswPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 10),
    _TmnxDiamPeerWatchdogAnswPending_Type()
)
tmnxDiamPeerWatchdogAnswPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerWatchdogAnswPending.setStatus("current")
_TmnxDiamPeerCooldownSeqPending_Type = TruthValue
_TmnxDiamPeerCooldownSeqPending_Object = MibTableColumn
tmnxDiamPeerCooldownSeqPending = _TmnxDiamPeerCooldownSeqPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 11),
    _TmnxDiamPeerCooldownSeqPending_Type()
)
tmnxDiamPeerCooldownSeqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerCooldownSeqPending.setStatus("current")
_TmnxDiamPeerCooldownSeqActive_Type = TruthValue
_TmnxDiamPeerCooldownSeqActive_Object = MibTableColumn
tmnxDiamPeerCooldownSeqActive = _TmnxDiamPeerCooldownSeqActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 12),
    _TmnxDiamPeerCooldownSeqActive_Type()
)
tmnxDiamPeerCooldownSeqActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerCooldownSeqActive.setStatus("current")
_TmnxDiamPeerPeerRemovalPending_Type = TruthValue
_TmnxDiamPeerPeerRemovalPending_Object = MibTableColumn
tmnxDiamPeerPeerRemovalPending = _TmnxDiamPeerPeerRemovalPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 13),
    _TmnxDiamPeerPeerRemovalPending_Type()
)
tmnxDiamPeerPeerRemovalPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPeerRemovalPending.setStatus("current")
_TmnxDiamPlcyPeerStatsTable_Object = MibTable
tmnxDiamPlcyPeerStatsTable = _TmnxDiamPlcyPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerStatsTable.setStatus("current")
_TmnxDiamPlcyPeerStatsEntry_Object = MibTableRow
tmnxDiamPlcyPeerStatsEntry = _TmnxDiamPlcyPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerStatsEntry.setStatus("current")
_TmnxDiamPeerStatsLastClearTime_Type = TimeStamp
_TmnxDiamPeerStatsLastClearTime_Object = MibTableColumn
tmnxDiamPeerStatsLastClearTime = _TmnxDiamPeerStatsLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 1),
    _TmnxDiamPeerStatsLastClearTime_Type()
)
tmnxDiamPeerStatsLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsLastClearTime.setStatus("current")
_TmnxDiamPeerStCiTcpSendFailed_Type = Counter32
_TmnxDiamPeerStCiTcpSendFailed_Object = MibTableColumn
tmnxDiamPeerStCiTcpSendFailed = _TmnxDiamPeerStCiTcpSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 2),
    _TmnxDiamPeerStCiTcpSendFailed_Type()
)
tmnxDiamPeerStCiTcpSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiTcpSendFailed.setStatus("current")
_TmnxDiamPeerStCiDiamRxDropCnt_Type = Counter32
_TmnxDiamPeerStCiDiamRxDropCnt_Object = MibTableColumn
tmnxDiamPeerStCiDiamRxDropCnt = _TmnxDiamPeerStCiDiamRxDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 3),
    _TmnxDiamPeerStCiDiamRxDropCnt_Type()
)
tmnxDiamPeerStCiDiamRxDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiDiamRxDropCnt.setStatus("current")
_TmnxDiamPeerStCiDiamTxReqs_Type = Counter32
_TmnxDiamPeerStCiDiamTxReqs_Object = MibTableColumn
tmnxDiamPeerStCiDiamTxReqs = _TmnxDiamPeerStCiDiamTxReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 4),
    _TmnxDiamPeerStCiDiamTxReqs_Type()
)
tmnxDiamPeerStCiDiamTxReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiDiamTxReqs.setStatus("current")
_TmnxDiamPeerStCiDiamRxResps_Type = Counter32
_TmnxDiamPeerStCiDiamRxResps_Object = MibTableColumn
tmnxDiamPeerStCiDiamRxResps = _TmnxDiamPeerStCiDiamRxResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 5),
    _TmnxDiamPeerStCiDiamRxResps_Type()
)
tmnxDiamPeerStCiDiamRxResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiDiamRxResps.setStatus("current")
_TmnxDiamPeerStCiPendMsgsPMQ_Type = Counter32
_TmnxDiamPeerStCiPendMsgsPMQ_Object = MibTableColumn
tmnxDiamPeerStCiPendMsgsPMQ = _TmnxDiamPeerStCiPendMsgsPMQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 6),
    _TmnxDiamPeerStCiPendMsgsPMQ_Type()
)
tmnxDiamPeerStCiPendMsgsPMQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiPendMsgsPMQ.setStatus("current")
_TmnxDiamPeerStCiReqTimeoutsPMQ_Type = Counter32
_TmnxDiamPeerStCiReqTimeoutsPMQ_Object = MibTableColumn
tmnxDiamPeerStCiReqTimeoutsPMQ = _TmnxDiamPeerStCiReqTimeoutsPMQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 7),
    _TmnxDiamPeerStCiReqTimeoutsPMQ_Type()
)
tmnxDiamPeerStCiReqTimeoutsPMQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiReqTimeoutsPMQ.setStatus("current")
_TmnxDiamPeerStSiTcpSendFailed_Type = Counter32
_TmnxDiamPeerStSiTcpSendFailed_Object = MibTableColumn
tmnxDiamPeerStSiTcpSendFailed = _TmnxDiamPeerStSiTcpSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 8),
    _TmnxDiamPeerStSiTcpSendFailed_Type()
)
tmnxDiamPeerStSiTcpSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiTcpSendFailed.setStatus("current")
_TmnxDiamPeerStSiDiamRxDropCnt_Type = Counter32
_TmnxDiamPeerStSiDiamRxDropCnt_Object = MibTableColumn
tmnxDiamPeerStSiDiamRxDropCnt = _TmnxDiamPeerStSiDiamRxDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 9),
    _TmnxDiamPeerStSiDiamRxDropCnt_Type()
)
tmnxDiamPeerStSiDiamRxDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiDiamRxDropCnt.setStatus("current")
_TmnxDiamPeerStSiDiamRxReqs_Type = Counter32
_TmnxDiamPeerStSiDiamRxReqs_Object = MibTableColumn
tmnxDiamPeerStSiDiamRxReqs = _TmnxDiamPeerStSiDiamRxReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 10),
    _TmnxDiamPeerStSiDiamRxReqs_Type()
)
tmnxDiamPeerStSiDiamRxReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiDiamRxReqs.setStatus("current")
_TmnxDiamPeerStSiDiamTxResps_Type = Counter32
_TmnxDiamPeerStSiDiamTxResps_Object = MibTableColumn
tmnxDiamPeerStSiDiamTxResps = _TmnxDiamPeerStSiDiamTxResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 11),
    _TmnxDiamPeerStSiDiamTxResps_Type()
)
tmnxDiamPeerStSiDiamTxResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiDiamTxResps.setStatus("current")
_TmnxDiamPeerStErrHdlDiamTxErrCnt_Type = Counter32
_TmnxDiamPeerStErrHdlDiamTxErrCnt_Object = MibTableColumn
tmnxDiamPeerStErrHdlDiamTxErrCnt = _TmnxDiamPeerStErrHdlDiamTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 12),
    _TmnxDiamPeerStErrHdlDiamTxErrCnt_Type()
)
tmnxDiamPeerStErrHdlDiamTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStErrHdlDiamTxErrCnt.setStatus("current")
_TmnxDiamPeerStErrHdlDiamRxErrCnt_Type = Counter32
_TmnxDiamPeerStErrHdlDiamRxErrCnt_Object = MibTableColumn
tmnxDiamPeerStErrHdlDiamRxErrCnt = _TmnxDiamPeerStErrHdlDiamRxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 13),
    _TmnxDiamPeerStErrHdlDiamRxErrCnt_Type()
)
tmnxDiamPeerStErrHdlDiamRxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStErrHdlDiamRxErrCnt.setStatus("current")
_TmnxDiamPeerStCcrInitialTx_Type = Counter32
_TmnxDiamPeerStCcrInitialTx_Object = MibTableColumn
tmnxDiamPeerStCcrInitialTx = _TmnxDiamPeerStCcrInitialTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 14),
    _TmnxDiamPeerStCcrInitialTx_Type()
)
tmnxDiamPeerStCcrInitialTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcrInitialTx.setStatus("current")
_TmnxDiamPeerStCcaInitialRx_Type = Counter32
_TmnxDiamPeerStCcaInitialRx_Object = MibTableColumn
tmnxDiamPeerStCcaInitialRx = _TmnxDiamPeerStCcaInitialRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 15),
    _TmnxDiamPeerStCcaInitialRx_Type()
)
tmnxDiamPeerStCcaInitialRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcaInitialRx.setStatus("current")
_TmnxDiamPeerStCcrUpdateTx_Type = Counter32
_TmnxDiamPeerStCcrUpdateTx_Object = MibTableColumn
tmnxDiamPeerStCcrUpdateTx = _TmnxDiamPeerStCcrUpdateTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 16),
    _TmnxDiamPeerStCcrUpdateTx_Type()
)
tmnxDiamPeerStCcrUpdateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcrUpdateTx.setStatus("current")
_TmnxDiamPeerStCcaUpdateRx_Type = Counter32
_TmnxDiamPeerStCcaUpdateRx_Object = MibTableColumn
tmnxDiamPeerStCcaUpdateRx = _TmnxDiamPeerStCcaUpdateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 17),
    _TmnxDiamPeerStCcaUpdateRx_Type()
)
tmnxDiamPeerStCcaUpdateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcaUpdateRx.setStatus("current")
_TmnxDiamPeerStCcrTerminateTx_Type = Counter32
_TmnxDiamPeerStCcrTerminateTx_Object = MibTableColumn
tmnxDiamPeerStCcrTerminateTx = _TmnxDiamPeerStCcrTerminateTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 18),
    _TmnxDiamPeerStCcrTerminateTx_Type()
)
tmnxDiamPeerStCcrTerminateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcrTerminateTx.setStatus("current")
_TmnxDiamPeerStCcaTerminateRx_Type = Counter32
_TmnxDiamPeerStCcaTerminateRx_Object = MibTableColumn
tmnxDiamPeerStCcaTerminateRx = _TmnxDiamPeerStCcaTerminateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 19),
    _TmnxDiamPeerStCcaTerminateRx_Type()
)
tmnxDiamPeerStCcaTerminateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcaTerminateRx.setStatus("current")
_TmnxDiamPeerStCerTx_Type = Counter32
_TmnxDiamPeerStCerTx_Object = MibTableColumn
tmnxDiamPeerStCerTx = _TmnxDiamPeerStCerTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 20),
    _TmnxDiamPeerStCerTx_Type()
)
tmnxDiamPeerStCerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCerTx.setStatus("current")
_TmnxDiamPeerStCeaRx_Type = Counter32
_TmnxDiamPeerStCeaRx_Object = MibTableColumn
tmnxDiamPeerStCeaRx = _TmnxDiamPeerStCeaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 21),
    _TmnxDiamPeerStCeaRx_Type()
)
tmnxDiamPeerStCeaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCeaRx.setStatus("current")
_TmnxDiamPeerStWdrTx_Type = Counter32
_TmnxDiamPeerStWdrTx_Object = MibTableColumn
tmnxDiamPeerStWdrTx = _TmnxDiamPeerStWdrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 24),
    _TmnxDiamPeerStWdrTx_Type()
)
tmnxDiamPeerStWdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdrTx.setStatus("current")
_TmnxDiamPeerStWdaRx_Type = Counter32
_TmnxDiamPeerStWdaRx_Object = MibTableColumn
tmnxDiamPeerStWdaRx = _TmnxDiamPeerStWdaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 25),
    _TmnxDiamPeerStWdaRx_Type()
)
tmnxDiamPeerStWdaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdaRx.setStatus("current")
_TmnxDiamPeerStWdrRx_Type = Counter32
_TmnxDiamPeerStWdrRx_Object = MibTableColumn
tmnxDiamPeerStWdrRx = _TmnxDiamPeerStWdrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 26),
    _TmnxDiamPeerStWdrRx_Type()
)
tmnxDiamPeerStWdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdrRx.setStatus("current")
_TmnxDiamPeerStWdaTx_Type = Counter32
_TmnxDiamPeerStWdaTx_Object = MibTableColumn
tmnxDiamPeerStWdaTx = _TmnxDiamPeerStWdaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 27),
    _TmnxDiamPeerStWdaTx_Type()
)
tmnxDiamPeerStWdaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdaTx.setStatus("current")
_TmnxDiamPeerStAsrRx_Type = Counter32
_TmnxDiamPeerStAsrRx_Object = MibTableColumn
tmnxDiamPeerStAsrRx = _TmnxDiamPeerStAsrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 30),
    _TmnxDiamPeerStAsrRx_Type()
)
tmnxDiamPeerStAsrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStAsrRx.setStatus("current")
_TmnxDiamPeerStAsaTx_Type = Counter32
_TmnxDiamPeerStAsaTx_Object = MibTableColumn
tmnxDiamPeerStAsaTx = _TmnxDiamPeerStAsaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 31),
    _TmnxDiamPeerStAsaTx_Type()
)
tmnxDiamPeerStAsaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStAsaTx.setStatus("current")
_TmnxDiamPeerStRarRx_Type = Counter32
_TmnxDiamPeerStRarRx_Object = MibTableColumn
tmnxDiamPeerStRarRx = _TmnxDiamPeerStRarRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 34),
    _TmnxDiamPeerStRarRx_Type()
)
tmnxDiamPeerStRarRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStRarRx.setStatus("current")
_TmnxDiamPeerStRaaTx_Type = Counter32
_TmnxDiamPeerStRaaTx_Object = MibTableColumn
tmnxDiamPeerStRaaTx = _TmnxDiamPeerStRaaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 35),
    _TmnxDiamPeerStRaaTx_Type()
)
tmnxDiamPeerStRaaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStRaaTx.setStatus("current")
_TmnxDiamPeerStDprTx_Type = Counter32
_TmnxDiamPeerStDprTx_Object = MibTableColumn
tmnxDiamPeerStDprTx = _TmnxDiamPeerStDprTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 36),
    _TmnxDiamPeerStDprTx_Type()
)
tmnxDiamPeerStDprTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDprTx.setStatus("current")
_TmnxDiamPeerStDpaRx_Type = Counter32
_TmnxDiamPeerStDpaRx_Object = MibTableColumn
tmnxDiamPeerStDpaRx = _TmnxDiamPeerStDpaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 37),
    _TmnxDiamPeerStDpaRx_Type()
)
tmnxDiamPeerStDpaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDpaRx.setStatus("current")
_TmnxDiamPeerStDprRx_Type = Counter32
_TmnxDiamPeerStDprRx_Object = MibTableColumn
tmnxDiamPeerStDprRx = _TmnxDiamPeerStDprRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 38),
    _TmnxDiamPeerStDprRx_Type()
)
tmnxDiamPeerStDprRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDprRx.setStatus("current")
_TmnxDiamPeerStDpaTx_Type = Counter32
_TmnxDiamPeerStDpaTx_Object = MibTableColumn
tmnxDiamPeerStDpaTx = _TmnxDiamPeerStDpaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 39),
    _TmnxDiamPeerStDpaTx_Type()
)
tmnxDiamPeerStDpaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDpaTx.setStatus("current")
_TmnxDiameterDccaObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterDccaObjects = _TmnxDiameterDccaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2)
)
_TmnxDiamPlcyDccaTableLastChngd_Type = TimeStamp
_TmnxDiamPlcyDccaTableLastChngd_Object = MibScalar
tmnxDiamPlcyDccaTableLastChngd = _TmnxDiamPlcyDccaTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 1),
    _TmnxDiamPlcyDccaTableLastChngd_Type()
)
tmnxDiamPlcyDccaTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTableLastChngd.setStatus("obsolete")
_TmnxDiameterPlcyDccaTable_Object = MibTable
tmnxDiameterPlcyDccaTable = _TmnxDiameterPlcyDccaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyDccaTable.setStatus("obsolete")
_TmnxDiameterPlcyDccaEntry_Object = MibTableRow
tmnxDiameterPlcyDccaEntry = _TmnxDiameterPlcyDccaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyDccaEntry.setStatus("obsolete")
_TmnxDiamPlcyDccaLastMgmtChange_Type = TimeStamp
_TmnxDiamPlcyDccaLastMgmtChange_Object = MibTableColumn
tmnxDiamPlcyDccaLastMgmtChange = _TmnxDiamPlcyDccaLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 1),
    _TmnxDiamPlcyDccaLastMgmtChange_Type()
)
tmnxDiamPlcyDccaLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaLastMgmtChange.setStatus("obsolete")


class _TmnxDiamPlcyDccaFailover_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaFailover based on TruthValue"""
    defaultValue = 1


_TmnxDiamPlcyDccaFailover_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaFailover_Object = MibTableColumn
tmnxDiamPlcyDccaFailover = _TmnxDiamPlcyDccaFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 2),
    _TmnxDiamPlcyDccaFailover_Type()
)
tmnxDiamPlcyDccaFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaFailover.setStatus("obsolete")


class _TmnxDiamPlcyDccaFailureHndlng_Type(TmnxDiamCcFailureHndlng):
    """Custom type tmnxDiamPlcyDccaFailureHndlng based on TmnxDiamCcFailureHndlng"""
    defaultValue = 1


_TmnxDiamPlcyDccaFailureHndlng_Type.__name__ = "TmnxDiamCcFailureHndlng"
_TmnxDiamPlcyDccaFailureHndlng_Object = MibTableColumn
tmnxDiamPlcyDccaFailureHndlng = _TmnxDiamPlcyDccaFailureHndlng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 3),
    _TmnxDiamPlcyDccaFailureHndlng_Type()
)
tmnxDiamPlcyDccaFailureHndlng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaFailureHndlng.setStatus("obsolete")


class _TmnxDiamPlcyDccaTxTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyDccaTxTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxDiamPlcyDccaTxTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyDccaTxTimer_Object = MibTableColumn
tmnxDiamPlcyDccaTxTimer = _TmnxDiamPlcyDccaTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 4),
    _TmnxDiamPlcyDccaTxTimer_Type()
)
tmnxDiamPlcyDccaTxTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTxTimer.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTxTimer.setUnits("seconds")


class _TmnxDiamPlcyDccaAvpServCntxtId_Type(DisplayString):
    """Custom type tmnxDiamPlcyDccaAvpServCntxtId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDiamPlcyDccaAvpServCntxtId_Type.__name__ = "DisplayString"
_TmnxDiamPlcyDccaAvpServCntxtId_Object = MibTableColumn
tmnxDiamPlcyDccaAvpServCntxtId = _TmnxDiamPlcyDccaAvpServCntxtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 5),
    _TmnxDiamPlcyDccaAvpServCntxtId_Type()
)
tmnxDiamPlcyDccaAvpServCntxtId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpServCntxtId.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpCldStationId_Type(DisplayString):
    """Custom type tmnxDiamPlcyDccaAvpCldStationId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamPlcyDccaAvpCldStationId_Type.__name__ = "DisplayString"
_TmnxDiamPlcyDccaAvpCldStationId_Object = MibTableColumn
tmnxDiamPlcyDccaAvpCldStationId = _TmnxDiamPlcyDccaAvpCldStationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 6),
    _TmnxDiamPlcyDccaAvpCldStationId_Type()
)
tmnxDiamPlcyDccaAvpCldStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpCldStationId.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpRadiusUsrNme_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaAvpRadiusUsrNme based on TruthValue"""
    defaultValue = 2


_TmnxDiamPlcyDccaAvpRadiusUsrNme_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaAvpRadiusUsrNme_Object = MibTableColumn
tmnxDiamPlcyDccaAvpRadiusUsrNme = _TmnxDiamPlcyDccaAvpRadiusUsrNme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 7),
    _TmnxDiamPlcyDccaAvpRadiusUsrNme_Type()
)
tmnxDiamPlcyDccaAvpRadiusUsrNme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpRadiusUsrNme.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpSubIdOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamPlcyDccaAvpSubIdOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1


_TmnxDiamPlcyDccaAvpSubIdOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamPlcyDccaAvpSubIdOrg_Object = MibTableColumn
tmnxDiamPlcyDccaAvpSubIdOrg = _TmnxDiamPlcyDccaAvpSubIdOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 8),
    _TmnxDiamPlcyDccaAvpSubIdOrg_Type()
)
tmnxDiamPlcyDccaAvpSubIdOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpSubIdOrg.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpSubIdType_Type(Integer32):
    """Custom type tmnxDiamPlcyDccaAvpSubIdType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endUserE164", 0),
          ("endUserImsi", 1),
          ("endUserPrivate", 4))
    )


_TmnxDiamPlcyDccaAvpSubIdType_Type.__name__ = "Integer32"
_TmnxDiamPlcyDccaAvpSubIdType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpSubIdType = _TmnxDiamPlcyDccaAvpSubIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 9),
    _TmnxDiamPlcyDccaAvpSubIdType_Type()
)
tmnxDiamPlcyDccaAvpSubIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpSubIdType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasP_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaAvpNasP based on TruthValue"""
    defaultValue = 2


_TmnxDiamPlcyDccaAvpNasP_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaAvpNasP_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasP = _TmnxDiamPlcyDccaAvpNasP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 10),
    _TmnxDiamPlcyDccaAvpNasP_Type()
)
tmnxDiamPlcyDccaAvpNasP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasP.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPPfixType_Type(TmnxSubNasPortPrefixType):
    """Custom type tmnxDiamPlcyDccaAvpNasPPfixType based on TmnxSubNasPortPrefixType"""
    defaultValue = 0


_TmnxDiamPlcyDccaAvpNasPPfixType_Type.__name__ = "TmnxSubNasPortPrefixType"
_TmnxDiamPlcyDccaAvpNasPPfixType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPPfixType = _TmnxDiamPlcyDccaAvpNasPPfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 11),
    _TmnxDiamPlcyDccaAvpNasPPfixType_Type()
)
tmnxDiamPlcyDccaAvpNasPPfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPPfixType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPPfixStr_Type(DisplayString):
    """Custom type tmnxDiamPlcyDccaAvpNasPPfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxDiamPlcyDccaAvpNasPPfixStr_Type.__name__ = "DisplayString"
_TmnxDiamPlcyDccaAvpNasPPfixStr_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPPfixStr = _TmnxDiamPlcyDccaAvpNasPPfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 12),
    _TmnxDiamPlcyDccaAvpNasPPfixStr_Type()
)
tmnxDiamPlcyDccaAvpNasPPfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPPfixStr.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPSfixType_Type(TmnxSubNasPortSuffixType):
    """Custom type tmnxDiamPlcyDccaAvpNasPSfixType based on TmnxSubNasPortSuffixType"""
    defaultValue = 0


_TmnxDiamPlcyDccaAvpNasPSfixType_Type.__name__ = "TmnxSubNasPortSuffixType"
_TmnxDiamPlcyDccaAvpNasPSfixType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPSfixType = _TmnxDiamPlcyDccaAvpNasPSfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 13),
    _TmnxDiamPlcyDccaAvpNasPSfixType_Type()
)
tmnxDiamPlcyDccaAvpNasPSfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPSfixType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPType_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaAvpNasPType based on TruthValue"""
    defaultValue = 2


_TmnxDiamPlcyDccaAvpNasPType_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaAvpNasPType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPType = _TmnxDiamPlcyDccaAvpNasPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 14),
    _TmnxDiamPlcyDccaAvpNasPType_Type()
)
tmnxDiamPlcyDccaAvpNasPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpImsiOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamPlcyDccaAvpImsiOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1


_TmnxDiamPlcyDccaAvpImsiOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamPlcyDccaAvpImsiOrg_Object = MibTableColumn
tmnxDiamPlcyDccaAvpImsiOrg = _TmnxDiamPlcyDccaAvpImsiOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 15),
    _TmnxDiamPlcyDccaAvpImsiOrg_Type()
)
tmnxDiamPlcyDccaAvpImsiOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpImsiOrg.setStatus("obsolete")


class _TmnxDiamPlcyDccaApplicationType_Type(TmnxDiamDccaApplicationType):
    """Custom type tmnxDiamPlcyDccaApplicationType based on TmnxDiamDccaApplicationType"""
    defaultValue = 1


_TmnxDiamPlcyDccaApplicationType_Type.__name__ = "TmnxDiamDccaApplicationType"
_TmnxDiamPlcyDccaApplicationType_Object = MibTableColumn
tmnxDiamPlcyDccaApplicationType = _TmnxDiamPlcyDccaApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 50),
    _TmnxDiamPlcyDccaApplicationType_Type()
)
tmnxDiamPlcyDccaApplicationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaApplicationType.setStatus("obsolete")


class _TmnxDiamPlcyDccaMaxPendingReq_Type(Unsigned32):
    """Custom type tmnxDiamPlcyDccaMaxPendingReq based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 131072),
    )


_TmnxDiamPlcyDccaMaxPendingReq_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyDccaMaxPendingReq_Object = MibTableColumn
tmnxDiamPlcyDccaMaxPendingReq = _TmnxDiamPlcyDccaMaxPendingReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 51),
    _TmnxDiamPlcyDccaMaxPendingReq_Type()
)
tmnxDiamPlcyDccaMaxPendingReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaMaxPendingReq.setStatus("obsolete")


class _TmnxDiamPlcyDccaTxRetryLimit_Type(Unsigned32):
    """Custom type tmnxDiamPlcyDccaTxRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxDiamPlcyDccaTxRetryLimit_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyDccaTxRetryLimit_Object = MibTableColumn
tmnxDiamPlcyDccaTxRetryLimit = _TmnxDiamPlcyDccaTxRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 52),
    _TmnxDiamPlcyDccaTxRetryLimit_Type()
)
tmnxDiamPlcyDccaTxRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTxRetryLimit.setStatus("obsolete")


class _TmnxDiamPlcyDccaOutOfCreditRep_Type(Integer32):
    """Custom type tmnxDiamPlcyDccaOutOfCreditRep based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("final", 1),
          ("quotaExhausted", 2))
    )


_TmnxDiamPlcyDccaOutOfCreditRep_Type.__name__ = "Integer32"
_TmnxDiamPlcyDccaOutOfCreditRep_Object = MibTableColumn
tmnxDiamPlcyDccaOutOfCreditRep = _TmnxDiamPlcyDccaOutOfCreditRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 53),
    _TmnxDiamPlcyDccaOutOfCreditRep_Type()
)
tmnxDiamPlcyDccaOutOfCreditRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaOutOfCreditRep.setStatus("obsolete")
_TmnxDiameterObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterObjects = _TmnxDiameterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3)
)
_TmnxDiamAppPlcyTableLastCh_Type = TimeStamp
_TmnxDiamAppPlcyTableLastCh_Object = MibScalar
tmnxDiamAppPlcyTableLastCh = _TmnxDiamAppPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 1),
    _TmnxDiamAppPlcyTableLastCh_Type()
)
tmnxDiamAppPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTableLastCh.setStatus("current")
_TmnxDiamAppPlcyTable_Object = MibTable
tmnxDiamAppPlcyTable = _TmnxDiamAppPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTable.setStatus("current")
_TmnxDiamAppPlcyEntry_Object = MibTableRow
tmnxDiamAppPlcyEntry = _TmnxDiamAppPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1)
)
tmnxDiamAppPlcyEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyEntry.setStatus("current")
_TmnxDiamAppPlcyId_Type = TNamedItem
_TmnxDiamAppPlcyId_Object = MibTableColumn
tmnxDiamAppPlcyId = _TmnxDiamAppPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 1),
    _TmnxDiamAppPlcyId_Type()
)
tmnxDiamAppPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyId.setStatus("current")
_TmnxDiamAppPlcyRowStatus_Type = RowStatus
_TmnxDiamAppPlcyRowStatus_Object = MibTableColumn
tmnxDiamAppPlcyRowStatus = _TmnxDiamAppPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 2),
    _TmnxDiamAppPlcyRowStatus_Type()
)
tmnxDiamAppPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyRowStatus.setStatus("current")
_TmnxDiamAppPlcyLastMgmtChange_Type = TimeStamp
_TmnxDiamAppPlcyLastMgmtChange_Object = MibTableColumn
tmnxDiamAppPlcyLastMgmtChange = _TmnxDiamAppPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 3),
    _TmnxDiamAppPlcyLastMgmtChange_Type()
)
tmnxDiamAppPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyLastMgmtChange.setStatus("current")


class _TmnxDiamAppPlcyFailover_Type(TruthValue):
    """Custom type tmnxDiamAppPlcyFailover based on TruthValue"""
    defaultValue = 1


_TmnxDiamAppPlcyFailover_Type.__name__ = "TruthValue"
_TmnxDiamAppPlcyFailover_Object = MibTableColumn
tmnxDiamAppPlcyFailover = _TmnxDiamAppPlcyFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 4),
    _TmnxDiamAppPlcyFailover_Type()
)
tmnxDiamAppPlcyFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyFailover.setStatus("current")


class _TmnxDiamAppPlcyFailureHndlng_Type(TmnxDiamCcFailureHndlng):
    """Custom type tmnxDiamAppPlcyFailureHndlng based on TmnxDiamCcFailureHndlng"""
    defaultValue = 1


_TmnxDiamAppPlcyFailureHndlng_Type.__name__ = "TmnxDiamCcFailureHndlng"
_TmnxDiamAppPlcyFailureHndlng_Object = MibTableColumn
tmnxDiamAppPlcyFailureHndlng = _TmnxDiamAppPlcyFailureHndlng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 5),
    _TmnxDiamAppPlcyFailureHndlng_Type()
)
tmnxDiamAppPlcyFailureHndlng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyFailureHndlng.setStatus("current")


class _TmnxDiamAppPlcyPeerPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamAppPlcyPeerPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamAppPlcyPeerPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamAppPlcyPeerPlcy_Object = MibTableColumn
tmnxDiamAppPlcyPeerPlcy = _TmnxDiamAppPlcyPeerPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 6),
    _TmnxDiamAppPlcyPeerPlcy_Type()
)
tmnxDiamAppPlcyPeerPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyPeerPlcy.setStatus("current")


class _TmnxDiamAppPlcyApplication_Type(Integer32):
    """Custom type tmnxDiamAppPlcyApplication based on Integer32"""
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
          ("gx", 1),
          ("gy", 2))
    )


_TmnxDiamAppPlcyApplication_Type.__name__ = "Integer32"
_TmnxDiamAppPlcyApplication_Object = MibTableColumn
tmnxDiamAppPlcyApplication = _TmnxDiamAppPlcyApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 7),
    _TmnxDiamAppPlcyApplication_Type()
)
tmnxDiamAppPlcyApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyApplication.setStatus("current")


class _TmnxDiamAppPlcyTxTimer_Type(Unsigned32):
    """Custom type tmnxDiamAppPlcyTxTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxDiamAppPlcyTxTimer_Type.__name__ = "Unsigned32"
_TmnxDiamAppPlcyTxTimer_Object = MibTableColumn
tmnxDiamAppPlcyTxTimer = _TmnxDiamAppPlcyTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 8),
    _TmnxDiamAppPlcyTxTimer_Type()
)
tmnxDiamAppPlcyTxTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTxTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTxTimer.setUnits("seconds")


class _TmnxDiamAppPlcyDescription_Type(TItemDescription):
    """Custom type tmnxDiamAppPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDiamAppPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxDiamAppPlcyDescription_Object = MibTableColumn
tmnxDiamAppPlcyDescription = _TmnxDiamAppPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 9),
    _TmnxDiamAppPlcyDescription_Type()
)
tmnxDiamAppPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyDescription.setStatus("current")
_TmnxDiamApGyTableLastCh_Type = TimeStamp
_TmnxDiamApGyTableLastCh_Object = MibScalar
tmnxDiamApGyTableLastCh = _TmnxDiamApGyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 3),
    _TmnxDiamApGyTableLastCh_Type()
)
tmnxDiamApGyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGyTableLastCh.setStatus("current")
_TmnxDiamApGyTable_Object = MibTable
tmnxDiamApGyTable = _TmnxDiamApGyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxDiamApGyTable.setStatus("current")
_TmnxDiamApGyEntry_Object = MibTableRow
tmnxDiamApGyEntry = _TmnxDiamApGyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1)
)
tmnxDiamApGyEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamApGyEntry.setStatus("current")
_TmnxDiamApGyLastMgmtChange_Type = TimeStamp
_TmnxDiamApGyLastMgmtChange_Object = MibTableColumn
tmnxDiamApGyLastMgmtChange = _TmnxDiamApGyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 1),
    _TmnxDiamApGyLastMgmtChange_Type()
)
tmnxDiamApGyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGyLastMgmtChange.setStatus("current")


class _TmnxDiamApGyAvpServCntxtId_Type(DisplayString):
    """Custom type tmnxDiamApGyAvpServCntxtId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDiamApGyAvpServCntxtId_Type.__name__ = "DisplayString"
_TmnxDiamApGyAvpServCntxtId_Object = MibTableColumn
tmnxDiamApGyAvpServCntxtId = _TmnxDiamApGyAvpServCntxtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 2),
    _TmnxDiamApGyAvpServCntxtId_Type()
)
tmnxDiamApGyAvpServCntxtId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpServCntxtId.setStatus("current")


class _TmnxDiamApGyAvpCldStationId_Type(DisplayString):
    """Custom type tmnxDiamApGyAvpCldStationId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamApGyAvpCldStationId_Type.__name__ = "DisplayString"
_TmnxDiamApGyAvpCldStationId_Object = MibTableColumn
tmnxDiamApGyAvpCldStationId = _TmnxDiamApGyAvpCldStationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 3),
    _TmnxDiamApGyAvpCldStationId_Type()
)
tmnxDiamApGyAvpCldStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpCldStationId.setStatus("current")


class _TmnxDiamApGyAvpRadiusUsrNme_Type(TruthValue):
    """Custom type tmnxDiamApGyAvpRadiusUsrNme based on TruthValue"""
    defaultValue = 2


_TmnxDiamApGyAvpRadiusUsrNme_Type.__name__ = "TruthValue"
_TmnxDiamApGyAvpRadiusUsrNme_Object = MibTableColumn
tmnxDiamApGyAvpRadiusUsrNme = _TmnxDiamApGyAvpRadiusUsrNme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 4),
    _TmnxDiamApGyAvpRadiusUsrNme_Type()
)
tmnxDiamApGyAvpRadiusUsrNme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpRadiusUsrNme.setStatus("current")


class _TmnxDiamApGyAvpImsiOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamApGyAvpImsiOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1

    subtypeSpec = TmnxDiamPlcyDccaAvpOriginType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3))
    )


_TmnxDiamApGyAvpImsiOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamApGyAvpImsiOrg_Object = MibTableColumn
tmnxDiamApGyAvpImsiOrg = _TmnxDiamApGyAvpImsiOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 5),
    _TmnxDiamApGyAvpImsiOrg_Type()
)
tmnxDiamApGyAvpImsiOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpImsiOrg.setStatus("current")


class _TmnxDiamApGyOutOfCreditRep_Type(Integer32):
    """Custom type tmnxDiamApGyOutOfCreditRep based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("final", 1),
          ("quotaExhausted", 2))
    )


_TmnxDiamApGyOutOfCreditRep_Type.__name__ = "Integer32"
_TmnxDiamApGyOutOfCreditRep_Object = MibTableColumn
tmnxDiamApGyOutOfCreditRep = _TmnxDiamApGyOutOfCreditRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 6),
    _TmnxDiamApGyOutOfCreditRep_Type()
)
tmnxDiamApGyOutOfCreditRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyOutOfCreditRep.setStatus("current")


class _TmnxDiamApGyVendorSupport_Type(TmnxDiamPlcyVendorSupportType):
    """Custom type tmnxDiamApGyVendorSupport based on TmnxDiamPlcyVendorSupportType"""
    defaultValue = 2


_TmnxDiamApGyVendorSupport_Type.__name__ = "TmnxDiamPlcyVendorSupportType"
_TmnxDiamApGyVendorSupport_Object = MibTableColumn
tmnxDiamApGyVendorSupport = _TmnxDiamApGyVendorSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 7),
    _TmnxDiamApGyVendorSupport_Type()
)
tmnxDiamApGyVendorSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyVendorSupport.setStatus("current")


class _TmnxDiamApGySubIdOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamApGySubIdOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1


_TmnxDiamApGySubIdOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamApGySubIdOrg_Object = MibTableColumn
tmnxDiamApGySubIdOrg = _TmnxDiamApGySubIdOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 8),
    _TmnxDiamApGySubIdOrg_Type()
)
tmnxDiamApGySubIdOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGySubIdOrg.setStatus("current")


class _TmnxDiamApGySubIdType_Type(Integer32):
    """Custom type tmnxDiamApGySubIdType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("imsi", 1),
          ("nai", 3),
          ("private", 4))
    )


_TmnxDiamApGySubIdType_Type.__name__ = "Integer32"
_TmnxDiamApGySubIdType_Object = MibTableColumn
tmnxDiamApGySubIdType = _TmnxDiamApGySubIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 9),
    _TmnxDiamApGySubIdType_Type()
)
tmnxDiamApGySubIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGySubIdType.setStatus("current")
_TmnxDiamApGxTableLastCh_Type = TimeStamp
_TmnxDiamApGxTableLastCh_Object = MibScalar
tmnxDiamApGxTableLastCh = _TmnxDiamApGxTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 5),
    _TmnxDiamApGxTableLastCh_Type()
)
tmnxDiamApGxTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGxTableLastCh.setStatus("current")
_TmnxDiamApGxTable_Object = MibTable
tmnxDiamApGxTable = _TmnxDiamApGxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxDiamApGxTable.setStatus("current")
_TmnxDiamApGxEntry_Object = MibTableRow
tmnxDiamApGxEntry = _TmnxDiamApGxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1)
)
tmnxDiamApGxEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamApGxEntry.setStatus("current")
_TmnxDiamApGxLastMgmtChange_Type = TimeStamp
_TmnxDiamApGxLastMgmtChange_Object = MibTableColumn
tmnxDiamApGxLastMgmtChange = _TmnxDiamApGxLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 1),
    _TmnxDiamApGxLastMgmtChange_Type()
)
tmnxDiamApGxLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGxLastMgmtChange.setStatus("current")


class _TmnxDiamApGxAvp_Type(Bits):
    """Custom type tmnxDiamApGxAvp based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("anGwAddress", 0),
          ("callingStationId", 1),
          ("calledStationId", 2),
          ("ipCanType", 3),
          ("logicalAccessId", 4),
          ("nasPort", 5),
          ("nasPortId", 6),
          ("nasPortType", 7),
          ("physicalAccessId", 8),
          ("ratType", 9),
          ("supportedFeatures", 10),
          ("userEquipmentInfo", 11))
    )

_TmnxDiamApGxAvp_Type.__name__ = "Bits"
_TmnxDiamApGxAvp_Object = MibTableColumn
tmnxDiamApGxAvp = _TmnxDiamApGxAvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 2),
    _TmnxDiamApGxAvp_Type()
)
tmnxDiamApGxAvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvp.setStatus("current")


class _TmnxDiamApGxAvpClngStationIdType_Type(TmnxSubCallingStationIdType):
    """Custom type tmnxDiamApGxAvpClngStationIdType based on TmnxSubCallingStationIdType"""
    defaultValue = 1


_TmnxDiamApGxAvpClngStationIdType_Type.__name__ = "TmnxSubCallingStationIdType"
_TmnxDiamApGxAvpClngStationIdType_Object = MibTableColumn
tmnxDiamApGxAvpClngStationIdType = _TmnxDiamApGxAvpClngStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 3),
    _TmnxDiamApGxAvpClngStationIdType_Type()
)
tmnxDiamApGxAvpClngStationIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpClngStationIdType.setStatus("current")


class _TmnxDiamApGxAvpNasPortBitspec_Type(TmnxBinarySpecification):
    """Custom type tmnxDiamApGxAvpNasPortBitspec based on TmnxBinarySpecification"""
    defaultValue = OctetString("")


_TmnxDiamApGxAvpNasPortBitspec_Type.__name__ = "TmnxBinarySpecification"
_TmnxDiamApGxAvpNasPortBitspec_Object = MibTableColumn
tmnxDiamApGxAvpNasPortBitspec = _TmnxDiamApGxAvpNasPortBitspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 4),
    _TmnxDiamApGxAvpNasPortBitspec_Type()
)
tmnxDiamApGxAvpNasPortBitspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortBitspec.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdPfixType_Type(TmnxSubNasPortPrefixType):
    """Custom type tmnxDiamApGxAvpNasPortIdPfixType based on TmnxSubNasPortPrefixType"""
    defaultValue = 0


_TmnxDiamApGxAvpNasPortIdPfixType_Type.__name__ = "TmnxSubNasPortPrefixType"
_TmnxDiamApGxAvpNasPortIdPfixType_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdPfixType = _TmnxDiamApGxAvpNasPortIdPfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 5),
    _TmnxDiamApGxAvpNasPortIdPfixType_Type()
)
tmnxDiamApGxAvpNasPortIdPfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdPfixType.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdPfixStr_Type(DisplayString):
    """Custom type tmnxDiamApGxAvpNasPortIdPfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxDiamApGxAvpNasPortIdPfixStr_Type.__name__ = "DisplayString"
_TmnxDiamApGxAvpNasPortIdPfixStr_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdPfixStr = _TmnxDiamApGxAvpNasPortIdPfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 6),
    _TmnxDiamApGxAvpNasPortIdPfixStr_Type()
)
tmnxDiamApGxAvpNasPortIdPfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdPfixStr.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdSfixType_Type(TmnxSubNasPortSuffixType):
    """Custom type tmnxDiamApGxAvpNasPortIdSfixType based on TmnxSubNasPortSuffixType"""
    defaultValue = 0


_TmnxDiamApGxAvpNasPortIdSfixType_Type.__name__ = "TmnxSubNasPortSuffixType"
_TmnxDiamApGxAvpNasPortIdSfixType_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdSfixType = _TmnxDiamApGxAvpNasPortIdSfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 7),
    _TmnxDiamApGxAvpNasPortIdSfixType_Type()
)
tmnxDiamApGxAvpNasPortIdSfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdSfixType.setStatus("current")


class _TmnxDiamApGxAvpNasPortTypeValue_Type(Unsigned32):
    """Custom type tmnxDiamApGxAvpNasPortTypeValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDiamApGxAvpNasPortTypeValue_Type.__name__ = "Unsigned32"
_TmnxDiamApGxAvpNasPortTypeValue_Object = MibTableColumn
tmnxDiamApGxAvpNasPortTypeValue = _TmnxDiamApGxAvpNasPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 8),
    _TmnxDiamApGxAvpNasPortTypeValue_Type()
)
tmnxDiamApGxAvpNasPortTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortTypeValue.setStatus("current")


class _TmnxDiamApGxAvpUeInfoType_Type(Integer32):
    """Custom type tmnxDiamApGxAvpUeInfoType based on Integer32"""
    defaultValue = 1

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
        *(("imeisv", 0),
          ("mac", 1),
          ("eui64", 2),
          ("modifiedEui64", 3))
    )


_TmnxDiamApGxAvpUeInfoType_Type.__name__ = "Integer32"
_TmnxDiamApGxAvpUeInfoType_Object = MibTableColumn
tmnxDiamApGxAvpUeInfoType = _TmnxDiamApGxAvpUeInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 9),
    _TmnxDiamApGxAvpUeInfoType_Type()
)
tmnxDiamApGxAvpUeInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpUeInfoType.setStatus("current")


class _TmnxDiamApGxSubIdOrg_Type(Integer32):
    """Custom type tmnxDiamApGxSubIdOrg based on Integer32"""
    defaultValue = 1

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
        *(("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3),
          ("msisdn", 4),
          ("imei", 5),
          ("dualStackRemoteId", 6),
          ("mac", 7),
          ("username", 8))
    )


_TmnxDiamApGxSubIdOrg_Type.__name__ = "Integer32"
_TmnxDiamApGxSubIdOrg_Object = MibTableColumn
tmnxDiamApGxSubIdOrg = _TmnxDiamApGxSubIdOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 10),
    _TmnxDiamApGxSubIdOrg_Type()
)
tmnxDiamApGxSubIdOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxSubIdOrg.setStatus("current")


class _TmnxDiamApGxSubIdType_Type(Integer32):
    """Custom type tmnxDiamApGxSubIdType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("imsi", 1),
          ("nai", 3),
          ("private", 4))
    )


_TmnxDiamApGxSubIdType_Type.__name__ = "Integer32"
_TmnxDiamApGxSubIdType_Object = MibTableColumn
tmnxDiamApGxSubIdType = _TmnxDiamApGxSubIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 11),
    _TmnxDiamApGxSubIdType_Type()
)
tmnxDiamApGxSubIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxSubIdType.setStatus("current")


class _TmnxDiamApGxMacFormat_Type(TmnxMacSpecification):
    """Custom type tmnxDiamApGxMacFormat based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxDiamApGxMacFormat_Type.__name__ = "TmnxMacSpecification"
_TmnxDiamApGxMacFormat_Object = MibTableColumn
tmnxDiamApGxMacFormat = _TmnxDiamApGxMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 12),
    _TmnxDiamApGxMacFormat_Type()
)
tmnxDiamApGxMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxMacFormat.setStatus("current")


class _TmnxDiamApGxReportIpAddrEvent_Type(TruthValue):
    """Custom type tmnxDiamApGxReportIpAddrEvent based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGxReportIpAddrEvent_Type.__name__ = "TruthValue"
_TmnxDiamApGxReportIpAddrEvent_Object = MibTableColumn
tmnxDiamApGxReportIpAddrEvent = _TmnxDiamApGxReportIpAddrEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 13),
    _TmnxDiamApGxReportIpAddrEvent_Type()
)
tmnxDiamApGxReportIpAddrEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxReportIpAddrEvent.setStatus("current")
_TmnxDiameterNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxDiameterNotificationObjs = _TmnxDiameterNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100)
)
_TmnxDiamAppPlcyName_Type = TNamedItem
_TmnxDiamAppPlcyName_Object = MibScalar
tmnxDiamAppPlcyName = _TmnxDiamAppPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 1),
    _TmnxDiamAppPlcyName_Type()
)
tmnxDiamAppPlcyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyName.setStatus("current")
_TmnxDiamAppPeerName_Type = TNamedItem
_TmnxDiamAppPeerName_Object = MibScalar
tmnxDiamAppPeerName = _TmnxDiamAppPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 2),
    _TmnxDiamAppPeerName_Type()
)
tmnxDiamAppPeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppPeerName.setStatus("current")
_TmnxDiamAppTrapDescription_Type = TItemDescription
_TmnxDiamAppTrapDescription_Object = MibScalar
tmnxDiamAppTrapDescription = _TmnxDiamAppTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 3),
    _TmnxDiamAppTrapDescription_Type()
)
tmnxDiamAppTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppTrapDescription.setStatus("current")


class _TmnxDiamAppSessionId_Type(DisplayString):
    """Custom type tmnxDiamAppSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 102),
    )


_TmnxDiamAppSessionId_Type.__name__ = "DisplayString"
_TmnxDiamAppSessionId_Object = MibScalar
tmnxDiamAppSessionId = _TmnxDiamAppSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 4),
    _TmnxDiamAppSessionId_Type()
)
tmnxDiamAppSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSessionId.setStatus("current")


class _TmnxDiamAppSubscrId_Type(DisplayString):
    """Custom type tmnxDiamAppSubscrId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxDiamAppSubscrId_Type.__name__ = "DisplayString"
_TmnxDiamAppSubscrId_Object = MibScalar
tmnxDiamAppSubscrId = _TmnxDiamAppSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 5),
    _TmnxDiamAppSubscrId_Type()
)
tmnxDiamAppSubscrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSubscrId.setStatus("current")


class _TmnxDiamAppSapId_Type(DisplayString):
    """Custom type tmnxDiamAppSapId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxDiamAppSapId_Type.__name__ = "DisplayString"
_TmnxDiamAppSapId_Object = MibScalar
tmnxDiamAppSapId = _TmnxDiamAppSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 6),
    _TmnxDiamAppSapId_Type()
)
tmnxDiamAppSapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSapId.setStatus("current")
_TmnxDiamAppSLAProfName_Type = TNamedItem
_TmnxDiamAppSLAProfName_Object = MibScalar
tmnxDiamAppSLAProfName = _TmnxDiamAppSLAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 7),
    _TmnxDiamAppSLAProfName_Type()
)
tmnxDiamAppSLAProfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSLAProfName.setStatus("current")
_TmnxDiameterNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDiameterNotifyPrefix = _TmnxDiameterNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58)
)
_TmnxDiameterNotifications_ObjectIdentity = ObjectIdentity
tmnxDiameterNotifications = _TmnxDiameterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0)
)
tmnxDiameterPlcyPeerEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamPlcyPeerInfoEntry")
)
tmnxDiamPlcyPeerInfoEntry.setIndexNames(*tmnxDiameterPlcyPeerEntry.getIndexNames())
tmnxDiameterPlcyPeerEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamPlcyPeerStatsEntry")
)
tmnxDiamPlcyPeerStatsEntry.setIndexNames(*tmnxDiameterPlcyPeerEntry.getIndexNames())
tmnxDiameterPlcyEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiameterPlcyDccaEntry")
)
tmnxDiameterPlcyDccaEntry.setIndexNames(*tmnxDiameterPlcyEntry.getIndexNames())

# Managed Objects groups

tmnxDiameterBaseV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 1)
)
tmnxDiameterBaseV7v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterPlcyTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyTransactionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportProt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransactTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerPreference"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseV7v0Group.setStatus("obsolete")

tmnxDiameterDccaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 2)
)
tmnxDiameterDccaGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailover"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailureHndlng"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpServCntxtId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpCldStationId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpRadiusUsrNme"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdType"))
)
if mibBuilder.loadTexts:
    tmnxDiameterDccaGroup.setStatus("obsolete")

tmnxDiameterBaseV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 3)
)
tmnxDiameterBaseV8v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterPlcyTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyTransactionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportProt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransactTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerPreference"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPsmState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerConnectionSuspended"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqStage"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerOrder"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPrimarySecondary"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTcTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTtTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTwTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerWatchdogAlgActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerWatchdogAnswPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPeerRemovalPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsLastClearTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamTxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamRxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiPendMsgsPMQ"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiReqTimeoutsPMQ"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamRxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamTxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStErrHdlDiamTxErrCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStErrHdlDiamRxErrCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrInitialTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaInitialRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrUpdateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaUpdateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrTerminateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaTerminateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCerTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCeaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAsrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAsaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStRarRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStRaaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDprTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDpaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDprRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDpaTx"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseV8v0Group.setStatus("current")

tmnxDiameterV8v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 5)
)
tmnxDiameterV8v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV8v0NotifyObjsGroup.setStatus("obsolete")

tmnxDiameterDccaGxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 6)
)
tmnxDiameterDccaGxGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasP"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaApplicationType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpImsiOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaMaxPendingReq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxRetryLimit"))
)
if mibBuilder.loadTexts:
    tmnxDiameterDccaGxGroup.setStatus("obsolete")

tmnxDiameterDccaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 7)
)
tmnxDiameterDccaV10v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyVendorSupport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaOutOfCreditRep"))
)
if mibBuilder.loadTexts:
    tmnxDiameterDccaV10v0Group.setStatus("obsolete")

tmnxDiameterV10v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 9)
)
tmnxDiameterV10v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSubscrId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSapId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSLAProfName"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV10v0NotifyObjsGroup.setStatus("current")

tmnxDiameterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 10)
)
tmnxDiameterV12v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyVendorSupport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyApplications"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyFailover"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyFailureHndlng"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyPeerPlcy"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyApplication"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyTxTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpServCntxtId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpCldStationId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpRadiusUsrNme"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpImsiOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyOutOfCreditRep"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyVendorSupport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGySubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGySubIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpClngStationIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortBitspec"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortTypeValue"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpUeInfoType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxSubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxSubIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxMacFormat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxReportIpAddrEvent"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPythonPolicy"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV12v0Group.setStatus("current")

tmnxDiamObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 98)
)
tmnxDiamObsoleteGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailover"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailureHndlng"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpServCntxtId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpCldStationId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpRadiusUsrNme"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaOutOfCreditRep"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasP"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaApplicationType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpImsiOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaMaxPendingReq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxRetryLimit"))
)
if mibBuilder.loadTexts:
    tmnxDiamObsoleteGroup.setStatus("current")


# Notification objects

tmnxDiamPolicyPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 1)
)
tmnxDiamPolicyPeerStateChange.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPrimarySecondary"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerConnectionSuspended"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamPolicyPeerStateChange.setStatus(
        "current"
    )

tmnxDiamAppMessageDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 2)
)
tmnxDiamAppMessageDropped.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamAppMessageDropped.setStatus(
        "current"
    )

tmnxDiamAppSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 3)
)
tmnxDiamAppSessionFailure.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSubscrId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSapId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSLAProfName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamAppSessionFailure.setStatus(
        "current"
    )


# Notifications groups

tmnxDiameterNotifyV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 4)
)
tmnxDiameterNotifyV8v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppMessageDropped"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV8v0Group.setStatus(
        "obsolete"
    )

tmnxDiameterNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 8)
)
tmnxDiameterNotifyV10v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppMessageDropped"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionFailure"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV10v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDiameterV8v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 1)
)
tmnxDiameterV8v0MIBCompliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV8v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxDiameterV10v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 2)
)
tmnxDiameterV10v0MIBCompliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV10v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaGxGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV10v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxDiameterV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 3)
)
tmnxDiameterV12v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV10v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DIAMETER-MIB",
    **{"TmnxDiamPeerTransportProt": TmnxDiamPeerTransportProt,
       "TmnxDiamCcFailureHndlng": TmnxDiamCcFailureHndlng,
       "TmnxDiamDccaApplicationType": TmnxDiamDccaApplicationType,
       "TmnxDiamPlcyVendorSupportType": TmnxDiamPlcyVendorSupportType,
       "TmnxDiamPlcyDccaAvpOriginType": TmnxDiamPlcyDccaAvpOriginType,
       "timetraDiameterMIBModule": timetraDiameterMIBModule,
       "tmnxDiameterConformance": tmnxDiameterConformance,
       "tmnxDiameterCompliances": tmnxDiameterCompliances,
       "tmnxDiameterV8v0MIBCompliance": tmnxDiameterV8v0MIBCompliance,
       "tmnxDiameterV10v0MIBCompliance": tmnxDiameterV10v0MIBCompliance,
       "tmnxDiameterV12v0Compliance": tmnxDiameterV12v0Compliance,
       "tmnxDiameterGroups": tmnxDiameterGroups,
       "tmnxDiameterBaseV7v0Group": tmnxDiameterBaseV7v0Group,
       "tmnxDiameterDccaGroup": tmnxDiameterDccaGroup,
       "tmnxDiameterBaseV8v0Group": tmnxDiameterBaseV8v0Group,
       "tmnxDiameterNotifyV8v0Group": tmnxDiameterNotifyV8v0Group,
       "tmnxDiameterV8v0NotifyObjsGroup": tmnxDiameterV8v0NotifyObjsGroup,
       "tmnxDiameterDccaGxGroup": tmnxDiameterDccaGxGroup,
       "tmnxDiameterDccaV10v0Group": tmnxDiameterDccaV10v0Group,
       "tmnxDiameterNotifyV10v0Group": tmnxDiameterNotifyV10v0Group,
       "tmnxDiameterV10v0NotifyObjsGroup": tmnxDiameterV10v0NotifyObjsGroup,
       "tmnxDiameterV12v0Group": tmnxDiameterV12v0Group,
       "tmnxDiamObsoleteGroup": tmnxDiamObsoleteGroup,
       "tmnxDiameter": tmnxDiameter,
       "tmnxDiameterBaseObjects": tmnxDiameterBaseObjects,
       "tmnxDiameterPlcyTableLastChngd": tmnxDiameterPlcyTableLastChngd,
       "tmnxDiameterPlcyTable": tmnxDiameterPlcyTable,
       "tmnxDiameterPlcyEntry": tmnxDiameterPlcyEntry,
       "tmnxDiamPlcyName": tmnxDiamPlcyName,
       "tmnxDiamPlcyRowStatus": tmnxDiamPlcyRowStatus,
       "tmnxDiamPlcyLastMgmtChange": tmnxDiamPlcyLastMgmtChange,
       "tmnxDiamPlcyDescription": tmnxDiamPlcyDescription,
       "tmnxDiamPlcyOriginHost": tmnxDiamPlcyOriginHost,
       "tmnxDiamPlcyOriginRealm": tmnxDiamPlcyOriginRealm,
       "tmnxDiamPlcyRouter": tmnxDiamPlcyRouter,
       "tmnxDiamPlcySourceAddrType": tmnxDiamPlcySourceAddrType,
       "tmnxDiamPlcySourceAddr": tmnxDiamPlcySourceAddr,
       "tmnxDiamPlcyWatchdogTimer": tmnxDiamPlcyWatchdogTimer,
       "tmnxDiamPlcyConnectionTimer": tmnxDiamPlcyConnectionTimer,
       "tmnxDiamPlcyTransactionTimer": tmnxDiamPlcyTransactionTimer,
       "tmnxDiamPlcyVendorSupport": tmnxDiamPlcyVendorSupport,
       "tmnxDiamPlcyApplications": tmnxDiamPlcyApplications,
       "tmnxDiamPlcyPythonPolicy": tmnxDiamPlcyPythonPolicy,
       "tmnxDiamPlcyPeerTableLastChngd": tmnxDiamPlcyPeerTableLastChngd,
       "tmnxDiameterPlcyPeerTable": tmnxDiameterPlcyPeerTable,
       "tmnxDiameterPlcyPeerEntry": tmnxDiameterPlcyPeerEntry,
       "tmnxDiamPlcyPeerName": tmnxDiamPlcyPeerName,
       "tmnxDiamPlcyPeerRowStatus": tmnxDiamPlcyPeerRowStatus,
       "tmnxDiamPlcyPeerLastMgmtChange": tmnxDiamPlcyPeerLastMgmtChange,
       "tmnxDiamPlcyPeerAdminState": tmnxDiamPlcyPeerAdminState,
       "tmnxDiamPlcyPeerAddrType": tmnxDiamPlcyPeerAddrType,
       "tmnxDiamPlcyPeerAddr": tmnxDiamPlcyPeerAddr,
       "tmnxDiamPlcyPeerTransportProt": tmnxDiamPlcyPeerTransportProt,
       "tmnxDiamPlcyPeerTransportPort": tmnxDiamPlcyPeerTransportPort,
       "tmnxDiamPlcyPeerDestHost": tmnxDiamPlcyPeerDestHost,
       "tmnxDiamPlcyPeerDestRealm": tmnxDiamPlcyPeerDestRealm,
       "tmnxDiamPlcyPeerWatchdogTimer": tmnxDiamPlcyPeerWatchdogTimer,
       "tmnxDiamPlcyPeerConnectionTimer": tmnxDiamPlcyPeerConnectionTimer,
       "tmnxDiamPlcyPeerTransactTimer": tmnxDiamPlcyPeerTransactTimer,
       "tmnxDiamPlcyPeerPreference": tmnxDiamPlcyPeerPreference,
       "tmnxDiamPlcyPeerInfoTable": tmnxDiamPlcyPeerInfoTable,
       "tmnxDiamPlcyPeerInfoEntry": tmnxDiamPlcyPeerInfoEntry,
       "tmnxDiamPeerPsmState": tmnxDiamPeerPsmState,
       "tmnxDiamPeerConnectionSuspended": tmnxDiamPeerConnectionSuspended,
       "tmnxDiamPeerCooldownSeqStage": tmnxDiamPeerCooldownSeqStage,
       "tmnxDiamPeerOrder": tmnxDiamPeerOrder,
       "tmnxDiamPeerPrimarySecondary": tmnxDiamPeerPrimarySecondary,
       "tmnxDiamPeerTcTimerTimeLeft": tmnxDiamPeerTcTimerTimeLeft,
       "tmnxDiamPeerTtTimerTimeLeft": tmnxDiamPeerTtTimerTimeLeft,
       "tmnxDiamPeerTwTimerTimeLeft": tmnxDiamPeerTwTimerTimeLeft,
       "tmnxDiamPeerWatchdogAlgActive": tmnxDiamPeerWatchdogAlgActive,
       "tmnxDiamPeerWatchdogAnswPending": tmnxDiamPeerWatchdogAnswPending,
       "tmnxDiamPeerCooldownSeqPending": tmnxDiamPeerCooldownSeqPending,
       "tmnxDiamPeerCooldownSeqActive": tmnxDiamPeerCooldownSeqActive,
       "tmnxDiamPeerPeerRemovalPending": tmnxDiamPeerPeerRemovalPending,
       "tmnxDiamPlcyPeerStatsTable": tmnxDiamPlcyPeerStatsTable,
       "tmnxDiamPlcyPeerStatsEntry": tmnxDiamPlcyPeerStatsEntry,
       "tmnxDiamPeerStatsLastClearTime": tmnxDiamPeerStatsLastClearTime,
       "tmnxDiamPeerStCiTcpSendFailed": tmnxDiamPeerStCiTcpSendFailed,
       "tmnxDiamPeerStCiDiamRxDropCnt": tmnxDiamPeerStCiDiamRxDropCnt,
       "tmnxDiamPeerStCiDiamTxReqs": tmnxDiamPeerStCiDiamTxReqs,
       "tmnxDiamPeerStCiDiamRxResps": tmnxDiamPeerStCiDiamRxResps,
       "tmnxDiamPeerStCiPendMsgsPMQ": tmnxDiamPeerStCiPendMsgsPMQ,
       "tmnxDiamPeerStCiReqTimeoutsPMQ": tmnxDiamPeerStCiReqTimeoutsPMQ,
       "tmnxDiamPeerStSiTcpSendFailed": tmnxDiamPeerStSiTcpSendFailed,
       "tmnxDiamPeerStSiDiamRxDropCnt": tmnxDiamPeerStSiDiamRxDropCnt,
       "tmnxDiamPeerStSiDiamRxReqs": tmnxDiamPeerStSiDiamRxReqs,
       "tmnxDiamPeerStSiDiamTxResps": tmnxDiamPeerStSiDiamTxResps,
       "tmnxDiamPeerStErrHdlDiamTxErrCnt": tmnxDiamPeerStErrHdlDiamTxErrCnt,
       "tmnxDiamPeerStErrHdlDiamRxErrCnt": tmnxDiamPeerStErrHdlDiamRxErrCnt,
       "tmnxDiamPeerStCcrInitialTx": tmnxDiamPeerStCcrInitialTx,
       "tmnxDiamPeerStCcaInitialRx": tmnxDiamPeerStCcaInitialRx,
       "tmnxDiamPeerStCcrUpdateTx": tmnxDiamPeerStCcrUpdateTx,
       "tmnxDiamPeerStCcaUpdateRx": tmnxDiamPeerStCcaUpdateRx,
       "tmnxDiamPeerStCcrTerminateTx": tmnxDiamPeerStCcrTerminateTx,
       "tmnxDiamPeerStCcaTerminateRx": tmnxDiamPeerStCcaTerminateRx,
       "tmnxDiamPeerStCerTx": tmnxDiamPeerStCerTx,
       "tmnxDiamPeerStCeaRx": tmnxDiamPeerStCeaRx,
       "tmnxDiamPeerStWdrTx": tmnxDiamPeerStWdrTx,
       "tmnxDiamPeerStWdaRx": tmnxDiamPeerStWdaRx,
       "tmnxDiamPeerStWdrRx": tmnxDiamPeerStWdrRx,
       "tmnxDiamPeerStWdaTx": tmnxDiamPeerStWdaTx,
       "tmnxDiamPeerStAsrRx": tmnxDiamPeerStAsrRx,
       "tmnxDiamPeerStAsaTx": tmnxDiamPeerStAsaTx,
       "tmnxDiamPeerStRarRx": tmnxDiamPeerStRarRx,
       "tmnxDiamPeerStRaaTx": tmnxDiamPeerStRaaTx,
       "tmnxDiamPeerStDprTx": tmnxDiamPeerStDprTx,
       "tmnxDiamPeerStDpaRx": tmnxDiamPeerStDpaRx,
       "tmnxDiamPeerStDprRx": tmnxDiamPeerStDprRx,
       "tmnxDiamPeerStDpaTx": tmnxDiamPeerStDpaTx,
       "tmnxDiameterDccaObjects": tmnxDiameterDccaObjects,
       "tmnxDiamPlcyDccaTableLastChngd": tmnxDiamPlcyDccaTableLastChngd,
       "tmnxDiameterPlcyDccaTable": tmnxDiameterPlcyDccaTable,
       "tmnxDiameterPlcyDccaEntry": tmnxDiameterPlcyDccaEntry,
       "tmnxDiamPlcyDccaLastMgmtChange": tmnxDiamPlcyDccaLastMgmtChange,
       "tmnxDiamPlcyDccaFailover": tmnxDiamPlcyDccaFailover,
       "tmnxDiamPlcyDccaFailureHndlng": tmnxDiamPlcyDccaFailureHndlng,
       "tmnxDiamPlcyDccaTxTimer": tmnxDiamPlcyDccaTxTimer,
       "tmnxDiamPlcyDccaAvpServCntxtId": tmnxDiamPlcyDccaAvpServCntxtId,
       "tmnxDiamPlcyDccaAvpCldStationId": tmnxDiamPlcyDccaAvpCldStationId,
       "tmnxDiamPlcyDccaAvpRadiusUsrNme": tmnxDiamPlcyDccaAvpRadiusUsrNme,
       "tmnxDiamPlcyDccaAvpSubIdOrg": tmnxDiamPlcyDccaAvpSubIdOrg,
       "tmnxDiamPlcyDccaAvpSubIdType": tmnxDiamPlcyDccaAvpSubIdType,
       "tmnxDiamPlcyDccaAvpNasP": tmnxDiamPlcyDccaAvpNasP,
       "tmnxDiamPlcyDccaAvpNasPPfixType": tmnxDiamPlcyDccaAvpNasPPfixType,
       "tmnxDiamPlcyDccaAvpNasPPfixStr": tmnxDiamPlcyDccaAvpNasPPfixStr,
       "tmnxDiamPlcyDccaAvpNasPSfixType": tmnxDiamPlcyDccaAvpNasPSfixType,
       "tmnxDiamPlcyDccaAvpNasPType": tmnxDiamPlcyDccaAvpNasPType,
       "tmnxDiamPlcyDccaAvpImsiOrg": tmnxDiamPlcyDccaAvpImsiOrg,
       "tmnxDiamPlcyDccaApplicationType": tmnxDiamPlcyDccaApplicationType,
       "tmnxDiamPlcyDccaMaxPendingReq": tmnxDiamPlcyDccaMaxPendingReq,
       "tmnxDiamPlcyDccaTxRetryLimit": tmnxDiamPlcyDccaTxRetryLimit,
       "tmnxDiamPlcyDccaOutOfCreditRep": tmnxDiamPlcyDccaOutOfCreditRep,
       "tmnxDiameterObjects": tmnxDiameterObjects,
       "tmnxDiamAppPlcyTableLastCh": tmnxDiamAppPlcyTableLastCh,
       "tmnxDiamAppPlcyTable": tmnxDiamAppPlcyTable,
       "tmnxDiamAppPlcyEntry": tmnxDiamAppPlcyEntry,
       "tmnxDiamAppPlcyId": tmnxDiamAppPlcyId,
       "tmnxDiamAppPlcyRowStatus": tmnxDiamAppPlcyRowStatus,
       "tmnxDiamAppPlcyLastMgmtChange": tmnxDiamAppPlcyLastMgmtChange,
       "tmnxDiamAppPlcyFailover": tmnxDiamAppPlcyFailover,
       "tmnxDiamAppPlcyFailureHndlng": tmnxDiamAppPlcyFailureHndlng,
       "tmnxDiamAppPlcyPeerPlcy": tmnxDiamAppPlcyPeerPlcy,
       "tmnxDiamAppPlcyApplication": tmnxDiamAppPlcyApplication,
       "tmnxDiamAppPlcyTxTimer": tmnxDiamAppPlcyTxTimer,
       "tmnxDiamAppPlcyDescription": tmnxDiamAppPlcyDescription,
       "tmnxDiamApGyTableLastCh": tmnxDiamApGyTableLastCh,
       "tmnxDiamApGyTable": tmnxDiamApGyTable,
       "tmnxDiamApGyEntry": tmnxDiamApGyEntry,
       "tmnxDiamApGyLastMgmtChange": tmnxDiamApGyLastMgmtChange,
       "tmnxDiamApGyAvpServCntxtId": tmnxDiamApGyAvpServCntxtId,
       "tmnxDiamApGyAvpCldStationId": tmnxDiamApGyAvpCldStationId,
       "tmnxDiamApGyAvpRadiusUsrNme": tmnxDiamApGyAvpRadiusUsrNme,
       "tmnxDiamApGyAvpImsiOrg": tmnxDiamApGyAvpImsiOrg,
       "tmnxDiamApGyOutOfCreditRep": tmnxDiamApGyOutOfCreditRep,
       "tmnxDiamApGyVendorSupport": tmnxDiamApGyVendorSupport,
       "tmnxDiamApGySubIdOrg": tmnxDiamApGySubIdOrg,
       "tmnxDiamApGySubIdType": tmnxDiamApGySubIdType,
       "tmnxDiamApGxTableLastCh": tmnxDiamApGxTableLastCh,
       "tmnxDiamApGxTable": tmnxDiamApGxTable,
       "tmnxDiamApGxEntry": tmnxDiamApGxEntry,
       "tmnxDiamApGxLastMgmtChange": tmnxDiamApGxLastMgmtChange,
       "tmnxDiamApGxAvp": tmnxDiamApGxAvp,
       "tmnxDiamApGxAvpClngStationIdType": tmnxDiamApGxAvpClngStationIdType,
       "tmnxDiamApGxAvpNasPortBitspec": tmnxDiamApGxAvpNasPortBitspec,
       "tmnxDiamApGxAvpNasPortIdPfixType": tmnxDiamApGxAvpNasPortIdPfixType,
       "tmnxDiamApGxAvpNasPortIdPfixStr": tmnxDiamApGxAvpNasPortIdPfixStr,
       "tmnxDiamApGxAvpNasPortIdSfixType": tmnxDiamApGxAvpNasPortIdSfixType,
       "tmnxDiamApGxAvpNasPortTypeValue": tmnxDiamApGxAvpNasPortTypeValue,
       "tmnxDiamApGxAvpUeInfoType": tmnxDiamApGxAvpUeInfoType,
       "tmnxDiamApGxSubIdOrg": tmnxDiamApGxSubIdOrg,
       "tmnxDiamApGxSubIdType": tmnxDiamApGxSubIdType,
       "tmnxDiamApGxMacFormat": tmnxDiamApGxMacFormat,
       "tmnxDiamApGxReportIpAddrEvent": tmnxDiamApGxReportIpAddrEvent,
       "tmnxDiameterNotificationObjs": tmnxDiameterNotificationObjs,
       "tmnxDiamAppPlcyName": tmnxDiamAppPlcyName,
       "tmnxDiamAppPeerName": tmnxDiamAppPeerName,
       "tmnxDiamAppTrapDescription": tmnxDiamAppTrapDescription,
       "tmnxDiamAppSessionId": tmnxDiamAppSessionId,
       "tmnxDiamAppSubscrId": tmnxDiamAppSubscrId,
       "tmnxDiamAppSapId": tmnxDiamAppSapId,
       "tmnxDiamAppSLAProfName": tmnxDiamAppSLAProfName,
       "tmnxDiameterNotifyPrefix": tmnxDiameterNotifyPrefix,
       "tmnxDiameterNotifications": tmnxDiameterNotifications,
       "tmnxDiamPolicyPeerStateChange": tmnxDiamPolicyPeerStateChange,
       "tmnxDiamAppMessageDropped": tmnxDiamAppMessageDropped,
       "tmnxDiamAppSessionFailure": tmnxDiamAppSessionFailure}
)
