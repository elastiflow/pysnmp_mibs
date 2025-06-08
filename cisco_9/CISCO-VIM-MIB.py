# SNMP MIB module (CISCO-VIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VIM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 855)
)
if mibBuilder.loadTexts:
    ciscoVimMIB.setRevisions(
        ("2018-07-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CFaultSeverity(TextualConvention, Integer32):
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
        *(("emergency", 1),
          ("critical", 2),
          ("major", 3),
          ("alert", 4),
          ("informational", 5))
    )



class CFaultCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("resourceUsage", 2),
          ("resourceThreshold", 3),
          ("serviceFailure", 4),
          ("hardwareFailure", 5),
          ("networkConnectivity", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVimMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVimMIBNotifs = _CiscoVimMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 0)
)
_CiscoVimMIBFaults_ObjectIdentity = ObjectIdentity
ciscoVimMIBFaults = _CiscoVimMIBFaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1)
)


class _CvimPodId_Type(OctetString):
    """Custom type cvimPodId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CvimPodId_Type.__name__ = "OctetString"
_CvimPodId_Object = MibScalar
cvimPodId = _CvimPodId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 1),
    _CvimPodId_Type()
)
cvimPodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimPodId.setStatus("current")
_CvimFaultCreationTime_Type = DateAndTime
_CvimFaultCreationTime_Object = MibScalar
cvimFaultCreationTime = _CvimFaultCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 2),
    _CvimFaultCreationTime_Type()
)
cvimFaultCreationTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimFaultCreationTime.setStatus("current")


class _CvimNodeId_Type(OctetString):
    """Custom type cvimNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CvimNodeId_Type.__name__ = "OctetString"
_CvimNodeId_Object = MibScalar
cvimNodeId = _CvimNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 3),
    _CvimNodeId_Type()
)
cvimNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimNodeId.setStatus("current")


class _CvimFaultSource_Type(OctetString):
    """Custom type cvimFaultSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 100),
    )


_CvimFaultSource_Type.__name__ = "OctetString"
_CvimFaultSource_Object = MibScalar
cvimFaultSource = _CvimFaultSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 4),
    _CvimFaultSource_Type()
)
cvimFaultSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimFaultSource.setStatus("current")
_CvimFaultSeverity_Type = CFaultSeverity
_CvimFaultSeverity_Object = MibScalar
cvimFaultSeverity = _CvimFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 5),
    _CvimFaultSeverity_Type()
)
cvimFaultSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimFaultSeverity.setStatus("current")
_CvimFaultCode_Type = CFaultCode
_CvimFaultCode_Object = MibScalar
cvimFaultCode = _CvimFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 6),
    _CvimFaultCode_Type()
)
cvimFaultCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimFaultCode.setStatus("current")


class _CvimFaultDescription_Type(OctetString):
    """Custom type cvimFaultDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_CvimFaultDescription_Type.__name__ = "OctetString"
_CvimFaultDescription_Object = MibScalar
cvimFaultDescription = _CvimFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 7),
    _CvimFaultDescription_Type()
)
cvimFaultDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvimFaultDescription.setStatus("current")
_CiscoVimMIBConform_ObjectIdentity = ObjectIdentity
ciscoVimMIBConform = _CiscoVimMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 2)
)
_CiscoVimMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVimMIBCompliances = _CiscoVimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1)
)
_CiscoVimMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVimMIBGroups = _CiscoVimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2)
)

# Managed Objects groups

cvimMIBFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 1)
)
cvimMIBFaultGroup.setObjects(
      *(("CISCO-VIM-MIB", "cvimPodId"),
        ("CISCO-VIM-MIB", "cvimFaultSource"),
        ("CISCO-VIM-MIB", "cvimFaultCreationTime"),
        ("CISCO-VIM-MIB", "cvimFaultSeverity"),
        ("CISCO-VIM-MIB", "cvimFaultCode"))
)
if mibBuilder.loadTexts:
    cvimMIBFaultGroup.setStatus("current")


# Notification objects

cvimFaultActiveNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 1)
)
cvimFaultActiveNotif.setObjects(
      *(("CISCO-VIM-MIB", "cvimPodId"),
        ("CISCO-VIM-MIB", "cvimFaultCreationTime"),
        ("CISCO-VIM-MIB", "cvimNodeId"),
        ("CISCO-VIM-MIB", "cvimFaultSource"),
        ("CISCO-VIM-MIB", "cvimFaultSeverity"),
        ("CISCO-VIM-MIB", "cvimFaultCode"),
        ("CISCO-VIM-MIB", "cvimFaultDescription"))
)
if mibBuilder.loadTexts:
    cvimFaultActiveNotif.setStatus(
        "current"
    )

cvimFaultClearNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 2)
)
cvimFaultClearNotif.setObjects(
      *(("CISCO-VIM-MIB", "cvimPodId"),
        ("CISCO-VIM-MIB", "cvimFaultCreationTime"),
        ("CISCO-VIM-MIB", "cvimNodeId"),
        ("CISCO-VIM-MIB", "cvimFaultSource"),
        ("CISCO-VIM-MIB", "cvimFaultSeverity"),
        ("CISCO-VIM-MIB", "cvimFaultCode"),
        ("CISCO-VIM-MIB", "cvimFaultDescription"))
)
if mibBuilder.loadTexts:
    cvimFaultClearNotif.setStatus(
        "current"
    )


# Notifications groups

cvimMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 2)
)
cvimMIBNotificationGroup.setObjects(
    ("CISCO-VIM-MIB", "cvimFaultActiveNotif")
)
if mibBuilder.loadTexts:
    cvimMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvimMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1, 1)
)
cvimMIBCompliance.setObjects(
      *(("CISCO-VIM-MIB", "cvimMIBFaultGroup"),
        ("CISCO-VIM-MIB", "cvimMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    cvimMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIM-MIB",
    **{"CFaultSeverity": CFaultSeverity,
       "CFaultCode": CFaultCode,
       "ciscoVimMIB": ciscoVimMIB,
       "ciscoVimMIBNotifs": ciscoVimMIBNotifs,
       "cvimFaultActiveNotif": cvimFaultActiveNotif,
       "cvimFaultClearNotif": cvimFaultClearNotif,
       "ciscoVimMIBFaults": ciscoVimMIBFaults,
       "cvimPodId": cvimPodId,
       "cvimFaultCreationTime": cvimFaultCreationTime,
       "cvimNodeId": cvimNodeId,
       "cvimFaultSource": cvimFaultSource,
       "cvimFaultSeverity": cvimFaultSeverity,
       "cvimFaultCode": cvimFaultCode,
       "cvimFaultDescription": cvimFaultDescription,
       "ciscoVimMIBConform": ciscoVimMIBConform,
       "ciscoVimMIBCompliances": ciscoVimMIBCompliances,
       "cvimMIBCompliance": cvimMIBCompliance,
       "ciscoVimMIBGroups": ciscoVimMIBGroups,
       "cvimMIBFaultGroup": cvimMIBFaultGroup,
       "cvimMIBNotificationGroup": cvimMIBNotificationGroup}
)
