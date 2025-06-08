# SNMP MIB module (VMWARE-VCHA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vmware_6876/VMWARE-VCHA-MIB.mib
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(vmwVCHA,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwVCHA")


# MODULE-IDENTITY

vmwVchaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1)
)
if mibBuilder.loadTexts:
    vmwVchaMIB.setRevisions(
        ("2016-07-19 00:00",
         "2016-04-06 00:00",
         "2016-02-03 00:00",
         "2016-01-27 00:00",
         "2016-01-15 00:00",
         "2016-01-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwVchaNodeRoleType(TextualConvention, Integer32):
    status = "current"
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
        *(("active", 1),
          ("passive", 2),
          ("witness", 3),
          ("unknown", 4))
    )



class VmwVchaClusterModeType(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("maintenance", 3))
    )



class VmwVchaClusterStateType(TextualConvention, Integer32):
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
        *(("healthy", 1),
          ("degraded", 2),
          ("isolated", 3))
    )



class VmwVchaDbReplicationStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noReplication", 1),
          ("sync", 3),
          ("async", 4))
    )



class VmwVchaFileReplicationProviderType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceConfig", 1),
          ("serviceState", 2))
    )



# MIB Managed Objects in the order of their OIDs

_VmwVCHANotifications_ObjectIdentity = ObjectIdentity
vmwVCHANotifications = _VmwVCHANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0)
)
_VmwVchaMIBConformance_ObjectIdentity = ObjectIdentity
vmwVchaMIBConformance = _VmwVchaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1, 2)
)
_VmwVchaMIBCompliances_ObjectIdentity = ObjectIdentity
vmwVchaMIBCompliances = _VmwVchaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 1)
)
_VmwVchaMIBGroups_ObjectIdentity = ObjectIdentity
vmwVchaMIBGroups = _VmwVchaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2)
)
_VmwVchaInstanceUuid_Type = OctetString
_VmwVchaInstanceUuid_Object = MibScalar
vmwVchaInstanceUuid = _VmwVchaInstanceUuid_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 5),
    _VmwVchaInstanceUuid_Type()
)
vmwVchaInstanceUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaInstanceUuid.setStatus("current")
_VmwVchaPrivateAddressType_Type = InetAddressType
_VmwVchaPrivateAddressType_Object = MibScalar
vmwVchaPrivateAddressType = _VmwVchaPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 11),
    _VmwVchaPrivateAddressType_Type()
)
vmwVchaPrivateAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaPrivateAddressType.setStatus("current")
_VmwVchaPublicAddressType_Type = InetAddressType
_VmwVchaPublicAddressType_Object = MibScalar
vmwVchaPublicAddressType = _VmwVchaPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 12),
    _VmwVchaPublicAddressType_Type()
)
vmwVchaPublicAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaPublicAddressType.setStatus("current")
_VmwVchaPrivateAddressAddr_Type = InetAddress
_VmwVchaPrivateAddressAddr_Object = MibScalar
vmwVchaPrivateAddressAddr = _VmwVchaPrivateAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 15),
    _VmwVchaPrivateAddressAddr_Type()
)
vmwVchaPrivateAddressAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaPrivateAddressAddr.setStatus("current")
_VmwVchaPublicAddressAddr_Type = InetAddress
_VmwVchaPublicAddressAddr_Object = MibScalar
vmwVchaPublicAddressAddr = _VmwVchaPublicAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 16),
    _VmwVchaPublicAddressAddr_Type()
)
vmwVchaPublicAddressAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaPublicAddressAddr.setStatus("current")
_VmwVchaTargetNodeRole_Type = VmwVchaNodeRoleType
_VmwVchaTargetNodeRole_Object = MibScalar
vmwVchaTargetNodeRole = _VmwVchaTargetNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 20),
    _VmwVchaTargetNodeRole_Type()
)
vmwVchaTargetNodeRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaTargetNodeRole.setStatus("current")
_VmwVchaClusterState_Type = VmwVchaClusterStateType
_VmwVchaClusterState_Object = MibScalar
vmwVchaClusterState = _VmwVchaClusterState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 25),
    _VmwVchaClusterState_Type()
)
vmwVchaClusterState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaClusterState.setStatus("current")
_VmwVchaClusterMode_Type = VmwVchaClusterModeType
_VmwVchaClusterMode_Object = MibScalar
vmwVchaClusterMode = _VmwVchaClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 30),
    _VmwVchaClusterMode_Type()
)
vmwVchaClusterMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaClusterMode.setStatus("current")
_VmwVchaIsPlannedFailover_Type = TruthValue
_VmwVchaIsPlannedFailover_Object = MibScalar
vmwVchaIsPlannedFailover = _VmwVchaIsPlannedFailover_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 40),
    _VmwVchaIsPlannedFailover_Type()
)
vmwVchaIsPlannedFailover.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaIsPlannedFailover.setStatus("current")
_VmwVchaDbReplicationState_Type = VmwVchaDbReplicationStateType
_VmwVchaDbReplicationState_Object = MibScalar
vmwVchaDbReplicationState = _VmwVchaDbReplicationState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 50),
    _VmwVchaDbReplicationState_Type()
)
vmwVchaDbReplicationState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaDbReplicationState.setStatus("current")
_VmwVchaIsFileProviderInSync_Type = TruthValue
_VmwVchaIsFileProviderInSync_Object = MibScalar
vmwVchaIsFileProviderInSync = _VmwVchaIsFileProviderInSync_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 55),
    _VmwVchaIsFileProviderInSync_Type()
)
vmwVchaIsFileProviderInSync.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaIsFileProviderInSync.setStatus("current")
_VmwVchaFileReplicationProvider_Type = VmwVchaFileReplicationProviderType
_VmwVchaFileReplicationProvider_Object = MibScalar
vmwVchaFileReplicationProvider = _VmwVchaFileReplicationProvider_Object(
    (1, 3, 6, 1, 4, 1, 6876, 53, 60),
    _VmwVchaFileReplicationProvider_Type()
)
vmwVchaFileReplicationProvider.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVchaFileReplicationProvider.setStatus("current")
_VmwVchaActive_ObjectIdentity = ObjectIdentity
vmwVchaActive = _VmwVchaActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 250)
)
_VmwVchaPassive_ObjectIdentity = ObjectIdentity
vmwVchaPassive = _VmwVchaPassive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 255)
)
_VmwVchaWitness_ObjectIdentity = ObjectIdentity
vmwVchaWitness = _VmwVchaWitness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53, 260)
)

# Managed Objects groups

vmwVchaNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2, 1)
)
vmwVchaNotificationInfoGroup.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"),
        ("VMWARE-VCHA-MIB", "vmwVchaClusterState"),
        ("VMWARE-VCHA-MIB", "vmwVchaClusterMode"),
        ("VMWARE-VCHA-MIB", "vmwVchaIsPlannedFailover"),
        ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationState"),
        ("VMWARE-VCHA-MIB", "vmwVchaIsFileProviderInSync"),
        ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationProvider"))
)
if mibBuilder.loadTexts:
    vmwVchaNotificationInfoGroup.setStatus("current")


# Notification objects

vmwVchaNodeJoined = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 100)
)
vmwVchaNodeJoined.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"),
        ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
)
if mibBuilder.loadTexts:
    vmwVchaNodeJoined.setStatus(
        "current"
    )

vmwVchaNodeLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 105)
)
vmwVchaNodeLeft.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"),
        ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
)
if mibBuilder.loadTexts:
    vmwVchaNodeLeft.setStatus(
        "current"
    )

vmwVchaNodeIsolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 110)
)
vmwVchaNodeIsolated.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"),
        ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
)
if mibBuilder.loadTexts:
    vmwVchaNodeIsolated.setStatus(
        "current"
    )

vmwVchaClusterStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 130)
)
vmwVchaClusterStateChanged.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaClusterState"))
)
if mibBuilder.loadTexts:
    vmwVchaClusterStateChanged.setStatus(
        "current"
    )

vmwVchaClusterModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 150)
)
vmwVchaClusterModeChanged.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaClusterMode"))
)
if mibBuilder.loadTexts:
    vmwVchaClusterModeChanged.setStatus(
        "current"
    )

vmwVchaPublicIpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 205)
)
vmwVchaPublicIpUp.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"))
)
if mibBuilder.loadTexts:
    vmwVchaPublicIpUp.setStatus(
        "current"
    )

vmwVchaPublicIpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 206)
)
vmwVchaPublicIpDown.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"))
)
if mibBuilder.loadTexts:
    vmwVchaPublicIpDown.setStatus(
        "current"
    )

vmwVchaFailoverTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 210)
)
vmwVchaFailoverTriggered.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaIsPlannedFailover"))
)
if mibBuilder.loadTexts:
    vmwVchaFailoverTriggered.setStatus(
        "current"
    )

vmwVchaFailoverSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 220)
)
vmwVchaFailoverSucceeded.setObjects(
    ("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid")
)
if mibBuilder.loadTexts:
    vmwVchaFailoverSucceeded.setStatus(
        "current"
    )

vmwVchaFailoverFailedDisabledMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 225)
)
vmwVchaFailoverFailedDisabledMode.setObjects(
    ("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid")
)
if mibBuilder.loadTexts:
    vmwVchaFailoverFailedDisabledMode.setStatus(
        "current"
    )

vmwVchaFailoverFailedNodeLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 226)
)
vmwVchaFailoverFailedNodeLost.setObjects(
    ("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid")
)
if mibBuilder.loadTexts:
    vmwVchaFailoverFailedNodeLost.setStatus(
        "current"
    )

vmwVchaFailoverFailedPassiveNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 227)
)
vmwVchaFailoverFailedPassiveNotReady.setObjects(
    ("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid")
)
if mibBuilder.loadTexts:
    vmwVchaFailoverFailedPassiveNotReady.setStatus(
        "current"
    )

vmwVchaContinueAsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 230)
)
vmwVchaContinueAsActive.setObjects(
    ("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid")
)
if mibBuilder.loadTexts:
    vmwVchaContinueAsActive.setStatus(
        "current"
    )

vmwVchaDbReplicationStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 300)
)
vmwVchaDbReplicationStateChanged.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationState"))
)
if mibBuilder.loadTexts:
    vmwVchaDbReplicationStateChanged.setStatus(
        "current"
    )

vmwVchaFileReplicationStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 53, 0, 350)
)
vmwVchaFileReplicationStateChanged.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"),
        ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationProvider"),
        ("VMWARE-VCHA-MIB", "vmwVchaIsFileProviderInSync"))
)
if mibBuilder.loadTexts:
    vmwVchaFileReplicationStateChanged.setStatus(
        "current"
    )


# Notifications groups

vmwVchaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2, 2)
)
vmwVchaNotificationGroup.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaNodeJoined"),
        ("VMWARE-VCHA-MIB", "vmwVchaNodeLeft"),
        ("VMWARE-VCHA-MIB", "vmwVchaNodeIsolated"),
        ("VMWARE-VCHA-MIB", "vmwVchaClusterStateChanged"),
        ("VMWARE-VCHA-MIB", "vmwVchaClusterModeChanged"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicIpUp"),
        ("VMWARE-VCHA-MIB", "vmwVchaPublicIpDown"),
        ("VMWARE-VCHA-MIB", "vmwVchaFailoverTriggered"),
        ("VMWARE-VCHA-MIB", "vmwVchaFailoverSucceeded"),
        ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedDisabledMode"),
        ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedNodeLost"),
        ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedPassiveNotReady"),
        ("VMWARE-VCHA-MIB", "vmwVchaContinueAsActive"),
        ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationStateChanged"),
        ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationStateChanged"))
)
if mibBuilder.loadTexts:
    vmwVchaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwVchaMIBBasicComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 1, 3)
)
vmwVchaMIBBasicComplianceRev2.setObjects(
      *(("VMWARE-VCHA-MIB", "vmwVchaNotificationInfoGroup"),
        ("VMWARE-VCHA-MIB", "vmwVchaNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwVchaMIBBasicComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VCHA-MIB",
    **{"VmwVchaNodeRoleType": VmwVchaNodeRoleType,
       "VmwVchaClusterModeType": VmwVchaClusterModeType,
       "VmwVchaClusterStateType": VmwVchaClusterStateType,
       "VmwVchaDbReplicationStateType": VmwVchaDbReplicationStateType,
       "VmwVchaFileReplicationProviderType": VmwVchaFileReplicationProviderType,
       "vmwVCHANotifications": vmwVCHANotifications,
       "vmwVchaNodeJoined": vmwVchaNodeJoined,
       "vmwVchaNodeLeft": vmwVchaNodeLeft,
       "vmwVchaNodeIsolated": vmwVchaNodeIsolated,
       "vmwVchaClusterStateChanged": vmwVchaClusterStateChanged,
       "vmwVchaClusterModeChanged": vmwVchaClusterModeChanged,
       "vmwVchaPublicIpUp": vmwVchaPublicIpUp,
       "vmwVchaPublicIpDown": vmwVchaPublicIpDown,
       "vmwVchaFailoverTriggered": vmwVchaFailoverTriggered,
       "vmwVchaFailoverSucceeded": vmwVchaFailoverSucceeded,
       "vmwVchaFailoverFailedDisabledMode": vmwVchaFailoverFailedDisabledMode,
       "vmwVchaFailoverFailedNodeLost": vmwVchaFailoverFailedNodeLost,
       "vmwVchaFailoverFailedPassiveNotReady": vmwVchaFailoverFailedPassiveNotReady,
       "vmwVchaContinueAsActive": vmwVchaContinueAsActive,
       "vmwVchaDbReplicationStateChanged": vmwVchaDbReplicationStateChanged,
       "vmwVchaFileReplicationStateChanged": vmwVchaFileReplicationStateChanged,
       "vmwVchaMIB": vmwVchaMIB,
       "vmwVchaMIBConformance": vmwVchaMIBConformance,
       "vmwVchaMIBCompliances": vmwVchaMIBCompliances,
       "vmwVchaMIBBasicComplianceRev2": vmwVchaMIBBasicComplianceRev2,
       "vmwVchaMIBGroups": vmwVchaMIBGroups,
       "vmwVchaNotificationInfoGroup": vmwVchaNotificationInfoGroup,
       "vmwVchaNotificationGroup": vmwVchaNotificationGroup,
       "vmwVchaInstanceUuid": vmwVchaInstanceUuid,
       "vmwVchaPrivateAddressType": vmwVchaPrivateAddressType,
       "vmwVchaPublicAddressType": vmwVchaPublicAddressType,
       "vmwVchaPrivateAddressAddr": vmwVchaPrivateAddressAddr,
       "vmwVchaPublicAddressAddr": vmwVchaPublicAddressAddr,
       "vmwVchaTargetNodeRole": vmwVchaTargetNodeRole,
       "vmwVchaClusterState": vmwVchaClusterState,
       "vmwVchaClusterMode": vmwVchaClusterMode,
       "vmwVchaIsPlannedFailover": vmwVchaIsPlannedFailover,
       "vmwVchaDbReplicationState": vmwVchaDbReplicationState,
       "vmwVchaIsFileProviderInSync": vmwVchaIsFileProviderInSync,
       "vmwVchaFileReplicationProvider": vmwVchaFileReplicationProvider,
       "vmwVchaActive": vmwVchaActive,
       "vmwVchaPassive": vmwVchaPassive,
       "vmwVchaWitness": vmwVchaWitness}
)
