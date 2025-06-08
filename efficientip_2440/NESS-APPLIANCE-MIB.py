# SNMP MIB module (NESS-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/efficientip_2440/NESS-APPLIANCE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:52:30 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(udpLocalPort,) = mibBuilder.importSymbols(
    "UDP-MIB",
    "udpLocalPort")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ness_ObjectIdentity = ObjectIdentity
ness = _Ness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1)
)
_NessAppliance_ObjectIdentity = ObjectIdentity
nessAppliance = _NessAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6)
)
_NessApplianceTrap_ObjectIdentity = ObjectIdentity
nessApplianceTrap = _NessApplianceTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 1)
)
_NessApplianceTrapSystem_ObjectIdentity = ObjectIdentity
nessApplianceTrapSystem = _NessApplianceTrapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 1, 1)
)
_NessApplianceUpgradeURL_Type = DisplayString
_NessApplianceUpgradeURL_Object = MibScalar
nessApplianceUpgradeURL = _NessApplianceUpgradeURL_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 2),
    _NessApplianceUpgradeURL_Type()
)
nessApplianceUpgradeURL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nessApplianceUpgradeURL.setStatus("mandatory")
_NessApplianceTrapSystemPartitionName_Type = DisplayString
_NessApplianceTrapSystemPartitionName_Object = MibScalar
nessApplianceTrapSystemPartitionName = _NessApplianceTrapSystemPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 3),
    _NessApplianceTrapSystemPartitionName_Type()
)
nessApplianceTrapSystemPartitionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nessApplianceTrapSystemPartitionName.setStatus("mandatory")
_NessApplianceTrapSystemPartitionSize_Type = DisplayString
_NessApplianceTrapSystemPartitionSize_Object = MibScalar
nessApplianceTrapSystemPartitionSize = _NessApplianceTrapSystemPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 4),
    _NessApplianceTrapSystemPartitionSize_Type()
)
nessApplianceTrapSystemPartitionSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nessApplianceTrapSystemPartitionSize.setStatus("mandatory")
_NessApplianceTrapSystemProcessName_Type = DisplayString
_NessApplianceTrapSystemProcessName_Object = MibScalar
nessApplianceTrapSystemProcessName = _NessApplianceTrapSystemProcessName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 5),
    _NessApplianceTrapSystemProcessName_Type()
)
nessApplianceTrapSystemProcessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nessApplianceTrapSystemProcessName.setStatus("mandatory")
_NessApplianceTrapSystemDhcpName_Type = DisplayString
_NessApplianceTrapSystemDhcpName_Object = MibScalar
nessApplianceTrapSystemDhcpName = _NessApplianceTrapSystemDhcpName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 6),
    _NessApplianceTrapSystemDhcpName_Type()
)
nessApplianceTrapSystemDhcpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nessApplianceTrapSystemDhcpName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nessApplianceUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 1, 0, 1)
)
nessApplianceUpgrade.setObjects(
    ("NESS-APPLIANCE-MIB", "nessApplianceUpgradeURL")
)
if mibBuilder.loadTexts:
    nessApplianceUpgrade.setStatus(
        ""
    )

nessSystemPartitionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 1, 1, 0, 1)
)
nessSystemPartitionAlarm.setObjects(
      *(("NESS-APPLIANCE-MIB", "nessApplianceTrapSystemPartitionName"),
        ("NESS-APPLIANCE-MIB", "nessApplianceTrapSystemPartitionSize"))
)
if mibBuilder.loadTexts:
    nessSystemPartitionAlarm.setStatus(
        ""
    )

nessSystemProcessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2440, 1, 6, 1, 1, 0, 2)
)
nessSystemProcessDown.setObjects(
    ("NESS-APPLIANCE-MIB", "nessApplianceTrapSystemProcessName")
)
if mibBuilder.loadTexts:
    nessSystemProcessDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NESS-APPLIANCE-MIB",
    **{"ness": ness,
       "products": products,
       "nessAppliance": nessAppliance,
       "nessApplianceTrap": nessApplianceTrap,
       "nessApplianceUpgrade": nessApplianceUpgrade,
       "nessApplianceTrapSystem": nessApplianceTrapSystem,
       "nessSystemPartitionAlarm": nessSystemPartitionAlarm,
       "nessSystemProcessDown": nessSystemProcessDown,
       "nessApplianceUpgradeURL": nessApplianceUpgradeURL,
       "nessApplianceTrapSystemPartitionName": nessApplianceTrapSystemPartitionName,
       "nessApplianceTrapSystemPartitionSize": nessApplianceTrapSystemPartitionSize,
       "nessApplianceTrapSystemProcessName": nessApplianceTrapSystemProcessName,
       "nessApplianceTrapSystemDhcpName": nessApplianceTrapSystemDhcpName}
)
