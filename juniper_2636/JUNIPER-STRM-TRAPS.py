# SNMP MIB module (JUNIPER-STRM-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-STRM-TRAPS.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:30:08 2025
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

(jnxStrm,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxStrm")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

strmTrapInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StrmTrap_ObjectIdentity = ObjectIdentity
strmTrap = _StrmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 0)
)
_StrmLocalHostAddress_Type = IpAddress
_StrmLocalHostAddress_Object = MibScalar
strmLocalHostAddress = _StrmLocalHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 1),
    _StrmLocalHostAddress_Type()
)
strmLocalHostAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmLocalHostAddress.setStatus("current")


class _StrmTimeString_Type(DisplayString):
    """Custom type strmTimeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StrmTimeString_Type.__name__ = "DisplayString"
_StrmTimeString_Object = MibScalar
strmTimeString = _StrmTimeString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 2),
    _StrmTimeString_Type()
)
strmTimeString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTimeString.setStatus("current")
_StrmTimeInMillis_Type = Counter64
_StrmTimeInMillis_Object = MibScalar
strmTimeInMillis = _StrmTimeInMillis_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 3),
    _StrmTimeInMillis_Type()
)
strmTimeInMillis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTimeInMillis.setStatus("current")
_StrmOffenseID_Type = Counter64
_StrmOffenseID_Object = MibScalar
strmOffenseID = _StrmOffenseID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 4),
    _StrmOffenseID_Type()
)
strmOffenseID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmOffenseID.setStatus("current")


class _StrmOffenseDescription_Type(DisplayString):
    """Custom type strmOffenseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmOffenseDescription_Type.__name__ = "DisplayString"
_StrmOffenseDescription_Object = MibScalar
strmOffenseDescription = _StrmOffenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 6),
    _StrmOffenseDescription_Type()
)
strmOffenseDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmOffenseDescription.setStatus("current")


class _StrmOffenseLink_Type(DisplayString):
    """Custom type strmOffenseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmOffenseLink_Type.__name__ = "DisplayString"
_StrmOffenseLink_Object = MibScalar
strmOffenseLink = _StrmOffenseLink_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 7),
    _StrmOffenseLink_Type()
)
strmOffenseLink.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmOffenseLink.setStatus("current")
_StrmMagnitude_Type = Integer32
_StrmMagnitude_Object = MibScalar
strmMagnitude = _StrmMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 8),
    _StrmMagnitude_Type()
)
strmMagnitude.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmMagnitude.setStatus("current")
_StrmSeverity_Type = Integer32
_StrmSeverity_Object = MibScalar
strmSeverity = _StrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 9),
    _StrmSeverity_Type()
)
strmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmSeverity.setStatus("current")
_StrmCreditibility_Type = Integer32
_StrmCreditibility_Object = MibScalar
strmCreditibility = _StrmCreditibility_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 10),
    _StrmCreditibility_Type()
)
strmCreditibility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmCreditibility.setStatus("current")
_StrmRelevance_Type = Integer32
_StrmRelevance_Object = MibScalar
strmRelevance = _StrmRelevance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 11),
    _StrmRelevance_Type()
)
strmRelevance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmRelevance.setStatus("current")
_StrmAttackerIP_Type = IpAddress
_StrmAttackerIP_Object = MibScalar
strmAttackerIP = _StrmAttackerIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 12),
    _StrmAttackerIP_Type()
)
strmAttackerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmAttackerIP.setStatus("current")


class _StrmAttackerUserName_Type(DisplayString):
    """Custom type strmAttackerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmAttackerUserName_Type.__name__ = "DisplayString"
_StrmAttackerUserName_Object = MibScalar
strmAttackerUserName = _StrmAttackerUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 13),
    _StrmAttackerUserName_Type()
)
strmAttackerUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmAttackerUserName.setStatus("current")
_StrmAttackerCount_Type = Counter64
_StrmAttackerCount_Object = MibScalar
strmAttackerCount = _StrmAttackerCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 14),
    _StrmAttackerCount_Type()
)
strmAttackerCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmAttackerCount.setStatus("current")


class _StrmTop5AttackerIPs_Type(DisplayString):
    """Custom type strmTop5AttackerIPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTop5AttackerIPs_Type.__name__ = "DisplayString"
_StrmTop5AttackerIPs_Object = MibScalar
strmTop5AttackerIPs = _StrmTop5AttackerIPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 15),
    _StrmTop5AttackerIPs_Type()
)
strmTop5AttackerIPs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTop5AttackerIPs.setStatus("current")
_StrmTopAttackerIP_Type = IpAddress
_StrmTopAttackerIP_Object = MibScalar
strmTopAttackerIP = _StrmTopAttackerIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 16),
    _StrmTopAttackerIP_Type()
)
strmTopAttackerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTopAttackerIP.setStatus("current")


class _StrmAttackerNetworks_Type(DisplayString):
    """Custom type strmAttackerNetworks based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmAttackerNetworks_Type.__name__ = "DisplayString"
_StrmAttackerNetworks_Object = MibScalar
strmAttackerNetworks = _StrmAttackerNetworks_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 17),
    _StrmAttackerNetworks_Type()
)
strmAttackerNetworks.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmAttackerNetworks.setStatus("current")
_StrmTargetIP_Type = IpAddress
_StrmTargetIP_Object = MibScalar
strmTargetIP = _StrmTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 18),
    _StrmTargetIP_Type()
)
strmTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTargetIP.setStatus("current")


class _StrmTargetUserName_Type(DisplayString):
    """Custom type strmTargetUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StrmTargetUserName_Type.__name__ = "DisplayString"
_StrmTargetUserName_Object = MibScalar
strmTargetUserName = _StrmTargetUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 19),
    _StrmTargetUserName_Type()
)
strmTargetUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTargetUserName.setStatus("current")
_StrmTargetCount_Type = Counter64
_StrmTargetCount_Object = MibScalar
strmTargetCount = _StrmTargetCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 20),
    _StrmTargetCount_Type()
)
strmTargetCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTargetCount.setStatus("current")


class _StrmTop5TargetIPs_Type(DisplayString):
    """Custom type strmTop5TargetIPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTop5TargetIPs_Type.__name__ = "DisplayString"
_StrmTop5TargetIPs_Object = MibScalar
strmTop5TargetIPs = _StrmTop5TargetIPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 21),
    _StrmTop5TargetIPs_Type()
)
strmTop5TargetIPs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTop5TargetIPs.setStatus("current")
_StrmTopTargetIP_Type = IpAddress
_StrmTopTargetIP_Object = MibScalar
strmTopTargetIP = _StrmTopTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 22),
    _StrmTopTargetIP_Type()
)
strmTopTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTopTargetIP.setStatus("current")


class _StrmTargetNetworks_Type(DisplayString):
    """Custom type strmTargetNetworks based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTargetNetworks_Type.__name__ = "DisplayString"
_StrmTargetNetworks_Object = MibScalar
strmTargetNetworks = _StrmTargetNetworks_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 23),
    _StrmTargetNetworks_Type()
)
strmTargetNetworks.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTargetNetworks.setStatus("current")
_StrmCategoryCount_Type = Integer32
_StrmCategoryCount_Object = MibScalar
strmCategoryCount = _StrmCategoryCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 24),
    _StrmCategoryCount_Type()
)
strmCategoryCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmCategoryCount.setStatus("current")


class _StrmTop5Categories_Type(DisplayString):
    """Custom type strmTop5Categories based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTop5Categories_Type.__name__ = "DisplayString"
_StrmTop5Categories_Object = MibScalar
strmTop5Categories = _StrmTop5Categories_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 25),
    _StrmTop5Categories_Type()
)
strmTop5Categories.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTop5Categories.setStatus("current")


class _StrmTopCategory_Type(DisplayString):
    """Custom type strmTopCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StrmTopCategory_Type.__name__ = "DisplayString"
_StrmTopCategory_Object = MibScalar
strmTopCategory = _StrmTopCategory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 26),
    _StrmTopCategory_Type()
)
strmTopCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTopCategory.setStatus("current")
_StrmCategoryID_Type = Integer32
_StrmCategoryID_Object = MibScalar
strmCategoryID = _StrmCategoryID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 27),
    _StrmCategoryID_Type()
)
strmCategoryID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmCategoryID.setStatus("current")


class _StrmCategory_Type(DisplayString):
    """Custom type strmCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StrmCategory_Type.__name__ = "DisplayString"
_StrmCategory_Object = MibScalar
strmCategory = _StrmCategory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 28),
    _StrmCategory_Type()
)
strmCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmCategory.setStatus("current")
_StrmAnnotationCount_Type = Integer32
_StrmAnnotationCount_Object = MibScalar
strmAnnotationCount = _StrmAnnotationCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 29),
    _StrmAnnotationCount_Type()
)
strmAnnotationCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmAnnotationCount.setStatus("current")


class _StrmTopAnnotation_Type(DisplayString):
    """Custom type strmTopAnnotation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTopAnnotation_Type.__name__ = "DisplayString"
_StrmTopAnnotation_Object = MibScalar
strmTopAnnotation = _StrmTopAnnotation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 30),
    _StrmTopAnnotation_Type()
)
strmTopAnnotation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTopAnnotation.setStatus("current")
_StrmRuleCount_Type = Integer32
_StrmRuleCount_Object = MibScalar
strmRuleCount = _StrmRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 31),
    _StrmRuleCount_Type()
)
strmRuleCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmRuleCount.setStatus("current")


class _StrmRuleNames_Type(DisplayString):
    """Custom type strmRuleNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmRuleNames_Type.__name__ = "DisplayString"
_StrmRuleNames_Object = MibScalar
strmRuleNames = _StrmRuleNames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 32),
    _StrmRuleNames_Type()
)
strmRuleNames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmRuleNames.setStatus("current")
_StrmRuleID_Type = Integer32
_StrmRuleID_Object = MibScalar
strmRuleID = _StrmRuleID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 33),
    _StrmRuleID_Type()
)
strmRuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmRuleID.setStatus("current")


class _StrmRuleName_Type(DisplayString):
    """Custom type strmRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StrmRuleName_Type.__name__ = "DisplayString"
_StrmRuleName_Object = MibScalar
strmRuleName = _StrmRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 34),
    _StrmRuleName_Type()
)
strmRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmRuleName.setStatus("current")


class _StrmRuleDescription_Type(DisplayString):
    """Custom type strmRuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmRuleDescription_Type.__name__ = "DisplayString"
_StrmRuleDescription_Object = MibScalar
strmRuleDescription = _StrmRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 35),
    _StrmRuleDescription_Type()
)
strmRuleDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmRuleDescription.setStatus("current")
_StrmEventCount_Type = Counter64
_StrmEventCount_Object = MibScalar
strmEventCount = _StrmEventCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 36),
    _StrmEventCount_Type()
)
strmEventCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmEventCount.setStatus("current")
_StrmEventID_Type = Integer32
_StrmEventID_Object = MibScalar
strmEventID = _StrmEventID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 37),
    _StrmEventID_Type()
)
strmEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmEventID.setStatus("current")
_StrmQid_Type = Integer32
_StrmQid_Object = MibScalar
strmQid = _StrmQid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 38),
    _StrmQid_Type()
)
strmQid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmQid.setStatus("current")


class _StrmEventName_Type(DisplayString):
    """Custom type strmEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StrmEventName_Type.__name__ = "DisplayString"
_StrmEventName_Object = MibScalar
strmEventName = _StrmEventName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 39),
    _StrmEventName_Type()
)
strmEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmEventName.setStatus("current")


class _StrmEventDescription_Type(DisplayString):
    """Custom type strmEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmEventDescription_Type.__name__ = "DisplayString"
_StrmEventDescription_Object = MibScalar
strmEventDescription = _StrmEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 40),
    _StrmEventDescription_Type()
)
strmEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmEventDescription.setStatus("current")
_StrmSourceIP_Type = IpAddress
_StrmSourceIP_Object = MibScalar
strmSourceIP = _StrmSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 41),
    _StrmSourceIP_Type()
)
strmSourceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmSourceIP.setStatus("current")
_StrmSourcePort_Type = Integer32
_StrmSourcePort_Object = MibScalar
strmSourcePort = _StrmSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 42),
    _StrmSourcePort_Type()
)
strmSourcePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmSourcePort.setStatus("current")
_StrmDestinationIP_Type = IpAddress
_StrmDestinationIP_Object = MibScalar
strmDestinationIP = _StrmDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 43),
    _StrmDestinationIP_Type()
)
strmDestinationIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmDestinationIP.setStatus("current")
_StrmDestinationPort_Type = Integer32
_StrmDestinationPort_Object = MibScalar
strmDestinationPort = _StrmDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 44),
    _StrmDestinationPort_Type()
)
strmDestinationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmDestinationPort.setStatus("current")
_StrmProtocol_Type = Integer32
_StrmProtocol_Object = MibScalar
strmProtocol = _StrmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 45),
    _StrmProtocol_Type()
)
strmProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmProtocol.setStatus("current")
_StrmAttackerPort_Type = Integer32
_StrmAttackerPort_Object = MibScalar
strmAttackerPort = _StrmAttackerPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 46),
    _StrmAttackerPort_Type()
)
strmAttackerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmAttackerPort.setStatus("current")
_StrmTargetPort_Type = Integer32
_StrmTargetPort_Object = MibScalar
strmTargetPort = _StrmTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 47),
    _StrmTargetPort_Type()
)
strmTargetPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTargetPort.setStatus("current")


class _StrmTop5AttackerUsernames_Type(DisplayString):
    """Custom type strmTop5AttackerUsernames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTop5AttackerUsernames_Type.__name__ = "DisplayString"
_StrmTop5AttackerUsernames_Object = MibScalar
strmTop5AttackerUsernames = _StrmTop5AttackerUsernames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 48),
    _StrmTop5AttackerUsernames_Type()
)
strmTop5AttackerUsernames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTop5AttackerUsernames.setStatus("current")


class _StrmTopAttackerUsername_Type(DisplayString):
    """Custom type strmTopAttackerUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StrmTopAttackerUsername_Type.__name__ = "DisplayString"
_StrmTopAttackerUsername_Object = MibScalar
strmTopAttackerUsername = _StrmTopAttackerUsername_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 49),
    _StrmTopAttackerUsername_Type()
)
strmTopAttackerUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTopAttackerUsername.setStatus("current")


class _StrmTop5TargetUsernames_Type(DisplayString):
    """Custom type strmTop5TargetUsernames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StrmTop5TargetUsernames_Type.__name__ = "DisplayString"
_StrmTop5TargetUsernames_Object = MibScalar
strmTop5TargetUsernames = _StrmTop5TargetUsernames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 50),
    _StrmTop5TargetUsernames_Type()
)
strmTop5TargetUsernames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTop5TargetUsernames.setStatus("current")


class _StrmTopTargetUsername_Type(DisplayString):
    """Custom type strmTopTargetUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StrmTopTargetUsername_Type.__name__ = "DisplayString"
_StrmTopTargetUsername_Object = MibScalar
strmTopTargetUsername = _StrmTopTargetUsername_Object(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 1, 51),
    _StrmTopTargetUsername_Type()
)
strmTopTargetUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strmTopTargetUsername.setStatus("current")

# Managed Objects groups


# Notification objects

strmEventCRENotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 0, 1)
)
strmEventCRENotification.setObjects(
      *(("JUNIPER-STRM-TRAPS", "strmLocalHostAddress"),
        ("JUNIPER-STRM-TRAPS", "strmTimeString"),
        ("JUNIPER-STRM-TRAPS", "strmRuleName"),
        ("JUNIPER-STRM-TRAPS", "strmRuleDescription"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerIP"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerPort"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerUserName"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerNetworks"),
        ("JUNIPER-STRM-TRAPS", "strmTargetIP"),
        ("JUNIPER-STRM-TRAPS", "strmTargetPort"),
        ("JUNIPER-STRM-TRAPS", "strmTargetUserName"),
        ("JUNIPER-STRM-TRAPS", "strmTargetNetworks"),
        ("JUNIPER-STRM-TRAPS", "strmProtocol"),
        ("JUNIPER-STRM-TRAPS", "strmQid"),
        ("JUNIPER-STRM-TRAPS", "strmEventName"),
        ("JUNIPER-STRM-TRAPS", "strmEventDescription"),
        ("JUNIPER-STRM-TRAPS", "strmCategory"))
)
if mibBuilder.loadTexts:
    strmEventCRENotification.setStatus(
        "current"
    )

strmOffenseCRENotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9, 0, 2)
)
strmOffenseCRENotification.setObjects(
      *(("JUNIPER-STRM-TRAPS", "strmLocalHostAddress"),
        ("JUNIPER-STRM-TRAPS", "strmTimeString"),
        ("JUNIPER-STRM-TRAPS", "strmRuleName"),
        ("JUNIPER-STRM-TRAPS", "strmRuleDescription"),
        ("JUNIPER-STRM-TRAPS", "strmOffenseID"),
        ("JUNIPER-STRM-TRAPS", "strmOffenseDescription"),
        ("JUNIPER-STRM-TRAPS", "strmOffenseLink"),
        ("JUNIPER-STRM-TRAPS", "strmMagnitude"),
        ("JUNIPER-STRM-TRAPS", "strmSeverity"),
        ("JUNIPER-STRM-TRAPS", "strmCreditibility"),
        ("JUNIPER-STRM-TRAPS", "strmRelevance"),
        ("JUNIPER-STRM-TRAPS", "strmEventCount"),
        ("JUNIPER-STRM-TRAPS", "strmCategoryCount"),
        ("JUNIPER-STRM-TRAPS", "strmTop5Categories"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerIP"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerUserName"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerNetworks"),
        ("JUNIPER-STRM-TRAPS", "strmAttackerCount"),
        ("JUNIPER-STRM-TRAPS", "strmTop5AttackerIPs"),
        ("JUNIPER-STRM-TRAPS", "strmTargetIP"),
        ("JUNIPER-STRM-TRAPS", "strmTargetUserName"),
        ("JUNIPER-STRM-TRAPS", "strmTargetNetworks"),
        ("JUNIPER-STRM-TRAPS", "strmTargetCount"),
        ("JUNIPER-STRM-TRAPS", "strmTop5TargetIPs"),
        ("JUNIPER-STRM-TRAPS", "strmRuleCount"),
        ("JUNIPER-STRM-TRAPS", "strmRuleNames"),
        ("JUNIPER-STRM-TRAPS", "strmAnnotationCount"))
)
if mibBuilder.loadTexts:
    strmOffenseCRENotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-STRM-TRAPS",
    **{"strmTrap": strmTrap,
       "strmEventCRENotification": strmEventCRENotification,
       "strmOffenseCRENotification": strmOffenseCRENotification,
       "strmTrapInfo": strmTrapInfo,
       "strmLocalHostAddress": strmLocalHostAddress,
       "strmTimeString": strmTimeString,
       "strmTimeInMillis": strmTimeInMillis,
       "strmOffenseID": strmOffenseID,
       "strmOffenseDescription": strmOffenseDescription,
       "strmOffenseLink": strmOffenseLink,
       "strmMagnitude": strmMagnitude,
       "strmSeverity": strmSeverity,
       "strmCreditibility": strmCreditibility,
       "strmRelevance": strmRelevance,
       "strmAttackerIP": strmAttackerIP,
       "strmAttackerUserName": strmAttackerUserName,
       "strmAttackerCount": strmAttackerCount,
       "strmTop5AttackerIPs": strmTop5AttackerIPs,
       "strmTopAttackerIP": strmTopAttackerIP,
       "strmAttackerNetworks": strmAttackerNetworks,
       "strmTargetIP": strmTargetIP,
       "strmTargetUserName": strmTargetUserName,
       "strmTargetCount": strmTargetCount,
       "strmTop5TargetIPs": strmTop5TargetIPs,
       "strmTopTargetIP": strmTopTargetIP,
       "strmTargetNetworks": strmTargetNetworks,
       "strmCategoryCount": strmCategoryCount,
       "strmTop5Categories": strmTop5Categories,
       "strmTopCategory": strmTopCategory,
       "strmCategoryID": strmCategoryID,
       "strmCategory": strmCategory,
       "strmAnnotationCount": strmAnnotationCount,
       "strmTopAnnotation": strmTopAnnotation,
       "strmRuleCount": strmRuleCount,
       "strmRuleNames": strmRuleNames,
       "strmRuleID": strmRuleID,
       "strmRuleName": strmRuleName,
       "strmRuleDescription": strmRuleDescription,
       "strmEventCount": strmEventCount,
       "strmEventID": strmEventID,
       "strmQid": strmQid,
       "strmEventName": strmEventName,
       "strmEventDescription": strmEventDescription,
       "strmSourceIP": strmSourceIP,
       "strmSourcePort": strmSourcePort,
       "strmDestinationIP": strmDestinationIP,
       "strmDestinationPort": strmDestinationPort,
       "strmProtocol": strmProtocol,
       "strmAttackerPort": strmAttackerPort,
       "strmTargetPort": strmTargetPort,
       "strmTop5AttackerUsernames": strmTop5AttackerUsernames,
       "strmTopAttackerUsername": strmTopAttackerUsername,
       "strmTop5TargetUsernames": strmTop5TargetUsernames,
       "strmTopTargetUsername": strmTopTargetUsername}
)
