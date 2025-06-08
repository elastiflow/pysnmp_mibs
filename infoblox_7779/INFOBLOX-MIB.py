# SNMP MIB module (INFOBLOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infoblox_7779/INFOBLOX-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:44:05 2025
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

infoblox = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PhysAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


# MIB Managed Objects in the order of their OIDs

_IbProducts_ObjectIdentity = ObjectIdentity
ibProducts = _IbProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1)
)
_DNSOne_ObjectIdentity = ObjectIdentity
DNSOne = _DNSOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1)
)
_IbGlobalCounters_ObjectIdentity = ObjectIdentity
ibGlobalCounters = _IbGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1)
)
_IbBindSuccess_Type = Integer32
_IbBindSuccess_Object = MibScalar
ibBindSuccess = _IbBindSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1, 1),
    _IbBindSuccess_Type()
)
ibBindSuccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindSuccess.setStatus("current")
_IbBindReferral_Type = Integer32
_IbBindReferral_Object = MibScalar
ibBindReferral = _IbBindReferral_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1, 2),
    _IbBindReferral_Type()
)
ibBindReferral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindReferral.setStatus("current")
_IbBindNxRRset_Type = Integer32
_IbBindNxRRset_Object = MibScalar
ibBindNxRRset = _IbBindNxRRset_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1, 3),
    _IbBindNxRRset_Type()
)
ibBindNxRRset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindNxRRset.setStatus("current")
_IbBindNxDomain_Type = Integer32
_IbBindNxDomain_Object = MibScalar
ibBindNxDomain = _IbBindNxDomain_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1, 4),
    _IbBindNxDomain_Type()
)
ibBindNxDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindNxDomain.setStatus("current")
_IbBindRecursion_Type = Integer32
_IbBindRecursion_Object = MibScalar
ibBindRecursion = _IbBindRecursion_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1, 5),
    _IbBindRecursion_Type()
)
ibBindRecursion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindRecursion.setStatus("current")
_IbBindFailure_Type = Integer32
_IbBindFailure_Object = MibScalar
ibBindFailure = _IbBindFailure_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 1, 6),
    _IbBindFailure_Type()
)
ibBindFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindFailure.setStatus("current")
_IbZoneStatisticsTable_Object = MibTable
ibZoneStatisticsTable = _IbZoneStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ibZoneStatisticsTable.setStatus("current")
_IbZoneStatisticsEntry_Object = MibTableRow
ibZoneStatisticsEntry = _IbZoneStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1)
)
ibZoneStatisticsEntry.setIndexNames(
    (0, "INFOBLOX-MIB", "ibBindZoneIndex"),
)
if mibBuilder.loadTexts:
    ibZoneStatisticsEntry.setStatus("current")
_IbBindZoneIndex_Type = Integer32
_IbBindZoneIndex_Object = MibTableColumn
ibBindZoneIndex = _IbBindZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 1),
    _IbBindZoneIndex_Type()
)
ibBindZoneIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneIndex.setStatus("current")
_IbBindZoneName_Type = String
_IbBindZoneName_Object = MibTableColumn
ibBindZoneName = _IbBindZoneName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 2),
    _IbBindZoneName_Type()
)
ibBindZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneName.setStatus("current")
_IbBindZoneSuccess_Type = Integer32
_IbBindZoneSuccess_Object = MibTableColumn
ibBindZoneSuccess = _IbBindZoneSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 3),
    _IbBindZoneSuccess_Type()
)
ibBindZoneSuccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneSuccess.setStatus("current")
_IbBindZoneReferral_Type = Integer32
_IbBindZoneReferral_Object = MibTableColumn
ibBindZoneReferral = _IbBindZoneReferral_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 4),
    _IbBindZoneReferral_Type()
)
ibBindZoneReferral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneReferral.setStatus("current")
_IbBindZoneNxRRset_Type = Integer32
_IbBindZoneNxRRset_Object = MibTableColumn
ibBindZoneNxRRset = _IbBindZoneNxRRset_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 5),
    _IbBindZoneNxRRset_Type()
)
ibBindZoneNxRRset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneNxRRset.setStatus("current")
_IbBindZoneNxDomain_Type = Integer32
_IbBindZoneNxDomain_Object = MibTableColumn
ibBindZoneNxDomain = _IbBindZoneNxDomain_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 6),
    _IbBindZoneNxDomain_Type()
)
ibBindZoneNxDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneNxDomain.setStatus("current")
_IbBindZoneRecursion_Type = Integer32
_IbBindZoneRecursion_Object = MibTableColumn
ibBindZoneRecursion = _IbBindZoneRecursion_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 7),
    _IbBindZoneRecursion_Type()
)
ibBindZoneRecursion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneRecursion.setStatus("current")
_IbBindZoneFailure_Type = Integer32
_IbBindZoneFailure_Object = MibTableColumn
ibBindZoneFailure = _IbBindZoneFailure_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 2, 1, 8),
    _IbBindZoneFailure_Type()
)
ibBindZoneFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibBindZoneFailure.setStatus("current")
_IbDHCPSubnetTable_Object = MibTable
ibDHCPSubnetTable = _IbDHCPSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ibDHCPSubnetTable.setStatus("current")
_IbDHCPSubnetEntry_Object = MibTableRow
ibDHCPSubnetEntry = _IbDHCPSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 3, 1)
)
ibDHCPSubnetEntry.setIndexNames(
    (0, "INFOBLOX-MIB", "ibDHCPSubnetIndex"),
)
if mibBuilder.loadTexts:
    ibDHCPSubnetEntry.setStatus("current")
_IbDHCPSubnetIndex_Type = Integer32
_IbDHCPSubnetIndex_Object = MibTableColumn
ibDHCPSubnetIndex = _IbDHCPSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 3, 1, 1),
    _IbDHCPSubnetIndex_Type()
)
ibDHCPSubnetIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPSubnetIndex.setStatus("current")
_IbDHCPSubnetNetworkAddress_Type = IpAddress
_IbDHCPSubnetNetworkAddress_Object = MibTableColumn
ibDHCPSubnetNetworkAddress = _IbDHCPSubnetNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 3, 1, 2),
    _IbDHCPSubnetNetworkAddress_Type()
)
ibDHCPSubnetNetworkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPSubnetNetworkAddress.setStatus("current")
_IbDHCPSubnetPercentUsed_Type = Integer32
_IbDHCPSubnetPercentUsed_Object = MibTableColumn
ibDHCPSubnetPercentUsed = _IbDHCPSubnetPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 3, 1, 3),
    _IbDHCPSubnetPercentUsed_Type()
)
ibDHCPSubnetPercentUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPSubnetPercentUsed.setStatus("current")
_IbDHCPLeaseTable_Object = MibTable
ibDHCPLeaseTable = _IbDHCPLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ibDHCPLeaseTable.setStatus("current")
_IbDHCPLeaseEntry_Object = MibTableRow
ibDHCPLeaseEntry = _IbDHCPLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1)
)
ibDHCPLeaseEntry.setIndexNames(
    (0, "INFOBLOX-MIB", "ibDHCPLeaseIndex"),
)
if mibBuilder.loadTexts:
    ibDHCPLeaseEntry.setStatus("current")
_IbDHCPLeaseIndex_Type = Integer32
_IbDHCPLeaseIndex_Object = MibTableColumn
ibDHCPLeaseIndex = _IbDHCPLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 1),
    _IbDHCPLeaseIndex_Type()
)
ibDHCPLeaseIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseIndex.setStatus("current")
_IbDHCPLeaseAddress_Type = IpAddress
_IbDHCPLeaseAddress_Object = MibTableColumn
ibDHCPLeaseAddress = _IbDHCPLeaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 2),
    _IbDHCPLeaseAddress_Type()
)
ibDHCPLeaseAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseAddress.setStatus("current")
_IbDHCPLeaseMACAddress_Type = String
_IbDHCPLeaseMACAddress_Object = MibTableColumn
ibDHCPLeaseMACAddress = _IbDHCPLeaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 3),
    _IbDHCPLeaseMACAddress_Type()
)
ibDHCPLeaseMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseMACAddress.setStatus("current")
_IbDHCPLeaseStart_Type = String
_IbDHCPLeaseStart_Object = MibTableColumn
ibDHCPLeaseStart = _IbDHCPLeaseStart_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 4),
    _IbDHCPLeaseStart_Type()
)
ibDHCPLeaseStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseStart.setStatus("current")
_IbDHCPLeaseEnd_Type = String
_IbDHCPLeaseEnd_Object = MibTableColumn
ibDHCPLeaseEnd = _IbDHCPLeaseEnd_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 5),
    _IbDHCPLeaseEnd_Type()
)
ibDHCPLeaseEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseEnd.setStatus("current")
_IbDHCPLeaseBindState_Type = String
_IbDHCPLeaseBindState_Object = MibTableColumn
ibDHCPLeaseBindState = _IbDHCPLeaseBindState_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 6),
    _IbDHCPLeaseBindState_Type()
)
ibDHCPLeaseBindState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseBindState.setStatus("current")
_IbDHCPLeaseNextBindState_Type = String
_IbDHCPLeaseNextBindState_Object = MibTableColumn
ibDHCPLeaseNextBindState = _IbDHCPLeaseNextBindState_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 7),
    _IbDHCPLeaseNextBindState_Type()
)
ibDHCPLeaseNextBindState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseNextBindState.setStatus("current")
_IbDHCPLeaseddnsFwdName_Type = String
_IbDHCPLeaseddnsFwdName_Object = MibTableColumn
ibDHCPLeaseddnsFwdName = _IbDHCPLeaseddnsFwdName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 8),
    _IbDHCPLeaseddnsFwdName_Type()
)
ibDHCPLeaseddnsFwdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseddnsFwdName.setStatus("current")
_IbDHCPLeaseddnsRevName_Type = String
_IbDHCPLeaseddnsRevName_Object = MibTableColumn
ibDHCPLeaseddnsRevName = _IbDHCPLeaseddnsRevName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 9),
    _IbDHCPLeaseddnsRevName_Type()
)
ibDHCPLeaseddnsRevName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseddnsRevName.setStatus("current")
_IbDHCPLeaseClientHostName_Type = String
_IbDHCPLeaseClientHostName_Object = MibTableColumn
ibDHCPLeaseClientHostName = _IbDHCPLeaseClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 10),
    _IbDHCPLeaseClientHostName_Type()
)
ibDHCPLeaseClientHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseClientHostName.setStatus("current")
_IbDHCPLeaseUID_Type = String
_IbDHCPLeaseUID_Object = MibTableColumn
ibDHCPLeaseUID = _IbDHCPLeaseUID_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 11),
    _IbDHCPLeaseUID_Type()
)
ibDHCPLeaseUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseUID.setStatus("current")
_IbDHCPLeaseGID_Type = String
_IbDHCPLeaseGID_Object = MibTableColumn
ibDHCPLeaseGID = _IbDHCPLeaseGID_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 12),
    _IbDHCPLeaseGID_Type()
)
ibDHCPLeaseGID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseGID.setStatus("current")
_IbDHCPLeaseTSTP_Type = String
_IbDHCPLeaseTSTP_Object = MibTableColumn
ibDHCPLeaseTSTP = _IbDHCPLeaseTSTP_Object(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 4, 1, 13),
    _IbDHCPLeaseTSTP_Type()
)
ibDHCPLeaseTSTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibDHCPLeaseTSTP.setStatus("current")
_IbInfo_ObjectIdentity = ObjectIdentity
ibInfo = _IbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 99)
)
_IbTrapInfo_ObjectIdentity = ObjectIdentity
ibTrapInfo = _IbTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 99, 101)
)
_IbFailure_ObjectIdentity = ObjectIdentity
ibFailure = _IbFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 99, 101, 1)
)
_IbTraps_ObjectIdentity = ObjectIdentity
ibTraps = _IbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100)
)
_IbTrapsV1_ObjectIdentity = ObjectIdentity
ibTrapsV1 = _IbTrapsV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 1)
)
_IbTrapsV2_ObjectIdentity = ObjectIdentity
ibTrapsV2 = _IbTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2)
)
_LDAPOne_ObjectIdentity = ObjectIdentity
LDAPOne = _LDAPOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 2)
)
_RadiusOne_ObjectIdentity = ObjectIdentity
RadiusOne = _RadiusOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 1, 3)
)

# Managed Objects groups


# Notification objects

ibUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    ibUnknown.setStatus(
        "current"
    )

ibDHCPdSoftwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 2)
)
if mibBuilder.loadTexts:
    ibDHCPdSoftwareFailure.setStatus(
        "current"
    )

ibHAStateChangeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 3)
)
if mibBuilder.loadTexts:
    ibHAStateChangeActive.setStatus(
        "current"
    )

ibHAStateChangePassive = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 4)
)
if mibBuilder.loadTexts:
    ibHAStateChangePassive.setStatus(
        "current"
    )

ibHAPublicRouterToleranceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 5)
)
if mibBuilder.loadTexts:
    ibHAPublicRouterToleranceFailure.setStatus(
        "current"
    )

ibHAPublicSharedAddressFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 6)
)
if mibBuilder.loadTexts:
    ibHAPublicSharedAddressFailure.setStatus(
        "current"
    )

ibHAPrivateRemoteAddressFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 7)
)
if mibBuilder.loadTexts:
    ibHAPrivateRemoteAddressFailure.setStatus(
        "current"
    )

ibApacheSoftwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 8)
)
if mibBuilder.loadTexts:
    ibApacheSoftwareFailure.setStatus(
        "current"
    )

ibNamedFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 9)
)
if mibBuilder.loadTexts:
    ibNamedFailure.setStatus(
        "current"
    )

ibDBFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 10)
)
if mibBuilder.loadTexts:
    ibDBFailure.setStatus(
        "current"
    )

ibHAFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 11)
)
if mibBuilder.loadTexts:
    ibHAFailureCleared.setStatus(
        "current"
    )

ibConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 1, 1, 100, 2, 88)
)
if mibBuilder.loadTexts:
    ibConfigurationChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFOBLOX-MIB",
    **{"String": String,
       "PhysAddress": PhysAddress,
       "infoblox": infoblox,
       "ibProducts": ibProducts,
       "DNSOne": DNSOne,
       "ibGlobalCounters": ibGlobalCounters,
       "ibBindSuccess": ibBindSuccess,
       "ibBindReferral": ibBindReferral,
       "ibBindNxRRset": ibBindNxRRset,
       "ibBindNxDomain": ibBindNxDomain,
       "ibBindRecursion": ibBindRecursion,
       "ibBindFailure": ibBindFailure,
       "ibZoneStatisticsTable": ibZoneStatisticsTable,
       "ibZoneStatisticsEntry": ibZoneStatisticsEntry,
       "ibBindZoneIndex": ibBindZoneIndex,
       "ibBindZoneName": ibBindZoneName,
       "ibBindZoneSuccess": ibBindZoneSuccess,
       "ibBindZoneReferral": ibBindZoneReferral,
       "ibBindZoneNxRRset": ibBindZoneNxRRset,
       "ibBindZoneNxDomain": ibBindZoneNxDomain,
       "ibBindZoneRecursion": ibBindZoneRecursion,
       "ibBindZoneFailure": ibBindZoneFailure,
       "ibDHCPSubnetTable": ibDHCPSubnetTable,
       "ibDHCPSubnetEntry": ibDHCPSubnetEntry,
       "ibDHCPSubnetIndex": ibDHCPSubnetIndex,
       "ibDHCPSubnetNetworkAddress": ibDHCPSubnetNetworkAddress,
       "ibDHCPSubnetPercentUsed": ibDHCPSubnetPercentUsed,
       "ibDHCPLeaseTable": ibDHCPLeaseTable,
       "ibDHCPLeaseEntry": ibDHCPLeaseEntry,
       "ibDHCPLeaseIndex": ibDHCPLeaseIndex,
       "ibDHCPLeaseAddress": ibDHCPLeaseAddress,
       "ibDHCPLeaseMACAddress": ibDHCPLeaseMACAddress,
       "ibDHCPLeaseStart": ibDHCPLeaseStart,
       "ibDHCPLeaseEnd": ibDHCPLeaseEnd,
       "ibDHCPLeaseBindState": ibDHCPLeaseBindState,
       "ibDHCPLeaseNextBindState": ibDHCPLeaseNextBindState,
       "ibDHCPLeaseddnsFwdName": ibDHCPLeaseddnsFwdName,
       "ibDHCPLeaseddnsRevName": ibDHCPLeaseddnsRevName,
       "ibDHCPLeaseClientHostName": ibDHCPLeaseClientHostName,
       "ibDHCPLeaseUID": ibDHCPLeaseUID,
       "ibDHCPLeaseGID": ibDHCPLeaseGID,
       "ibDHCPLeaseTSTP": ibDHCPLeaseTSTP,
       "ibInfo": ibInfo,
       "ibTrapInfo": ibTrapInfo,
       "ibFailure": ibFailure,
       "ibTraps": ibTraps,
       "ibTrapsV1": ibTrapsV1,
       "ibTrapsV2": ibTrapsV2,
       "ibUnknown": ibUnknown,
       "ibDHCPdSoftwareFailure": ibDHCPdSoftwareFailure,
       "ibHAStateChangeActive": ibHAStateChangeActive,
       "ibHAStateChangePassive": ibHAStateChangePassive,
       "ibHAPublicRouterToleranceFailure": ibHAPublicRouterToleranceFailure,
       "ibHAPublicSharedAddressFailure": ibHAPublicSharedAddressFailure,
       "ibHAPrivateRemoteAddressFailure": ibHAPrivateRemoteAddressFailure,
       "ibApacheSoftwareFailure": ibApacheSoftwareFailure,
       "ibNamedFailure": ibNamedFailure,
       "ibDBFailure": ibDBFailure,
       "ibHAFailureCleared": ibHAFailureCleared,
       "ibConfigurationChanged": ibConfigurationChanged,
       "LDAPOne": LDAPOne,
       "RadiusOne": RadiusOne}
)
