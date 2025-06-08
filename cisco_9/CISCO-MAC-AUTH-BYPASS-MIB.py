# SNMP MIB module (CISCO-MAC-AUTH-BYPASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MAC-AUTH-BYPASS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:02 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMabMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654)
)
if mibBuilder.loadTexts:
    ciscoMabMIB.setRevisions(
        ("2008-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmabNotification_ObjectIdentity = ObjectIdentity
cmabNotification = _CmabNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 0)
)
_CmabMIBObjects_ObjectIdentity = ObjectIdentity
cmabMIBObjects = _CmabMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1)
)
_CmabInterfaceConfig_ObjectIdentity = ObjectIdentity
cmabInterfaceConfig = _CmabInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 1)
)
_CmabIfConfigTable_Object = MibTable
cmabIfConfigTable = _CmabIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmabIfConfigTable.setStatus("current")
_CmabIfConfigEntry_Object = MibTableRow
cmabIfConfigEntry = _CmabIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 1, 1, 1)
)
cmabIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmabIfConfigEntry.setStatus("current")
_CmabIfAuthEnabled_Type = TruthValue
_CmabIfAuthEnabled_Object = MibTableColumn
cmabIfAuthEnabled = _CmabIfAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 1, 1, 1, 1),
    _CmabIfAuthEnabled_Type()
)
cmabIfAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmabIfAuthEnabled.setStatus("current")


class _CmabIfAuthMethod_Type(Integer32):
    """Custom type cmabIfAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("eap", 2))
    )


_CmabIfAuthMethod_Type.__name__ = "Integer32"
_CmabIfAuthMethod_Object = MibTableColumn
cmabIfAuthMethod = _CmabIfAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 1, 1, 1, 2),
    _CmabIfAuthMethod_Type()
)
cmabIfAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmabIfAuthMethod.setStatus("current")
_CmabSession_ObjectIdentity = ObjectIdentity
cmabSession = _CmabSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2)
)
_CmabClientInfoTable_Object = MibTable
cmabClientInfoTable = _CmabClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmabClientInfoTable.setStatus("current")
_CmabClientInfoEntry_Object = MibTableRow
cmabClientInfoEntry = _CmabClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2, 1, 1)
)
cmabClientInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "CISCO-MAC-AUTH-BYPASS-MIB", "cmabClientSessionId"),
)
if mibBuilder.loadTexts:
    cmabClientInfoEntry.setStatus("current")


class _CmabClientSessionId_Type(OctetString):
    """Custom type cmabClientSessionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CmabClientSessionId_Type.__name__ = "OctetString"
_CmabClientSessionId_Object = MibTableColumn
cmabClientSessionId = _CmabClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2, 1, 1, 1),
    _CmabClientSessionId_Type()
)
cmabClientSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmabClientSessionId.setStatus("current")
_CmabClientMacAddress_Type = MacAddress
_CmabClientMacAddress_Object = MibTableColumn
cmabClientMacAddress = _CmabClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2, 1, 1, 2),
    _CmabClientMacAddress_Type()
)
cmabClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmabClientMacAddress.setStatus("current")


class _CmabClientMabState_Type(Integer32):
    """Custom type cmabClientMabState based on Integer32"""
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
          ("initialize", 2),
          ("acquiring", 3),
          ("authorizing", 4),
          ("terminate", 5))
    )


_CmabClientMabState_Type.__name__ = "Integer32"
_CmabClientMabState_Object = MibTableColumn
cmabClientMabState = _CmabClientMabState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2, 1, 1, 3),
    _CmabClientMabState_Type()
)
cmabClientMabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmabClientMabState.setStatus("current")


class _CmabClientAuthStatus_Type(Integer32):
    """Custom type cmabClientAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_CmabClientAuthStatus_Type.__name__ = "Integer32"
_CmabClientAuthStatus_Object = MibTableColumn
cmabClientAuthStatus = _CmabClientAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 1, 2, 1, 1, 4),
    _CmabClientAuthStatus_Type()
)
cmabClientAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmabClientAuthStatus.setStatus("current")
_CmabMIBConformance_ObjectIdentity = ObjectIdentity
cmabMIBConformance = _CmabMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 2)
)
_CmabMIBCompliances_ObjectIdentity = ObjectIdentity
cmabMIBCompliances = _CmabMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 2, 1)
)
_CmabMIBGroups_ObjectIdentity = ObjectIdentity
cmabMIBGroups = _CmabMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 2, 2)
)

# Managed Objects groups

cmabIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 2, 2, 1)
)
cmabIfConfigGroup.setObjects(
      *(("CISCO-MAC-AUTH-BYPASS-MIB", "cmabIfAuthEnabled"),
        ("CISCO-MAC-AUTH-BYPASS-MIB", "cmabIfAuthMethod"))
)
if mibBuilder.loadTexts:
    cmabIfConfigGroup.setStatus("current")

cmabClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 2, 2, 2)
)
cmabClientInfoGroup.setObjects(
      *(("CISCO-MAC-AUTH-BYPASS-MIB", "cmabClientMacAddress"),
        ("CISCO-MAC-AUTH-BYPASS-MIB", "cmabClientMabState"),
        ("CISCO-MAC-AUTH-BYPASS-MIB", "cmabClientAuthStatus"))
)
if mibBuilder.loadTexts:
    cmabClientInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmabCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 654, 2, 1, 1)
)
cmabCompliance.setObjects(
      *(("CISCO-MAC-AUTH-BYPASS-MIB", "cmabIfConfigGroup"),
        ("CISCO-MAC-AUTH-BYPASS-MIB", "cmabClientInfoGroup"))
)
if mibBuilder.loadTexts:
    cmabCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MAC-AUTH-BYPASS-MIB",
    **{"ciscoMabMIB": ciscoMabMIB,
       "cmabNotification": cmabNotification,
       "cmabMIBObjects": cmabMIBObjects,
       "cmabInterfaceConfig": cmabInterfaceConfig,
       "cmabIfConfigTable": cmabIfConfigTable,
       "cmabIfConfigEntry": cmabIfConfigEntry,
       "cmabIfAuthEnabled": cmabIfAuthEnabled,
       "cmabIfAuthMethod": cmabIfAuthMethod,
       "cmabSession": cmabSession,
       "cmabClientInfoTable": cmabClientInfoTable,
       "cmabClientInfoEntry": cmabClientInfoEntry,
       "cmabClientSessionId": cmabClientSessionId,
       "cmabClientMacAddress": cmabClientMacAddress,
       "cmabClientMabState": cmabClientMabState,
       "cmabClientAuthStatus": cmabClientAuthStatus,
       "cmabMIBConformance": cmabMIBConformance,
       "cmabMIBCompliances": cmabMIBCompliances,
       "cmabCompliance": cmabCompliance,
       "cmabMIBGroups": cmabMIBGroups,
       "cmabIfConfigGroup": cmabIfConfigGroup,
       "cmabClientInfoGroup": cmabClientInfoGroup}
)
