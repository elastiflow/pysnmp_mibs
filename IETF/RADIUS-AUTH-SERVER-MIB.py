# SNMP MIB module (RADIUS-AUTH-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/RADIUS-AUTH-SERVER-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:50:29 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

radiusAuthServMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 1)
)
if mibBuilder.loadTexts:
    radiusAuthServMIB.setRevisions(
        ("2006-08-21 00:00",
         "1999-06-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusMIB_ObjectIdentity = ObjectIdentity
radiusMIB = _RadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67)
)
if mibBuilder.loadTexts:
    radiusMIB.setStatus("current")
_RadiusAuthentication_ObjectIdentity = ObjectIdentity
radiusAuthentication = _RadiusAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1)
)
_RadiusAuthServMIBObjects_ObjectIdentity = ObjectIdentity
radiusAuthServMIBObjects = _RadiusAuthServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1)
)
_RadiusAuthServ_ObjectIdentity = ObjectIdentity
radiusAuthServ = _RadiusAuthServ_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1)
)
_RadiusAuthServIdent_Type = SnmpAdminString
_RadiusAuthServIdent_Object = MibScalar
radiusAuthServIdent = _RadiusAuthServIdent_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 1),
    _RadiusAuthServIdent_Type()
)
radiusAuthServIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServIdent.setStatus("current")
_RadiusAuthServUpTime_Type = TimeTicks
_RadiusAuthServUpTime_Object = MibScalar
radiusAuthServUpTime = _RadiusAuthServUpTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 2),
    _RadiusAuthServUpTime_Type()
)
radiusAuthServUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServUpTime.setStatus("current")
_RadiusAuthServResetTime_Type = TimeTicks
_RadiusAuthServResetTime_Object = MibScalar
radiusAuthServResetTime = _RadiusAuthServResetTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 3),
    _RadiusAuthServResetTime_Type()
)
radiusAuthServResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServResetTime.setStatus("current")


class _RadiusAuthServConfigReset_Type(Integer32):
    """Custom type radiusAuthServConfigReset based on Integer32"""
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
          ("reset", 2),
          ("initializing", 3),
          ("running", 4))
    )


_RadiusAuthServConfigReset_Type.__name__ = "Integer32"
_RadiusAuthServConfigReset_Object = MibScalar
radiusAuthServConfigReset = _RadiusAuthServConfigReset_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 4),
    _RadiusAuthServConfigReset_Type()
)
radiusAuthServConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServConfigReset.setStatus("current")
_RadiusAuthServTotalAccessRequests_Type = Counter32
_RadiusAuthServTotalAccessRequests_Object = MibScalar
radiusAuthServTotalAccessRequests = _RadiusAuthServTotalAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 5),
    _RadiusAuthServTotalAccessRequests_Type()
)
radiusAuthServTotalAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessRequests.setUnits("packets")
_RadiusAuthServTotalInvalidRequests_Type = Counter32
_RadiusAuthServTotalInvalidRequests_Object = MibScalar
radiusAuthServTotalInvalidRequests = _RadiusAuthServTotalInvalidRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 6),
    _RadiusAuthServTotalInvalidRequests_Type()
)
radiusAuthServTotalInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalInvalidRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalInvalidRequests.setUnits("packets")
_RadiusAuthServTotalDupAccessRequests_Type = Counter32
_RadiusAuthServTotalDupAccessRequests_Object = MibScalar
radiusAuthServTotalDupAccessRequests = _RadiusAuthServTotalDupAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 7),
    _RadiusAuthServTotalDupAccessRequests_Type()
)
radiusAuthServTotalDupAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalDupAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalDupAccessRequests.setUnits("packets")
_RadiusAuthServTotalAccessAccepts_Type = Counter32
_RadiusAuthServTotalAccessAccepts_Object = MibScalar
radiusAuthServTotalAccessAccepts = _RadiusAuthServTotalAccessAccepts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 8),
    _RadiusAuthServTotalAccessAccepts_Type()
)
radiusAuthServTotalAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessAccepts.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessAccepts.setUnits("packets")
_RadiusAuthServTotalAccessRejects_Type = Counter32
_RadiusAuthServTotalAccessRejects_Object = MibScalar
radiusAuthServTotalAccessRejects = _RadiusAuthServTotalAccessRejects_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 9),
    _RadiusAuthServTotalAccessRejects_Type()
)
radiusAuthServTotalAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessRejects.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessRejects.setUnits("packets")
_RadiusAuthServTotalAccessChallenges_Type = Counter32
_RadiusAuthServTotalAccessChallenges_Object = MibScalar
radiusAuthServTotalAccessChallenges = _RadiusAuthServTotalAccessChallenges_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 10),
    _RadiusAuthServTotalAccessChallenges_Type()
)
radiusAuthServTotalAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessChallenges.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessChallenges.setUnits("packets")
_RadiusAuthServTotalMalformedAccessRequests_Type = Counter32
_RadiusAuthServTotalMalformedAccessRequests_Object = MibScalar
radiusAuthServTotalMalformedAccessRequests = _RadiusAuthServTotalMalformedAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 11),
    _RadiusAuthServTotalMalformedAccessRequests_Type()
)
radiusAuthServTotalMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalMalformedAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalMalformedAccessRequests.setUnits("packets")
_RadiusAuthServTotalBadAuthenticators_Type = Counter32
_RadiusAuthServTotalBadAuthenticators_Object = MibScalar
radiusAuthServTotalBadAuthenticators = _RadiusAuthServTotalBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 12),
    _RadiusAuthServTotalBadAuthenticators_Type()
)
radiusAuthServTotalBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalBadAuthenticators.setUnits("packets")
_RadiusAuthServTotalPacketsDropped_Type = Counter32
_RadiusAuthServTotalPacketsDropped_Object = MibScalar
radiusAuthServTotalPacketsDropped = _RadiusAuthServTotalPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 13),
    _RadiusAuthServTotalPacketsDropped_Type()
)
radiusAuthServTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalPacketsDropped.setUnits("packets")
_RadiusAuthServTotalUnknownTypes_Type = Counter32
_RadiusAuthServTotalUnknownTypes_Object = MibScalar
radiusAuthServTotalUnknownTypes = _RadiusAuthServTotalUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 14),
    _RadiusAuthServTotalUnknownTypes_Type()
)
radiusAuthServTotalUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServTotalUnknownTypes.setUnits("packets")
_RadiusAuthClientTable_Object = MibTable
radiusAuthClientTable = _RadiusAuthClientTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    radiusAuthClientTable.setStatus("deprecated")
_RadiusAuthClientEntry_Object = MibTableRow
radiusAuthClientEntry = _RadiusAuthClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1)
)
radiusAuthClientEntry.setIndexNames(
    (0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthClientEntry.setStatus("deprecated")


class _RadiusAuthClientIndex_Type(Integer32):
    """Custom type radiusAuthClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAuthClientIndex_Type.__name__ = "Integer32"
_RadiusAuthClientIndex_Object = MibTableColumn
radiusAuthClientIndex = _RadiusAuthClientIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 1),
    _RadiusAuthClientIndex_Type()
)
radiusAuthClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthClientIndex.setStatus("deprecated")
_RadiusAuthClientAddress_Type = IpAddress
_RadiusAuthClientAddress_Object = MibTableColumn
radiusAuthClientAddress = _RadiusAuthClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 2),
    _RadiusAuthClientAddress_Type()
)
radiusAuthClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAddress.setStatus("deprecated")
_RadiusAuthClientID_Type = SnmpAdminString
_RadiusAuthClientID_Object = MibTableColumn
radiusAuthClientID = _RadiusAuthClientID_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 3),
    _RadiusAuthClientID_Type()
)
radiusAuthClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientID.setStatus("deprecated")
_RadiusAuthServAccessRequests_Type = Counter32
_RadiusAuthServAccessRequests_Object = MibTableColumn
radiusAuthServAccessRequests = _RadiusAuthServAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 4),
    _RadiusAuthServAccessRequests_Type()
)
radiusAuthServAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServAccessRequests.setUnits("packets")
_RadiusAuthServDupAccessRequests_Type = Counter32
_RadiusAuthServDupAccessRequests_Object = MibTableColumn
radiusAuthServDupAccessRequests = _RadiusAuthServDupAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 5),
    _RadiusAuthServDupAccessRequests_Type()
)
radiusAuthServDupAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServDupAccessRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServDupAccessRequests.setUnits("packets")
_RadiusAuthServAccessAccepts_Type = Counter32
_RadiusAuthServAccessAccepts_Object = MibTableColumn
radiusAuthServAccessAccepts = _RadiusAuthServAccessAccepts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 6),
    _RadiusAuthServAccessAccepts_Type()
)
radiusAuthServAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessAccepts.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServAccessAccepts.setUnits("packets")
_RadiusAuthServAccessRejects_Type = Counter32
_RadiusAuthServAccessRejects_Object = MibTableColumn
radiusAuthServAccessRejects = _RadiusAuthServAccessRejects_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 7),
    _RadiusAuthServAccessRejects_Type()
)
radiusAuthServAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessRejects.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServAccessRejects.setUnits("packets")
_RadiusAuthServAccessChallenges_Type = Counter32
_RadiusAuthServAccessChallenges_Object = MibTableColumn
radiusAuthServAccessChallenges = _RadiusAuthServAccessChallenges_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 8),
    _RadiusAuthServAccessChallenges_Type()
)
radiusAuthServAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessChallenges.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServAccessChallenges.setUnits("packets")
_RadiusAuthServMalformedAccessRequests_Type = Counter32
_RadiusAuthServMalformedAccessRequests_Object = MibTableColumn
radiusAuthServMalformedAccessRequests = _RadiusAuthServMalformedAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 9),
    _RadiusAuthServMalformedAccessRequests_Type()
)
radiusAuthServMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServMalformedAccessRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServMalformedAccessRequests.setUnits("packets")
_RadiusAuthServBadAuthenticators_Type = Counter32
_RadiusAuthServBadAuthenticators_Object = MibTableColumn
radiusAuthServBadAuthenticators = _RadiusAuthServBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 10),
    _RadiusAuthServBadAuthenticators_Type()
)
radiusAuthServBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServBadAuthenticators.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServBadAuthenticators.setUnits("packets")
_RadiusAuthServPacketsDropped_Type = Counter32
_RadiusAuthServPacketsDropped_Object = MibTableColumn
radiusAuthServPacketsDropped = _RadiusAuthServPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 11),
    _RadiusAuthServPacketsDropped_Type()
)
radiusAuthServPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServPacketsDropped.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServPacketsDropped.setUnits("packets")
_RadiusAuthServUnknownTypes_Type = Counter32
_RadiusAuthServUnknownTypes_Object = MibTableColumn
radiusAuthServUnknownTypes = _RadiusAuthServUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 15, 1, 12),
    _RadiusAuthServUnknownTypes_Type()
)
radiusAuthServUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServUnknownTypes.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthServUnknownTypes.setUnits("packets")
_RadiusAuthClientExtTable_Object = MibTable
radiusAuthClientExtTable = _RadiusAuthClientExtTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    radiusAuthClientExtTable.setStatus("current")
_RadiusAuthClientExtEntry_Object = MibTableRow
radiusAuthClientExtEntry = _RadiusAuthClientExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1)
)
radiusAuthClientExtEntry.setIndexNames(
    (0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientExtIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthClientExtEntry.setStatus("current")


class _RadiusAuthClientExtIndex_Type(Integer32):
    """Custom type radiusAuthClientExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAuthClientExtIndex_Type.__name__ = "Integer32"
_RadiusAuthClientExtIndex_Object = MibTableColumn
radiusAuthClientExtIndex = _RadiusAuthClientExtIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 1),
    _RadiusAuthClientExtIndex_Type()
)
radiusAuthClientExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthClientExtIndex.setStatus("current")
_RadiusAuthClientInetAddressType_Type = InetAddressType
_RadiusAuthClientInetAddressType_Object = MibTableColumn
radiusAuthClientInetAddressType = _RadiusAuthClientInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 2),
    _RadiusAuthClientInetAddressType_Type()
)
radiusAuthClientInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientInetAddressType.setStatus("current")
_RadiusAuthClientInetAddress_Type = InetAddress
_RadiusAuthClientInetAddress_Object = MibTableColumn
radiusAuthClientInetAddress = _RadiusAuthClientInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 3),
    _RadiusAuthClientInetAddress_Type()
)
radiusAuthClientInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientInetAddress.setStatus("current")
_RadiusAuthClientExtID_Type = SnmpAdminString
_RadiusAuthClientExtID_Object = MibTableColumn
radiusAuthClientExtID = _RadiusAuthClientExtID_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 4),
    _RadiusAuthClientExtID_Type()
)
radiusAuthClientExtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtID.setStatus("current")
_RadiusAuthServExtAccessRequests_Type = Counter32
_RadiusAuthServExtAccessRequests_Object = MibTableColumn
radiusAuthServExtAccessRequests = _RadiusAuthServExtAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 5),
    _RadiusAuthServExtAccessRequests_Type()
)
radiusAuthServExtAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessRequests.setUnits("packets")
_RadiusAuthServExtDupAccessRequests_Type = Counter32
_RadiusAuthServExtDupAccessRequests_Object = MibTableColumn
radiusAuthServExtDupAccessRequests = _RadiusAuthServExtDupAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 6),
    _RadiusAuthServExtDupAccessRequests_Type()
)
radiusAuthServExtDupAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtDupAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtDupAccessRequests.setUnits("packets")
_RadiusAuthServExtAccessAccepts_Type = Counter32
_RadiusAuthServExtAccessAccepts_Object = MibTableColumn
radiusAuthServExtAccessAccepts = _RadiusAuthServExtAccessAccepts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 7),
    _RadiusAuthServExtAccessAccepts_Type()
)
radiusAuthServExtAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessAccepts.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessAccepts.setUnits("packets")
_RadiusAuthServExtAccessRejects_Type = Counter32
_RadiusAuthServExtAccessRejects_Object = MibTableColumn
radiusAuthServExtAccessRejects = _RadiusAuthServExtAccessRejects_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 8),
    _RadiusAuthServExtAccessRejects_Type()
)
radiusAuthServExtAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessRejects.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessRejects.setUnits("packets")
_RadiusAuthServExtAccessChallenges_Type = Counter32
_RadiusAuthServExtAccessChallenges_Object = MibTableColumn
radiusAuthServExtAccessChallenges = _RadiusAuthServExtAccessChallenges_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 9),
    _RadiusAuthServExtAccessChallenges_Type()
)
radiusAuthServExtAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessChallenges.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtAccessChallenges.setUnits("packets")
_RadiusAuthServExtMalformedAccessRequests_Type = Counter32
_RadiusAuthServExtMalformedAccessRequests_Object = MibTableColumn
radiusAuthServExtMalformedAccessRequests = _RadiusAuthServExtMalformedAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 10),
    _RadiusAuthServExtMalformedAccessRequests_Type()
)
radiusAuthServExtMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtMalformedAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtMalformedAccessRequests.setUnits("packets")
_RadiusAuthServExtBadAuthenticators_Type = Counter32
_RadiusAuthServExtBadAuthenticators_Object = MibTableColumn
radiusAuthServExtBadAuthenticators = _RadiusAuthServExtBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 11),
    _RadiusAuthServExtBadAuthenticators_Type()
)
radiusAuthServExtBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtBadAuthenticators.setUnits("packets")
_RadiusAuthServExtPacketsDropped_Type = Counter32
_RadiusAuthServExtPacketsDropped_Object = MibTableColumn
radiusAuthServExtPacketsDropped = _RadiusAuthServExtPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 12),
    _RadiusAuthServExtPacketsDropped_Type()
)
radiusAuthServExtPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtPacketsDropped.setUnits("packets")
_RadiusAuthServExtUnknownTypes_Type = Counter32
_RadiusAuthServExtUnknownTypes_Object = MibTableColumn
radiusAuthServExtUnknownTypes = _RadiusAuthServExtUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 13),
    _RadiusAuthServExtUnknownTypes_Type()
)
radiusAuthServExtUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServExtUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServExtUnknownTypes.setUnits("packets")
_RadiusAuthServCounterDiscontinuity_Type = TimeTicks
_RadiusAuthServCounterDiscontinuity_Object = MibTableColumn
radiusAuthServCounterDiscontinuity = _RadiusAuthServCounterDiscontinuity_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 1, 1, 16, 1, 14),
    _RadiusAuthServCounterDiscontinuity_Type()
)
radiusAuthServCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthServCounterDiscontinuity.setUnits("centiseconds")
_RadiusAuthServMIBConformance_ObjectIdentity = ObjectIdentity
radiusAuthServMIBConformance = _RadiusAuthServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2)
)
_RadiusAuthServMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAuthServMIBCompliances = _RadiusAuthServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1)
)
_RadiusAuthServMIBGroups_ObjectIdentity = ObjectIdentity
radiusAuthServMIBGroups = _RadiusAuthServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2)
)

# Managed Objects groups

radiusAuthServMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2, 1)
)
radiusAuthServMIBGroup.setObjects(
      *(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownTypes"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientAddress"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientID"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServDupAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessAccepts"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRejects"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessChallenges"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMalformedAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServBadAuthenticators"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServPacketsDropped"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUnknownTypes"))
)
if mibBuilder.loadTexts:
    radiusAuthServMIBGroup.setStatus("deprecated")

radiusAuthServExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 2, 2)
)
radiusAuthServExtMIBGroup.setObjects(
      *(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownTypes"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientInetAddressType"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientInetAddress"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientExtID"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtDupAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessAccepts"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessRejects"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtAccessChallenges"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtMalformedAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtBadAuthenticators"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtPacketsDropped"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtUnknownTypes"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServCounterDiscontinuity"))
)
if mibBuilder.loadTexts:
    radiusAuthServExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAuthServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1, 1)
)
radiusAuthServMIBCompliance.setObjects(
    ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAuthServMIBCompliance.setStatus(
        "deprecated"
    )

radiusAuthServMIBExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 1, 1, 2, 1, 2)
)
radiusAuthServMIBExtCompliance.setObjects(
    ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServExtMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAuthServMIBExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-AUTH-SERVER-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAuthentication": radiusAuthentication,
       "radiusAuthServMIB": radiusAuthServMIB,
       "radiusAuthServMIBObjects": radiusAuthServMIBObjects,
       "radiusAuthServ": radiusAuthServ,
       "radiusAuthServIdent": radiusAuthServIdent,
       "radiusAuthServUpTime": radiusAuthServUpTime,
       "radiusAuthServResetTime": radiusAuthServResetTime,
       "radiusAuthServConfigReset": radiusAuthServConfigReset,
       "radiusAuthServTotalAccessRequests": radiusAuthServTotalAccessRequests,
       "radiusAuthServTotalInvalidRequests": radiusAuthServTotalInvalidRequests,
       "radiusAuthServTotalDupAccessRequests": radiusAuthServTotalDupAccessRequests,
       "radiusAuthServTotalAccessAccepts": radiusAuthServTotalAccessAccepts,
       "radiusAuthServTotalAccessRejects": radiusAuthServTotalAccessRejects,
       "radiusAuthServTotalAccessChallenges": radiusAuthServTotalAccessChallenges,
       "radiusAuthServTotalMalformedAccessRequests": radiusAuthServTotalMalformedAccessRequests,
       "radiusAuthServTotalBadAuthenticators": radiusAuthServTotalBadAuthenticators,
       "radiusAuthServTotalPacketsDropped": radiusAuthServTotalPacketsDropped,
       "radiusAuthServTotalUnknownTypes": radiusAuthServTotalUnknownTypes,
       "radiusAuthClientTable": radiusAuthClientTable,
       "radiusAuthClientEntry": radiusAuthClientEntry,
       "radiusAuthClientIndex": radiusAuthClientIndex,
       "radiusAuthClientAddress": radiusAuthClientAddress,
       "radiusAuthClientID": radiusAuthClientID,
       "radiusAuthServAccessRequests": radiusAuthServAccessRequests,
       "radiusAuthServDupAccessRequests": radiusAuthServDupAccessRequests,
       "radiusAuthServAccessAccepts": radiusAuthServAccessAccepts,
       "radiusAuthServAccessRejects": radiusAuthServAccessRejects,
       "radiusAuthServAccessChallenges": radiusAuthServAccessChallenges,
       "radiusAuthServMalformedAccessRequests": radiusAuthServMalformedAccessRequests,
       "radiusAuthServBadAuthenticators": radiusAuthServBadAuthenticators,
       "radiusAuthServPacketsDropped": radiusAuthServPacketsDropped,
       "radiusAuthServUnknownTypes": radiusAuthServUnknownTypes,
       "radiusAuthClientExtTable": radiusAuthClientExtTable,
       "radiusAuthClientExtEntry": radiusAuthClientExtEntry,
       "radiusAuthClientExtIndex": radiusAuthClientExtIndex,
       "radiusAuthClientInetAddressType": radiusAuthClientInetAddressType,
       "radiusAuthClientInetAddress": radiusAuthClientInetAddress,
       "radiusAuthClientExtID": radiusAuthClientExtID,
       "radiusAuthServExtAccessRequests": radiusAuthServExtAccessRequests,
       "radiusAuthServExtDupAccessRequests": radiusAuthServExtDupAccessRequests,
       "radiusAuthServExtAccessAccepts": radiusAuthServExtAccessAccepts,
       "radiusAuthServExtAccessRejects": radiusAuthServExtAccessRejects,
       "radiusAuthServExtAccessChallenges": radiusAuthServExtAccessChallenges,
       "radiusAuthServExtMalformedAccessRequests": radiusAuthServExtMalformedAccessRequests,
       "radiusAuthServExtBadAuthenticators": radiusAuthServExtBadAuthenticators,
       "radiusAuthServExtPacketsDropped": radiusAuthServExtPacketsDropped,
       "radiusAuthServExtUnknownTypes": radiusAuthServExtUnknownTypes,
       "radiusAuthServCounterDiscontinuity": radiusAuthServCounterDiscontinuity,
       "radiusAuthServMIBConformance": radiusAuthServMIBConformance,
       "radiusAuthServMIBCompliances": radiusAuthServMIBCompliances,
       "radiusAuthServMIBCompliance": radiusAuthServMIBCompliance,
       "radiusAuthServMIBExtCompliance": radiusAuthServMIBExtCompliance,
       "radiusAuthServMIBGroups": radiusAuthServMIBGroups,
       "radiusAuthServMIBGroup": radiusAuthServMIBGroup,
       "radiusAuthServExtMIBGroup": radiusAuthServExtMIBGroup}
)
