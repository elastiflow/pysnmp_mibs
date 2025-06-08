# SNMP MIB module (RUIJIE-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VOICE-VLAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieVoiceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52)
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanMIB.setRevisions(
        ("2009-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVoiceVlanMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVoiceVlanMIBObjects = _RuijieVoiceVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1)
)
_RuijieVoiceVlanOuiTable_Object = MibTable
ruijieVoiceVlanOuiTable = _RuijieVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanOuiTable.setStatus("current")
_RuijieVoiceVlanOuiEntry_Object = MibTableRow
ruijieVoiceVlanOuiEntry = _RuijieVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 1, 1)
)
ruijieVoiceVlanOuiEntry.setIndexNames(
    (0, "RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanOuiEntry.setStatus("current")
_RuijieVoiceVlanOuiAddress_Type = MacAddress
_RuijieVoiceVlanOuiAddress_Object = MibTableColumn
ruijieVoiceVlanOuiAddress = _RuijieVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 1, 1, 1),
    _RuijieVoiceVlanOuiAddress_Type()
)
ruijieVoiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoiceVlanOuiAddress.setStatus("current")
_RuijieVoiceVlanOuiMask_Type = MacAddress
_RuijieVoiceVlanOuiMask_Object = MibTableColumn
ruijieVoiceVlanOuiMask = _RuijieVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 1, 1, 2),
    _RuijieVoiceVlanOuiMask_Type()
)
ruijieVoiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanOuiMask.setStatus("current")


class _RuijieVoiceVlanOuiDescription_Type(OctetString):
    """Custom type ruijieVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RuijieVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_RuijieVoiceVlanOuiDescription_Object = MibTableColumn
ruijieVoiceVlanOuiDescription = _RuijieVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 1, 1, 3),
    _RuijieVoiceVlanOuiDescription_Type()
)
ruijieVoiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanOuiDescription.setStatus("current")
_RuijieVoiceVlanOuiRowStatus_Type = RowStatus
_RuijieVoiceVlanOuiRowStatus_Object = MibTableColumn
ruijieVoiceVlanOuiRowStatus = _RuijieVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 1, 1, 4),
    _RuijieVoiceVlanOuiRowStatus_Type()
)
ruijieVoiceVlanOuiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanOuiRowStatus.setStatus("current")
_RuijieVoiceVlanEnabledId_Type = Integer32
_RuijieVoiceVlanEnabledId_Object = MibScalar
ruijieVoiceVlanEnabledId = _RuijieVoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 2),
    _RuijieVoiceVlanEnabledId_Type()
)
ruijieVoiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanEnabledId.setStatus("current")
_RuijieVoiceVlanPortEnableTable_Object = MibTable
ruijieVoiceVlanPortEnableTable = _RuijieVoiceVlanPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortEnableTable.setStatus("current")
_RuijieVoiceVlanPortEnableEntry_Object = MibTableRow
ruijieVoiceVlanPortEnableEntry = _RuijieVoiceVlanPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 3, 1)
)
ruijieVoiceVlanPortEnableEntry.setIndexNames(
    (0, "RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanPortEnableIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortEnableEntry.setStatus("current")
_RuijieVoiceVlanPortEnableIfIndex_Type = IfIndex
_RuijieVoiceVlanPortEnableIfIndex_Object = MibTableColumn
ruijieVoiceVlanPortEnableIfIndex = _RuijieVoiceVlanPortEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 3, 1, 1),
    _RuijieVoiceVlanPortEnableIfIndex_Type()
)
ruijieVoiceVlanPortEnableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortEnableIfIndex.setStatus("current")
_RuijieVoiceVlanPortStatus_Type = EnabledStatus
_RuijieVoiceVlanPortStatus_Object = MibTableColumn
ruijieVoiceVlanPortStatus = _RuijieVoiceVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 3, 1, 2),
    _RuijieVoiceVlanPortStatus_Type()
)
ruijieVoiceVlanPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortStatus.setStatus("current")


class _RuijieVoiceVlanAgingTime_Type(Integer32):
    """Custom type ruijieVoiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_RuijieVoiceVlanAgingTime_Type.__name__ = "Integer32"
_RuijieVoiceVlanAgingTime_Object = MibScalar
ruijieVoiceVlanAgingTime = _RuijieVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 4),
    _RuijieVoiceVlanAgingTime_Type()
)
ruijieVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanAgingTime.setStatus("current")


class _RuijieVoiceVlanSecurityState_Type(Integer32):
    """Custom type ruijieVoiceVlanSecurityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("security", 1),
          ("normal", 2))
    )


_RuijieVoiceVlanSecurityState_Type.__name__ = "Integer32"
_RuijieVoiceVlanSecurityState_Object = MibScalar
ruijieVoiceVlanSecurityState = _RuijieVoiceVlanSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 5),
    _RuijieVoiceVlanSecurityState_Type()
)
ruijieVoiceVlanSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanSecurityState.setStatus("current")


class _RuijieVoiceVlanCos_Type(Integer32):
    """Custom type ruijieVoiceVlanCos based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieVoiceVlanCos_Type.__name__ = "Integer32"
_RuijieVoiceVlanCos_Object = MibScalar
ruijieVoiceVlanCos = _RuijieVoiceVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 6),
    _RuijieVoiceVlanCos_Type()
)
ruijieVoiceVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanCos.setStatus("current")


class _RuijieVoiceVlanDscp_Type(Integer32):
    """Custom type ruijieVoiceVlanDscp based on Integer32"""
    defaultValue = 46


_RuijieVoiceVlanDscp_Type.__name__ = "Integer32"
_RuijieVoiceVlanDscp_Object = MibScalar
ruijieVoiceVlanDscp = _RuijieVoiceVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 7),
    _RuijieVoiceVlanDscp_Type()
)
ruijieVoiceVlanDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanDscp.setStatus("current")
_RuijieVoiceVlanPortModeTable_Object = MibTable
ruijieVoiceVlanPortModeTable = _RuijieVoiceVlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortModeTable.setStatus("current")
_RuijieVoiceVlanPortModeEntry_Object = MibTableRow
ruijieVoiceVlanPortModeEntry = _RuijieVoiceVlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 8, 1)
)
ruijieVoiceVlanPortModeEntry.setIndexNames(
    (0, "RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanPortIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortModeEntry.setStatus("current")
_RuijieVoiceVlanPortIfIndex_Type = IfIndex
_RuijieVoiceVlanPortIfIndex_Object = MibTableColumn
ruijieVoiceVlanPortIfIndex = _RuijieVoiceVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 8, 1, 1),
    _RuijieVoiceVlanPortIfIndex_Type()
)
ruijieVoiceVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortIfIndex.setStatus("current")


class _RuijieVoiceVlanPortMode_Type(Integer32):
    """Custom type ruijieVoiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_RuijieVoiceVlanPortMode_Type.__name__ = "Integer32"
_RuijieVoiceVlanPortMode_Object = MibTableColumn
ruijieVoiceVlanPortMode = _RuijieVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 8, 1, 2),
    _RuijieVoiceVlanPortMode_Type()
)
ruijieVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVoiceVlanPortMode.setStatus("current")
_RuijieVoiceVlanMacTable_Object = MibTable
ruijieVoiceVlanMacTable = _RuijieVoiceVlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanMacTable.setStatus("current")
_RuijieVoiceVlanMacEntry_Object = MibTableRow
ruijieVoiceVlanMacEntry = _RuijieVoiceVlanMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 9, 1)
)
ruijieVoiceVlanMacEntry.setIndexNames(
    (0, "RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanMacAddress"),
    (0, "RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanMacIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanMacEntry.setStatus("current")
_RuijieVoiceVlanMacAddress_Type = MacAddress
_RuijieVoiceVlanMacAddress_Object = MibTableColumn
ruijieVoiceVlanMacAddress = _RuijieVoiceVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 9, 1, 1),
    _RuijieVoiceVlanMacAddress_Type()
)
ruijieVoiceVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoiceVlanMacAddress.setStatus("current")
_RuijieVoiceVlanMacIfIndex_Type = IfIndex
_RuijieVoiceVlanMacIfIndex_Object = MibTableColumn
ruijieVoiceVlanMacIfIndex = _RuijieVoiceVlanMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 9, 1, 2),
    _RuijieVoiceVlanMacIfIndex_Type()
)
ruijieVoiceVlanMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoiceVlanMacIfIndex.setStatus("current")


class _RuijieVoiceVlanMacDescription_Type(OctetString):
    """Custom type ruijieVoiceVlanMacDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RuijieVoiceVlanMacDescription_Type.__name__ = "OctetString"
_RuijieVoiceVlanMacDescription_Object = MibTableColumn
ruijieVoiceVlanMacDescription = _RuijieVoiceVlanMacDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 1, 9, 1, 3),
    _RuijieVoiceVlanMacDescription_Type()
)
ruijieVoiceVlanMacDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoiceVlanMacDescription.setStatus("current")
_RuijieVoiceVlanMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVoiceVlanMIBConformance = _RuijieVoiceVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 2)
)
_RuijieVoiceVlanMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieVoiceVlanMIBCompliances = _RuijieVoiceVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 2, 1)
)
_RuijieVoiceVlanMIBGroups_ObjectIdentity = ObjectIdentity
ruijieVoiceVlanMIBGroups = _RuijieVoiceVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 2, 2)
)

# Managed Objects groups

ruijieVoiceVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 2, 2, 1)
)
ruijieVoiceVlanMIBGroup.setObjects(
      *(("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanOuiAddress"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanOuiMask"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanOuiDescription"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanOuiRowStatus"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanEnabledId"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanPortStatus"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanAgingTime"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanSecurityState"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanCos"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanDscp"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanPortMode"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanMacAddress"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanMacIfIndex"),
        ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanMacDescription"))
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieVoiceVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 52, 2, 1, 1)
)
ruijieVoiceVlanMIBCompliance.setObjects(
    ("RUIJIE-VOICE-VLAN-MIB", "ruijieVoiceVlanMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieVoiceVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VOICE-VLAN-MIB",
    **{"ruijieVoiceVlanMIB": ruijieVoiceVlanMIB,
       "ruijieVoiceVlanMIBObjects": ruijieVoiceVlanMIBObjects,
       "ruijieVoiceVlanOuiTable": ruijieVoiceVlanOuiTable,
       "ruijieVoiceVlanOuiEntry": ruijieVoiceVlanOuiEntry,
       "ruijieVoiceVlanOuiAddress": ruijieVoiceVlanOuiAddress,
       "ruijieVoiceVlanOuiMask": ruijieVoiceVlanOuiMask,
       "ruijieVoiceVlanOuiDescription": ruijieVoiceVlanOuiDescription,
       "ruijieVoiceVlanOuiRowStatus": ruijieVoiceVlanOuiRowStatus,
       "ruijieVoiceVlanEnabledId": ruijieVoiceVlanEnabledId,
       "ruijieVoiceVlanPortEnableTable": ruijieVoiceVlanPortEnableTable,
       "ruijieVoiceVlanPortEnableEntry": ruijieVoiceVlanPortEnableEntry,
       "ruijieVoiceVlanPortEnableIfIndex": ruijieVoiceVlanPortEnableIfIndex,
       "ruijieVoiceVlanPortStatus": ruijieVoiceVlanPortStatus,
       "ruijieVoiceVlanAgingTime": ruijieVoiceVlanAgingTime,
       "ruijieVoiceVlanSecurityState": ruijieVoiceVlanSecurityState,
       "ruijieVoiceVlanCos": ruijieVoiceVlanCos,
       "ruijieVoiceVlanDscp": ruijieVoiceVlanDscp,
       "ruijieVoiceVlanPortModeTable": ruijieVoiceVlanPortModeTable,
       "ruijieVoiceVlanPortModeEntry": ruijieVoiceVlanPortModeEntry,
       "ruijieVoiceVlanPortIfIndex": ruijieVoiceVlanPortIfIndex,
       "ruijieVoiceVlanPortMode": ruijieVoiceVlanPortMode,
       "ruijieVoiceVlanMacTable": ruijieVoiceVlanMacTable,
       "ruijieVoiceVlanMacEntry": ruijieVoiceVlanMacEntry,
       "ruijieVoiceVlanMacAddress": ruijieVoiceVlanMacAddress,
       "ruijieVoiceVlanMacIfIndex": ruijieVoiceVlanMacIfIndex,
       "ruijieVoiceVlanMacDescription": ruijieVoiceVlanMacDescription,
       "ruijieVoiceVlanMIBConformance": ruijieVoiceVlanMIBConformance,
       "ruijieVoiceVlanMIBCompliances": ruijieVoiceVlanMIBCompliances,
       "ruijieVoiceVlanMIBCompliance": ruijieVoiceVlanMIBCompliance,
       "ruijieVoiceVlanMIBGroups": ruijieVoiceVlanMIBGroups,
       "ruijieVoiceVlanMIBGroup": ruijieVoiceVlanMIBGroup}
)
