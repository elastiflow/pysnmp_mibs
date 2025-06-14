# SNMP MIB module (CISCO-VQE-TOOLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VQE-TOOLS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:14 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVqeToolsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969)
)
if mibBuilder.loadTexts:
    ciscoVqeToolsMIB.setRevisions(
        ("2009-12-18 13:41",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVqeToolsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVqeToolsMIBNotifs = _CiscoVqeToolsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 0)
)
_CiscoVqeToolsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVqeToolsMIBObjects = _CiscoVqeToolsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 1)
)
_CvqtVcdsInfo_ObjectIdentity = ObjectIdentity
cvqtVcdsInfo = _CvqtVcdsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1)
)
_CvqtNumberOfSessions_Type = Gauge32
_CvqtNumberOfSessions_Object = MibScalar
cvqtNumberOfSessions = _CvqtNumberOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 1),
    _CvqtNumberOfSessions_Type()
)
cvqtNumberOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqtNumberOfSessions.setStatus("current")
if mibBuilder.loadTexts:
    cvqtNumberOfSessions.setUnits("RTSP connections")
_CvqtTotalReceivedRequests_Type = Counter64
_CvqtTotalReceivedRequests_Object = MibScalar
cvqtTotalReceivedRequests = _CvqtTotalReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 2),
    _CvqtTotalReceivedRequests_Type()
)
cvqtTotalReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqtTotalReceivedRequests.setStatus("current")
if mibBuilder.loadTexts:
    cvqtTotalReceivedRequests.setUnits("RTSP requests")
_CvqtTotalSentResponses_Type = Counter64
_CvqtTotalSentResponses_Object = MibScalar
cvqtTotalSentResponses = _CvqtTotalSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 3),
    _CvqtTotalSentResponses_Type()
)
cvqtTotalSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqtTotalSentResponses.setStatus("current")
if mibBuilder.loadTexts:
    cvqtTotalSentResponses.setUnits("RTSP responses")
_CvqtRequestRate_Type = Gauge32
_CvqtRequestRate_Object = MibScalar
cvqtRequestRate = _CvqtRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 4),
    _CvqtRequestRate_Type()
)
cvqtRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvqtRequestRate.setStatus("current")
if mibBuilder.loadTexts:
    cvqtRequestRate.setUnits("requests per second")
_CiscoVqeToolsMIBConform_ObjectIdentity = ObjectIdentity
ciscoVqeToolsMIBConform = _CiscoVqeToolsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 2)
)
_CvqtMIBCompliances_ObjectIdentity = ObjectIdentity
cvqtMIBCompliances = _CvqtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1)
)
_CvqtMIBGroups_ObjectIdentity = ObjectIdentity
cvqtMIBGroups = _CvqtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2)
)

# Managed Objects groups

ciscoVqeToolsVcdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2, 1)
)
ciscoVqeToolsVcdsGroup.setObjects(
      *(("CISCO-VQE-TOOLS-MIB", "cvqtNumberOfSessions"),
        ("CISCO-VQE-TOOLS-MIB", "cvqtTotalReceivedRequests"),
        ("CISCO-VQE-TOOLS-MIB", "cvqtTotalSentResponses"),
        ("CISCO-VQE-TOOLS-MIB", "cvqtRequestRate"))
)
if mibBuilder.loadTexts:
    ciscoVqeToolsVcdsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvqtMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1, 1)
)
cvqtMIBReadOnlyCompliance.setObjects(
    ("CISCO-VQE-TOOLS-MIB", "ciscoVqeToolsVcdsGroup")
)
if mibBuilder.loadTexts:
    cvqtMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VQE-TOOLS-MIB",
    **{"ciscoVqeToolsMIB": ciscoVqeToolsMIB,
       "ciscoVqeToolsMIBNotifs": ciscoVqeToolsMIBNotifs,
       "ciscoVqeToolsMIBObjects": ciscoVqeToolsMIBObjects,
       "cvqtVcdsInfo": cvqtVcdsInfo,
       "cvqtNumberOfSessions": cvqtNumberOfSessions,
       "cvqtTotalReceivedRequests": cvqtTotalReceivedRequests,
       "cvqtTotalSentResponses": cvqtTotalSentResponses,
       "cvqtRequestRate": cvqtRequestRate,
       "ciscoVqeToolsMIBConform": ciscoVqeToolsMIBConform,
       "cvqtMIBCompliances": cvqtMIBCompliances,
       "cvqtMIBReadOnlyCompliance": cvqtMIBReadOnlyCompliance,
       "cvqtMIBGroups": cvqtMIBGroups,
       "ciscoVqeToolsVcdsGroup": ciscoVqeToolsVcdsGroup}
)
