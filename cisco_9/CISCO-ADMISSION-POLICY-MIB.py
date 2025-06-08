# SNMP MIB module (CISCO-ADMISSION-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ADMISSION-POLICY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:28:31 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAdmissionPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653)
)
if mibBuilder.loadTexts:
    ciscoAdmissionPolicyMIB.setRevisions(
        ("2008-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CapSessionId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class CapQosPolicy(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CapAclName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CapURLString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CapPolicyState(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("success", 2),
          ("failure", 3),
          ("inProgress", 4),
          ("ipWait", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAdmissionPolicyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoAdmissionPolicyMIBNotifs = _CiscoAdmissionPolicyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 0)
)
_CiscoAdmissionPolicyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAdmissionPolicyMIBObjects = _CiscoAdmissionPolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1)
)
_CapSessions_ObjectIdentity = ObjectIdentity
capSessions = _CapSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1)
)
_CapTotalSessions_Type = Counter32
_CapTotalSessions_Object = MibScalar
capTotalSessions = _CapTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 1),
    _CapTotalSessions_Type()
)
capTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capTotalSessions.setStatus("current")
_CapActiveSessions_Type = Gauge32
_CapActiveSessions_Object = MibScalar
capActiveSessions = _CapActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 2),
    _CapActiveSessions_Type()
)
capActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capActiveSessions.setStatus("current")
_CapSidSessionInfoTable_Object = MibTable
capSidSessionInfoTable = _CapSidSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3)
)
if mibBuilder.loadTexts:
    capSidSessionInfoTable.setStatus("current")
_CapSidSessionInfoEntry_Object = MibTableRow
capSidSessionInfoEntry = _CapSidSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1)
)
capSidSessionInfoEntry.setIndexNames(
    (1, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"),
)
if mibBuilder.loadTexts:
    capSidSessionInfoEntry.setStatus("current")
_CapSidSessionIndex_Type = CapSessionId
_CapSidSessionIndex_Object = MibTableColumn
capSidSessionIndex = _CapSidSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 1),
    _CapSidSessionIndex_Type()
)
capSidSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capSidSessionIndex.setStatus("current")
_CapSidSessionIfIndex_Type = InterfaceIndex
_CapSidSessionIfIndex_Object = MibTableColumn
capSidSessionIfIndex = _CapSidSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 2),
    _CapSidSessionIfIndex_Type()
)
capSidSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidSessionIfIndex.setStatus("current")
_CapSidSessionMacAddress_Type = MacAddress
_CapSidSessionMacAddress_Object = MibTableColumn
capSidSessionMacAddress = _CapSidSessionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 3),
    _CapSidSessionMacAddress_Type()
)
capSidSessionMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidSessionMacAddress.setStatus("current")
_CapSidSessionAddressType_Type = InetAddressType
_CapSidSessionAddressType_Object = MibTableColumn
capSidSessionAddressType = _CapSidSessionAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 4),
    _CapSidSessionAddressType_Type()
)
capSidSessionAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidSessionAddressType.setStatus("current")
_CapSidSessionAddress_Type = InetAddress
_CapSidSessionAddress_Object = MibTableColumn
capSidSessionAddress = _CapSidSessionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 5),
    _CapSidSessionAddress_Type()
)
capSidSessionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidSessionAddress.setStatus("current")


class _CapSidSessionFeatureType_Type(Bits):
    """Custom type capSidSessionFeatureType based on Bits"""
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("mab", 1),
          ("eou", 2),
          ("authProxy", 3))
    )

_CapSidSessionFeatureType_Type.__name__ = "Bits"
_CapSidSessionFeatureType_Object = MibTableColumn
capSidSessionFeatureType = _CapSidSessionFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 6),
    _CapSidSessionFeatureType_Type()
)
capSidSessionFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidSessionFeatureType.setStatus("current")
_CapSidSessionPolicyTable_Object = MibTable
capSidSessionPolicyTable = _CapSidSessionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4)
)
if mibBuilder.loadTexts:
    capSidSessionPolicyTable.setStatus("current")
_CapSidSessionPolicyEntry_Object = MibTableRow
capSidSessionPolicyEntry = _CapSidSessionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1)
)
capSidSessionPolicyEntry.setIndexNames(
    (0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"),
    (0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyIndex"),
)
if mibBuilder.loadTexts:
    capSidSessionPolicyEntry.setStatus("current")


class _CapSidSessionPolicyIndex_Type(Integer32):
    """Custom type capSidSessionPolicyIndex based on Integer32"""
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
        *(("dot1x", 1),
          ("mab", 2),
          ("eou", 3),
          ("authProxy", 4))
    )


_CapSidSessionPolicyIndex_Type.__name__ = "Integer32"
_CapSidSessionPolicyIndex_Object = MibTableColumn
capSidSessionPolicyIndex = _CapSidSessionPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 1),
    _CapSidSessionPolicyIndex_Type()
)
capSidSessionPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capSidSessionPolicyIndex.setStatus("current")
_CapSidIngressQosPolicy_Type = CapQosPolicy
_CapSidIngressQosPolicy_Object = MibTableColumn
capSidIngressQosPolicy = _CapSidIngressQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 2),
    _CapSidIngressQosPolicy_Type()
)
capSidIngressQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidIngressQosPolicy.setStatus("current")
_CapSidIngressQosPolicyState_Type = CapPolicyState
_CapSidIngressQosPolicyState_Object = MibTableColumn
capSidIngressQosPolicyState = _CapSidIngressQosPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 3),
    _CapSidIngressQosPolicyState_Type()
)
capSidIngressQosPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidIngressQosPolicyState.setStatus("current")
_CapSidEgressQosPolicy_Type = CapQosPolicy
_CapSidEgressQosPolicy_Object = MibTableColumn
capSidEgressQosPolicy = _CapSidEgressQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 4),
    _CapSidEgressQosPolicy_Type()
)
capSidEgressQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidEgressQosPolicy.setStatus("current")
_CapSidEgressQosPolicyState_Type = CapPolicyState
_CapSidEgressQosPolicyState_Object = MibTableColumn
capSidEgressQosPolicyState = _CapSidEgressQosPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 5),
    _CapSidEgressQosPolicyState_Type()
)
capSidEgressQosPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidEgressQosPolicyState.setStatus("current")
_CapSidDownloadableAclName_Type = CapAclName
_CapSidDownloadableAclName_Object = MibTableColumn
capSidDownloadableAclName = _CapSidDownloadableAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 6),
    _CapSidDownloadableAclName_Type()
)
capSidDownloadableAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidDownloadableAclName.setStatus("current")
_CapSidDownloadableAclState_Type = CapPolicyState
_CapSidDownloadableAclState_Object = MibTableColumn
capSidDownloadableAclState = _CapSidDownloadableAclState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 7),
    _CapSidDownloadableAclState_Type()
)
capSidDownloadableAclState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidDownloadableAclState.setStatus("current")
_CapSidUrlRedirectAclName_Type = CapAclName
_CapSidUrlRedirectAclName_Object = MibTableColumn
capSidUrlRedirectAclName = _CapSidUrlRedirectAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 8),
    _CapSidUrlRedirectAclName_Type()
)
capSidUrlRedirectAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidUrlRedirectAclName.setStatus("current")
_CapSidUrlRedirectAclState_Type = CapPolicyState
_CapSidUrlRedirectAclState_Object = MibTableColumn
capSidUrlRedirectAclState = _CapSidUrlRedirectAclState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 9),
    _CapSidUrlRedirectAclState_Type()
)
capSidUrlRedirectAclState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidUrlRedirectAclState.setStatus("current")
_CapSidRedirectUrlString_Type = CapURLString
_CapSidRedirectUrlString_Object = MibTableColumn
capSidRedirectUrlString = _CapSidRedirectUrlString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 10),
    _CapSidRedirectUrlString_Type()
)
capSidRedirectUrlString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidRedirectUrlString.setStatus("current")
_CapSidRedirectUrlStringState_Type = CapPolicyState
_CapSidRedirectUrlStringState_Object = MibTableColumn
capSidRedirectUrlStringState = _CapSidRedirectUrlStringState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 11),
    _CapSidRedirectUrlStringState_Type()
)
capSidRedirectUrlStringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidRedirectUrlStringState.setStatus("current")


class _CapSidSecurityGroupTag_Type(Integer32):
    """Custom type capSidSecurityGroupTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CapSidSecurityGroupTag_Type.__name__ = "Integer32"
_CapSidSecurityGroupTag_Object = MibTableColumn
capSidSecurityGroupTag = _CapSidSecurityGroupTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 12),
    _CapSidSecurityGroupTag_Type()
)
capSidSecurityGroupTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capSidSecurityGroupTag.setStatus("current")
_CiscoAdmissionPolicyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAdmissionPolicyMIBConformance = _CiscoAdmissionPolicyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2)
)
_CiscoAdmissionPolicyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAdmissionPolicyMIBCompliances = _CiscoAdmissionPolicyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1)
)
_CiscoAdmissionPolicyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAdmissionPolicyMIBGroups = _CiscoAdmissionPolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2)
)

# Managed Objects groups

capSessionStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 1)
)
capSessionStatisticsGroup.setObjects(
      *(("CISCO-ADMISSION-POLICY-MIB", "capTotalSessions"),
        ("CISCO-ADMISSION-POLICY-MIB", "capActiveSessions"))
)
if mibBuilder.loadTexts:
    capSessionStatisticsGroup.setStatus("current")

capSidSessionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 2)
)
capSidSessionInfoGroup.setObjects(
      *(("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddressType"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddress"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionIfIndex"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionMacAddress"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionFeatureType"))
)
if mibBuilder.loadTexts:
    capSidSessionInfoGroup.setStatus("current")

capSidSessionPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 3)
)
capSidSessionPolicyGroup.setObjects(
      *(("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicy"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicyState"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicy"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicyState"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclName"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclState"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlString"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlStringState"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclName"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclState"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSecurityGroupTag"))
)
if mibBuilder.loadTexts:
    capSidSessionPolicyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAdmissionPolicyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1, 1)
)
ciscoAdmissionPolicyMIBCompliance.setObjects(
      *(("CISCO-ADMISSION-POLICY-MIB", "capSessionStatisticsGroup"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyGroup"),
        ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionInfoGroup"))
)
if mibBuilder.loadTexts:
    ciscoAdmissionPolicyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ADMISSION-POLICY-MIB",
    **{"CapSessionId": CapSessionId,
       "CapQosPolicy": CapQosPolicy,
       "CapAclName": CapAclName,
       "CapURLString": CapURLString,
       "CapPolicyState": CapPolicyState,
       "ciscoAdmissionPolicyMIB": ciscoAdmissionPolicyMIB,
       "ciscoAdmissionPolicyMIBNotifs": ciscoAdmissionPolicyMIBNotifs,
       "ciscoAdmissionPolicyMIBObjects": ciscoAdmissionPolicyMIBObjects,
       "capSessions": capSessions,
       "capTotalSessions": capTotalSessions,
       "capActiveSessions": capActiveSessions,
       "capSidSessionInfoTable": capSidSessionInfoTable,
       "capSidSessionInfoEntry": capSidSessionInfoEntry,
       "capSidSessionIndex": capSidSessionIndex,
       "capSidSessionIfIndex": capSidSessionIfIndex,
       "capSidSessionMacAddress": capSidSessionMacAddress,
       "capSidSessionAddressType": capSidSessionAddressType,
       "capSidSessionAddress": capSidSessionAddress,
       "capSidSessionFeatureType": capSidSessionFeatureType,
       "capSidSessionPolicyTable": capSidSessionPolicyTable,
       "capSidSessionPolicyEntry": capSidSessionPolicyEntry,
       "capSidSessionPolicyIndex": capSidSessionPolicyIndex,
       "capSidIngressQosPolicy": capSidIngressQosPolicy,
       "capSidIngressQosPolicyState": capSidIngressQosPolicyState,
       "capSidEgressQosPolicy": capSidEgressQosPolicy,
       "capSidEgressQosPolicyState": capSidEgressQosPolicyState,
       "capSidDownloadableAclName": capSidDownloadableAclName,
       "capSidDownloadableAclState": capSidDownloadableAclState,
       "capSidUrlRedirectAclName": capSidUrlRedirectAclName,
       "capSidUrlRedirectAclState": capSidUrlRedirectAclState,
       "capSidRedirectUrlString": capSidRedirectUrlString,
       "capSidRedirectUrlStringState": capSidRedirectUrlStringState,
       "capSidSecurityGroupTag": capSidSecurityGroupTag,
       "ciscoAdmissionPolicyMIBConformance": ciscoAdmissionPolicyMIBConformance,
       "ciscoAdmissionPolicyMIBCompliances": ciscoAdmissionPolicyMIBCompliances,
       "ciscoAdmissionPolicyMIBCompliance": ciscoAdmissionPolicyMIBCompliance,
       "ciscoAdmissionPolicyMIBGroups": ciscoAdmissionPolicyMIBGroups,
       "capSessionStatisticsGroup": capSessionStatisticsGroup,
       "capSidSessionInfoGroup": capSidSessionInfoGroup,
       "capSidSessionPolicyGroup": capSidSessionPolicyGroup}
)
