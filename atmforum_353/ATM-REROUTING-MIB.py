# SNMP MIB module (ATM-REROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/ATM-REROUTING-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:04:44 2025
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

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atmfreroutingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1)
)
if mibBuilder.loadTexts:
    atmfreroutingMIB.setRevisions(
        ("2001-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NetworkReroutingCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dbrHardRerouting", 0),
          ("dbrAsymmetricSoftRerouting", 1),
          ("dbrSymmetricSoftRerouting", 2))
    )


class HardReroutingServicesClass(TextualConvention, Integer32):
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
          ("dbrInterDomainHardRerouting", 2),
          ("dbrIntraDomainHardRerouting", 3))
    )



class SoftReroutingServicesClass(TextualConvention, Integer32):
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
          ("dbrIntraDomainAsymmetricSoftRerouting", 2),
          ("dbrIntraDomainSymmetricSoftRerouting", 3))
    )



class ReroutingNodeRole(TextualConvention, Integer32):
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
        *(("other", 1),
          ("sourceNode", 2),
          ("destinationNode", 3))
    )



class ReroutingState(TextualConvention, Integer32):
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
        *(("idle", 1),
          ("hardReroute", 2),
          ("softReroute", 3))
    )



class ExtendedReroutingState(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("reroutingIdle", 2),
          ("hardRerouteTriggered", 3),
          ("hardRerouteProceeding", 4),
          ("hardRerouteIndicated", 5),
          ("hardRerouteInitiated", 6),
          ("softRerouteTriggered", 7),
          ("softRerouteProceeding", 8),
          ("softRerouteInitiated", 9),
          ("awaitingSwitchover", 10))
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSignalling_ObjectIdentity = ObjectIdentity
atmfSignalling = _AtmfSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9)
)
_AtmfRerouting_ObjectIdentity = ObjectIdentity
atmfRerouting = _AtmfRerouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3)
)
_ReroutingMIBObjects_ObjectIdentity = ObjectIdentity
reroutingMIBObjects = _ReroutingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1)
)
_ReroutingBaseGroup_ObjectIdentity = ObjectIdentity
reroutingBaseGroup = _ReroutingBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1)
)


class _ReroutingVersion_Type(Integer32):
    """Custom type reroutingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version1point0", 2))
    )


_ReroutingVersion_Type.__name__ = "Integer32"
_ReroutingVersion_Object = MibScalar
reroutingVersion = _ReroutingVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1, 1),
    _ReroutingVersion_Type()
)
reroutingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVersion.setStatus("current")


class _ReroutingCapabilitiesSupported_Type(Bits):
    """Custom type reroutingCapabilitiesSupported based on Bits"""
    namedValues = NamedValues(
        *(("dbrHardRerouting", 0),
          ("dbrAsymmetricSoftRerouting", 1),
          ("dbrSymmetricSoftRerouting", 2))
    )

_ReroutingCapabilitiesSupported_Type.__name__ = "Bits"
_ReroutingCapabilitiesSupported_Object = MibScalar
reroutingCapabilitiesSupported = _ReroutingCapabilitiesSupported_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1, 2),
    _ReroutingCapabilitiesSupported_Type()
)
reroutingCapabilitiesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingCapabilitiesSupported.setStatus("current")
_ReroutingHardReroutingTime_Type = Unsigned32
_ReroutingHardReroutingTime_Object = MibScalar
reroutingHardReroutingTime = _ReroutingHardReroutingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1, 3),
    _ReroutingHardReroutingTime_Type()
)
reroutingHardReroutingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reroutingHardReroutingTime.setStatus("current")
_ReroutingFilterTable_Object = MibTable
reroutingFilterTable = _ReroutingFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    reroutingFilterTable.setStatus("current")
_ReroutingFilterEntry_Object = MibTableRow
reroutingFilterEntry = _ReroutingFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1)
)
reroutingFilterEntry.setIndexNames(
    (0, "ATM-REROUTING-MIB", "reroutingFilterIndex"),
)
if mibBuilder.loadTexts:
    reroutingFilterEntry.setStatus("current")


class _ReroutingFilterIndex_Type(Integer32):
    """Custom type reroutingFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ReroutingFilterIndex_Type.__name__ = "Integer32"
_ReroutingFilterIndex_Object = MibTableColumn
reroutingFilterIndex = _ReroutingFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 1),
    _ReroutingFilterIndex_Type()
)
reroutingFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reroutingFilterIndex.setStatus("current")


class _ReroutingFilterIfDirection_Type(Integer32):
    """Custom type reroutingFilterIfDirection based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("in", 1),
          ("out", 2),
          ("both", 3))
    )


_ReroutingFilterIfDirection_Type.__name__ = "Integer32"
_ReroutingFilterIfDirection_Object = MibTableColumn
reroutingFilterIfDirection = _ReroutingFilterIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 2),
    _ReroutingFilterIfDirection_Type()
)
reroutingFilterIfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterIfDirection.setStatus("current")
_ReroutingFilterInterface_Type = InterfaceIndex
_ReroutingFilterInterface_Object = MibTableColumn
reroutingFilterInterface = _ReroutingFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 3),
    _ReroutingFilterInterface_Type()
)
reroutingFilterInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterInterface.setStatus("current")


class _ReroutingFilterConnKind_Type(Bits):
    """Custom type reroutingFilterConnKind based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("svcAndSpvcNotInitiator", 1),
          ("spvcInitiator", 2),
          ("svpAndSpvpNotInitiator", 3),
          ("spvpInitiator", 4))
    )

_ReroutingFilterConnKind_Type.__name__ = "Bits"
_ReroutingFilterConnKind_Object = MibTableColumn
reroutingFilterConnKind = _ReroutingFilterConnKind_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 4),
    _ReroutingFilterConnKind_Type()
)
reroutingFilterConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterConnKind.setStatus("current")


class _ReroutingFilterServiceCategory_Type(Bits):
    """Custom type reroutingFilterServiceCategory based on Bits"""
    namedValues = NamedValues(
        *(("cbr", 0),
          ("rtVbr", 1),
          ("nrtVbr", 2),
          ("abr", 3),
          ("ubr", 4),
          ("gfr", 5),
          ("other", 6))
    )

_ReroutingFilterServiceCategory_Type.__name__ = "Bits"
_ReroutingFilterServiceCategory_Object = MibTableColumn
reroutingFilterServiceCategory = _ReroutingFilterServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 5),
    _ReroutingFilterServiceCategory_Type()
)
reroutingFilterServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterServiceCategory.setStatus("current")


class _ReroutingFilterCallingPartyPrefix_Type(AtmAddr):
    """Custom type reroutingFilterCallingPartyPrefix based on AtmAddr"""
    defaultValue = OctetString("")


_ReroutingFilterCallingPartyPrefix_Type.__name__ = "AtmAddr"
_ReroutingFilterCallingPartyPrefix_Object = MibTableColumn
reroutingFilterCallingPartyPrefix = _ReroutingFilterCallingPartyPrefix_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 6),
    _ReroutingFilterCallingPartyPrefix_Type()
)
reroutingFilterCallingPartyPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterCallingPartyPrefix.setStatus("current")


class _ReroutingFilterCallingPartyLength_Type(Integer32):
    """Custom type reroutingFilterCallingPartyLength based on Integer32"""
    defaultValue = 152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_ReroutingFilterCallingPartyLength_Type.__name__ = "Integer32"
_ReroutingFilterCallingPartyLength_Object = MibTableColumn
reroutingFilterCallingPartyLength = _ReroutingFilterCallingPartyLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 7),
    _ReroutingFilterCallingPartyLength_Type()
)
reroutingFilterCallingPartyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterCallingPartyLength.setStatus("current")


class _ReroutingFilterCalledPartyPrefix_Type(AtmAddr):
    """Custom type reroutingFilterCalledPartyPrefix based on AtmAddr"""
    defaultValue = OctetString("")


_ReroutingFilterCalledPartyPrefix_Type.__name__ = "AtmAddr"
_ReroutingFilterCalledPartyPrefix_Object = MibTableColumn
reroutingFilterCalledPartyPrefix = _ReroutingFilterCalledPartyPrefix_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 8),
    _ReroutingFilterCalledPartyPrefix_Type()
)
reroutingFilterCalledPartyPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterCalledPartyPrefix.setStatus("current")


class _ReroutingFilterCalledPartyLength_Type(Integer32):
    """Custom type reroutingFilterCalledPartyLength based on Integer32"""
    defaultValue = 152

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_ReroutingFilterCalledPartyLength_Type.__name__ = "Integer32"
_ReroutingFilterCalledPartyLength_Object = MibTableColumn
reroutingFilterCalledPartyLength = _ReroutingFilterCalledPartyLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 9),
    _ReroutingFilterCalledPartyLength_Type()
)
reroutingFilterCalledPartyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterCalledPartyLength.setStatus("current")
_ReroutingFilterNetworkServicesAvailable_Type = NetworkReroutingCapabilities
_ReroutingFilterNetworkServicesAvailable_Object = MibTableColumn
reroutingFilterNetworkServicesAvailable = _ReroutingFilterNetworkServicesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 10),
    _ReroutingFilterNetworkServicesAvailable_Type()
)
reroutingFilterNetworkServicesAvailable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterNetworkServicesAvailable.setStatus("current")


class _ReroutingFilterHardReroutingServiceRequest_Type(HardReroutingServicesClass):
    """Custom type reroutingFilterHardReroutingServiceRequest based on HardReroutingServicesClass"""
    defaultValue = 1


_ReroutingFilterHardReroutingServiceRequest_Type.__name__ = "HardReroutingServicesClass"
_ReroutingFilterHardReroutingServiceRequest_Object = MibTableColumn
reroutingFilterHardReroutingServiceRequest = _ReroutingFilterHardReroutingServiceRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 11),
    _ReroutingFilterHardReroutingServiceRequest_Type()
)
reroutingFilterHardReroutingServiceRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterHardReroutingServiceRequest.setStatus("current")


class _ReroutingFilterSoftReroutingServiceRequest_Type(SoftReroutingServicesClass):
    """Custom type reroutingFilterSoftReroutingServiceRequest based on SoftReroutingServicesClass"""
    defaultValue = 1


_ReroutingFilterSoftReroutingServiceRequest_Type.__name__ = "SoftReroutingServicesClass"
_ReroutingFilterSoftReroutingServiceRequest_Object = MibTableColumn
reroutingFilterSoftReroutingServiceRequest = _ReroutingFilterSoftReroutingServiceRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 12),
    _ReroutingFilterSoftReroutingServiceRequest_Type()
)
reroutingFilterSoftReroutingServiceRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterSoftReroutingServiceRequest.setStatus("current")
_ReroutingFilterRowStatus_Type = RowStatus
_ReroutingFilterRowStatus_Object = MibTableColumn
reroutingFilterRowStatus = _ReroutingFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 13),
    _ReroutingFilterRowStatus_Type()
)
reroutingFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    reroutingFilterRowStatus.setStatus("current")
_ReroutingVpTable_Object = MibTable
reroutingVpTable = _ReroutingVpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    reroutingVpTable.setStatus("current")
_ReroutingVpEntry_Object = MibTableRow
reroutingVpEntry = _ReroutingVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1)
)
reroutingVpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    reroutingVpEntry.setStatus("current")
_ReroutingVpNodeRole_Type = ReroutingNodeRole
_ReroutingVpNodeRole_Object = MibTableColumn
reroutingVpNodeRole = _ReroutingVpNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 1),
    _ReroutingVpNodeRole_Type()
)
reroutingVpNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpNodeRole.setStatus("current")
_ReroutingVpRemoteNodeAddress_Type = AtmAddr
_ReroutingVpRemoteNodeAddress_Object = MibTableColumn
reroutingVpRemoteNodeAddress = _ReroutingVpRemoteNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 2),
    _ReroutingVpRemoteNodeAddress_Type()
)
reroutingVpRemoteNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpRemoteNodeAddress.setStatus("current")
_ReroutingVpHardReroutingServiceActivated_Type = HardReroutingServicesClass
_ReroutingVpHardReroutingServiceActivated_Object = MibTableColumn
reroutingVpHardReroutingServiceActivated = _ReroutingVpHardReroutingServiceActivated_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 3),
    _ReroutingVpHardReroutingServiceActivated_Type()
)
reroutingVpHardReroutingServiceActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpHardReroutingServiceActivated.setStatus("current")
_ReroutingVpSoftReroutingServiceActivated_Type = SoftReroutingServicesClass
_ReroutingVpSoftReroutingServiceActivated_Object = MibTableColumn
reroutingVpSoftReroutingServiceActivated = _ReroutingVpSoftReroutingServiceActivated_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 4),
    _ReroutingVpSoftReroutingServiceActivated_Type()
)
reroutingVpSoftReroutingServiceActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpSoftReroutingServiceActivated.setStatus("current")
_ReroutingVpReroutingState_Type = ReroutingState
_ReroutingVpReroutingState_Object = MibTableColumn
reroutingVpReroutingState = _ReroutingVpReroutingState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 5),
    _ReroutingVpReroutingState_Type()
)
reroutingVpReroutingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpReroutingState.setStatus("current")
_ReroutingVpReroutingOperationSuccessCounter_Type = Counter32
_ReroutingVpReroutingOperationSuccessCounter_Object = MibTableColumn
reroutingVpReroutingOperationSuccessCounter = _ReroutingVpReroutingOperationSuccessCounter_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 6),
    _ReroutingVpReroutingOperationSuccessCounter_Type()
)
reroutingVpReroutingOperationSuccessCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpReroutingOperationSuccessCounter.setStatus("current")
_ReroutingVpReroutingOperationFailuresCounter_Type = Counter32
_ReroutingVpReroutingOperationFailuresCounter_Object = MibTableColumn
reroutingVpReroutingOperationFailuresCounter = _ReroutingVpReroutingOperationFailuresCounter_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 7),
    _ReroutingVpReroutingOperationFailuresCounter_Type()
)
reroutingVpReroutingOperationFailuresCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpReroutingOperationFailuresCounter.setStatus("current")


class _ReroutingVpLocalIncarnationNumber_Type(Integer32):
    """Custom type reroutingVpLocalIncarnationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ReroutingVpLocalIncarnationNumber_Type.__name__ = "Integer32"
_ReroutingVpLocalIncarnationNumber_Object = MibTableColumn
reroutingVpLocalIncarnationNumber = _ReroutingVpLocalIncarnationNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 8),
    _ReroutingVpLocalIncarnationNumber_Type()
)
reroutingVpLocalIncarnationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpLocalIncarnationNumber.setStatus("current")


class _ReroutingVpRemoteIncarnationNumber_Type(Integer32):
    """Custom type reroutingVpRemoteIncarnationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ReroutingVpRemoteIncarnationNumber_Type.__name__ = "Integer32"
_ReroutingVpRemoteIncarnationNumber_Object = MibTableColumn
reroutingVpRemoteIncarnationNumber = _ReroutingVpRemoteIncarnationNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 9),
    _ReroutingVpRemoteIncarnationNumber_Type()
)
reroutingVpRemoteIncarnationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpRemoteIncarnationNumber.setStatus("current")
_ReroutingVpExtendedReroutingState_Type = ExtendedReroutingState
_ReroutingVpExtendedReroutingState_Object = MibTableColumn
reroutingVpExtendedReroutingState = _ReroutingVpExtendedReroutingState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 10),
    _ReroutingVpExtendedReroutingState_Type()
)
reroutingVpExtendedReroutingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVpExtendedReroutingState.setStatus("current")
_ReroutingVcTable_Object = MibTable
reroutingVcTable = _ReroutingVcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    reroutingVcTable.setStatus("current")
_ReroutingVcEntry_Object = MibTableRow
reroutingVcEntry = _ReroutingVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1)
)
reroutingVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    reroutingVcEntry.setStatus("current")
_ReroutingVcNodeRole_Type = ReroutingNodeRole
_ReroutingVcNodeRole_Object = MibTableColumn
reroutingVcNodeRole = _ReroutingVcNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 1),
    _ReroutingVcNodeRole_Type()
)
reroutingVcNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcNodeRole.setStatus("current")
_ReroutingVcRemoteNodeAddress_Type = AtmAddr
_ReroutingVcRemoteNodeAddress_Object = MibTableColumn
reroutingVcRemoteNodeAddress = _ReroutingVcRemoteNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 2),
    _ReroutingVcRemoteNodeAddress_Type()
)
reroutingVcRemoteNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcRemoteNodeAddress.setStatus("current")
_ReroutingVcHardReroutingServiceActivated_Type = HardReroutingServicesClass
_ReroutingVcHardReroutingServiceActivated_Object = MibTableColumn
reroutingVcHardReroutingServiceActivated = _ReroutingVcHardReroutingServiceActivated_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 3),
    _ReroutingVcHardReroutingServiceActivated_Type()
)
reroutingVcHardReroutingServiceActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcHardReroutingServiceActivated.setStatus("current")
_ReroutingVcSoftReroutingServiceActivated_Type = SoftReroutingServicesClass
_ReroutingVcSoftReroutingServiceActivated_Object = MibTableColumn
reroutingVcSoftReroutingServiceActivated = _ReroutingVcSoftReroutingServiceActivated_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 4),
    _ReroutingVcSoftReroutingServiceActivated_Type()
)
reroutingVcSoftReroutingServiceActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcSoftReroutingServiceActivated.setStatus("current")
_ReroutingVcReroutingState_Type = ReroutingState
_ReroutingVcReroutingState_Object = MibTableColumn
reroutingVcReroutingState = _ReroutingVcReroutingState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 5),
    _ReroutingVcReroutingState_Type()
)
reroutingVcReroutingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcReroutingState.setStatus("current")
_ReroutingVcReroutingOperationSuccessCounter_Type = Counter32
_ReroutingVcReroutingOperationSuccessCounter_Object = MibTableColumn
reroutingVcReroutingOperationSuccessCounter = _ReroutingVcReroutingOperationSuccessCounter_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 6),
    _ReroutingVcReroutingOperationSuccessCounter_Type()
)
reroutingVcReroutingOperationSuccessCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcReroutingOperationSuccessCounter.setStatus("current")
_ReroutingVcReroutingOperationFailuresCounter_Type = Counter32
_ReroutingVcReroutingOperationFailuresCounter_Object = MibTableColumn
reroutingVcReroutingOperationFailuresCounter = _ReroutingVcReroutingOperationFailuresCounter_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 7),
    _ReroutingVcReroutingOperationFailuresCounter_Type()
)
reroutingVcReroutingOperationFailuresCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcReroutingOperationFailuresCounter.setStatus("current")


class _ReroutingVcLocalIncarnationNumber_Type(Integer32):
    """Custom type reroutingVcLocalIncarnationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ReroutingVcLocalIncarnationNumber_Type.__name__ = "Integer32"
_ReroutingVcLocalIncarnationNumber_Object = MibTableColumn
reroutingVcLocalIncarnationNumber = _ReroutingVcLocalIncarnationNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 8),
    _ReroutingVcLocalIncarnationNumber_Type()
)
reroutingVcLocalIncarnationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcLocalIncarnationNumber.setStatus("current")


class _ReroutingVcRemoteIncarnationNumber_Type(Integer32):
    """Custom type reroutingVcRemoteIncarnationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ReroutingVcRemoteIncarnationNumber_Type.__name__ = "Integer32"
_ReroutingVcRemoteIncarnationNumber_Object = MibTableColumn
reroutingVcRemoteIncarnationNumber = _ReroutingVcRemoteIncarnationNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 9),
    _ReroutingVcRemoteIncarnationNumber_Type()
)
reroutingVcRemoteIncarnationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcRemoteIncarnationNumber.setStatus("current")
_ReroutingVcExtendedReroutingState_Type = ExtendedReroutingState
_ReroutingVcExtendedReroutingState_Object = MibTableColumn
reroutingVcExtendedReroutingState = _ReroutingVcExtendedReroutingState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 10),
    _ReroutingVcExtendedReroutingState_Type()
)
reroutingVcExtendedReroutingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reroutingVcExtendedReroutingState.setStatus("current")
_ReroutingMIBConformance_ObjectIdentity = ObjectIdentity
reroutingMIBConformance = _ReroutingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2)
)
_ReroutingMIBCompliances_ObjectIdentity = ObjectIdentity
reroutingMIBCompliances = _ReroutingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 1)
)
_ReroutingMIBGroups_ObjectIdentity = ObjectIdentity
reroutingMIBGroups = _ReroutingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2)
)

# Managed Objects groups

reroutingBaseSwMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 1)
)
reroutingBaseSwMinGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingVersion"),
        ("ATM-REROUTING-MIB", "reroutingCapabilitiesSupported"))
)
if mibBuilder.loadTexts:
    reroutingBaseSwMinGroup.setStatus("current")

reroutingFilterSwMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 2)
)
reroutingFilterSwMinGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingFilterIfDirection"),
        ("ATM-REROUTING-MIB", "reroutingFilterInterface"),
        ("ATM-REROUTING-MIB", "reroutingFilterNetworkServicesAvailable"),
        ("ATM-REROUTING-MIB", "reroutingFilterHardReroutingServiceRequest"),
        ("ATM-REROUTING-MIB", "reroutingFilterSoftReroutingServiceRequest"),
        ("ATM-REROUTING-MIB", "reroutingFilterRowStatus"))
)
if mibBuilder.loadTexts:
    reroutingFilterSwMinGroup.setStatus("current")

reroutingVcSwMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 3)
)
reroutingVcSwMinGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingVcNodeRole"),
        ("ATM-REROUTING-MIB", "reroutingVcRemoteNodeAddress"),
        ("ATM-REROUTING-MIB", "reroutingVcHardReroutingServiceActivated"),
        ("ATM-REROUTING-MIB", "reroutingVcSoftReroutingServiceActivated"),
        ("ATM-REROUTING-MIB", "reroutingVcReroutingState"),
        ("ATM-REROUTING-MIB", "reroutingVcReroutingOperationSuccessCounter"),
        ("ATM-REROUTING-MIB", "reroutingVcReroutingOperationFailuresCounter"))
)
if mibBuilder.loadTexts:
    reroutingVcSwMinGroup.setStatus("current")

reroutingBaseSwOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 4)
)
reroutingBaseSwOptionalGroup.setObjects(
    ("ATM-REROUTING-MIB", "reroutingHardReroutingTime")
)
if mibBuilder.loadTexts:
    reroutingBaseSwOptionalGroup.setStatus("current")

reroutingFilterSwOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 5)
)
reroutingFilterSwOptionalGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingFilterConnKind"),
        ("ATM-REROUTING-MIB", "reroutingFilterServiceCategory"),
        ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyPrefix"),
        ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyLength"),
        ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyPrefix"),
        ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyLength"))
)
if mibBuilder.loadTexts:
    reroutingFilterSwOptionalGroup.setStatus("current")

reroutingVpSwOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 6)
)
reroutingVpSwOptionalGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingVpNodeRole"),
        ("ATM-REROUTING-MIB", "reroutingVpRemoteNodeAddress"),
        ("ATM-REROUTING-MIB", "reroutingVpHardReroutingServiceActivated"),
        ("ATM-REROUTING-MIB", "reroutingVpSoftReroutingServiceActivated"),
        ("ATM-REROUTING-MIB", "reroutingVpReroutingState"),
        ("ATM-REROUTING-MIB", "reroutingVpReroutingOperationSuccessCounter"),
        ("ATM-REROUTING-MIB", "reroutingVpReroutingOperationFailuresCounter"),
        ("ATM-REROUTING-MIB", "reroutingVpLocalIncarnationNumber"),
        ("ATM-REROUTING-MIB", "reroutingVpRemoteIncarnationNumber"),
        ("ATM-REROUTING-MIB", "reroutingVpExtendedReroutingState"))
)
if mibBuilder.loadTexts:
    reroutingVpSwOptionalGroup.setStatus("current")

reroutingVcSwOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 7)
)
reroutingVcSwOptionalGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingVcLocalIncarnationNumber"),
        ("ATM-REROUTING-MIB", "reroutingVcRemoteIncarnationNumber"),
        ("ATM-REROUTING-MIB", "reroutingVcExtendedReroutingState"))
)
if mibBuilder.loadTexts:
    reroutingVcSwOptionalGroup.setStatus("current")

reroutingBaseEsMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 8)
)
reroutingBaseEsMinGroup.setObjects(
    ("ATM-REROUTING-MIB", "reroutingVersion")
)
if mibBuilder.loadTexts:
    reroutingBaseEsMinGroup.setStatus("current")

reroutingFilterEsMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 9)
)
reroutingFilterEsMinGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingFilterIfDirection"),
        ("ATM-REROUTING-MIB", "reroutingFilterInterface"),
        ("ATM-REROUTING-MIB", "reroutingFilterHardReroutingServiceRequest"),
        ("ATM-REROUTING-MIB", "reroutingFilterRowStatus"))
)
if mibBuilder.loadTexts:
    reroutingFilterEsMinGroup.setStatus("current")

reroutingVcEsMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 10)
)
reroutingVcEsMinGroup.setObjects(
    ("ATM-REROUTING-MIB", "reroutingVcHardReroutingServiceActivated")
)
if mibBuilder.loadTexts:
    reroutingVcEsMinGroup.setStatus("current")

reroutingFilterEsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 11)
)
reroutingFilterEsOptionalGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingFilterConnKind"),
        ("ATM-REROUTING-MIB", "reroutingFilterServiceCategory"),
        ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyPrefix"),
        ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyLength"),
        ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyPrefix"),
        ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyLength"))
)
if mibBuilder.loadTexts:
    reroutingFilterEsOptionalGroup.setStatus("current")

reroutingVpEsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 12)
)
reroutingVpEsOptionalGroup.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingVpHardReroutingServiceActivated"),
        ("ATM-REROUTING-MIB", "reroutingVpSoftReroutingServiceActivated"),
        ("ATM-REROUTING-MIB", "reroutingVcSoftReroutingServiceActivated"))
)
if mibBuilder.loadTexts:
    reroutingVpEsOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

reroutingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 1, 1)
)
reroutingMIBCompliance.setObjects(
      *(("ATM-REROUTING-MIB", "reroutingBaseSwMinGroup"),
        ("ATM-REROUTING-MIB", "reroutingFilterSwMinGroup"),
        ("ATM-REROUTING-MIB", "reroutingVcSwMinGroup"),
        ("ATM-REROUTING-MIB", "reroutingBaseEsMinGroup"),
        ("ATM-REROUTING-MIB", "reroutingFilterEsMinGroup"),
        ("ATM-REROUTING-MIB", "reroutingVcEsMinGroup"))
)
if mibBuilder.loadTexts:
    reroutingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-REROUTING-MIB",
    **{"NetworkReroutingCapabilities": NetworkReroutingCapabilities,
       "HardReroutingServicesClass": HardReroutingServicesClass,
       "SoftReroutingServicesClass": SoftReroutingServicesClass,
       "ReroutingNodeRole": ReroutingNodeRole,
       "ReroutingState": ReroutingState,
       "ExtendedReroutingState": ExtendedReroutingState,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSignalling": atmfSignalling,
       "atmfRerouting": atmfRerouting,
       "atmfreroutingMIB": atmfreroutingMIB,
       "reroutingMIBObjects": reroutingMIBObjects,
       "reroutingBaseGroup": reroutingBaseGroup,
       "reroutingVersion": reroutingVersion,
       "reroutingCapabilitiesSupported": reroutingCapabilitiesSupported,
       "reroutingHardReroutingTime": reroutingHardReroutingTime,
       "reroutingFilterTable": reroutingFilterTable,
       "reroutingFilterEntry": reroutingFilterEntry,
       "reroutingFilterIndex": reroutingFilterIndex,
       "reroutingFilterIfDirection": reroutingFilterIfDirection,
       "reroutingFilterInterface": reroutingFilterInterface,
       "reroutingFilterConnKind": reroutingFilterConnKind,
       "reroutingFilterServiceCategory": reroutingFilterServiceCategory,
       "reroutingFilterCallingPartyPrefix": reroutingFilterCallingPartyPrefix,
       "reroutingFilterCallingPartyLength": reroutingFilterCallingPartyLength,
       "reroutingFilterCalledPartyPrefix": reroutingFilterCalledPartyPrefix,
       "reroutingFilterCalledPartyLength": reroutingFilterCalledPartyLength,
       "reroutingFilterNetworkServicesAvailable": reroutingFilterNetworkServicesAvailable,
       "reroutingFilterHardReroutingServiceRequest": reroutingFilterHardReroutingServiceRequest,
       "reroutingFilterSoftReroutingServiceRequest": reroutingFilterSoftReroutingServiceRequest,
       "reroutingFilterRowStatus": reroutingFilterRowStatus,
       "reroutingVpTable": reroutingVpTable,
       "reroutingVpEntry": reroutingVpEntry,
       "reroutingVpNodeRole": reroutingVpNodeRole,
       "reroutingVpRemoteNodeAddress": reroutingVpRemoteNodeAddress,
       "reroutingVpHardReroutingServiceActivated": reroutingVpHardReroutingServiceActivated,
       "reroutingVpSoftReroutingServiceActivated": reroutingVpSoftReroutingServiceActivated,
       "reroutingVpReroutingState": reroutingVpReroutingState,
       "reroutingVpReroutingOperationSuccessCounter": reroutingVpReroutingOperationSuccessCounter,
       "reroutingVpReroutingOperationFailuresCounter": reroutingVpReroutingOperationFailuresCounter,
       "reroutingVpLocalIncarnationNumber": reroutingVpLocalIncarnationNumber,
       "reroutingVpRemoteIncarnationNumber": reroutingVpRemoteIncarnationNumber,
       "reroutingVpExtendedReroutingState": reroutingVpExtendedReroutingState,
       "reroutingVcTable": reroutingVcTable,
       "reroutingVcEntry": reroutingVcEntry,
       "reroutingVcNodeRole": reroutingVcNodeRole,
       "reroutingVcRemoteNodeAddress": reroutingVcRemoteNodeAddress,
       "reroutingVcHardReroutingServiceActivated": reroutingVcHardReroutingServiceActivated,
       "reroutingVcSoftReroutingServiceActivated": reroutingVcSoftReroutingServiceActivated,
       "reroutingVcReroutingState": reroutingVcReroutingState,
       "reroutingVcReroutingOperationSuccessCounter": reroutingVcReroutingOperationSuccessCounter,
       "reroutingVcReroutingOperationFailuresCounter": reroutingVcReroutingOperationFailuresCounter,
       "reroutingVcLocalIncarnationNumber": reroutingVcLocalIncarnationNumber,
       "reroutingVcRemoteIncarnationNumber": reroutingVcRemoteIncarnationNumber,
       "reroutingVcExtendedReroutingState": reroutingVcExtendedReroutingState,
       "reroutingMIBConformance": reroutingMIBConformance,
       "reroutingMIBCompliances": reroutingMIBCompliances,
       "reroutingMIBCompliance": reroutingMIBCompliance,
       "reroutingMIBGroups": reroutingMIBGroups,
       "reroutingBaseSwMinGroup": reroutingBaseSwMinGroup,
       "reroutingFilterSwMinGroup": reroutingFilterSwMinGroup,
       "reroutingVcSwMinGroup": reroutingVcSwMinGroup,
       "reroutingBaseSwOptionalGroup": reroutingBaseSwOptionalGroup,
       "reroutingFilterSwOptionalGroup": reroutingFilterSwOptionalGroup,
       "reroutingVpSwOptionalGroup": reroutingVpSwOptionalGroup,
       "reroutingVcSwOptionalGroup": reroutingVcSwOptionalGroup,
       "reroutingBaseEsMinGroup": reroutingBaseEsMinGroup,
       "reroutingFilterEsMinGroup": reroutingFilterEsMinGroup,
       "reroutingVcEsMinGroup": reroutingVcEsMinGroup,
       "reroutingFilterEsOptionalGroup": reroutingFilterEsOptionalGroup,
       "reroutingVpEsOptionalGroup": reroutingVpEsOptionalGroup}
)
