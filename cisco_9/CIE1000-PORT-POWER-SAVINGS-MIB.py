# SNMP MIB module (CIE1000-PORT-POWER-SAVINGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-PORT-POWER-SAVINGS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000InterfaceIndex,) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InterfaceIndex")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000PortPowerSavingsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100)
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsMib.setRevisions(
        ("2014-08-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000PortPowerSavingsStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("notSupported", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000PortPowerSavingsMibObjects_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsMibObjects = _Cie1000PortPowerSavingsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1)
)
_Cie1000PortPowerSavingsCapabilities_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsCapabilities = _Cie1000PortPowerSavingsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 1)
)
_Cie1000PortPowerSavingsCapabilitiesInterfaceTable_Object = MibTable
cie1000PortPowerSavingsCapabilitiesInterfaceTable = _Cie1000PortPowerSavingsCapabilitiesInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsCapabilitiesInterfaceTable.setStatus("current")
_Cie1000PortPowerSavingsCapabilitiesInterfaceEntry_Object = MibTableRow
cie1000PortPowerSavingsCapabilitiesInterfaceEntry = _Cie1000PortPowerSavingsCapabilitiesInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 1, 1, 1)
)
cie1000PortPowerSavingsCapabilitiesInterfaceEntry.setIndexNames(
    (0, "CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsCapabilitiesInterfaceEntry.setStatus("current")
_Cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex_Object = MibTableColumn
cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex = _Cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 1, 1, 1, 1),
    _Cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex_Type()
)
cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex.setStatus("current")
_Cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner_Type = TruthValue
_Cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner_Object = MibTableColumn
cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner = _Cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 1, 1, 1, 2),
    _Cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner_Type()
)
cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner.setStatus("current")
_Cie1000PortPowerSavingsCapabilitiesInterfaceShortReach_Type = TruthValue
_Cie1000PortPowerSavingsCapabilitiesInterfaceShortReach_Object = MibTableColumn
cie1000PortPowerSavingsCapabilitiesInterfaceShortReach = _Cie1000PortPowerSavingsCapabilitiesInterfaceShortReach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 1, 1, 1, 3),
    _Cie1000PortPowerSavingsCapabilitiesInterfaceShortReach_Type()
)
cie1000PortPowerSavingsCapabilitiesInterfaceShortReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsCapabilitiesInterfaceShortReach.setStatus("current")
_Cie1000PortPowerSavingsConfig_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsConfig = _Cie1000PortPowerSavingsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 2)
)
_Cie1000PortPowerSavingsConfigInterfaceParamTable_Object = MibTable
cie1000PortPowerSavingsConfigInterfaceParamTable = _Cie1000PortPowerSavingsConfigInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsConfigInterfaceParamTable.setStatus("current")
_Cie1000PortPowerSavingsConfigInterfaceParamEntry_Object = MibTableRow
cie1000PortPowerSavingsConfigInterfaceParamEntry = _Cie1000PortPowerSavingsConfigInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 2, 1, 1)
)
cie1000PortPowerSavingsConfigInterfaceParamEntry.setIndexNames(
    (0, "CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsConfigInterfaceParamIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsConfigInterfaceParamEntry.setStatus("current")
_Cie1000PortPowerSavingsConfigInterfaceParamIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortPowerSavingsConfigInterfaceParamIfIndex_Object = MibTableColumn
cie1000PortPowerSavingsConfigInterfaceParamIfIndex = _Cie1000PortPowerSavingsConfigInterfaceParamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 2, 1, 1, 1),
    _Cie1000PortPowerSavingsConfigInterfaceParamIfIndex_Type()
)
cie1000PortPowerSavingsConfigInterfaceParamIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsConfigInterfaceParamIfIndex.setStatus("current")
_Cie1000PortPowerSavingsConfigInterfaceParamLinkPartner_Type = TruthValue
_Cie1000PortPowerSavingsConfigInterfaceParamLinkPartner_Object = MibTableColumn
cie1000PortPowerSavingsConfigInterfaceParamLinkPartner = _Cie1000PortPowerSavingsConfigInterfaceParamLinkPartner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 2, 1, 1, 2),
    _Cie1000PortPowerSavingsConfigInterfaceParamLinkPartner_Type()
)
cie1000PortPowerSavingsConfigInterfaceParamLinkPartner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsConfigInterfaceParamLinkPartner.setStatus("current")
_Cie1000PortPowerSavingsConfigInterfaceParamShortReach_Type = TruthValue
_Cie1000PortPowerSavingsConfigInterfaceParamShortReach_Object = MibTableColumn
cie1000PortPowerSavingsConfigInterfaceParamShortReach = _Cie1000PortPowerSavingsConfigInterfaceParamShortReach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 2, 1, 1, 3),
    _Cie1000PortPowerSavingsConfigInterfaceParamShortReach_Type()
)
cie1000PortPowerSavingsConfigInterfaceParamShortReach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsConfigInterfaceParamShortReach.setStatus("current")
_Cie1000PortPowerSavingsStatus_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsStatus = _Cie1000PortPowerSavingsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 3)
)
_Cie1000PortPowerSavingsStatusInterfaceTable_Object = MibTable
cie1000PortPowerSavingsStatusInterfaceTable = _Cie1000PortPowerSavingsStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsStatusInterfaceTable.setStatus("current")
_Cie1000PortPowerSavingsStatusInterfaceEntry_Object = MibTableRow
cie1000PortPowerSavingsStatusInterfaceEntry = _Cie1000PortPowerSavingsStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 3, 1, 1)
)
cie1000PortPowerSavingsStatusInterfaceEntry.setIndexNames(
    (0, "CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsStatusInterfaceEntry.setStatus("current")
_Cie1000PortPowerSavingsStatusInterfaceIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PortPowerSavingsStatusInterfaceIfIndex_Object = MibTableColumn
cie1000PortPowerSavingsStatusInterfaceIfIndex = _Cie1000PortPowerSavingsStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 3, 1, 1, 1),
    _Cie1000PortPowerSavingsStatusInterfaceIfIndex_Type()
)
cie1000PortPowerSavingsStatusInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsStatusInterfaceIfIndex.setStatus("current")
_Cie1000PortPowerSavingsStatusInterfaceNoLinkPartner_Type = CIE1000PortPowerSavingsStatusType
_Cie1000PortPowerSavingsStatusInterfaceNoLinkPartner_Object = MibTableColumn
cie1000PortPowerSavingsStatusInterfaceNoLinkPartner = _Cie1000PortPowerSavingsStatusInterfaceNoLinkPartner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 3, 1, 1, 2),
    _Cie1000PortPowerSavingsStatusInterfaceNoLinkPartner_Type()
)
cie1000PortPowerSavingsStatusInterfaceNoLinkPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsStatusInterfaceNoLinkPartner.setStatus("current")
_Cie1000PortPowerSavingsStatusInterfaceShortCable_Type = CIE1000PortPowerSavingsStatusType
_Cie1000PortPowerSavingsStatusInterfaceShortCable_Object = MibTableColumn
cie1000PortPowerSavingsStatusInterfaceShortCable = _Cie1000PortPowerSavingsStatusInterfaceShortCable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 1, 3, 1, 1, 3),
    _Cie1000PortPowerSavingsStatusInterfaceShortCable_Type()
)
cie1000PortPowerSavingsStatusInterfaceShortCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsStatusInterfaceShortCable.setStatus("current")
_Cie1000PortPowerSavingsMibConformance_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsMibConformance = _Cie1000PortPowerSavingsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2)
)
_Cie1000PortPowerSavingsMibCompliances_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsMibCompliances = _Cie1000PortPowerSavingsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2, 1)
)
_Cie1000PortPowerSavingsMibGroups_ObjectIdentity = ObjectIdentity
cie1000PortPowerSavingsMibGroups = _Cie1000PortPowerSavingsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2, 2)
)

# Managed Objects groups

cie1000PortPowerSavingsCapabilitiesInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2, 2, 1)
)
cie1000PortPowerSavingsCapabilitiesInterfaceInfoGroup.setObjects(
      *(("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsCapabilitiesInterfaceShortReach"))
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsCapabilitiesInterfaceInfoGroup.setStatus("current")

cie1000PortPowerSavingsConfigInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2, 2, 2)
)
cie1000PortPowerSavingsConfigInterfaceParamTableInfoGroup.setObjects(
      *(("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsConfigInterfaceParamIfIndex"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsConfigInterfaceParamLinkPartner"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsConfigInterfaceParamShortReach"))
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsConfigInterfaceParamTableInfoGroup.setStatus("current")

cie1000PortPowerSavingsStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2, 2, 3)
)
cie1000PortPowerSavingsStatusInterfaceTableInfoGroup.setObjects(
      *(("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsStatusInterfaceIfIndex"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsStatusInterfaceNoLinkPartner"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsStatusInterfaceShortCable"))
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsStatusInterfaceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000PortPowerSavingsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 100, 2, 1, 1)
)
cie1000PortPowerSavingsMibCompliance.setObjects(
      *(("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsCapabilitiesInterfaceInfoGroup"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsConfigInterfaceParamTableInfoGroup"),
        ("CIE1000-PORT-POWER-SAVINGS-MIB", "cie1000PortPowerSavingsStatusInterfaceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000PortPowerSavingsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-PORT-POWER-SAVINGS-MIB",
    **{"CIE1000PortPowerSavingsStatusType": CIE1000PortPowerSavingsStatusType,
       "cie1000PortPowerSavingsMib": cie1000PortPowerSavingsMib,
       "cie1000PortPowerSavingsMibObjects": cie1000PortPowerSavingsMibObjects,
       "cie1000PortPowerSavingsCapabilities": cie1000PortPowerSavingsCapabilities,
       "cie1000PortPowerSavingsCapabilitiesInterfaceTable": cie1000PortPowerSavingsCapabilitiesInterfaceTable,
       "cie1000PortPowerSavingsCapabilitiesInterfaceEntry": cie1000PortPowerSavingsCapabilitiesInterfaceEntry,
       "cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex": cie1000PortPowerSavingsCapabilitiesInterfaceIfIndex,
       "cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner": cie1000PortPowerSavingsCapabilitiesInterfaceLinkPartner,
       "cie1000PortPowerSavingsCapabilitiesInterfaceShortReach": cie1000PortPowerSavingsCapabilitiesInterfaceShortReach,
       "cie1000PortPowerSavingsConfig": cie1000PortPowerSavingsConfig,
       "cie1000PortPowerSavingsConfigInterfaceParamTable": cie1000PortPowerSavingsConfigInterfaceParamTable,
       "cie1000PortPowerSavingsConfigInterfaceParamEntry": cie1000PortPowerSavingsConfigInterfaceParamEntry,
       "cie1000PortPowerSavingsConfigInterfaceParamIfIndex": cie1000PortPowerSavingsConfigInterfaceParamIfIndex,
       "cie1000PortPowerSavingsConfigInterfaceParamLinkPartner": cie1000PortPowerSavingsConfigInterfaceParamLinkPartner,
       "cie1000PortPowerSavingsConfigInterfaceParamShortReach": cie1000PortPowerSavingsConfigInterfaceParamShortReach,
       "cie1000PortPowerSavingsStatus": cie1000PortPowerSavingsStatus,
       "cie1000PortPowerSavingsStatusInterfaceTable": cie1000PortPowerSavingsStatusInterfaceTable,
       "cie1000PortPowerSavingsStatusInterfaceEntry": cie1000PortPowerSavingsStatusInterfaceEntry,
       "cie1000PortPowerSavingsStatusInterfaceIfIndex": cie1000PortPowerSavingsStatusInterfaceIfIndex,
       "cie1000PortPowerSavingsStatusInterfaceNoLinkPartner": cie1000PortPowerSavingsStatusInterfaceNoLinkPartner,
       "cie1000PortPowerSavingsStatusInterfaceShortCable": cie1000PortPowerSavingsStatusInterfaceShortCable,
       "cie1000PortPowerSavingsMibConformance": cie1000PortPowerSavingsMibConformance,
       "cie1000PortPowerSavingsMibCompliances": cie1000PortPowerSavingsMibCompliances,
       "cie1000PortPowerSavingsMibCompliance": cie1000PortPowerSavingsMibCompliance,
       "cie1000PortPowerSavingsMibGroups": cie1000PortPowerSavingsMibGroups,
       "cie1000PortPowerSavingsCapabilitiesInterfaceInfoGroup": cie1000PortPowerSavingsCapabilitiesInterfaceInfoGroup,
       "cie1000PortPowerSavingsConfigInterfaceParamTableInfoGroup": cie1000PortPowerSavingsConfigInterfaceParamTableInfoGroup,
       "cie1000PortPowerSavingsStatusInterfaceTableInfoGroup": cie1000PortPowerSavingsStatusInterfaceTableInfoGroup}
)
