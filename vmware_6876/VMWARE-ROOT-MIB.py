# SNMP MIB module (VMWARE-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vmware_6876/VMWARE-ROOT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:23:14 2025
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

vmware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876)
)
if mibBuilder.loadTexts:
    vmware.setRevisions(
        ("2018-08-30 00:00",
         "2017-10-30 00:00",
         "2017-06-07 00:00",
         "2016-11-03 00:00",
         "2016-01-02 20:00",
         "2010-04-02 00:00",
         "2007-07-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwNotifications_ObjectIdentity = ObjectIdentity
vmwNotifications = _VmwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 0)
)
if mibBuilder.loadTexts:
    vmwNotifications.setStatus("current")
_VmwSystem_ObjectIdentity = ObjectIdentity
vmwSystem = _VmwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1)
)
if mibBuilder.loadTexts:
    vmwSystem.setStatus("current")
_VmwVirtMachines_ObjectIdentity = ObjectIdentity
vmwVirtMachines = _VmwVirtMachines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2)
)
if mibBuilder.loadTexts:
    vmwVirtMachines.setStatus("current")
_VmwResources_ObjectIdentity = ObjectIdentity
vmwResources = _VmwResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3)
)
if mibBuilder.loadTexts:
    vmwResources.setStatus("current")
_VmwProductSpecific_ObjectIdentity = ObjectIdentity
vmwProductSpecific = _VmwProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4)
)
if mibBuilder.loadTexts:
    vmwProductSpecific.setStatus("current")
_VmwLdap_ObjectIdentity = ObjectIdentity
vmwLdap = _VmwLdap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 40)
)
if mibBuilder.loadTexts:
    vmwLdap.setStatus("current")
_VmwTraps_ObjectIdentity = ObjectIdentity
vmwTraps = _VmwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 50)
)
if mibBuilder.loadTexts:
    vmwTraps.setStatus("current")
_VmwSRM_ObjectIdentity = ObjectIdentity
vmwSRM = _VmwSRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51)
)
if mibBuilder.loadTexts:
    vmwSRM.setStatus("current")
_VmwVCHA_ObjectIdentity = ObjectIdentity
vmwVCHA = _VmwVCHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53)
)
if mibBuilder.loadTexts:
    vmwVCHA.setStatus("current")
_VmwVmon_ObjectIdentity = ObjectIdentity
vmwVmon = _VmwVmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 55)
)
if mibBuilder.loadTexts:
    vmwVmon.setStatus("current")
_VmwOID_ObjectIdentity = ObjectIdentity
vmwOID = _VmwOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 60)
)
if mibBuilder.loadTexts:
    vmwOID.setStatus("deprecated")
_VmwareAgentCapabilities_ObjectIdentity = ObjectIdentity
vmwareAgentCapabilities = _VmwareAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70)
)
if mibBuilder.loadTexts:
    vmwareAgentCapabilities.setStatus("current")
_VmwNsxManager_ObjectIdentity = ObjectIdentity
vmwNsxManager = _VmwNsxManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90)
)
if mibBuilder.loadTexts:
    vmwNsxManager.setStatus("current")
_VmwNetworkInsight_ObjectIdentity = ObjectIdentity
vmwNetworkInsight = _VmwNetworkInsight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 100)
)
if mibBuilder.loadTexts:
    vmwNetworkInsight.setStatus("current")
_VmwHCX_ObjectIdentity = ObjectIdentity
vmwHCX = _VmwHCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 110)
)
if mibBuilder.loadTexts:
    vmwHCX.setStatus("current")
_VmwNSXsys_ObjectIdentity = ObjectIdentity
vmwNSXsys = _VmwNSXsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120)
)
if mibBuilder.loadTexts:
    vmwNSXsys.setStatus("current")
_VmwPerAppTunnel_ObjectIdentity = ObjectIdentity
vmwPerAppTunnel = _VmwPerAppTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 130)
)
if mibBuilder.loadTexts:
    vmwPerAppTunnel.setStatus("current")
_VmwExperimental_ObjectIdentity = ObjectIdentity
vmwExperimental = _VmwExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 700)
)
if mibBuilder.loadTexts:
    vmwExperimental.setStatus("current")
_VmwDocumentation_ObjectIdentity = ObjectIdentity
vmwDocumentation = _VmwDocumentation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 750)
)
if mibBuilder.loadTexts:
    vmwDocumentation.setStatus("current")
_VmwObsolete_ObjectIdentity = ObjectIdentity
vmwObsolete = _VmwObsolete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 800)
)
if mibBuilder.loadTexts:
    vmwObsolete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-ROOT-MIB",
    **{"vmware": vmware,
       "vmwNotifications": vmwNotifications,
       "vmwSystem": vmwSystem,
       "vmwVirtMachines": vmwVirtMachines,
       "vmwResources": vmwResources,
       "vmwProductSpecific": vmwProductSpecific,
       "vmwLdap": vmwLdap,
       "vmwTraps": vmwTraps,
       "vmwSRM": vmwSRM,
       "vmwVCHA": vmwVCHA,
       "vmwVmon": vmwVmon,
       "vmwOID": vmwOID,
       "vmwareAgentCapabilities": vmwareAgentCapabilities,
       "vmwNsxManager": vmwNsxManager,
       "vmwNetworkInsight": vmwNetworkInsight,
       "vmwHCX": vmwHCX,
       "vmwNSXsys": vmwNSXsys,
       "vmwPerAppTunnel": vmwPerAppTunnel,
       "vmwExperimental": vmwExperimental,
       "vmwDocumentation": vmwDocumentation,
       "vmwObsolete": vmwObsolete}
)
